from . import views
from .models import Movie
from django.shortcuts import render

# HINT: Create a view to provide movie recommendations list for the HTML template


def movie_recommendation_view(request):
    context = {}

    return render(request, "movierecommender/movie_list.html", context)
