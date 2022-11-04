from django.db import models

# Create your models here.

class Integrante(models.Model):

   nombre = models.CharField(max_length=50)
   apellido = models.CharField(max_length=50)
   dni = models.IntegerField(default = None)
   alta = models.DateField(default = None)
   
