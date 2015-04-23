#encoding=utf-8
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import ValidationError
#zonas horarias
from datetime import *
from django.utils import timezone #zonas horarias



class Profesor(models.Model):
	parteAsignatura=(
	('Teoria','TEORIA'),
	('Problemas','PROBLEMAS'),
	('Practicas','PRACTICAS'),
	('Sustituto','SUSTITUTO'),
	)
	nombre = models.CharField(max_length=50)
	dni = models.CharField(max_length=10,unique=True)
	email = models.EmailField(max_length=50,unique=True) #habia clase email? comprobar en form
	titulo = models.CharField(max_length=30) #ideal foreignkey a class titulos (repositorio de titulos)
	salario = models.IntegerField(blank=True,null=True)
	#lo que impartira es orientativo, puesto que un profesor puede dar ambas cosas
	impartira=models.CharField(max_length=13,choices=parteAsignatura,blank=True,null=True)
	imagen = models.ImageField(upload_to='fotos_profesores',blank=True,null=True)

	def __unicode__(self):
		return self.nombre


class Aula(models.Model): 
	nombre = models.CharField(max_length=30,unique=True)
	otros_datos = models.CharField(max_length=300,blank=True,null=True)

	def __unicode__(self):
		return self.nombre

class Titulacion(models.Model):
	Tipo=(
	('Grado','GRADO'),
	('Licenciatura','LICENCIATURA'),
	('Master','MASTER'),
	('Otro','OTRO'),
	)
	nombre = models.CharField(max_length=30,unique=True)
	tipo=models.CharField(max_length=13,choices=Tipo)
	facultad=models.CharField(max_length=30,blank=True,null=True) #ideal foreign key a class Facutad, pero no añadida para no saturar el modelo
	especialidad = models.CharField(max_length=300,blank=True,null=True)
	otros_datos = models.CharField(max_length=300,blank=True,null=True)

	def __unicode__(self):
		return self.nombre

class Asignatura(models.Model):
	OpcionCurso=(
	('Primero','PRIMERO'),
	('Segundo','SEGUNDO'),
	('Tercero','TERCERO'),
	('Cuarto','CUARTO'),
	)
	OpcionCuatrimestre=(
	('Primer','PRIMER'),
	('Segundo','SEGUNDO'),
	('Anual','ANUAL'),
	)
	TiposAsignaturas=(
	('Basica','Basica'),
	('Obligatoria','Obligatoria'),
	('Optativa','OPTATIVA'),
	('Practicas externas','PRACTICAS EXTERNAS'),
	('Trabajo fin titulacion','TRABAJO FIN TITULACION'),
	('Otro','Otro'),
	)
	nombre = models.CharField(max_length=30)
	otros_datos = models.CharField(max_length=300,blank=True,null=True)
	titulacion = models.ForeignKey(Titulacion)
	curso=models.CharField(max_length=13,choices=OpcionCurso)
	cuatrimestre=models.CharField(max_length=13,choices=OpcionCuatrimestre)
	tipo=models.CharField(max_length=35,choices=TiposAsignaturas)
	#docente = models.ForeignKey(Profesor) #solo 1 profesor
	docentes=models.ManyToManyField(Profesor, related_name='profesores') #varios profesores
	aula = models.ManyToManyField(Aula, related_name='AULASASIGNATURA',blank=True,null=True)
	
	def __unicode__(self):
		return self.nombre

class Alumno(models.Model): #meter formulario de edicion para matricularse, solo seleccionando asignaturas matriculadas
	nombre = models.CharField(max_length=30)
	dni = models.CharField(max_length=10,unique=True)
	ciudad = models.CharField(max_length=20)
	email = models.EmailField(max_length=50,unique=True)
	imagen = models.ImageField(upload_to='fotos_alumnos',blank=True,null=True)
		#asignaturas matriculadas, carrera y fecha opcional para poder matricularse luego (formulario)
	asignaturas_matriculadas=models.ManyToManyField(Asignatura, related_name='asignaturas_matriculadas',blank=True,null=True)
	titulacion = models.ForeignKey(Titulacion,blank=True,null=True)
	especialidad = models.CharField(max_length=30,blank=True,null=True)
	fecha_matricula=models.DateField()

	def __unicode__(self):
		return self.nombre
	def matricula_Reciente(self): #si se ha matriculado en menos de 30 dias
		return self.fecha_matricula >= date.today()-timedelta(days=30), 


class Nota_Alumno(models.Model):
	selecConvocatoria=(
	('Febrero','FEBRERO'),
	('Junio','JUNIO'),
	('Septiembre','SEPTIEMBRE'),
	('Diciembre','Diciembre'),
	)
	alumno = models.ForeignKey(Alumno,related_name="notaalumno")
	asignatura = models.ForeignKey(Asignatura)
	fecha = models.DateField() #implementación simple para ver la fecha, convotoria y año. 
	convocatoria = models.CharField(max_length=13,choices=selecConvocatoria)
	nota = models.DecimalField(max_digits=3,decimal_places=1) #definir luego entre 0 y 10

	def clean_fields(self,exclude=None):
        	if self.nota > 10:
           		raise ValidationError({'nota': ["Entre 0 y 10!",]})
        	if self.nota < 0:
           		raise ValidationError({'nota': ["Entre 0 y 10!",]})

	def __unicode__(self):
		return self.alumno.nombre

	
