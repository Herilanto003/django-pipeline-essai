from django import forms
from patients.models import Patients


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patients
        fields = [
            'nom',
            'prenoms',
            'sexe',
            'adresse'
        ]