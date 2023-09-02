from django.db import models

class Produit(models.Model):
    libelle = models.CharField(max_length=150, blank=False)
    description = models.CharField(max_length=255)
    prix = models.BigIntegerField(blank=False)
    stock = models.IntegerField(blank=False)
