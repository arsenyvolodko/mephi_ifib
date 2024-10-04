from rest_framework import serializers

from ifib.enums import KnowledgeBaseEnum


class GetKnowledgeBaseRequest(serializers.Serializer):
    name = serializers.ChoiceField(choices=KnowledgeBaseEnum.api_choices())
