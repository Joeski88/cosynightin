from . import views
from django.urls import path
from .views import signin, HomePageView, movie_search_view, MovieDetailView
from .views import ReviewCreateView, ReviewUpdateView, ReviewDeleteView
from .views import ReviewDetailView, UserReviewsView


urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('signin/', signin, name="signin"),
    path('movie-search/', movie_search_view, name='movie_search'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),

    # CRUD for Reviews
    path('review/<int:pk>/', ReviewDetailView.as_view(), name='review_detail'),
    path('movie/<int:movie_id>/review/add/', ReviewCreateView.as_view(),
         name='review_add'),
    path('review/<int:pk>/update/', ReviewUpdateView.as_view(),
         name='review_update'),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(),
         name='review_delete'),
    path('user/<int:pk>/reviews/', UserReviewsView.as_view(),
         name='user_reviews'),
]
