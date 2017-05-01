from django.contrib.auth.models import User, Group
from restapp.models import Autor, Libro
from rest_framework import serializers

"""
    Declaro serializer para los modelos
    y digo que campos quieron que devuelva cada modelo
"""


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class AutorSerializer(serializers.HyperlinkedModelSerializer):
    libros = serializers.StringRelatedField(many=True)  #relación Autor ->* Libro

    class Meta:
        model = Autor
        fields = ('nombre', 'libros')
