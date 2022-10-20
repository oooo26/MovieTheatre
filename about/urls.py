from django.urls import path
from django.shortcuts import redirect

from . import views

app_name = "about"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("movies/", views.MovieView.as_view(), name="movie"),
    path("subscribe/", lambda req: redirect("about:subscribe", 1)),
    path("subscribe/<int:sub_type>", views.subscribe_movie, name="subscribe"),
    path("unsubscribe/<int:pk>", views.unsubscribe_movie, name="unsubscribe"),
    path("movies/star/<int:pk>", views.star_movie, name="star"),
    path("movies/unstar/<int:pk>", views.unstar_movie, name="unstar"),
    path("movies/search", views.search_movie, name="search")
]
