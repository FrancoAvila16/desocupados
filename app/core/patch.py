# Notece que esto es lo que se conoce como Monkey patching, y que no es la
# mejor solución posible. Sin embargo esto es relativamente util para saber
# si el usuario actualmente logueado es una empresa o un desocupado, y pedir el
# perfil sin importar lo que corresponda.
from django.contrib.auth.models import User 

def is_empresa(self):
    return (self.empresa.cuit is not None) and (self.empresa.cuit > 0)

def is_desocupado(self):
    return (self.desocupado.dni is not None) and (self.desocupado.dni is not "")

def profile(self):
    return self.empresa if self.is_empresa() else self.desocupado

def profile_type(self):
    if self.is_desocupado():
        return "desocupado"
    elif self.is_empresa():
        return "empresa"
    else:
        return "administrador"

User.add_to_class("is_empresa", is_empresa)
User.add_to_class("is_desocupado", is_desocupado)
User.add_to_class("profile", profile)
User.add_to_class("profile_type", profile_type)