from django.urls import path
from application.usecases import usuariosviews

urlpatterns = [
    path('', usuariosviews.getData),
    path ('create', usuariosviews.addUser),
    path ('read/<str:pk>', usuariosviews.getUser),
    path ('readcpf/<str:cpf>', usuariosviews.getUserCPF),
    path ('update/<str:pk>', usuariosviews.updateUser),
    path ('delete/<str:pk>', usuariosviews.deleteUser),
]
