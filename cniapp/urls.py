from . import views
from django.urls import path


urlpatterns = [
    path('', views.Reviews.as_view(), name='home'),
    path('movie-search/', views.MovieSearchView.as_view(), name='movie_search'),
    path('movie/<int:pk>/', views.MovieDetailView.as_view(), name='movie_detail'),
]