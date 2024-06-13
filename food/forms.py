#v11
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Formulario Nuevo Usuario
class NewUserForm(UserCreationForm):
    email = forms.EmailField(max_length=100, required=True, help_text='Ingrese una direccion de email valida')
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
