from django.test import TestCase
from produit.models import Produit

class ProduitModelTest(TestCase):

    @classmethod
    def create_produit(cls):
        Produit.objects.create(libelle="Iphone 14 Pro Max", description="Téléphone Apple", prix=14500, stock=25)

    def test_produit_creation(self):
        try:
            p = Produit.objects.get(libelle="Iphone 14 Pro Max")
            self.assertEquals(p.libelle, "Iphone 14 Pro Max")
        except Produit.DoesNotExist:
            print("Produit n'existe pas")