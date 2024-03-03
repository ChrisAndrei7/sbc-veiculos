from rest_framework import serializers
from entities.produtos.produtosmodels import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'