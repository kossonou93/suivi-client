from django.shortcuts import render
from produit.models import Produit
from produit.serializers import ProduitSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

def produit(request):

      return render(request, 'produit.html')

class ProduitList(APIView):
    def get(self, request):
        produits = Produit.objects.all()
        serializer = ProduitSerializer(produits, many=True)
        return Response(serializer.data)