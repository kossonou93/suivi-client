from django.urls import path, include
from . import views

urlpatterns = [
    path('lister/', views.UtilisateurList.as_view(), name='utilisateur-list')
]