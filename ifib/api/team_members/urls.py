from django.urls import path

from .views import get_team_members

urlpatterns = [
    path("home/team-members/", get_team_members),
]
