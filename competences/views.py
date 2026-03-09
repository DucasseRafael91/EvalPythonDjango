from django.shortcuts import render
from competences.models import Slot


def index(request):
    slots_list = Slot.objects.all()
    context = {"slots_list": slots_list}
    return render(request, "competences/index.html", context)