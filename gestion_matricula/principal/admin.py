#encoding=utf-8

from principal.models import * #el importar todas las clases da flexibilidad y ahorra problemas
from django.contrib import admin

#importaciones básicas
#admin.site.register(Alumno)
#admin.site.register(Profesor)
#admin.site.register(Asignatura)
admin.site.register(Aula)
#admin.site.register(Titulacion)
#admin.site.register(Nota_Alumno)

class InlineNota(admin.TabularInline): #poder añadir varias notas al alumno facilmente
	model = Nota_Alumno
	extra = 5

class AlumnoAdmin(admin.ModelAdmin):
	inlines = [InlineNota]
	list_display = ('nombre', 'dni', 'email', 'titulacion','fecha_matricula','matricula_Reciente') #para mostrar mas datos de un alumno sin entrar en su ficha
	list_filter = ['titulacion'] #barra lateral de filtrado por carrera
	list_per_page = 10
	search_fields = ['nombre', 'dni', 'email', 'titulacion'] #búsqueda por datos del alumno
	date_hierarchy = 'fecha_matricula' #fechas de los registros
	filter_horizontal = ('asignaturas_matriculadas',) #mejor visualización de manytomany

admin.site.register(Alumno, AlumnoAdmin)

class ProfesorAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'dni', 'email', 'titulo') #para mostrar mas datos de un profesor sin entrar en su ficha
	list_filter = ['titulo'] #barra lateral de filtrado por carrera
	list_editable = ['titulo', 'email'] #edicion en el menu de cambios
	list_per_page = 10
	search_fields = ['nombre', 'dni', 'email', 'titulo'] #búsqueda por datos

admin.site.register(Profesor, ProfesorAdmin)

class AsignaturaAdmin(admin.ModelAdmin):
	inlines = [InlineNota]
	list_display = ('nombre', 'titulacion', 'curso', 'cuatrimestre','tipo') #para mostrar mas datos sin entrar en su ficha
	list_filter = ['titulacion','curso', 'cuatrimestre','tipo'] #barra lateral de filtrado
	list_editable = ['tipo', 'cuatrimestre'] #edicion en el menu de cambios
	list_per_page = 10
	search_fields = ['nombre', 'titulacion', 'curso', 'cuatrimestre','tipo'] #búsqueda por datos
	filter_horizontal = ('docentes',) #mejor visualización de manytomany

admin.site.register(Asignatura, AsignaturaAdmin)

class TitulacionAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'tipo', 'facultad', 'especialidad') #para mostrar mas datos sin entrar en su ficha
	list_filter = ['nombre', 'tipo'] #barra lateral de filtrado
	list_editable = ['especialidad'] #edicion en el menu de cambios
	list_per_page = 10
	search_fields = ['nombre', 'tipo', 'facultad', 'especialidad'] #búsqueda por datos

admin.site.register(Titulacion, TitulacionAdmin)

class Nota_AlumnoAdmin(admin.ModelAdmin):
	list_display = ('alumno', 'asignatura', 'nota', 'convocatoria','fecha') #para mostrar mas datos de un alumno sin entrar en su ficha
	list_filter = ['asignatura','convocatoria'] #barra lateral de filtrado
	list_editable = ['nota','convocatoria'] #edicion en el menu de cambios
	list_per_page = 10
	search_fields = ['alumno', 'asignatura'] #búsqueda por datos del alumno
	date_hierarchy = 'fecha' #fechas de los registros

admin.site.register(Nota_Alumno, Nota_AlumnoAdmin)

