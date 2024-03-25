from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    game = models.ForeignKey(
        "Game", on_delete=models.CASCADE, related_name="game_reviews"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviews_given"
    )
