from django.urls import path

from . import views

urlpatterns = [
    path("teams/", views.TeamViews.as_view()),
    path("teams/<int:team_id>/", views.TeamDetailsViews.as_view()),
]
