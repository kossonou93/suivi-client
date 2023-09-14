from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UtilisateurSerializer
from .models import Utilisateur

class UtilisateurList(APIView):
    def get(self, request):
        utilisateurs = Utilisateur.objects.all()
        serializer = UtilisateurSerializer(utilisateurs, many=True)
        return Response(serializer.data)

# Create your views here.
