from django.db import models

# Create your models here.

class Curso(models.Model):
    Nombre = models.CharField(max_length = 60)
    Credito = models.DecimalField(max_digits = 4, decimal_places=2, default=0.00)
