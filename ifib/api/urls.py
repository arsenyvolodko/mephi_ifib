from .auth.urls import urlpatterns as auth_urls
from .home.urls import urlpatterns as home_urls
from .nuclear_medicine_intro.urls import urlpatterns as nuclear_medicine_intro_urls
from .knowledge_base.urls import urlpatterns as knowledge_base_urls


api_urls = [
    *auth_urls,
    *nuclear_medicine_intro_urls,
    *home_urls,
    *knowledge_base_urls
]
