from django.core.paginator import Paginator, EmptyPage
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from ifib.api.team_members.serializers import (
    TeamMembersRequestSerializer,
    TeamMembersSerializer,
    TeamMembersSerializerResponse,
)
from ifib.api.tools import get_paginated_response
from ifib.models import TeamMember


@api_view(["GET"])
def get_team_members(request: Request) -> Response:
    serializer = TeamMembersRequestSerializer(data=request.query_params)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    data = serializer.validated_data
    team_members = TeamMember.objects.all()
    response_dict = get_paginated_response(team_members, TeamMembersSerializer, data)
    serialized_response = TeamMembersSerializerResponse(data=response_dict)
    return Response(serialized_response.initial_data)
