# from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Load
from .serializers import LoadSerializer

class LoadViewSet(viewsets.ModelViewSet):
    queryset = Load.objects.all()
    serializer_class = LoadSerializer