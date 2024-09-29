from rest_framework import serializers

from ifib.api.serializers import BasePaginationSerializer
from ifib.models import TeamMember


class TeamMembersRequestSerializer(serializers.Serializer):
    page_size = serializers.IntegerField(min_value=1, default=4)
    page_number = serializers.IntegerField(min_value=1, default=1)


class TeamMembersSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeamMember
        fields = "__all__"

    def to_representation(self, instance: TeamMember):
        representation = super().to_representation(instance)
        representation["imageUrl"] = representation.pop("image")
        return representation


class TeamMembersSerializerResponse(BasePaginationSerializer):
    items = TeamMembersSerializer(many=True)
