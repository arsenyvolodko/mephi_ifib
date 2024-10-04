from rest_framework import serializers

from ifib.api.serializers import BasePaginationSerializer
from ifib.models import Terms


class TermsRequestSerializer(serializers.Serializer):
    starts_with = serializers.CharField(required=False, allow_null=True, default="")
    name = serializers.CharField(required=False, allow_blank=True, default="")
    page_size = serializers.IntegerField(min_value=1, default=10)
    page_number = serializers.IntegerField(min_value=1, default=1)


class TermsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terms
        fields = "__all__"


class TermsResponse(BasePaginationSerializer):
    items = TermsSerializer(many=True)
