from django.urls import path

from .terms.views import get_terms
from .views import get_knowledge_base

urlpatterns = [
    path("", get_knowledge_base),
    path("<int:knowledge_base_id>/terms", get_terms)
]
