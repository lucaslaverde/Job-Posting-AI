from django.db import models

# Create your models here.
class User(models.Model):
    Usuario = models.CharField(unique = True, max_length=50)
    Nombre = models.CharField(unique=False,max_length=25)
    Email = models.CharField(unique=True,max_length=25)
    Tpassw = models.CharField(unique=True,max_length=500)

class IACONTENT(models.Model):
    Empresa = models.CharField(unique=True, max_length=50)
    COLOR_paletas = models.CharField(unique=False, max_length=100)
    #plantillas = models.ForeignObject()