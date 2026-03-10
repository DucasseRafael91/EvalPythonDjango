from django.contrib.auth.models import User
from django.db import models

class Categorie(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Competence(models.Model):
    name = models.CharField(max_length=50)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class UserCompetence(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    competence = models.ForeignKey(Competence, on_delete=models.CASCADE)

class Slot(models.Model):
    creator_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='slots_created' )
    helper_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='slots_helped')
    competence = models.ForeignKey(Competence,on_delete=models.CASCADE)
    activity = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return f"{self.activity} - {self.competence.name} - {self.date}"
