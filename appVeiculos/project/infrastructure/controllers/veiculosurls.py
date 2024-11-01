from django.urls import path
from application.usecases import veiculosviews

urlpatterns = [
    path('', veiculosviews.getData),
    path('create', veiculosviews.addVeiculo),
    path('read/<str:pk>', veiculosviews.getVeiculo),
    path('readplaca/<str:placa>', veiculosviews.getVeiculoPlaca),
    path('update/<str:pk>', veiculosviews.updateVeiculo),
    path('delete/<str:pk>', veiculosviews.deleteVeiculo),
    path('getForSale', veiculosviews.getVeiculosParaVenda),
    path('getSold', veiculosviews.getVeiculosvendidos),
]
