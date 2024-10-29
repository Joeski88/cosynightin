from . import views
from django.urls import path
from .views import leave_review


urlpatterns = [
    path('', views.Review, name='home'),
    path('movie-search/', views.MovieSearchView, name='movie_search'),
    path('movie/<int:pk>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('movies/<int:movie_id>/review/', leave_review, name='leave_review'),
]