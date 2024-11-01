from typing import Any, Optional

VARIABLES_TO_HEADERS: dict[str, str] = {
    "X_FRAME_OPTIONS": "X-Frame-Options",
    "STRICT_TRANSPORT_SECURITY": "Strict-Transport-Security",
    "X_CONTENT_TYPE_OPTIONS": "X-Content-Type-Options",
    "REPORT_TO": "Report-To",
    "CONTENT_SECURITY_POLICY": "Content-Security-Policy",
    "X_XSS_PROTECTION": "X-XSS-Protection",
    "REFERRER_POLICY": "Referrer-Policy",
    "PERMISSIONS_POLICY": "Permissions-Policy",
    "CROSS_ORIGIN_EMBEDDER_POLICY": "Cross-Origin-Embedder-Policy",
    "CROSS_ORIGIN_OPENER_POLICY": "Cross-Origin-Opener-Policy",
    "CROSS_ORIGIN_RESOURCE_POLICY": "Cross-Origin-Resource-Policy",
    "X_PERMITTED_CROSS_DOMAIN_POLICIES": "X-Permitted-Cross-Domain-Policies",
}

UI_DEFAULTS: dict[str, Any] = {
    "X_FRAME_OPTIONS": "DENY",
    "STRICT_TRANSPORT_SECURITY": "max-age=31536000; includeSubDomains",
    "X_CONTENT_TYPE_OPTIONS": "nosniff",
    "REPORT_TO": '{{"group":"default","max_age":10886400,"endpoints":[{{"url": "{full_report_uri}"}}]}}',
    "CONTENT_SECURITY_POLICY": "default-src 'self';"
    "script-src 'self' {script_src} {script_hashes} https://*.googletagmanager.com;"
    "connect-src 'self' https://*.google-analytics.com https://*.analytics.google.com https://*.googletagmanager.com;"
    "img-src 'self' https://*.google-analytics.com https://*.googletagmanager.com;"
    "font-src 'self' data:;"  # GOV.UK template loads it's fonts with a data URI
    "style-src {style_src};"
    "object-src 'none';"
    "block-all-mixed-content;"
    "{report_uri}"
    "report-to default;",
    "X_XSS_PROTECTION": "1; mode=block",
    "REFERRER_POLICY": "strict-origin-when-cross-origin",
    "PERMISSIONS_POLICY": "accelerometer=(), ambient-light-sensor=(), autoplay=(), battery=(), camera=(),"
    " cross-origin-isolated=(), display-capture=(), document-domain=(), encrypted-media=(),"
    " execution-while-not-rendered=(), execution-while-out-of-viewport=(), fullscreen=(),"
    " geolocation=(), gyroscope=(), keyboard-map=(), magnetometer=(), microphone=(), midi=(),"
    " navigation-override=(), payment=(), picture-in-picture=(), publickey-credentials-get=(),"
    " screen-wake-lock=(), sync-xhr=(), usb=(), web-share=(), xr-spatial-tracking=(),"
    " clipboard-read=(), clipboard-write=(), gamepad=(), speaker-selection=(),"
    " conversion-measurement=(), focus-without-user-activation=(), hid=(), idle-detection=(),"
    " interest-cohort=(), serial=(), sync-script=(), trust-token-redemption=(),"
    " window-management=(), vertical-scroll=()",
    "CROSS_ORIGIN_EMBEDDER_POLICY": "require-corp",
    "CROSS_ORIGIN_OPENER_POLICY": "same-origin",
    "CROSS_ORIGIN_RESOURCE_POLICY": "same-origin",
    "X_PERMITTED_CROSS_DOMAIN_POLICIES": "none",
}

API_DEFAULTS: dict[str, Any] = {
    "X_FRAME_OPTIONS": None,
    "STRICT_TRANSPORT_SECURITY": "max-age=31536000",
    "X_CONTENT_TYPE_OPTIONS": None,
    "REPORT_TO": None,
    "CONTENT_SECURITY_POLICY": "default-src 'none'; frame-ancestors 'none'",
    "X_XSS_PROTECTION": None,
    "REFERRER_POLICY": None,
    "PERMISSIONS_POLICY": None,
    "CROSS_ORIGIN_EMBEDDER_POLICY": None,
    "CROSS_ORIGIN_OPENER_POLICY": None,
    "CROSS_ORIGIN_RESOURCE_POLICY": None,
    "X_PERMITTED_CROSS_DOMAIN_POLICIES": None,
}

DEFAULT_STYLE_SOURCE: str = "'self'"
DEFAULT_SCRIPT_SOURCES: str = "https://*.googletagmanager.com"
DEFAULT_SCRIPT_HASHES: str = " ".join(
    [
        "'sha256-+6WnXIl4mbFTCARd8N3COQmT3bJJmo32N8q8ZSQAIcU='",
        "'sha256-G29/qSW/JHHANtFhlrZVDZW1HOkCDRc78ggbqwwIJ2g='",
        "'sha256-s7w4Nk/Xk6wc1nlA5PiGroLjvaV+XU1ddIlx89jmBjc='",  # Google analytics
    ]
)


class Header(object):
    def __init__(self, config_name: str, header_name: str, default: Optional[str]) -> None:
        self.config_name: str = config_name
        self.header_name: str = header_name
        self.default: Optional[str] = default

    def __repr__(self) -> str:  # pragma: no cover
        return f"{self.header_name}: {self.default}"


class HeaderDefaults(object):
    def __init__(self) -> None:
        self.as_list: list[Header] = []

    def populate_ui_default(self) -> "HeaderDefaults":
        for variable_name in VARIABLES_TO_HEADERS.keys():
            self.as_list.append(
                Header(
                    config_name=variable_name,
                    header_name=VARIABLES_TO_HEADERS[variable_name],
                    default=UI_DEFAULTS[variable_name],
                )
            )
        return self

    def populate_api_default(self) -> "HeaderDefaults":
        for variable_name in VARIABLES_TO_HEADERS.keys():
            self.as_list.append(
                Header(
                    config_name=variable_name,
                    header_name=VARIABLES_TO_HEADERS[variable_name],
                    default=API_DEFAULTS[variable_name],
                )
            )
        return self

    def populate_empty(self) -> "HeaderDefaults":
        for variable_name in VARIABLES_TO_HEADERS.keys():
            self.as_list.append(
                Header(
                    config_name=variable_name,
                    header_name=VARIABLES_TO_HEADERS[variable_name],
                    default=None,
                )
            )
        return self


APIDefaultHeaders = HeaderDefaults().populate_api_default()
UIDefaultHeaders = HeaderDefaults().populate_ui_default()
EmptyDefaultHeaders = HeaderDefaults().populate_empty()
