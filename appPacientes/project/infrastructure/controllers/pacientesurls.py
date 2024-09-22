from django.urls import path
from application.usecases import pacientesviews

urlpatterns = [
    path('', pacientesviews.getData),
    path ('create', pacientesviews.addPaciente),
    path ('read/<str:pk>', pacientesviews.getPaciente),
    path ('readcpf/<str:cpf>', pacientesviews.getPacienteCPF),
    path ('update/<str:pk>', pacientesviews.updatePaciente),
    path ('delete/<str:pk>', pacientesviews.deletePaciente),
    path ('readmed/<str:data>/<str:horario>', pacientesviews.getMedicosDisponiveis),
]
