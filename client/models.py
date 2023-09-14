from django.db import models

class Client(models.Model):
    nom = models.CharField(max_length=100, blank=False)
    prenom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)

class Adresse(models.Model):
    ville = models.CharField(max_length=100, blank=False)
    code_postal = models.CharField(max_length=50, blank=False)
    rue = models.CharField(max_length=50)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='adresses')




