from django.shortcuts import render
from rest_framework.views import APIView
from .models import Vente
from rest_framework.response import Response
from vente.serializers import VenteSerializer

def home(request):

    return render(request)

class VenteList(APIView):

    def get(self, request):
        ventes = Vente.objects.all()
        serializer = VenteSerializer(ventes, many=True)
        return Response(serializer.data)
