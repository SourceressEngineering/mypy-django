# Stubs for django.views.generic.base (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

logger = ...  # type: Any

class ContextMixin:
    def get_context_data(self, **kwargs): ...

class View:
    http_method_names = ...  # type: Any
    request = ...  # type: Any
    args = ...  # type: Any
    kwargs = ...  # type: Any
    def __init__(self, **kwargs) -> None: ...
    head = ...  # type: Any
    def as_view(cls, **initkwargs): ...
    def dispatch(self, request, *args, **kwargs): ...
    def http_method_not_allowed(self, request, *args, **kwargs): ...
    def options(self, request, *args, **kwargs): ...

class TemplateResponseMixin:
    template_name = ...  # type: Any
    template_engine = ...  # type: Any
    response_class = ...  # type: Any
    content_type = ...  # type: Any
    request = ...  # type: Any
    def render_to_response(self, context, **response_kwargs): ...
    def get_template_names(self): ...

class TemplateView(TemplateResponseMixin, ContextMixin, View):
    def get(self, request, *args, **kwargs): ...

class RedirectView(View):
    permanent = ...  # type: bool
    url = ...  # type: Any
    pattern_name = ...  # type: Any
    query_string = ...  # type: bool
    def get_redirect_url(self, *args, **kwargs): ...
    def get(self, request, *args, **kwargs): ...
    def head(self, request, *args, **kwargs): ...
    def post(self, request, *args, **kwargs): ...
    def options(self, request, *args, **kwargs): ...
    def delete(self, request, *args, **kwargs): ...
    def put(self, request, *args, **kwargs): ...
    def patch(self, request, *args, **kwargs): ...
