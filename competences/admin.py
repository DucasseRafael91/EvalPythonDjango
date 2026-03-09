from django.contrib import admin
from competences.models import Categorie, Competence, UtilisateurCompetence, Slot

class CategorieAdmin(admin.ModelAdmin):
    list_display = ["name"]

class CompetenceAdmin(admin.ModelAdmin):
    list_display = ["name", "categorie"]


admin.site.register(Categorie,CategorieAdmin)
admin.site.register(Competence, CompetenceAdmin)
admin.site.register(UtilisateurCompetence)
admin.site.register(Slot)
