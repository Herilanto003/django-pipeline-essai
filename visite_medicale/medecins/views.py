from django.forms import BaseModelForm
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Medecins
from .forms import MedecinForm
from django.urls import reverse, reverse_lazy


# Create your views here.
class MedecinsIndexView(ListView):
    model = Medecins
    template_name = "medecins/liste-medecins.html"
    context_object_name = "medecins"



class MedecinsCreateview(CreateView):
    model = Medecins
    template_name = 'medecins/ajout-medecin.html'
    form_class = MedecinForm
    success_url = reverse_lazy('liste-medecins')

    def get_success_url(self) -> str:
        return reverse('liste-medecins')
    
    def form_valid(self, form):
        return super().form_valid(form)
    

class MedecinsUpdateView(UpdateView):
    model = Medecins
    template_name = 'medecins/modifier-medecin.html'
    form_class = MedecinForm
    success_url = reverse_lazy('liste-medecins')

    def get_success_url(self) -> str:
        return reverse('liste-medecins')
    
    def form_valid(self, form):
        return super().form_valid(form)
    

class MedecinsDeleteView(DeleteView):
    model = Medecins
    template_name = 'medecins/supprimer-medecin.html'
    success_url = reverse_lazy('liste-medecins')