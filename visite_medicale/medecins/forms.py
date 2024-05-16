from django import forms
from medecins.models import Medecins


class MedecinForm(forms.ModelForm):
    class Meta:
        model = Medecins
        fields = [
            'nom',
            'prenoms',
            'grade'
        ]