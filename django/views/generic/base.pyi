from typing import Any, Callable, Dict, List, Optional, Tuple, Type

from django import http as http

logger = ...  # type: Any

class ContextMixin:
    def get_context_data(self, **kwargs: object) -> Dict[str, object]: ...

class View:
    http_method_names = ...  # type: List[str]
    request = ...  # type: http.HttpRequest
    args = ...  # type: Tuple[object, ...]
    kwargs = ...  # type: Dict[str, object]
    def __init__(self, **kwargs: object) -> None: ...
    @classmethod
    def as_view(cls: Any, **initkwargs: object) -> Callable[..., http.HttpResponse]: ...
    def dispatch(self, request: http.HttpRequest, *args: object, **kwargs: object) -> http.HttpResponse: ...
    def http_method_not_allowed(self, request: http.HttpRequest, *args: object, **kwargs: object) -> http.HttpResponse: ...
    def options(self, request: http.HttpRequest, *args: object, **kwargs: object) -> http.HttpResponse: ...

class TemplateResponseMixin:
    template_name = ...  # type: str
    template_engine = ...  # type: Optional[str]
    response_class = ...  # type: Type[http.HttpResponse]
    content_type = ...  # type: Optional[str]
    request = ...  # type: http.HttpRequest
    def render_to_response(self, context: Dict[str, object], **response_kwargs: object) -> http.HttpResponse: ...
    def get_template_names(self) -> List[str]: ...

class TemplateView(TemplateResponseMixin, ContextMixin, View):
    def get(self, request: http.HttpRequest, *args: object, **kwargs: object) -> http.HttpResponse: ...

class RedirectView(View):
    permanent = ...  # type: bool
    url = ...  # type: Optional[str]
    pattern_name = ...  # type: Optional[str]
    query_string = ...  # type: bool
    def get_redirect_url(self, *args: object, **kwargs: object) -> Optional[str]: ...
    def get(self, request: http.HttpRequest, *args: object, **kwargs: object) -> http.HttpResponse: ...
    def head(self, request: http.HttpRequest, *args: object, **kwargs: object) -> http.HttpResponse: ...
    def post(self, request: http.HttpRequest, *args: object, **kwargs: object) -> http.HttpResponse: ...
    def options(self, request: http.HttpRequest, *args: object, **kwargs: object) -> http.HttpResponse: ...
    def delete(self, request: http.HttpRequest, *args: object, **kwargs: object) -> http.HttpResponse: ...
    def put(self, request: http.HttpRequest, *args: object, **kwargs: object) -> http.HttpResponse: ...
    def patch(self, request: http.HttpRequest, *args: object, **kwargs: object) -> http.HttpResponse: ...
