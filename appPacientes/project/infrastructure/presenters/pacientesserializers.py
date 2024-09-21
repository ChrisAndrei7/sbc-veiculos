from rest_framework import serializers
from entities.pacientes.pacientesmodels import Paciente

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'