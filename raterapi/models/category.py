from django.db import models
from .gamecategory import GameCategory


class Category(models.Model):
    name = models.CharField(max_length=80)
    games = models.ManyToManyField(
        "Game", through=GameCategory, related_name="game_categories"
    )
