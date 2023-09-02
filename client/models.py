from django.db import models

class Client(models.Model):
    nom = models.CharField(max_length=100, blank=False)
    prenom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)




