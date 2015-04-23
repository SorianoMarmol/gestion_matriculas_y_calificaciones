# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from forms import UserCreationForm, MyUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from principal.models import *
from models import *

def usersNew(request):
    # if (request.user.is_superuser and request.user.is_staff):
    if request.method == 'POST':
        # Can use standard form
        # form = UserCreationForm(request.POST)
        # Or customize it
        form = MyUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        # form = UserCreationForm()
        form = MyUserForm()
    context = {'form':form}
    return render(request, 'users/newuser.html',  context)

def userList(request):
    list = User.objects.all().order_by('last_name')
    context = {'userList': list}
    return render(request, 'users/userslist.html', context)

def userDelete(request, user_id):
    if (request.user.is_superuser and request.user.is_staff):
        user = get_object_or_404(User, pk = user_id)
        user.delete()
    return redirect('/users/list')

def userLogin(request):
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
    context = {'form': form}
    return render(request,'users/login.html', context)



@login_required(login_url='/users/login')
def userLogout(request):
    logout(request)
    return redirect('/')
