from django.urls import path

from .views import get_articles, get_article

urlpatterns = [
    path("article/", get_articles),
    path("article/<int:article_id>", get_article),
]
