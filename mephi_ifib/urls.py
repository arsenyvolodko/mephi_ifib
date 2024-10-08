from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from ifib.api.urls import api_urls

urlpatterns = [
    path('api/v1/', include(api_urls)),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
