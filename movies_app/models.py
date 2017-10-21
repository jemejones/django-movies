from django.db import models
from django.urls import reverse

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    birthday = models.DateField()

    class Meta:
        abstract = True

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Actor(Person):

    def get_absolute_url(self):
        return reverse('actor-detail', kwargs={'pk': self.pk})

class Director(Person):

    def get_absolute_url(self):
        return reverse('director-detail', kwargs={'pk': self.pk})

class Movie(models.Model):
    name = models.CharField(max_length=250)
    year = models.IntegerField()
    RATINGS = [
        ('G', 'G - General Audiences'),
        ('PG', 'PG - Parental Guidance Suggested'),
        ('PG-13', 'PG-13 - Parents Strongly Cautioned'),
        ('R', 'R - Restricted'),
        ('NC-17', 'NC-17 - No One Under 17 Admitted'),

    ]
    rating = models.CharField(max_length=7, choices=RATINGS)
    director = models.ForeignKey(Director, related_name='movies')
    actors = models.ManyToManyField(Actor, related_name='movies')

    def __str__(self):
        return '{} ({})'.format(self.name, self.year)

    def get_absolute_url(self):
        return reverse('movie-detail', kwargs={'pk': self.pk})
