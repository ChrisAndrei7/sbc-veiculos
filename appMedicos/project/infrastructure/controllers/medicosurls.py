from django.urls import path
from application.usecases import medicosviews

urlpatterns = [
    path('', medicosviews.getData),
    path ('create', medicosviews.addMedico),
    path ('read/<str:pk>', medicosviews.getMedico),
    path ('readcpf/<str:cpf>', medicosviews.getMedicoCPF),
    path ('update/<str:pk>', medicosviews.updateMedico),
    path ('delete/<str:pk>', medicosviews.deleteMedico),
]
