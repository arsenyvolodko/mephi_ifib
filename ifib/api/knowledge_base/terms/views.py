from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from ifib.api.knowledge_base.terms.serializers import (
    TermsRequestSerializer,
    TermsResponse,
    TermsSerializer,
)
from ifib.api.tools import get_paginated_response
from ifib.models import Terms, KnowledgeBase


@api_view(["GET"])
def get_terms(request: Request, knowledge_base_id: int) -> Response:
    serializer = TermsRequestSerializer(data=request.query_params)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    knowledge_base = get_object_or_404(KnowledgeBase, pk=knowledge_base_id)
    data = serializer.validated_data
    terms = Terms.objects.filter(
        knowledge_base=knowledge_base,
        name__startswith=data["starts_with"],
        name__icontains=data["name"],
    )
    response_dict = get_paginated_response(terms, TermsSerializer, data)
    serialized_response = TermsResponse(data=response_dict)
    return Response(serialized_response.initial_data)
