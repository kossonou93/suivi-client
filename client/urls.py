from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('all/', views.ClientList.as_view(), name='client-list'),
]
