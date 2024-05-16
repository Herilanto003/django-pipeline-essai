from django.urls import path
from .views import MedecinsIndexView, MedecinsCreateview, MedecinsUpdateView, MedecinsDeleteView


# urls pour medecins
urlpatterns = [
    path("", MedecinsIndexView.as_view(), name="liste-medecins"),
    path('ajouter/', MedecinsCreateview.as_view(), name='ajout-medecin'),
    path('modifier/<int:pk>', MedecinsUpdateView.as_view(), name='modifier-medecins'),
    path('supprimer/<int:pk>', MedecinsDeleteView.as_view(), name='supprimer-medecins') 
]