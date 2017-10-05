El sistema se actualizó para utilizar python 3 en lugar de python 2, y utilizar
la última versión de Django. Esto trae aparejados algunos inconvenientes, pues
hay que instalar python 3 si no lo tienen, incluyendo pip 3. En windows, se
debe ir a la página de [python](http://python.org) y descargarlo y luego descargar setuptools y pip.

En linux en general, hoy en dia python 3 ya está incluido, pero por defecto se
usa la dos, para usar la 3 basta escribir

```
python3
```

en lugar de solamente

```
python
```

También deberían tener pip3 como comando, sino

```
sudo apt-get install python3.6
apt-get install python3-pip
```

Luego, hay que instalar las dependencias. Todo lo requerido ya está en el archivo
requirements.txt en la raiz del proyecto, así que basta decirle a pip que tome de
ahi lo que debe instalar

```
pip3 install -r requirements.txt
```

Y listo, ya pueden arrancar el proyecto, etc. como lo venían haciendo.
Recuerden primero crear las migraciones si modifican algún dato del modelo.

```
python3 manage.py makemigrations
```

Luego aplicar las migraciones

```
python3 manage.py migrate
```

Y luego correr el servidor.

```
python3 manage.py runserver
```

P.D. Algunos archivos se movieron de lugar. Ahora, la configuración (lo que antes
era mysite) es "app", y la aplicación en si (lo que antes era sideco) está dentro
de "app", como "core", aunque los templates y los archivos estáticos viven afuera
de "core" directamente en "app", pero desde core puedo mencionarlos sin problemas.

Ahora hay un solo archivo de "urls.py", lo cual hace que sea menos confuso, allí
están todas las rutas de la aplicación y de otros detalles de django, como el admin.

Por último, el sistema de templates se cambió a jinja2, que es un sistema más
poderoso que los templates de django. Tiene como desventaja que, si buscan codigo
en internet, y este usa el sistema de templates de django, hay que adaptarlo
minimamente a Jinja2, pero la adaptación es sencilla.

La base de datos también fué borrada por lo que se crea de cero cuando hacen
migrate, si quieren un superusuario tienen que crearlo.

```
python3 manage.py createsuperuser
```

P.P.D. Si instalan todo global tal cual se indica acá, se olvidan del tema del
entorno. Salvo que esten haciendo otro proyecto en django, lo recomiendo.