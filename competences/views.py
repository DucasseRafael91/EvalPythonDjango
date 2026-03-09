from django.shortcuts import render
from competences.models import Slot, Competence


def index(request):
    slots_list = Slot.objects.filter(helper_user__isnull=False).order_by("-date")
    competences_list = Competence.objects.all()
    context = {"slots_list": slots_list, "competences_list": competences_list}
    return render(request, "competences/index.html", context)