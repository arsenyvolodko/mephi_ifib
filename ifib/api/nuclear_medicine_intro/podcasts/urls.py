from django.urls import path

from ifib.api.nuclear_medicine_intro.podcasts.views import ListPodcastsView

urlpatterns = [
    path("podcasts/", ListPodcastsView.as_view()),
]
