from django.urls import path

from .terms.views import get_terms
from .views import get_knowledge_base

urlpatterns = [
    path("knowledge-base/", get_knowledge_base),
    path("knowledge-base/<int:knowledge_base_id>/terms", get_terms)
]
