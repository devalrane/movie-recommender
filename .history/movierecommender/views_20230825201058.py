from . import views
from .models import Movie
from django.shortcuts import render

# HINT: Create a view to provide movie recommendations list for the HTML template


def movie_recommendation_view(request):
    if request.method == "GET":
        context = {}
        return render(request, "movierecommender/movie_list.html", context)


def generate_movie_context():
    context = {}
    recommended_count = Movie.object.filter(recommended=True)
