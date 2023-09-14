from django.shortcuts import render
from rest_framework.views import APIView
from .models import Commande
from rest_framework.response import Response
from commande.serializers import CommandeSerializer

class CommandeList(APIView):

    def get(self, request):
        commandes = Commande.objects.all()
        serializer = CommandeSerializer(commandes, many=True)
        return Response(serializer.data)
