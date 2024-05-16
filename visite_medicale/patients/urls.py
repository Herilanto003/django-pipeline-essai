from django.urls import path
import patients.views as _view


urlpatterns = [
    path('', _view.PatientsIndexView.as_view(), name='liste-patients'),
    path('ajouter/', _view.PatientsCreateView.as_view(), name='ajouter-patient'),
    path('modifier/<int:pk>', _view.PatientUpdateView.as_view(), name='modifier-patient'),
    path('supprimer/<int:pk>', _view.PatientsDeleteView.as_view(), name='supprimer-patient')
]