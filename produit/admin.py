from django.contrib import admin
from produit import models

# Register your models here.
@admin.register(models.Produit)
class ProduitAdmin(admin.ModelAdmin):
    search_fields = ['libelle']