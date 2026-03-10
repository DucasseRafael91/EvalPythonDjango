from django.contrib.auth.models import User  # type: ignore
from django.db import models  # type: ignore


class Categorie(models.Model):
    name: models.CharField = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Competence(models.Model):
    name: models.CharField = models.CharField(max_length=50)
    categorie: models.ForeignKey = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class UserCompetence(models.Model):
    user: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE)
    competence: models.ForeignKey = models.ForeignKey(Competence, on_delete=models.CASCADE)


class Slot(models.Model):
    creator_user: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                                                        related_name='slots_created')
    helper_user: models.ForeignKey = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                                       related_name='slots_helped')
    competence: models.ForeignKey = models.ForeignKey(Competence, on_delete=models.CASCADE, null=True, blank=True,)
    activity: models.CharField = models.CharField(max_length=200, null=True, blank=True,)
    date: models.DateField = models.DateField()

    def __str__(self):
        return f"{self.activity} - {self.competence} - {self.date}"

