from django.urls import path
from application.usecases import medicosviews

urlpatterns = [
    path('', medicosviews.getData),
    path ('create', medicosviews.addUser),
    path ('read/<str:pk>', medicosviews.getUser),
    path ('readcpf/<str:cpf>', medicosviews.getUserCPF),
    path ('update/<str:pk>', medicosviews.updateUser),
    path ('delete/<str:pk>', medicosviews.deleteUser),
]
