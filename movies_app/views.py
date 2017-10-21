from django.shortcuts import render
from django.views import generic

from .models import Actor, Director, Movie
#from .forms import PersonForm
from django.views.generic.edit import CreateView, UpdateView

#from django.views.generic.edit import FormView

def home(request):
    return render(request, 'home.html')

class ActorIndexView(generic.ListView):
    template_name = 'actor_list.html'
    context_object_name = 'actors'

    def get_queryset(self):
        """Return the last five published questions."""
        return Actor.objects.order_by('birthday')

class ActorDetailView(generic.DetailView):
    model = Actor
    template_name = 'actor_detail.html'

class ActorCreateView(CreateView):
    template_name = 'actor_form.html'
    model = Actor
    success_url = '../'
    fields = [
        'first_name', 
        'last_name', 
        'slug', 
        'birthday', 
    ]

class ActorUpdateView(UpdateView):
    template_name = 'actor_form.html'
    model = Actor
    fields = [
        'first_name', 
        'last_name', 
        'slug', 
        'birthday', 
    ]

class MovieIndexView(generic.ListView):
    template_name = 'movie_list.html'
    context_object_name = 'movies'

    def get_queryset(self):
        """Return the last five published questions."""
        return Movie.objects.order_by('year')

class MovieDetailView(generic.DetailView):
    model = Movie
    template_name = 'movie_detail.html'

class MovieCreateView(CreateView):
    template_name = 'movie_form.html'
    model = Movie
    success_url = '../'
    fields = [
        'name', 
        'year', 
        'rating', 
        'director', 
        'actors', 
    ]

class MovieUpdateView(UpdateView):
    template_name = 'movie_form.html'
    model = Movie
    fields = [
        'name', 
        'year', 
        'rating', 
        'director', 
        'actors', 
    ]

class DirectorIndexView(generic.ListView):
    template_name = 'director_list.html'
    context_object_name = 'directors'

    def get_queryset(self):
        """Return the last five published questions."""
        return Director.objects.order_by('birthday')

class DirectorDetailView(generic.DetailView):
    model = Director
    template_name = 'director_detail.html'

class DirectorCreateView(CreateView):
    template_name = 'director_form.html'
    model = Director
    success_url = '../'
    fields = [
        'first_name', 
        'last_name', 
        'slug', 
        'birthday', 
    ]

class DirectorUpdateView(UpdateView):
    template_name = 'director_form.html'
    model = Director
    fields = [
        'first_name', 
        'last_name', 
        'slug', 
        'birthday', 
    ]
