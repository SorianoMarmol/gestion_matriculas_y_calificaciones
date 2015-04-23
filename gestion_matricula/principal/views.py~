from principal.models import *
from principal.forms import *
from django.template import RequestContext
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

def inicio(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid:
	    try:
            	user = request.POST['username']
	    except:
		user = None
            passwd = request.POST['password']
            access = authenticate(username=user, password=passwd)
	    try:
	    	USER = User.objects.get(username=request.POST['username'])
	    except:
		USER = None
            if access is not None:
                if access.is_active:
                    login(request, access)
                    print "logueado correcto"
	            request.session['email'] = USER.email
                    return redirect('/')
                else:
                    return render(request, 'users/inactive.html')
            else:
                return render(request, 'users/nouser.html')
    else:
        form = AuthenticationForm()
    EMAIL= request.session.get('email')
    try:
	    	alumno= Alumno.objects.get(email=EMAIL)
    except Alumno.DoesNotExist:
		alumno = None
    return render_to_response('inicio.html',{'alumno':alumno,'form': form}, context_instance=RequestContext(request))


def lista_usuarios(request):
	alumnos = Alumno.objects.all()
	return render_to_response('lista_usuarios.html',{'datos':alumnos},context_instance=RequestContext(request))


def detalle_alumno(request, id_usuario):
    dato = get_object_or_404(Alumno, pk=id_usuario)
    nota= dato.notaalumno.all()
    return render_to_response('alumno.html',{'alumno':dato,'nota':nota}, context_instance=RequestContext(request))

@login_required
def nuevo_alumno(request):
	if request.method=='POST':
		formulario = AlumnoForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = AlumnoForm()
	EMAIL= request.session.get('email')
	try:
	    	alumno= Alumno.objects.get(email=EMAIL)
	except Alumno.DoesNotExist:
		alumno = None
	return render_to_response('alumnoform.html',{'formulario':formulario, 'alumno':alumno},context_instance=RequestContext(request))


def contacto(request):
    if request.method=='POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            titulo = 'Mensaje'
            contenido = formulario.cleaned_data['mensaje'] + "\n"
            contenido += 'Comunicarse a: ' + formulario.cleaned_data['correo']
            correo = EmailMessage(titulo, contenido, to=['i02somar@uco.es'])
            correo.send()
            return HttpResponseRedirect('/')
    else:
        formulario = ContactoForm()
    return render_to_response('contactoform.html',{'formulario':formulario}, context_instance=RequestContext(request))

def lista_asignaturas(request):
	asignaturas = Asignatura.objects.all()
	return render_to_response('lista_asignaturas.html',{'datos':asignaturas},context_instance=RequestContext(request))

def detalle_asignatura(request, id_asignatura):
    	asignatura = get_object_or_404(Asignatura, pk=id_asignatura)
	return render_to_response('asignatura.html',{'dato':asignatura},context_instance=RequestContext(request))

def lista_profesores(request):
	profesores = Profesor.objects.all()
	return render_to_response('lista_profesores.html',{'datos':profesores},context_instance=RequestContext(request))



def detalle_profesor(request, id_usuario):
    dato = get_object_or_404(Profesor, pk=id_usuario)
    return render_to_response('profesor.html',{'profesor':dato}, context_instance=RequestContext(request))

@staff_member_required
def nuevo_profesor(request):
	if request.method=='POST':
		formulario = ProfesorForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/profesores')
	else:
		formulario = ProfesorForm()
	return render_to_response('profesorForm.html',{'formulario':formulario},context_instance=RequestContext(request))

@staff_member_required
def editar_profesor(request, id_usuario): #editar
	profesor = get_object_or_404(Profesor, id = id_usuario)
	if request.method=='POST':
		formulario = ProfesorForm(request.POST, request.FILES, instance = profesor)
		if formulario.is_valid(): #esto llamara a funcion clean
			formulario.save()
			return redirect('/profesores')
	else:
		formulario= ProfesorForm(instance = profesor)
	return render(request, 'profesorForm.html', {'formulario':formulario})

@staff_member_required
def eliminar_profesor(request, id_usuario): #eliminar profesor
	profesor = Profesor.objects.all().get(id=id_usuario)  
	profesor.delete()
	return redirect('/profesores')

def lista_titulaciones(request):
	titulaciones = Titulacion.objects.all()
	return render_to_response('lista_titulaciones.html',{'datos':titulaciones},context_instance=RequestContext(request))

def detalle_titulacion(request, id_titulacion):
	dato = get_object_or_404(Titulacion, pk=id_titulacion)
	return render_to_response('titulacion.html',{'dato':dato}, context_instance=RequestContext(request))

@staff_member_required
def calificaciones(request):
	calificacioneslist = Nota_Alumno.objects.all()
	return render_to_response('calificaciones.html',{'datos':calificacioneslist},context_instance=RequestContext(request))

@login_required
def calificaciones_privadas(request,id_usuario):
	datoalumno = get_object_or_404(Alumno, pk=id_usuario)
	dato= datoalumno.notaalumno.all()
	EMAIL= request.session.get('email')
	try:
	    	alumno= Alumno.objects.get(email=EMAIL)
	except Alumno.DoesNotExist:
		alumno = None
	return render_to_response('calificaciones_privadas.html',{'dato':dato,'alumno':alumno},context_instance=RequestContext(request))
















