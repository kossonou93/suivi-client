from django.contrib import admin
from vente.models import Vente

# Register your models here.
@admin.register(Vente)
class VenteAdmin(admin.ModelAdmin):
    search_fields = ['date']
