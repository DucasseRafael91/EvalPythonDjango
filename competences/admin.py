from django.contrib import admin
from competences.models import Categorie, Competence, UtilisateurCompetence, Slot

admin.site.register(Categorie)
admin.site.register(Competence)
admin.site.register(UtilisateurCompetence)
admin.site.register(Slot)
