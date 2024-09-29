from typing import Type

from django.core.paginator import Paginator, EmptyPage
from django.db import models
from rest_framework.serializers import Serializer


def get_paginated_response(
    all_items: list, serializer: Type[Serializer], data: dict
) -> dict:
    paginator = Paginator(all_items, data["page_size"])
    try:
        paginated_team_members = list(paginator.page(data["page_number"]).object_list)
        items = [serializer(team_member).data for team_member in paginated_team_members]
    except EmptyPage:
        items = []

    response_dict = {
        "total_items": len(all_items),
        "page_size": data["page_size"],
        "total_pages": paginator.num_pages,
        "page_number": data["page_number"],
        "items": items,
    }
    return response_dict
