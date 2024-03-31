from django.urls import path, include
from rest_framework import routers
from Matricula import views

routers = routers.DefaultRouter()
routers.register("Curso", views.CursoViewSet)

urlpatterns = [path("",include(routers.urls)),]