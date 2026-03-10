from django.contrib.auth.decorators import login_required  # type: ignore
from django.shortcuts import render  # type: ignore
from django.shortcuts import get_object_or_404, redirect
from .models import Slot
from competences.forms import UserCompetenceForm, SlotForm
from competences.models import Competence, UserCompetence


def index(request):
    slots_list = Slot.objects.filter(helper_user__isnull=False).order_by("-date")
    competences_list = Competence.objects.all()
    my_slots_list_proposed = []
    if request.user.is_authenticated:
        my_slots_list_proposed = (Slot.objects
                                  .filter(creator_user=request.user)
                                  .filter(helper_user__isnull=False)
                                  .order_by("-date"))
    context = {"slots_list": slots_list,
               "competences_list": competences_list,
               "my_slots_list_proposed": my_slots_list_proposed}
    return render(request, "competences/index.html", context)


@login_required
def skills(request):
    user_competences_list = UserCompetence.objects.filter(user=request.user)
    available_competences = Competence.objects.exclude(usercompetence__in=user_competences_list)

    if request.method == "POST":
        form = UserCompetenceForm(request.POST)
        form.fields["competence"].queryset = available_competences

        if form.is_valid():
            user_competence = form.save(commit=False)
            user_competence.user = request.user
            user_competence.save()
            return redirect("competences:skills")
    else:
        form = UserCompetenceForm()
        form.fields["competence"].queryset = available_competences

    context = {"user_competences_list": user_competences_list,
               "available_competences": available_competences,
               "form": form}

    return render(request, "competences/skills.html", context)

@login_required
def add_slot(request):
    used_competences = UserCompetence.objects.filter(user=request.user)
    available_competences = Competence.objects.exclude(usercompetence__in=used_competences)

    if request.method == "POST":
        form = SlotForm(request.POST)
        form.fields['competence'].queryset = available_competences

        if form.is_valid():
            slot = form.save(commit=False)
            slot.creator_user = request.user
            slot.save()
            return redirect("competences:index")
    else:
        form = SlotForm()
        form.fields['competence'].queryset = available_competences

    return render(request, "competences/add.html", {"form": form})

def search(request):
    slots_list = Slot.objects.filter(helper_user__isnull=True).exclude(creator_user=request.user)
    context = {"slots_list": slots_list}
    return render(request, "competences/search.html", context)

def purpose_help(request, slot_id):
    slot = get_object_or_404(Slot, id=slot_id)
    slot.helper_user = request.user
    slot.save()
    return redirect("competences:index")
