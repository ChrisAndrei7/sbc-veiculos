from rest_framework import serializers
from entities.usuarios.usuariosmodels import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'