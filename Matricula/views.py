# from django.shortcuts import render
from rest_framework import viewsets
from .serializer import CursoSerializer
from .models import Curso

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

# Create your views here.
