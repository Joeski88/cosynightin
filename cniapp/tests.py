from django.test import TestCase
from django.urls import reverse
from .models import Movies, Review
from django.contrib.auth.models import User

class MovieSearchViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Created sample movie data for testing
        Movies.objects.create(id=1, movie_title="Inception", genres="Sci-Fi", original_release_date="2010-07-16")
        Movies.objects.create(id=2, movie_title="Interstellar", genres="Sci-Fi", original_release_date="2014-11-07")
        Movies.objects.create(id=3, movie_title="The Dark Knight", genres="Action", original_release_date="2008-07-18")

    def test_movie_search_with_query(self):
        response = self.client.get(reverse('movie_search'), {'query': 'Inception'})
        self.assertIn(response.status_code, [200, 302])
        self.assertTemplateUsed(response, 'cniapp/movie_search.html')
        self.assertContains(response, "Inception")
        self.assertNotContains(response, "Interstellar")
        self.assertNotContains(response, "The Dark Knight")

    def test_movie_search_with_genre(self):
        response = self.client.get(reverse('movie_search'), {'genre': 'Action'})
        self.assertIn(response.status_code, [200, 302])
        self.assertTemplateUsed(response, 'cniapp/movie_search.html')
        self.assertContains(response, "The Dark Knight")
        self.assertNotContains(response, "Inception")
        self.assertNotContains(response, "Interstellar")

    def test_movie_search_with_release_date(self):
        response = self.client.get(reverse('movie_search'), {'release_date': '2014-11-07'})
        self.assertIn(response.status_code, [200, 302])
        self.assertTemplateUsed(response, 'cniapp/movie_search.html')
        self.assertContains(response, "Interstellar")
        self.assertNotContains(response, "Inception")
        self.assertNotContains(response, "The Dark Knight")

    def test_movie_search_with_no_results(self):
        response = self.client.get(reverse('movie_search'), {'query': 'Nonexistent Movie'})
        self.assertIn(response.status_code, [200, 302])
        self.assertTemplateUsed(response, 'cniapp/movie_search.html')
        self.assertContains(response, "No movies found.")


class LeaveReviewViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create sample user and movie for review testing
        cls.user = User.objects.create_user(username='testuser', password='testpassword')
        cls.movie = Movies.objects.create(id=1, movie_title="Inception", genres="Sci-Fi", original_release_date="2010-07-16")

    def test_leave_review_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('leave_review', args=[self.movie.id]), {
            'title': 'Great movie!', 'slug': 'great-movie', 'content': 'Great movie!', 'status': 1,
            'rating': 5
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful review submission
        self.assertEqual(Review.objects.count(), 1)
        self.assertEqual(Review.objects.first().content, 'Great movie!')

    def test_leave_review_unauthenticated(self):
        response = self.client.post(reverse('leave_review', args=[self.movie.id]), {
            'title': 'Great movie!', 'slug': 'great-movie', 'content': 'Great movie!', 'status': 1,
            'rating': 5
        })
        self.assertEqual(response.status_code, 302)  # Redirect to login page (unauthenticated access)
        self.assertEqual(Review.objects.count(), 0)


class home_page_viewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create some sample reviews for testing the home page
        movie = Movies.objects.create(id=1, movie_title="Inception", genres="Sci-Fi", original_release_date="2010-07-16")
        Review.objects.create(movie=movie, author=User.objects.create_user('user1_unique'), title="Amazing movie!", slug="amazing-movie", content="Amazing movie!", status=1)
        Review.objects.create(movie=movie, author=User.objects.create_user('user2_unique'), title="Loved it!", slug="loved-it", content="Loved it!", status=1)

    def test_home_page(self):
        response = self.client.get(reverse('index'))
        self.assertIn(response.status_code, [200, 302])
        self.assertTemplateUsed(response, 'cniapp/index.html')
        self.assertContains(response, "Amazing movie!")
        self.assertContains(response, "Loved it!")
