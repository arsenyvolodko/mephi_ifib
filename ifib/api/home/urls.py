from django.urls import path

from .views import get_team_members, send_feedback_form

urlpatterns = [
    path("home/team-members/", get_team_members),
    path("home/feedback-form", send_feedback_form)
]
