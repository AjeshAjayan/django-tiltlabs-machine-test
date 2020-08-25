from django.db import models
from authentication.models import User

# Create your models here.
class Games(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=2500)

class GamesRatings(models.Model):
    game_id = models.ForeignKey(Games, on_delete= models.CASCADE, blank=True, null=True)
    user_id = models.ForeignKey(User, on_delete= models.CASCADE, blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)