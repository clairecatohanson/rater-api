from django.db import models
from django.core import validators
from django.contrib.auth.models import User


class Rating(models.Model):
    value = models.IntegerField(
        validators=[
            validators.MinValueValidator(limit_value=1),
            validators.MaxValueValidator(limit_value=5),
        ]
    )
    game = models.ForeignKey(
        "Game", on_delete=models.CASCADE, related_name="game_ratings"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="ratings_given"
    )
