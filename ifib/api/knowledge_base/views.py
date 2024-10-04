from rest_framework import status
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ifib.api.knowledge_base.serializers import GetKnowledgeBaseRequest
from ifib.enums import KnowledgeBaseEnum


@api_view(["GET"])
def get_knowledge_base(request: Request) -> Response:
    serializer = GetKnowledgeBaseRequest(data=request.query_params)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    data = serializer.validated_data
    knowledge_base_enum_obj = KnowledgeBaseEnum.from_api_name(data["name"])
    knowledge_base = knowledge_base_enum_obj.to_db_obj()
    return Response({"id": knowledge_base.id})
