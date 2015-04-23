#encoding: utf-8

from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyUserForm(UserCreationForm):
    """A form for creating new users. Includes all the required fields, plus a repeated password."""
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmación de contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'username', 'email')

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username = username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("A user with this user name already exists.")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            raise forms.ValidationError("The two password fields did not match.")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_staff = False
        user.is_superuser = False
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs): #cambiar el nombre a los campos en la presentacion
		super(MyUserForm,self).__init__(*args,**kwargs)
		self.fields['first_name'].label="Nombre Completo"
		self.fields['username'].label="Nombre de usuario"
		self.fields['email'].label="Email"
