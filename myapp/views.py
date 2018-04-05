from rest_framework import viewsets
from django.shortcuts import render
from .serializers import PersonSerializer
from .models import Person

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
