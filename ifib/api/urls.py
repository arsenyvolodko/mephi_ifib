from .auth.urls import urlpatterns as auth_urls
from .article.urls import urlpatterns as article_urls

api_urls = [
    *auth_urls,
    *article_urls
]
