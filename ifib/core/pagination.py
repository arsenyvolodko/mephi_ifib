from rest_framework import pagination
from rest_framework.response import Response


class PageNumberPagination(pagination.PageNumberPagination):
    page_size = 10
    max_page_size = 100
    page_size_query_param = "page_size"
    page_query_param = "page_number"

    def get_paginated_response(self, data: dict) -> Response:
        return Response(
            {
                "totalItems": self.page.paginator.count,
                "pageNumber": self.page.number,
                "pageSize": self.get_page_size(self.request),
                "totalPages": self.page.paginator.num_pages,
                "items": data,
            }
        )
