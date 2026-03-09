from django.contrib import admin
from competences.models import Categorie, Competence, UserCompetence, Slot

class CategorieAdmin(admin.ModelAdmin):
    list_display = ["name"]

class CompetenceAdmin(admin.ModelAdmin):
    list_display = ["name", "categorie"]


class UserCompetenceAdmin(admin.ModelAdmin):
    list_display = ["user", "competence"]

class SlotAdmin(admin.ModelAdmin):
    list_display = ["activity", "competence", "date", "creator_user", "helper_user"]


admin.site.register(Categorie,CategorieAdmin)
admin.site.register(Competence, CompetenceAdmin)
admin.site.register(UserCompetence, UserCompetenceAdmin)
admin.site.register(Slot, SlotAdmin)
