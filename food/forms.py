#v11
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Descuento


#Formulario Nuevo Usuario
class NewUserForm(UserCreationForm):
    email = forms.EmailField(max_length=100, required=True, help_text='Ingrese una direccion de email valida')
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class DescuentoForm(forms.ModelForm):
    # Definir una lista de opciones para los porcentajes
    PORCENTAJES = [(i, f"{i}%") for i in range(5, 101, 5)]  # Generar una lista de tuplas (valor, etiqueta)

    # Definir los campos del formulario
    nombre_descuento = forms.CharField(max_length=100)
    cantidad_minima = forms.IntegerField(min_value=0)
    cantidad_maxima = forms.IntegerField(min_value=0)
    porcentaje_descuento = forms.ChoiceField(choices=PORCENTAJES)

    class Meta:
        model = Descuento
        fields = ['nombre_descuento', 'cantidad_minima', 'cantidad_maxima', 'porcentaje_descuento']

    def clean(self):
        cleaned_data = super().clean()
        cantidad_minima = cleaned_data.get('cantidad_minima')
        cantidad_maxima = cleaned_data.get('cantidad_maxima')

        if cantidad_minima is not None and cantidad_maxima is not None:
            if cantidad_minima > cantidad_maxima:
                raise forms.ValidationError("La cantidad mínima debe ser menor o igual a la máxima.")

        return cleaned_data

    def save(self, commit=True):
        descuento = super().save(commit=False)
        # Realiza acciones adicionales aquí si es necesario
        if commit:
            descuento.save()
        return descuento
