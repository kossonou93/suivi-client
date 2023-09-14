from django.db import models

class Fournisseur(models.Model):
    nom = models.CharField(max_length=100, blank=False)
    prenom = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
# Create your models here.
