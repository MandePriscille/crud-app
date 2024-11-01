from django.db import models

# Create your models here.
from django.db import models

class Employe(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=15, blank=True)
    date_naissance = models.DateField()
    date_embauche = models.DateField()
    poste = models.CharField(max_length=100)
    salaire = models.DecimalField(max_digits=10, decimal_places=2)
    adresse = models.TextField(blank=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"