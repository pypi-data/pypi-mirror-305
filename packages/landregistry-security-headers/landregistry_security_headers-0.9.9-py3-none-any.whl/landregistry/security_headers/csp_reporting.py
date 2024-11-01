import json
import logging
from typing import Optional, Union, cast

from flask import Blueprint, current_app, request

reporting = Blueprint("reporting", __name__)
logger = logging.getLogger("content_security_policy")


def log_level() -> Optional[int]:
    level = current_app.config.get("CONTENT_SECURITY_POLICY_REPORT_LEVEL", "ERROR")

    if level in ["NONE", ""]:
        return None

    level_int = cast(int, logging.getLevelName(level))
    if not isinstance(level_int, int):
        logger.debug(
            f"Invalid log level '{level}'",
            extra={"content_security_policy_report": None},
        )
        level_int = logging.ERROR

    if level_int not in [
        logging.CRITICAL,
        logging.ERROR,
        logging.WARNING,
        logging.INFO,
        logging.DEBUG,
    ]:
        logger.debug(
            f"Invalid log level '{level}'",
            extra={"content_security_policy_report": None},
        )
        level_int = logging.ERROR

    return level_int


def get_csp_report_lines(payload: Union[dict, list]) -> Optional[list]:
    if isinstance(payload, dict):
        if "csp-report" in payload:
            return [payload["csp-report"]]

        return [payload]

    if isinstance(payload, list):
        return payload

    return None


@reporting.route("/", methods=["POST"])
def report() -> tuple[str, int]:
    try:
        data = json.loads(request.data.decode("utf-8"))
        lines = get_csp_report_lines(data)
    except json.JSONDecodeError:
        return "", 400
    except KeyError:
        return "", 400

    if lines is None:
        return "", 400

    level = log_level()
    if level is not None:
        for line in lines:
            logger.log(level, "CSP violation", extra={"content_security_policy_report": line})
    return "", 204
