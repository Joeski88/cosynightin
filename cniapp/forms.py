from django import forms
from .models import Movies, Review


class ReviewForm(forms.ModelForm):
    """ form for leaving a review """
    class Meta:
        model = Review
        fields = ['title', 'content']


class MovieSearchForm(forms.ModelForm):
    """ form for movie search and filter """
    query = forms.CharField(
        max_length=255,
        label='Search for a movie',
        required=False
        )
    genre = forms.CharField(
        max_length=50,
        label='Genre',
        required=False
        )
    release_date = forms.CharField(
        max_length=50,
        label='Release Date',
        required=False
        )
    directors = forms.CharField(
        max_length=50,
        label='Directors',
        required=False
        )
    actors = forms.CharField(
        max_length=50,
        label='Actors',
        required=False
        )
    tomatometer_rating = forms.CharField(
        max_length=50,
        label='Rating',
        required=False
        )

    class Meta:
        model = Movies
        fields = ()
        ordering = ['movie_title']
