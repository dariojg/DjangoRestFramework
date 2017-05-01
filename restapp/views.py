from django.shortcuts import render
from django.contrib.auth.models import User, Group
from restapp.models import Autor, Libro
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from restapp.serializers import UserSerializer, GroupSerializer, AutorSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticated,)

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


# Create your views here.
