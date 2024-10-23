from django.db import models

# Create your models here.
class SystemUser(models.Model):
    Usuario = models.CharField(unique = True, max_length=50,primary_key=True)

class IACONTENT(models.Model):
    Empresa = models.CharField(unique=True, max_length=50,primary_key=True)
    COLOR_paletas = models.CharField(unique=False, max_length=100)
    #plantillas = models.ForeignObject()