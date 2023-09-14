from django.db import models
from produit.models import Produit
from client.models import Client

class Commande(models.Model):
    STATUS_EN_ATTENTE = 'en attente'
    STATUS_EN_COURS_DE_TRAITEMENT = 'en cours de traitement'
    STATUS_EXPEDIER = 'expedier'
    STATUS_LIVRER = 'livrer'
    STATUS_ANNULER = 'annuler'

    STATUS_CHOICES = (
        (STATUS_EN_ATTENTE, 'En Attente'),
        (STATUS_EN_COURS_DE_TRAITEMENT, 'En Cours De Traitement'),
        (STATUS_EXPEDIER, 'Expedier'),
        (STATUS_LIVRER, 'Livrer'),
        (STATUS_ANNULER, 'Annuler')
    )

    produits = models.ManyToManyField(Produit)
    client = models.ForeignKey(Client, related_name='clients', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)



# Create your models here.
