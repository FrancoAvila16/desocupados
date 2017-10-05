from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin as admin_views
from django.contrib.auth import views as auth_views 
from app.core import views as core_views

urlpatterns = [
    # El admin, en realidad esto solo nos sirve a nosotros para
    # administrar el sitio y verificar que estémos haciendo bien las cosas
    # Habría que sacarlo cuando el sitio vaya online.
    # Ya viene hecho por django.
    url(r'^admin/', admin_views.site.urls),
    # Estas URLs sirven para hacer el login y logout de usuarios. Es algo que ya
    # viene de farica con Django. Pero debemos darle una ruta, y además, debemos
    # indicarle algunos detalles, como el template HTML a usar y el nombre.
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    # El resto de las URLs ya no vienen cn django, y dependen del views que
    # hayamos definido en "core". Entre estas están la página principal y el
    # registro de empresas y desocupados. Además de cualquier otra cosa que
    # pongamos luego.
    url(r'^$', core_views.home, name='home'),
    url(r'^registrar/desocupado$', core_views.registro_desocupado, name='registrar.desocupado'),
    url(r'^registrar/empresa$', core_views.registro_empresa, name='registrar.empresa'),
]
