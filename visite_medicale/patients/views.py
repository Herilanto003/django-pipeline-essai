import django.views.generic as _view
from .models import Patients
from .forms import PatientForm
from django.urls import reverse, reverse_lazy


# Create your views here.
class PatientsIndexView(_view.ListView):
    model = Patients
    template_name = 'patients/liste-patients.html'
    context_object_name = 'patients'


class PatientsCreateView(_view.CreateView):
    model = Patients
    template_name = 'patients/ajout-patient.html'
    form_class = PatientForm
    success_url = reverse_lazy('liste-patients')

    def get_success_url(self) -> str:
        return reverse('liste-patients')
    
    def form_valid(self, form):
        return super().form_valid(form)
    

class PatientUpdateView(_view.UpdateView):
    model = Patients
    template_name = 'patients/modifier-patient.html'
    form_class = PatientForm
    success_url = reverse_lazy('liste-patients')

    def get_success_url(self) -> str:
        return reverse('liste-patients')
    
    def form_valid(self, form):
        return super().form_valid(form)
    

class PatientsDeleteView(_view.DeleteView):
    model = Patients
    template_name = 'patients/supprimer-patient.html'
    success_url = reverse_lazy('liste-patients')