from . import views
from django.urls import path
from .views import leave_review, home_page_view, movie_search_view, MovieDetailView


urlpatterns = [
    path('', home_page_view, name='index'),
    path('movie-search/', movie_search_view, name='movie_search'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('movies/<int:movie_id>/review/', views.leave_review, name='leave_review'),
]