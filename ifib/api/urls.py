from .auth.urls import urlpatterns as auth_urls
from .article.urls import urlpatterns as article_urls
from .home.urls import urlpatterns as home_urls
from .knowledge_base.urls import urlpatterns as knowledge_base_urls


api_urls = [
    *auth_urls,
    *article_urls,
    *home_urls,
    *knowledge_base_urls
]
