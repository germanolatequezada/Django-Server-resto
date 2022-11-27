
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Dim_cliente(models.Model):
	#id_cliente=models.IntegerField
	nombre = models.CharField(max_length=30, default =' SOME STRING')
	apellidoP = models.CharField(max_length=30, default =' SOME STRING')
	#apellidoM = models.CharField(max_length=50, default =' SOME STRING')
	rut = models.CharField(max_length=30, default =' SOME STRING')
	#digitoVerificador = models.CharField(max_length=30, default =' SOME STRING')

class Dim_ingrediente(models.Model):
	#id_ingrediente=models.IntegerField
	nombre=models.CharField(max_length=30, default =' SOME STRING')
	unidad=models.CharField(max_length=30, default =' SOME STRING')

class  Dim_mesa(models.Model):
   # id_mesa =models.IntegerField
    nombre=models.CharField(max_length=30, default =' SOME STRING')
    capacidad=models.IntegerField(default =0)
    #capacidad=models.IntegerField(max_length=30, default =' SOME STRING')

class Dim_modulo(models.Model):
  #  id_modulo =models.IntegerField,
    nombre = models.CharField(max_length=30, default =' SOME STRING')

class Dim_plato(models.Model):
    #id_plato =models.IntegerField,
    nombre=models.CharField(max_length=30, default =' SOME STRING')
    tiempoPreparacionMin=models.IntegerField(default =0)
    id_ingrediente1=models.IntegerField(default =0)
    id_ingrediente2=models.IntegerField(default =0)
    id_ingrediente3=models.IntegerField(default =0)
    id_ingrediente4=models.IntegerField(default =0)
    id_ingrediente5=models.IntegerField(default =0)
    #otros =models.IntegerField
    #img= models.ImageField()

class Dim_sucursales(models.Model):
    id_sucursal=models.IntegerField
    nombre = models.CharField(max_length=30, default =' SOME STRING')
    direccion = models.CharField(max_length=30, default =' SOME STRING')

class Dim_usuario(models.Model):
    #id_usuario=models.IntegerField,
    nombre = models.CharField(max_length=30, default =' SOME STRING')
    apellidoP =models.CharField(max_length=30, default =' SOME STRING')
    #apellidoM =models.CharField(max_length=30, default =' SOME STRING')
    rut =models.CharField(max_length=30, default =' SOME STRING')
   # digitoVerificador =models.CharField(max_length=30, default =' SOME STRING')
    id_cargo=models.IntegerField

class Fact_comanda(models.Model):
   # id_factcom = models.IntegerField,
    id_cliente =models.IntegerField(default =0)
    id_mesa=models.IntegerField(default =0)
    id_usuario=models.IntegerField(default =0)

class Fact_comandaDetalle(models.Model):
  #  id_factcomDet = models.IntegerField
    id_factcom = models.IntegerField(default =0)
    id_comanda= models.IntegerField(default =0)
    id_cliente= models.IntegerField(default =0)
    id_plato= models.IntegerField(default =0)
    #precioPlato= models.IntegerField
    unidadPlato= models.IntegerField(default =0)
    totalPlato= models.IntegerField(default =0)
    id_postre= models.IntegerField(default =0)
    precioPostre= models.IntegerField(default =0)
    unidadPostre= models.IntegerField(default =0)
    totalPostre= models.IntegerField(default =0)
    id_bebida= models.IntegerField(default =0)
    precioBebida= models.IntegerField(default =0)
    UnidadBebida= models.IntegerField(default =0)
    totalBebida= models.IntegerField(default =0)
    id_otros= models.IntegerField(default =0)
    preciootros= models.IntegerField(default =0)
    unidadotros= models.IntegerField(default =0)
    totalOtros= models.IntegerField(default =0)

class Log_acceso(models.Model):
    #id_logAcc = models.IntegerField
    id_usuario= models.IntegerField(default =0)
    fecha = models.DateTimeField(default =0)
    id_modulo= models.IntegerField(default =0)
    fechaini= models.DateTimeField(default =0)
    fechafin= models.DateTimeField(default =0)








