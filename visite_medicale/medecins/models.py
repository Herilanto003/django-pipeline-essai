from django.db import models


# Create your models here.
class Medecins(models.Model):
    nom = models.CharField(max_length=25)
    prenoms = models.CharField(max_length=255, null=True, blank=True)
    grade = models.CharField(max_length=25)