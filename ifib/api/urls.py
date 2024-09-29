from .auth.urls import urlpatterns as auth_urls
from .article.urls import urlpatterns as article_urls
from .team_members.urls import urlpatterns as team_members_urls

api_urls = [
    *auth_urls,
    *article_urls,
    *team_members_urls,
]
