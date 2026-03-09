from django.db import models

class Categorie(models.Model):
    name = models.CharField(max_length=50)

class Competence(models.Model):
    name = models.CharField(max_length=50)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

class Utilisateur_Competence(models.Model):
    utilisateur = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    competence = models.ForeignKey(Competence, on_delete=models.CASCADE)

