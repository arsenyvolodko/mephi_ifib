from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from ifib.api.team_members.serializers import (
    TeamMembersSerializer,
)
from ifib.models import TeamMember


@api_view(["GET"])
def get_team_members(request: Request) -> Response:
    team_members = TeamMember.objects.all()
    serialized_response = [TeamMembersSerializer(team_member).data for team_member in team_members]
    return Response(serialized_response)
