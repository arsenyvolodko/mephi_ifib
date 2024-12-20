from .article.urls import urlpatterns as article_urls
from .films.urls import urlpatterns as films_urls
from .equipment.urls import urlpatterns as equipment_urls
from .podcasts.urls import urlpatterns as podcasts_urls


urlpatterns = [
    *article_urls,
    *films_urls,
    *equipment_urls,
    *podcasts_urls
]
