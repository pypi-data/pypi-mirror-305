from flask import Response


class ResponseWithoutCSP(Response):
    """Return this type of Response from your views if you want to withhold the CSP

    Uses cases for this so far include:
        - Withholding CSP from views which return a PDF. When Chrome renders these it puts them in an html page
          which violates the CSP

    NOTE:
    The CSP is here for a reason, don't withhold it just because it makes development easier
    (e.g. using inline styles etc)
    """
