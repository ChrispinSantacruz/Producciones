# api_produccion/models.py

from django.db import models
from django.contrib.auth.models import User

class Content(models.Model):
    TYPE_CHOICES = (
        ('movie', 'Movie'),
        ('series', 'Series'),
    )

    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    title = models.CharField(max_length=255)
    poster_url = models.URLField()
    trailer_url = models.URLField()
    duration_minutes = models.PositiveIntegerField(blank=True, null=True)
    num_episodes = models.PositiveIntegerField(blank=True, null=True)
    actors = models.ManyToManyField('Actor', related_name='contents', blank=True)
    directors = models.ManyToManyField('Director', related_name='contents', blank=True)
    genres = models.ManyToManyField('Genre', related_name='contents', blank=True)

    def __str__(self):
        return self.title

class Rating(models.Model):
    content = models.ForeignKey(Content, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='ratings', on_delete=models.CASCADE)
    stars = models.DecimalField(max_digits=3, decimal_places=1)

    class Meta:
        unique_together = ('content', 'user')

    def __str__(self):
        return f'{self.content.title} - {self.stars} stars by {self.user.username}'

class Actor(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
