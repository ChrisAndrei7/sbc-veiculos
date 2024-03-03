from django.urls import path
from application.usecases import pedidosviews

urlpatterns = [
    path('', pedidosviews.getData),
    path ('create', pedidosviews.addPedido),
    path ('read/<str:pk>', pedidosviews.getPedido),
    path ('readporstatus/<str:pk>', pedidosviews.getPedidoPorStatus),
    path ('update/<str:pk>', pedidosviews.updatePedido),
    path ('delete/<str:pk>', pedidosviews.deletePedido),
]
