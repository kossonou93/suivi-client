from django.contrib import admin
from client import models

# Register your models here.
@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['nom']
