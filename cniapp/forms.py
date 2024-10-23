from django import forms
from .models import Movies
from .models import Comment

""" form for movie commenting """
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

""" form for movie search and filter """
class MovieSearchForm(forms.ModelForm):
    query = forms.CharField(max_length=255, label='Search for a movie', required=False)
    genre = forms.CharField(max_length=50, label='Genre', required=False)
    release_date = forms.CharField(max_length=50, label='Release Date', required=False)
    directors = forms.CharField(max_length=50, label='Directors', required=False)
    actors = forms.CharField(max_length=50, label='Actors', required=False)
    tomatometer_rating = forms.CharField(max_length=50, label='Rating', required=False)
    
    class Meta:
        model = Movies
        fields = ()
        ordering = ['movie_title']