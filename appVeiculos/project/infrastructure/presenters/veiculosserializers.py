from rest_framework import serializers
from entities.veiculos.veiculosmodels import Veiculo

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = '__all__'