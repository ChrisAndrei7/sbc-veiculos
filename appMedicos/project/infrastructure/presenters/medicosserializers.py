from rest_framework import serializers
from entities.medicos.medicosmodels import Medico

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'