from django.db import models

class Utilisateur(models.Model):

    TYPE_ADMIN = 'admin'
    TYPE_DEVELOPER = 'developer'
    TYPE_UTILISATEUR = 'utilisateur'

    TYPE_CHOICES = (
        (TYPE_ADMIN, 'Admin'),
        (TYPE_DEVELOPER, 'Developer'),
        (TYPE_UTILISATEUR, 'Utilisateur')
    )

    STATUS_ACTIVE = 'activer'
    STATUS_DESACTIVE = 'desactiver'
    STATUS_EN_ATTENTE = 'en attente'
    STATUS_SUSPENDU = 'suspendu'

    STATUS_CHOICES = (
        (STATUS_ACTIVE, 'Activer'),
        (STATUS_DESACTIVE, 'Desactiver'),
        (STATUS_SUSPENDU, 'Suspendu'),
        (STATUS_EN_ATTENTE, 'En Attente')
    )

    CIVILITE_MR = 'MR'
    CIVILITE_MME = 'MME'
    CIVILITE_MLLE = 'MLLE'

    CIVILITE_CHOICES = (
        (CIVILITE_MR, 'Mr'),
        (CIVILITE_MME, 'Mme'),
        (CIVILITE_MLLE, 'Mlle')
    )

    nom = models.CharField(max_length=100, blank=False)
    prenom = models.CharField(max_length=100)
    civilite = models.CharField(max_length=50, choices=CIVILITE_CHOICES)
    fonction = models.CharField(max_length=100)
    username = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES, default='Utilisateur')
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='En Attente')

# Create your models here.
