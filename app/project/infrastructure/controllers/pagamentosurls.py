from django.urls import path
from application.usecases import pagamentosviews

urlpatterns = [
    path('', pagamentosviews.getData),
    path ('create', pagamentosviews.addPagamento),
    path ('read/<str:pk>', pagamentosviews.getPagamento),
    path ('readporstatus/<str:pk>', pagamentosviews.getPagamentoPorStatus),
    path ('update/<str:pk>', pagamentosviews.updatePagamento),
    path ('delete/<str:pk>', pagamentosviews.deletePagamento),
]
