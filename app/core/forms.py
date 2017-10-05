from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroDesocupado(UserCreationForm):
    dni = forms.CharField(required=True)
    fecha_nacimiento = forms.DateField(required=True)
    profesion = forms.CharField(max_length=200, required=False)
    experiencia_laboral = forms.CharField(widget=forms.Textarea, max_length=700, required=False)
    formacion = forms.CharField(widget=forms.Textarea, max_length=500, required=False)
    habilidades = forms.CharField(widget=forms.Textarea, max_length=500, required=False)
    trabajo_realizable = forms.CharField(max_length=500, required=False)
    localidad = forms.CharField(max_length=500, required=False)

    class Meta:
        model = User
        # Le pega a user, porq queremos que guarde el usuario,
        # la creación del perfil la manejamos en el metodo de más abajo
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self):
        # Llamamos al save ya definido en el formulario, esto automaticamente
        # crea la empresa y el desocupado que actuan de perfil
        user = super(RegistroDesocupado, self).save()
        # Ahora le digo que rellene al usuario con todos los datos que correspondan
        user.refresh_from_db()
        # Y finalmente cargamos todos los elementos del desocupado desde el formulario
        user.desocupado.dni = self.cleaned_data.get('dni')
        user.desocupado.nombre = self.cleaned_data.get('first_name')
        user.desocupado.apellido = self.cleaned_data.get('last_name')
        user.desocupado.fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')
        user.desocupado.profesion = self.cleaned_data.get('profesion')
        user.desocupado.experiencia_laboral = self.cleaned_data.get('experiencia_laboral')
        user.desocupado.formacion = self.cleaned_data.get('formacion')
        user.desocupado.habilidades = self.cleaned_data.get('habilidades')
        user.desocupado.trabajo_realizable = self.cleaned_data.get('trabajo_realizable')
        user.desocupado.localidad = self.cleaned_data.get('localidad')
        # Finalmente, guardamos el usuario con el desocupado ya completo
        user.save()
        # Y lo devolvemos
        return user

class RegistroEmpresa(UserCreationForm):
    cuit = forms.CharField(max_length=10)
    razon_social = forms.CharField()
    rubro = forms.CharField()

    class Meta:
        model = User
        # Le pega a user, porq queremos que guarde el usuario,
        # la creación del perfil la manejamos en el metodo de más abajo
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self):
        # Llamamos al save ya definido en el formulario, esto automaticamente
        # crea la empresa y el desocupado que actuan de perfil
        user = super(RegistroEmpresa, self).save()
        # Ahora le digo que rellene al usuario con todos los datos que correspondan
        user.refresh_from_db()
        # Y finalmente cargamos todos los elementos de la empresa
        user.empresa.cuit = self.cleaned_data.get('cuit')
        user.empresa.razon_social = self.cleaned_data.get('razon_social')
        user.empresa.rubro = self.cleaned_data.get('rubro')
        # Finalmente, guardamos el usuario con la empresa ya completo
        user.save()
        # Y lo devolvemos
        return user