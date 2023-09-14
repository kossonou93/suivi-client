from django.contrib import admin
from commande import models

@admin.register(models.Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ['client', 'date', 'status']

# Register your models here.
