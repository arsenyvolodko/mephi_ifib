from .article.urls import urlpatterns as article_urls
from .films.urls import urlpatterns as films_urls


urlpatterns = [
    *article_urls,
    *films_urls,
]
