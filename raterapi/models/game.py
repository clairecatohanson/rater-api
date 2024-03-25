from django.db import models
from .gamecategory import GameCategory
from django.contrib.auth.models import User


class Game(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    designer = models.CharField(max_length=100)
    year_released = models.IntegerField()
    number_players = models.IntegerField()
    estimated_time = models.DurationField()
    age_recommendation = models.IntegerField()
    categories = models.ManyToManyField("Category", through=GameCategory)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="games_added")
