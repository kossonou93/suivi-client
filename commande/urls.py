from django.urls import path, include
from . import views

urlpatterns = [
    path('all/', views.CommandeList.as_view(), name='commande-list')
]