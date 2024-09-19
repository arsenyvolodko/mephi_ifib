from django.conf.urls.static import static
from django.conf import settings

from ifib.api.urls import api_urls

urlpatterns = [
    *api_urls
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
