from django import forms
from .models import Movie
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class MovieSearchForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"
        ordering = ['title']
    query = forms.CharField(max_length=255, label='Search for a movie', required=False)
    genre = forms.CharField(max_length=100, label='Genre', required=False)
    release_date = forms.CharField(max_length=100, label='Release Date', required=False)