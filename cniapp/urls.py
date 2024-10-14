from . import views
from django.urls import path
from .views import MovieDetailView, MovieSearchForm

urlpatterns = [
    path('/movie_detail', MovieDetailView.as_view(), name='movie_detail'),
    path('/movie_search', MovieSearchForm.as_view(), name='movie_search'),
    path('', views.Reviews.as_view(), name='home'),
]