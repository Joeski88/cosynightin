from django.test import TestCase
from django.urls import reverse
from .models import Movies
from .forms import MovieSearchForm

"""
test code for movie search view
"""

class MovieSearchViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Created sample movie data for testing
        Movies.objects.create(movie_title="Inception", genres="Sci-Fi", original_release_date="2010-07-16")
        Movies.objects.create(movie_title="Interstellar", genres="Sci-Fi", original_release_date="2014-11-07")
        Movies.objects.create(movie_title="The Dark Knight", genres="Action", original_release_date="2008-07-18")

    def test_movie_search_with_query(self):
        response = self.client.get(reverse('movie-search'), {'query': 'Inception'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cniapp/movie_search.html')
        self.assertContains(response, "Inception")
        self.assertNotContains(response, "Interstellar")
        self.assertNotContains(response, "The Dark Knight")

    def test_movie_search_with_genre(self):
        response = self.client.get(reverse('movie-search'), {'genre': 'Action'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cniapp/movie_search.html')
        self.assertContains(response, "The Dark Knight")
        self.assertNotContains(response, "Inception")
        self.assertNotContains(response, "Interstellar")

    def test_movie_search_with_release_date(self):
        response = self.client.get(reverse('movie-search'), {'release_date': '2014-11-07'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cniapp/movie_search.html')
        self.assertContains(response, "Interstellar")
        self.assertNotContains(response, "Inception")
        self.assertNotContains(response, "The Dark Knight")

    def test_movie_search_with_no_results(self):
        response = self.client.get(reverse('movie-search'), {'query': 'Nonexistent Movie'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cniapp/movie_search.html')
        self.assertContains(response, "No movies found.")

