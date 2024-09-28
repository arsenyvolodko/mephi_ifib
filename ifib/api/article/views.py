from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage

from ifib.api.article.serializers import (
    ArticlesRequestSerializer,
    BriefArticleSerializer,
    BriefArticleSerializerResponse, ArticleSerializer,
)
from ifib.models import Article


@api_view(["GET"])
def get_articles(request: Request) -> Response:
    serializer = ArticlesRequestSerializer(data=request.query_params)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    data = serializer.validated_data
    articles = Article.objects.filter(name__icontains=data["search_name"])
    paginator = Paginator(articles, data["page_size"])
    try:
        paginated_articles: list[Article] = list(paginator.page(data["page_number"]).object_list)
        items = [BriefArticleSerializer(article).data for article in paginated_articles]
    except EmptyPage:
        items = []

    response_dict = {
        "total_items": len(articles),
        "page_size": data["page_size"],
        "total_pages": paginator.num_pages,
        "page_number": data["page_number"],
        "items": items,
    }

    serialized_response = BriefArticleSerializerResponse(data=response_dict)
    return Response(serialized_response.initial_data)


@api_view(["GET"])
def get_article(request: Request, article_id: int) -> Response:
    article = get_object_or_404(Article, pk=article_id)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)
