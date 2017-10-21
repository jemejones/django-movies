from django.contrib import admin

# Register your models here.
from .models import Actor, Director, Movie

admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Movie)
