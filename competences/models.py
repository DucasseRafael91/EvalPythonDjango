from django.db import models

class Categorie(models.Model):
    name = models.CharField(max_length=50)

class Competence(models.Model):
    name = models.CharField(max_length=50)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
