from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.db import IntegrityError
from asignaciones.models import UserProfile
from .modelos.empresa import Empresa
from .modelos.materia_prima import MateriaPrima
from .modelos.producto import Producto

#probar esto

class CustomUserCreationForm(UserCreationForm):
    #campo rut_body
    rut_body = forms.CharField(
        widget=forms.TextInput(attrs={'inputmode': 'numeric', 'class' : 'input-rut-body'}),
        label="RUT",
        max_length=8
    )
    #campo rut_dv
    rut_dv = forms.CharField(
        max_length=1, 
        label="digito rutificador",
        widget=forms.TextInput(attrs={'class': 'input-rut-dv'})
    )
    #campo rut_empresa_body
    rut_empresa_body = forms.CharField(
        widget=forms.TextInput(attrs={'inputmode' : 'numeric', 'class' : 'input-rut-body rut-body-empresa'}),
        label="RUT empresa",
        max_length=8
    )
    #campo rut_empresa_dv
    rut_empresa_dv = forms.CharField(
        max_length=1, 
        label="digito rutificador empresa", 
        widget=forms.TextInput(attrs={'class': 'input-rut-dv'})
    )


    #class Meta especifica detalles importantes del formulario, en este caso el modelo y los campos
    class Meta:
        model = UserProfile
        fields = ['username', 'password1', 'password2', 'rut_body', 'rut_dv', 'rut_empresa_body', 'rut_empresa_dv']

    def clean(self):
        #se hace la validación del modelo
        return super().clean()

    def save(self, commit=True):
        user = super().save(commit=False)
        rut_body = self.cleaned_data['rut_body']
        rut_dv = self.cleaned_data['rut_dv']
        rut_body_e = self.cleaned_data['rut_empresa_body']
        rut_dv_e = self.cleaned_data['rut_empresa_dv']
        rut_empresa = f'{rut_body_e}-{rut_dv_e}'
        user.rut = f'{rut_body}-{rut_dv}'
        empresa = Empresa.objects.filter(rut_empresa=rut_empresa).first()
        if empresa:
            user.empresa = empresa
        else:
            raise ValueError('No se encontró una instancia válida de Empresa')
        return user

class LoginForm(forms.Form):
    rut_body = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-rut-body', 'placeholder': '12345678'}), max_length=8, label="")
    rut_dv = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-rut-dv', 'placeholder': '9'}), max_length=1, label="")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}), max_length=25, label="")

    def clean(self):
        return super().clean()

#administracion limitacion de caracteres en procesos
user_name = forms.CharField(
        widget=forms.TextInput(attrs={'class' : 'form-control-sm'}),
        label="Usuario",
        max_length=20
    )

correo = forms.CharField(
        widget=forms.TextInput(attrs={'class' : 'form-control-sm'}),
        label="correo",
        max_length=25
    )

class ActualizarMateriaPrimaForm(forms.ModelForm):
    """Esta clase permite actualizar la materia prima de la vista de 'Materia Prima'"""

    class Meta:
        model = MateriaPrima
        fields = ['numero_buzon', 'tipo_madera', 'clase_diametrica', 'longitud', 'cantidad']
        
class CrearProductoForm(forms.ModelForm):
    """Esta clase permite crear un nuevo producto"""

    class Meta:
        model = Producto
        fields = ['codigo', 'nombre', 'grosor', 'ancho', 'largo']