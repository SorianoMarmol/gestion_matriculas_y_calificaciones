from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$','principal.views.inicio'),
	url(r'^alumnos/$','principal.views.lista_usuarios'),
	url(r'^alumno/(?P<id_usuario>\d+)$','principal.views.detalle_alumno'),
    	url(r'^alumno/nuevo/$','principal.views.nuevo_alumno'),
	url(r'^profesores/$','principal.views.lista_profesores'),
	url(r'^profesor/(?P<id_usuario>\d+)$','principal.views.detalle_profesor'),
	url(r'^editprofesor/(?P<id_usuario>\d+)$','principal.views.editar_profesor'),
	url(r'^delprofesor/(?P<id_usuario>\d+)$','principal.views.eliminar_profesor'),
    	url(r'^profesor/nuevo/$','principal.views.nuevo_profesor'),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^media/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT,}
	),
	url(r'^contacto/$','principal.views.contacto'),
	url(r'^asignaturas/$','principal.views.lista_asignaturas'),
	url(r'^asignaturas/(?P<id_asignatura>\d+)$$','principal.views.detalle_asignatura'),
	url(r'^users/',include('users.urls')), #redireccionar a aplicacion users
	url(r'^titulaciones/$','principal.views.lista_titulaciones'),
	url(r'^titulacion/(?P<id_titulacion>\d+)$','principal.views.detalle_titulacion'),
	url(r'^calificaciones/$','principal.views.calificaciones'),
	url(r'^calificacion/(?P<id_usuario>\d+)$','principal.views.calificaciones_privadas'),
)


