from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))


""" Movie model, all fields available to be pulled from database """

class Movies(models.Model):
    id = models.IntegerField(blank=False, null=False, primary_key=True)
    rotten_tomatoes_link = models.TextField(blank=True, null=True)
    movie_title = models.TextField(blank=True, null=True)
    movie_info = models.TextField(blank=True, null=True)
    critics_consensus = models.TextField(blank=True, null=True)
    content_rating = models.TextField(blank=True, null=True)
    genres = models.TextField(blank=True, null=True)
    directors = models.TextField(blank=True, null=True)
    authors = models.TextField(blank=True, null=True)
    actors = models.TextField(blank=True, null=True)
    original_release_date = models.TextField(blank=True, null=True)
    streaming_release_date = models.TextField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)
    production_company = models.TextField(blank=True, null=True)
    tomatometer_status = models.TextField(blank=True, null=True)
    tomatometer_rating = models.IntegerField(blank=True, null=True)
    tomatometer_count = models.IntegerField(blank=True, null=True)
    audience_status = models.TextField(blank=True, null=True)
    audience_rating = models.IntegerField(blank=True, null=True)
    audience_count = models.IntegerField(blank=True, null=True)
    tomatometer_top_critics_count = models.IntegerField(blank=True, null=True)
    tomatometer_fresh_critics_count = models.IntegerField(blank=True, null=True)
    tomatometer_rotten_critics_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movies'

    def __str__(self):
        return f"{self.movie_title if self.movie_title else 'Unknown title'}"

""" Review Model """ 

class Review(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="film_review")
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name="Reviews")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        ordering = ["-created_on"]
        def __str__(self):
            return f"{self.title} | written by {self.author}"

""" Comment model """

class Comment(models.Model):
    review = models.ForeignKey('Review', on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]
        def __str__(self):
            return f"Comment {self.body} by {self.author}"
