from django.urls import path
from application.usecases import produtosviews

urlpatterns = [
    path('', produtosviews.getData),
    path ('create', produtosviews.addProduto),
    path ('read/<str:pk>', produtosviews.getProduto),
    path ('readcategoria/<str:cat>', produtosviews.getProdutoCategoria),
    path ('update/<str:pk>', produtosviews.updateProduto),
    path ('delete/<str:pk>', produtosviews.deleteProduto),
]
