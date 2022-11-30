from django.urls import path

from . import views

urlpatterns = [
    path("teams/", views.TeamViews.as_view()),
]
