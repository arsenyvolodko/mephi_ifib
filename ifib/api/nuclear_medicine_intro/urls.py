from django.urls import path, include

from .article.urls import urlpatterns as article_urls
from .equipment.urls import urlpatterns as equipment_urls

urlpatterns = [
    path('nuclear-medicine-intro/', include(article_urls)),
    path('nuclear-medicine-intro/', include(equipment_urls)),
]
