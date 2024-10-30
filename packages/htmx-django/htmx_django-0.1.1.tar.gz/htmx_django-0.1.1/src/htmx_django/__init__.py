__all__ = [
    "is_page_request",
    "is_frag_request",
    "is_frag_target",
    "is_htmx",
    "is_htmx_target",
    "is_unpoly",
    "is_unpoly_target",
    "is_alpine_ajax",
    "is_alpine_ajax_target",
]

from .view_funcs import (
    is_alpine_ajax,
    is_alpine_ajax_target,
    is_frag_request,
    is_frag_target,
    is_htmx,
    is_htmx_target,
    is_page_request,
    is_unpoly,
    is_unpoly_target,
)
