from django.db import models


# Create your models here.
class Patients(models.Model):
    nom = models.CharField(max_length=25)
    prenoms = models.CharField(max_length=255, null=True, blank=True)
    sexe = models.CharField(max_length=25)
    adresse = models.CharField(max_length=255)