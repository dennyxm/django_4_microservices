from django.shortcuts import render
from rest_framework import viewsets

from sevenhabits.models import Roles, Goals
from sevenhabits.serializers import RolesSerializer, GoalsSerializer

# Create your views here.
class RolesViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer

class GoalsViewSet(viewsets.ModelViewSet):
    queryset = Goals.objects.all()
    serializer_class = GoalsSerializer
