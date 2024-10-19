from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from ifib.api.nuclear_medicine_intro.article.serializers import (
    ArticlesRequestSerializer,
    BriefArticleSerializer,
    BriefArticleSerializerResponse, ArticleSerializer,
)
from ifib.api.tools import get_paginated_response
from ifib.models import Article


@api_view(["GET"])
def get_articles(request: Request) -> Response:
    serializer = ArticlesRequestSerializer(data=request.query_params)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    data = serializer.validated_data
    articles = Article.objects.filter(name__icontains=data["search_name"])
    response_dict = get_paginated_response(articles, BriefArticleSerializer, data)
    serialized_response = BriefArticleSerializerResponse(data=response_dict)
    return Response(serialized_response.initial_data)


@api_view(["GET"])
def get_article(request: Request, article_id: int) -> Response:
    article = get_object_or_404(Article, pk=article_id)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)
