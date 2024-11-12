from .auth.urls import urlpatterns as auth_urls
from .home.urls import urlpatterns as home_urls
from .knowledge_base.urls import urlpatterns as knowledge_base_urls
from django.urls import path, include
from .nuclear_medicine_intro.urls import urlpatterns as nuclear_medicine_intro_urls

api_urls = [
    *auth_urls,
    *home_urls,
    path('knowledge-base/', include(knowledge_base_urls)),
    path('nuclear-medicine-intro/', include(nuclear_medicine_intro_urls)),
]
