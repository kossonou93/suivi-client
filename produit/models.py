from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=150, blank=False)
    description = models.CharField(max_length=255)

class Produit(models.Model):
    libelle = models.CharField(max_length=150, blank=False)
    description = models.CharField(max_length=255)
    prix = models.BigIntegerField(blank=False)
    stock = models.IntegerField(blank=False)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    def __str__(self):
        return f"Libelle: {self.libelle} {self.description}"

    class Meta:
        ordering = ["libelle"]
