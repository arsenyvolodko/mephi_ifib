from django.urls import path

from ifib.api.practice.views import ListPracticeView

urlpatterns = [
    path("", ListPracticeView.as_view()),
]
