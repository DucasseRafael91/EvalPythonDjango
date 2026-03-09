from django import forms
from django.forms import ModelForm
from .models import UserCompetence, Competence


class UserCompetenceForm(ModelForm):

    competence = forms.ModelChoiceField(queryset=None, label="Compétence")

    class Meta:
        model = UserCompetence
        fields = ['competence']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['competence'].queryset = Competence.objects.all()
