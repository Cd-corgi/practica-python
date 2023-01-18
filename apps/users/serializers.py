from rest_framework import serializers
from apps.users.models import User

from apps.configuracion.serializers import EmpresaListSerializer


class LoginTradicionalSerializers(serializers.Serializer):
    correo   = serializers.EmailField(required= True)
    password = serializers.CharField(required= True)





class UserListSerializers(serializers.ModelSerializer):
    empresa = EmpresaListSerializer()
    genero = serializers.CharField( source= 'get_genero_display')
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'username',
            'avatar_url',
            'nombres',
            'apellidos',
            'genero',
            'empresa'
        ]

class UserListSerializers1(serializers.ModelSerializer):
    empresa = EmpresaListSerializer()
    class Meta:
        model = User
        fields = [
            'username',
            'avatar_url',
            'nombres',
            'apellidos',
            'genero',
            'empresa'
        ]

class UserUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'avatar_url',
            'nombres',
            'apellidos',
            'genero',
        ]
