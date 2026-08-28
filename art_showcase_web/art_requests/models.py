from django.db import models

from art_showcase_web.artwork.models import TypeOfArt

# Create your models here.

class ArtRequest(models.Model):
    category = models.ForeignKey(TypeOfArt, on_delete=models.CASCADE)
    deadline = models.DateField()
    description = models.TextField()
    done = models.BooleanField(default=False)
    discount = models.FloatField(default=0.0)

class Annexes(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to="annexes/")
    art_request_referenced = models.ForeignKey(ArtRequest, on_delete=models.CASCADE, null=True, blank=True)