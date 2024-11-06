from . import views
from django.urls import path
from .views import leave_review, HomePageView, MovieSearchView, MovieDetailView


urlpatterns = [
    path('', HomePageView, name='index'),
    path('movie-search/', MovieSearchView, name='movie_search'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('movies/<int:movie_id>/review/', views.leave_review, name='leave_review'),
]