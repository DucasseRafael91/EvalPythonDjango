from django.contrib.auth import user_logged_in
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from competences.forms import UserCompetenceForm
from competences.models import Slot, Competence, UserCompetence


def index(request):
    slots_list = Slot.objects.filter(helper_user__isnull=False).order_by("-date")
    competences_list = Competence.objects.all()
    context = {"slots_list": slots_list, "competences_list": competences_list}
    return render(request, "competences/index.html", context)


@login_required
def skills(request):
    user_competences_list = UserCompetence.objects.filter(user=request.user)

    if request.method == "POST":
        form = UserCompetenceForm(request.POST)
        if form.is_valid():
            user_competence = form.save(commit=False)
            user_competence.user = request.user
            user_competence.save()
            return redirect('competences:skills')
    else:
        form = UserCompetenceForm()

    context = {"user_competences_list": user_competences_list,"form": form}
    return render(request, "competences/skills.html", context)