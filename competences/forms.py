from django import forms  # type: ignore
from django.forms import ModelForm  # type: ignore
from .models import UserCompetence, Competence, Slot

class UserCompetenceForm(ModelForm):

    competence = forms.ModelChoiceField(queryset=None, label="Compétence")

    class Meta:
        model = UserCompetence
        fields = ['competence']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['competence'].queryset = Competence.objects.all()


class SlotForm(ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    competence = forms.ModelChoiceField(queryset=None, label="Compétence")

    class Meta:
        model = Slot
        fields = ['activity', 'competence', 'date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['competence'].queryset = Competence.objects.all()
