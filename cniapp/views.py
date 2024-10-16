from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views import View #maybe change to list view
from .models import Review
from .forms import CommentForm
from .models import Movie
from .forms import MovieSearchForm
# Create your views here.

class Reviews(generic.ListView):
    queryset = Review.objects.all()
    template_name = "cniapp/index.html"
    paginate_by = 6


"""view for search filter"""

class MovieSearchView(View):
    template_name = "cniapp/movie_search.html"
    # starts with all movies, then filters based on form input
    def get(self, request):
        form = MovieSearchForm(request.GET)
        movies = Movie.objects.none()
        # check the movies in the database
        

        if form.is_valid():
            query = form.cleaned_data.get('query')
            genre = form.cleaned_data.get('genre')
            release_date = form.cleaned_data.get('release_date')
            # check the query is being passed here
            print("Query: ", query)

            # filters to apply if provided
            if query:
                movies = movies.filter(title__icontains=query)
            if genre:
                movies = movies.filter(genre__icontains=genre)
            if release_date:
                movies = movies.filter(release_date__icontains=release_date)
                print("Moves: ", movies)
        context = {
            'form': form,
            'movies': movies,
        }
        return render(request, self.template_name, context)

"""view for details provided from database"""

class MovieDetailView(View):
    template_name = "cniapp/movie_detail.html"

    def get(self,request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        context = {
            'movie': movie
        }
        return render(request, self.template_name, context)