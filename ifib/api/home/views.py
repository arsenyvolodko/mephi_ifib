from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from ifib.api.home.serializers import (
    TeamMembersSerializer, FeedbackFormSerializer,
)
from ifib.models import TeamMember


@api_view(["GET"])
def get_team_members(request: Request) -> Response:
    team_members = TeamMember.objects.all()
    serialized_response = [TeamMembersSerializer(team_member).data for team_member in team_members]
    return Response(serialized_response)


@api_view(["POST"])
def send_feedback_form(request: Request) -> Response:
    serializer = FeedbackFormSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer.save()
    return Response()
