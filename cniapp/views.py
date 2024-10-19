from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views import View #maybe change to list view
from .models import Review
from .forms import CommentForm
from .models import Movies
from .forms import MovieSearchForm
# Create your views here.

class Reviews(generic.ListView):
    queryset = Review.objects.all()
    template_name = "cniapp/index.html"
    paginate_by = 6


"""view for search filter"""

def MovieSearchView(request):
    template_name = "cniapp/movie_search.html"
    # starts with all movies, then filters based on form input
    form = MovieSearchForm()
    movies = Movies.objects.all()
    all_movies_count = Movies.objects.count()


    # check the movies in the database
    if request.method == 'GET':
        query = request.GET.get('query')
        genre = request.GET.get('genre')
        release_date = request.GET.get('release_date')
        directors = request.GET.get('directors')
        actors = request.GET.get('actors')
        tomatometer_rating = request.GET.get('tomatometer_rating')
        # check the query is being passed here
        print("Query: ", query)

        # filters to apply if provided
        if query:
            movies = movies.filter(movie_title__icontains=query)
        if genre:
            movies = movies.filter(genres__icontains=genre)
        if release_date:
            movies = movies.filter(original_release_date__icontains=release_date)
        if directors: 
            directors = movies.filter(directors__icontains=directors)
        if actors: 
            actors = movies.filter(actors__icontains=actors)
        if tomatometer_rating: 
            tomatometer_rating = movies.filter(tomatometer_rating__icontains=tomatometer_rating)    
            print(query, movies)

        filtered_movies_count = movies.count()
        if filtered_movies_count == all_movies_count:
            movies = []
        return render(request, template_name, {'form': form, 'movies': movies}) 

"""view for details provided from database"""

class MovieDetailView(View):
    template_name = "cniapp/movie_detail.html"

    def get(self,request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        context = {
            'movie': movie
        }
        return render(request, self.template_name, context)