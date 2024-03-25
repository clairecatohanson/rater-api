from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    upload = models.ImageField()
    game = models.ForeignKey(
        "Game", on_delete=models.CASCADE, related_name="game_pictures"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="pictures_added"
    )
