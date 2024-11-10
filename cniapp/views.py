from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views import View
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.views.generic import TemplateView, ListView
from django.db.models import Count
from .models import Movies, Review
from .forms import MovieSearchForm, ReviewForm


def signin(request):
    """ Forces user to signin or create an account"""
    template_name = "cniapp/index.html"
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
    return redirect("/")


class HomePageView(TemplateView):
    """set which html template to use for home page """
    template_name = "cniapp/index.html"

    def get_context_data(self, **kwargs):
        # Get the context from the superclass
        context = super().get_context_data(**kwargs)
        # Query for all movies to be displayed on the home page
        movies = Movies.objects.all()
        # Instantiate the form for movie search
        form = MovieSearchForm()
        # Add the movies and form to the context
        context['movies'] = movies
        context['form'] = form

        return context


class ReviewCreateView(LoginRequiredMixin, CreateView):
    """ Movie Review View """
    model = Review
    form_class = ReviewForm
    template_name = 'cniapp/review_form.html'
    success_url = reverse_lazy('index')
    print(model, dir(model))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movie = get_object_or_404(Movies, pk=self.kwargs['movie_id'])
        # Add the movie to the context
        context['movie_title'] = movie.movie_title
        context['reviews'] = Review.objects.all()
        return context

    def form_valid(self, form):
        movie_id = self.kwargs['movie_id']
        author = self.request.user  # Set the current user as the author
        # Note: form.instance is pointing to Review model
        form.instance.author = author  # Set the current user as the author
        form.instance.movie_id = movie_id  # Associate with a movie
        return super().form_valid(form)


class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    """ View to allow user to edit/update reviews they have left """
    model = Review
    form_class = ReviewForm
    template_name = 'cniapp/review_form.html'
    success_url = reverse_lazy('index')

    def get_queryset(self):
        # Ensure that only the author can update their own review
        return Review.objects.filter(author=self.request.user)


class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    """ View to allow user to delete their own reviews """
    model = Review
    template_name = 'cniapp/review_confirm_delete.html'
    success_url = reverse_lazy('index')

    def get_queryset(self):
        # Ensure that only the author can delete their own review
        return Review.objects.filter(author=self.request.user)


class ReviewDetailView(DetailView):
    model = Review
    template_name = 'cniapp/review_detail.html'


class UserReviewsView(LoginRequiredMixin, ListView):
    model = Review
    template_name = "cniapp/user_reviews.html"
    context_object_name = "reviews"

    def get_queryset(self):
        # Get reviews written by the logged-in user
        return Review.objects.filter(author=self.request.user)


# login authentication and redirection path
@login_required(login_url="/accounts/login/")
def movie_search_view(request):
    """view for search filter"""
    template_name = "cniapp/movie_search.html"
    # starts with all movies, then filters based on form input
    form = MovieSearchForm()

    # Query for all movies, including review counts
    movies = Movies.objects.annotate(review_count=Count('Reviews'))

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

        full_search_query = []

        # filters to apply if provided
        if query:
            movies = movies.filter(movie_title__icontains=query)
            full_search_query.append(query)
        if genre:
            movies = movies.filter(genres__icontains=genre)
            full_search_query.append(genre)
        if release_date:
            movies = movies.filter(
                original_release_date__icontains=release_date)
            full_search_query.append(release_date)
        if directors:
            movies = movies.filter(directors__icontains=directors)
            full_search_query.append(directors)
        if actors:
            movies = movies.filter(actors__icontains=actors)
            full_search_query.append(actors)
        if tomatometer_rating:
            # added gt to stop filter sending only the rating provided by user
            movies = movies.filter(tomatometer_rating__gt=tomatometer_rating)
            full_search_query.append(tomatometer_rating)

        # Apply ordering by 'tomatometer_rating' after all filters are set
        movies = movies.order_by('-tomatometer_rating')

        filtered_movies_count = movies.count()
        if filtered_movies_count == all_movies_count:
            movies = []

        topn = 10  # Return just the first 10 actors
        for movie in movies:
            if movie.actors:
                movie.actors = ", ".join(
                    movie.actors.split(',')[:topn]
                ).rstrip(",")

        context = {
            'form': form,
            'movies': movies,
            'reviews': reviews,
            'search_query': " + ".join(full_search_query).rstrip(" + "),
            'search_results_total': filtered_movies_count,
        }
        return render(request, template_name, context)


class MovieDetailView(View):
    """view for details provided from database"""
    template_name = "cniapp/movie_detail.html"

    def get(self, request, pk):
        movie = get_object_or_404(
            Movies.objects.annotate(review_count=Count('Reviews')), pk=pk)

        reviews = Review.objects.all()
        reviews = reviews.filter(movie_id__exact=movie.id)

        print(movie)
        context = {
            'movie': movie,
            'reviews': reviews,
        }
        return render(request, self.template_name, context)
