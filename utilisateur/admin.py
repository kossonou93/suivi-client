from django.contrib import admin
from utilisateur import models

# Register your models here.
@admin.register(models.Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ['nom', 'prenom', 'username', 'email', 'status']
