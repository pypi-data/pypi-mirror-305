from django.http import HttpRequest

frag_headers = ("HX-Request", "X-Up-Version", "X-Alpine-Request")


# -------- Generic Functions
def is_page_request(request: HttpRequest) -> bool:
    """Return True if the request is for a full page (not a fragment)."""
    return not is_frag_request(request)


def is_frag_request(request: HttpRequest) -> bool:
    """Return True if the request is from HTMX, Unpoly, or others."""
    return any((hdr in request.headers) for hdr in frag_headers)


def is_frag_target(request: HttpRequest, target: str) -> bool:
    """Return True if the request specified a target for the fragment."""
    req_target = (
        request.headers.get("HX-Target", False)
        or request.headers.get("X-Up-Target", False)
        or request.headers.get("X-Alpine-Target", False)
        or None
    )
    return req_target == target


# -------- HTMX Functions
def is_htmx(request: HttpRequest) -> bool:
    """Return True if the request if from HTMX."""
    return "HX-Request" in request.headers


def is_htmx_target(request: HttpRequest, target: str) -> bool:
    """Return True if the request is HTMX and is for a specific target."""
    req_target = request.headers.get("HX-Target", False)
    return req_target and req_target == target


# -------- Unpoly Functions
def is_unpoly(request: HttpRequest) -> bool:
    return "X-Up-Version" in request.headers


def is_unpoly_target(request: HttpRequest, target: str) -> bool:
    req_target = request.headers.get("X-Up-Target", False)
    return req_target and req_target == target


# -------- Alpine-AJAX
def is_alpine_ajax(request: HttpRequest) -> bool:
    return "X-Alpine-Request" in request.headers


def is_alpine_ajax_target(request: HttpRequest, target: str) -> bool:
    req_target = request.headers.get("X-Alpine-Target", False)
    return req_target and req_target == target
