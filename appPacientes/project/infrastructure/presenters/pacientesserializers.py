from rest_framework import serializers
from entities.pacientes.medicosmodels import Paciente

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'