from django.urls import path

from ifib.api.nuclear_medicine_intro.films.views import ListFilmView

urlpatterns = [
    path("films/", ListFilmView.as_view()),
]
