from django.contrib.auth.models import User
from django.db import models

class Categorie(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Competence(models.Model):
    name = models.CharField(max_length=50)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

class UtilisateurCompetence(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    competence = models.ForeignKey(Competence, on_delete=models.CASCADE)

class Slot(models.Model):
    creator_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='slots_created' )
    helper_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='slots_helped')
    activity = models.CharField(max_length=2002)
    date = models.DateTimeField()
