from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.produit, name='home'),
    path('all/', views.ProduitList.as_view(), name='produit-list'),
]
