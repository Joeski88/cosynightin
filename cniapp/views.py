from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views import View
from django.views.generic import TemplateView 
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import CommentForm
from .models import Movies
from .forms import MovieSearchForm, ReviewForm


"""set which html template to use for home page """
class HomePageView(generic.ListView):
    queryset = Review.objects.all()
    template_name = "cniapp/index.html"


""" Movie Review View """
def leave_review(request, movie_id):
    movie = get_object_or_404(Movies, id=movie_id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user  # Set the current user as the author
            review.movie = movie  # Associate the review with the movie
            review.slug = str(review.movie_id) + "-" + movie.movie_title
            review.save()
            return redirect('movie_detail', pk=movie_id)  # Redirect to the movie detail page
    else:
        form = ReviewForm()

    return render(request, 'cniapp/leave_review.html', {'form': form, 'movie': movie})


"""view for search filter"""
# login authentication and redirection path
@login_required(login_url="/accounts/login/")
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

        # Pulls all reviews
        reviews = Review.objects.all()

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
            movies = movies.filter(directors__icontains=directors)
        if actors: 
            movies = movies.filter(actors__icontains=actors)
        if tomatometer_rating:
            # added gt to stop filter sending only the specific rating provided by user 
            movies = movies.filter(tomatometer_rating__gt=tomatometer_rating)    
            print(query, movies)

        filtered_movies_count = movies.count()
        if filtered_movies_count == all_movies_count:
            movies = []
        
        context = {'form': form,
                'movies': movies,
                'reviews': reviews
                    }
        return render(request, template_name, context) 

"""view for details provided from database"""

class MovieDetailView(View):
    template_name = "cniapp/movie_detail.html"

    def get(self,request, pk):
        movie = get_object_or_404(Movies, pk=pk)
        reviews = Reviews.objects.all()
        reviews = reviews.filter(movie_id__exact=movie.id)
        context = {
            'movie': movie,
            'reviews': reviews,
        }
        return render(request, self.template_name, context)