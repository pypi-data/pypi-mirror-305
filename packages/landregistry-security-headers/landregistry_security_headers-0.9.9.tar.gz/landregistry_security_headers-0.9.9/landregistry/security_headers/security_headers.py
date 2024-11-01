from typing import Callable, Optional, cast

from flask import Flask, Response, request, url_for

from .csp_reporting import reporting
from .exceptions import InvalidSecurityHeaderError, SecurityHeadersError
from .header_defaults import (
    DEFAULT_SCRIPT_HASHES,
    DEFAULT_SCRIPT_SOURCES,
    DEFAULT_STYLE_SOURCE,
    VARIABLES_TO_HEADERS,
    EmptyDefaultHeaders,
    Header,
    HeaderDefaults,
)
from .response_without_csp import ResponseWithoutCSP


class SecurityHeaders(object):
    def __init__(self, app: Optional[Flask] = None, defaults: Optional[HeaderDefaults] = None) -> None:
        self.app = app
        self.current_app: Flask
        self._approved_script_hashes: str
        self._approved_script_sources: str
        self._approved_style_sources: str

        if app is not None:  # pragma: no cover
            self.init_app(app, defaults)

    def _complete_csp(self, value: str) -> str:
        report_url_for = url_for("reporting.report")
        report_uri = f"report-uri {report_url_for};"
        return value.format(
            value,
            script_hashes=self._approved_script_hashes,
            report_uri=report_uri,
            script_src=self._approved_script_sources,
            style_src=self._approved_style_sources,
        )

    def _handle_report_to(self, response: Response, header: Header, value: str) -> None:
        if isinstance(response, ResponseWithoutCSP):
            return

        custom_report_to = self.current_app.config.get("REPORT_TO_URI", None)
        if custom_report_to is not None:
            full_report_uri = custom_report_to
        else:
            full_report_uri = url_for("reporting.report", _external=True)

        report_to = value.format(full_report_uri=full_report_uri)
        response.headers[header.header_name] = report_to

    def _handle_csp(self, response: Response, header: Header, value: str) -> None:
        if isinstance(response, ResponseWithoutCSP):
            return

        csp_value = self._complete_csp(value)
        if self.current_app is None:
            raise SecurityHeadersError("current_app must not be None")

        if self.current_app.config["CONTENT_SECURITY_POLICY_MODE"] == "report-only":
            response.headers["Content-Security-Policy-Report-Only"] = csp_value
        else:
            response.headers[header.header_name] = csp_value
            response.headers["X-Content-Security-Policy"] = csp_value  # For IE, natch

    def _handle_overrides(self) -> None:
        if self.current_app is None:
            raise SecurityHeadersError("current_app must not be None")

        if request.endpoint is None:
            view = None
        else:
            view = self.current_app.view_functions.get(request.endpoint)
        options = getattr(view, "security_headers_options", {})
        self._overrides = options

    def _apply_headers(self, response: Response) -> Response:
        self._handle_overrides()

        if self.current_app is None:
            raise SecurityHeadersError("current_app must not be None")

        for header in self.header_defaults.as_list:
            if header.header_name in response.headers:
                continue

            if header.config_name in self._overrides:
                value = self._overrides[header.config_name]
            else:
                value = self.current_app.config.get(header.config_name, None)

            if value is not None:
                if header.config_name == "CONTENT_SECURITY_POLICY":
                    self._handle_csp(response, header, value)
                elif header.config_name == "REPORT_TO":
                    self._handle_report_to(response, header, value)
                else:
                    response.headers[header.header_name] = value
        return response

    def _update_config(self, app: Flask) -> None:
        app.config.setdefault("CONTENT_SECURITY_POLICY_MODE", "full")
        for header in self.header_defaults.as_list:
            if header.default is not None:
                app.config.setdefault(header.config_name, header.default)

        hashes = app.config.get("SECURITY_CSP_SCRIPT_HASHES", DEFAULT_SCRIPT_HASHES)
        if not isinstance(hashes, str):
            raise InvalidSecurityHeaderError("SECURITY_CSP_SCRIPT_HASHES must be 'str'")

        sources = app.config.get("SECURITY_CSP_SCRIPT_SOURCES", DEFAULT_SCRIPT_SOURCES)
        if not isinstance(sources, str):
            raise InvalidSecurityHeaderError("SECURITY_CSP_SCRIPT_SOURCES must be 'str'")

        style = app.config.get("SECURITY_CSP_STYLE_SOURCES", DEFAULT_STYLE_SOURCE)
        if not isinstance(style, str):
            raise InvalidSecurityHeaderError("SECURITY_CSP_STYLE_SOURCES must be 'str'")

        self._approved_script_hashes = cast(str, hashes)
        self._approved_script_sources = cast(str, sources)
        self._approved_style_sources = cast(str, style)

    def init_app(self, app: Flask, defaults: Optional[HeaderDefaults] = None) -> None:
        if defaults is None:
            defaults = EmptyDefaultHeaders

        self._script_sources = DEFAULT_SCRIPT_SOURCES

        self.current_app = app
        self.header_defaults = defaults
        self._update_config(app)

        app.register_blueprint(reporting, url_prefix="/content-security-policy-report/")
        # If we've got flask_wtf's CSRF protection enabled, we need to exempt the reporting blueprint
        try:
            csrf = app.extensions["csrf"]
        except KeyError:
            pass
        else:
            csrf.exempt(reporting)

        app.after_request(self._apply_headers)

    def __call__(self, **kwargs: str) -> Callable:
        for key in kwargs.keys():
            if key not in VARIABLES_TO_HEADERS:
                raise InvalidSecurityHeaderError(f"Header '{key}' not recognised.")

        def decorator(f: Callable) -> Callable:
            setattr(f, "security_headers_options", kwargs)  # noqa: B010
            return f

        return decorator
