from typing import List

from django.contrib.auth.decorators import login_required
from django.db.models import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from competences.forms import UserCompetenceForm, SlotForm, AvailableForm, SubmitAvailableForm
from competences.models import Competence, UserCompetence, Slot




def index(request: HttpRequest) -> HttpResponse:
    '''
    Affiche la page d'accueil avec les créneaux proposés, les compétences disponibles et les créneaux proposés par l'utilisateur connecté.

    Param request : HttpRequest - la requête HTTP reçue par la vue.
    Return : HttpResponse - la réponse HTTP contenant le rendu de la page d'accueil.
    '''
    slots_list: QuerySet[Slot] = (Slot.objects
                                  .filter(helper_user__isnull=False)
                                  .filter(creator_user__isnull=False)
                                  .order_by("-date"))
    competences_list: QuerySet[Competence] = Competence.objects.all()

    my_slots_list_proposed: QuerySet[Slot] | List[Slot] = []

    if request.user.is_authenticated:
        my_slots_list_proposed = (
            Slot.objects
            .filter(creator_user=request.user, helper_user__isnull=False)
            .order_by("-date")
        )

    context = {
        "slots_list": slots_list,
        "competences_list": competences_list,
        "my_slots_list_proposed": my_slots_list_proposed,
    }
    return render(request, "competences/index.html", context)


@login_required
def skills(request: HttpRequest) -> HttpResponse:
    '''
    Affiche la page des compétences de l'utilisateur connecté, avec un formulaire pour ajouter de nouvelles compétences.

    Param request : HttpRequest - la requête HTTP reçue par la vue.
    Return : HttpResponse - la réponse HTTP contenant le rendu de la page d'accueil.
    '''
    user_competences_list: QuerySet[UserCompetence] = UserCompetence.objects.filter(user=request.user)
    available_competences: QuerySet[Competence] = Competence.objects.exclude(usercompetence__in=user_competences_list)

    if request.method == "POST":
        form = UserCompetenceForm(request.POST)
        form.fields["competence"].queryset = available_competences

        if form.is_valid():
            user_competence: UserCompetence = form.save(commit=False)
            user_competence.user = request.user
            user_competence.save()
            return redirect("competences:skills")
    else:
        form = UserCompetenceForm()
        form.fields["competence"].queryset = available_competences

    context = {
        "user_competences_list": user_competences_list,
        "available_competences": available_competences,
        "form": form,
    }
    return render(request, "competences/skills.html", context)


@login_required
def available(request: HttpRequest) -> HttpResponse:
    '''
    Affiche la page des créneaux disponibles proposés par l'utilisateur connecté, avec un formulaire pour ajouter de nouveaux créneaux.

    Param request : HttpRequest - la requête HTTP reçue par la vue.
    Return : HttpResponse - la réponse HTTP contenant le rendu de la page d'accueil.
    '''
    available_slots_list: QuerySet[Slot] = (Slot.objects.filter(helper_user=request.user)
                                            .filter(creator_user__isnull=True)
                                            .order_by("-date"))

    if request.method == "POST":
        form = AvailableForm(request.POST)

        if form.is_valid():
            slot: Slot = form.save(commit=False)
            slot.helper_user = request.user
            slot.save()
            return redirect("competences:available")
    else:
        form = AvailableForm()

    context = {"form": form, "available_slots_list": available_slots_list}
    return render(request, "competences/available.html", context)

@login_required
def add_slot(request: HttpRequest) -> HttpResponse:

    '''
    Affiche la page pour ajouter un créneau proposé par l'utilisateur connecté, avec un formulaire pour ajouter de nouveaux créneaux.

    Param request : HttpRequest - la requête HTTP reçue par la vue.
    Return : HttpResponse - la réponse HTTP contenant le rendu de la page d'accueil.
    '''
    used_competences: QuerySet[UserCompetence] = UserCompetence.objects.filter(user=request.user)
    available_competences: QuerySet[Competence] = Competence.objects.exclude(usercompetence__in=used_competences)

    if request.method == "POST":
        form = SlotForm(request.POST)
        form.fields["competence"].queryset = available_competences

        if form.is_valid():
            slot: Slot = form.save(commit=False)
            slot.creator_user = request.user
            slot.save()
            return redirect("competences:index")
    else:
        form = SlotForm()
        form.fields["competence"].queryset = available_competences

    return render(request, "competences/add.html", {"form": form})

@login_required
def submit_available(request, slot_id):
    '''
    Affiche la page pour soumettre un créneau disponible proposé par l'utilisateur connecté, avec un formulaire pour ajouter de nouveaux créneaux.

    Param request : HttpRequest - la requête HTTP reçue par la vue.
    Return : HttpResponse - la réponse HTTP contenant le rendu de la page d'accueil.
    '''

    slot = get_object_or_404(Slot, id=slot_id)

    used_competences = UserCompetence.objects.filter(user=request.user)
    available_competences = Competence.objects.exclude(usercompetence__in=used_competences)

    if request.method == "POST":
        form = SubmitAvailableForm(request.POST, instance=slot)
        form.fields["competence"].queryset = available_competences

        if form.is_valid():
            slot = form.save(commit=False)
            slot.creator_user = request.user
            slot.save()
            return redirect("competences:index")

    else:
        form = SubmitAvailableForm(instance=slot)
        form.fields["competence"].queryset = available_competences

    return render(request, "competences/form_submit_available.html", {
        "form": form,
        "slot": slot
    })

@login_required
def search(request: HttpRequest) -> HttpResponse:
    '''
    Affiche la page de recherche de créneaux proposés par d'autres utilisateurs, avec une liste de créneaux disponibles.

    Param request : HttpRequest - la requête HTTP reçue par la vue.
    Return : HttpResponse - la réponse HTTP contenant le rendu de la page d'accueil.
    '''
    slots_list: QuerySet[Slot] = Slot.objects.filter(helper_user__isnull=True).exclude(creator_user=request.user)
    context = {"slots_list": slots_list}
    return render(request, "competences/search.html", context)

@login_required
def search_available_slots(request: HttpRequest) -> HttpResponse:
    '''
    Affiche la page de recherche de créneaux proposés par d'autres utilisateurs, avec une liste de créneaux disponibles.

    Param request : HttpRequest - la requête HTTP reçue par la vue.
    Return : HttpResponse - la réponse HTTP contenant le rendu de la page d'accueil.
    '''
    slots_list: QuerySet[Slot] = (Slot.objects
                                  .filter(helper_user__isnull=False)
                                  .filter(creator_user__isnull=True)
                                  .exclude(helper_user=request.user))
    context = {"slots_list": slots_list}
    return render(request, "competences/search_available_slots.html", context)


@login_required
def purpose_help(request: HttpRequest, slot_id: int) -> HttpResponse:
    '''
    Fonction pour proposer de l'aide pour un créneau proposé par un autre utilisateur

    Param request : HttpRequest - la requête HTTP reçue par la vue.
    Return : HttpResponse - la réponse HTTP contenant le rendu de la page d'accueil.
    '''
    slot: Slot = get_object_or_404(Slot, id=slot_id)
    slot.helper_user = request.user
    slot.save()
    return redirect("competences:index")
