import inflection
from django.http import QueryDict


class CamelToSnakeQueryParamsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        new_query_params = QueryDict(mutable=True)

        for key in request.GET.keys():
            snake_key = inflection.underscore(key)
            new_query_params.setlist(snake_key, request.GET.getlist(key))

        request.GET = new_query_params

        response = self.get_response(request)
        return response
