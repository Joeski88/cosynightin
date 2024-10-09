from django.shortcuts import render
from django.views import generic
from .models import Review
from .forms import CommentForm
# Create your views here.

class Reviews(generic.ListView):
    queryset = Review.objects.all()
    template_name = "cniapp/index.html"
    paginate_by = 6
