from django.contrib.auth import user_logged_in
from django.shortcuts import render
from competences.models import Slot, Competence, UserCompetence


def index(request):
    slots_list = Slot.objects.filter(helper_user__isnull=False).order_by("-date")
    competences_list = Competence.objects.all()
    context = {"slots_list": slots_list, "competences_list": competences_list}
    return render(request, "competences/index.html", context)

def skills(request):
    user_competences_list = UserCompetence.objects.filter(user = request.user)
    context = {"user_competences_list": user_competences_list}
    return render(request, "competences/skills.html", context)