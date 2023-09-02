from django.db import models

# Create your models here.
class Vente(models.Model):
    date = models.DateTimeField(blank=False)
    montant = models.BigIntegerField()