# Bootstrap prototype

Este sistema está basado en Django por lo cual se debe instalar 1.9 para que funcione correctamente, pueden encontrar buena documentación de como instalarlo en https://docs.djangoproject.com/en/1.9/intro/install/

Con este proyecto podrá desarrollar prototipos de forma rápida y fácil pues proporciona las  bibliotecas de bootstrap dentro de la plantilla maestra, así solo debe correr la aplicación y comenzar a realizar su prototipo, si no conoce el lenguaje de plantillas puede leer https://docs.djangoproject.com/en/1.9/ref/templates/language/. 

Las plantillas de trabajo se encuentran en el directorio template, ahí encontrará la plantilla base en la cual están enlazados  todos componentes necesarios para correr Bootstrap y la plantilla index.html donde debe trabajar, puede agregar tantas plantillas como quiera y referenciarlas con el nombre ej. (http://localhost:8000/miplantilla.html).

## Modo de trabajo

* Haga un fork de este repositorio para tener un repositorio de trabajo propio.
* Instale [Python](https://www.python.org/) y [Django](https://www.djangoproject.com/download/) en su máquina.
* Clone su repositorio para trabajarlo en su máquina (git clone **url mi repo**)
* Posiciónese en la carpeta de trabajo en una terminal (ej. cd bootstrap_prototype en Linux).
* Ejecute python manage.py runserver
* Diríjase en un navegador web a http://localhost:8000/
* Cree y modifique los archivos que considere necesarios.
* Haga commit de los cambios y push al servidor cuando considere oportuno.
* Cuando ya esté listo el prototipo envíe un correo a jobs@solvosoft.com con su nombre y la URL del repositorio

## Hora de recepción 

Lunes 18 de enero de 2016 a las **3:00 pm**.

## Indicaciones del prototipo a realizar

La prueba consiste en elaborar un prototipo de la vista de listado de objetos de Django para dos tipos de objeto, los cuales son: un Cantón y un Distrito.

Un cantón esta compuesto por un nombre, un código y una provincia.  Un distrito esta compuesto por un nombre, un código y una referencia al cantón de donde se puede obtener el nombre del cantón y la provincia. Se espera encontrar esos campos en el prototipo.

La vista de listado de objetos permite hacer búsquedas por nombre (es un prototipo las búsquedas no tienen que funcionar), tiene una opción para realizar acciones predefinidas como por ejemplo eliminar elementos y una sección de filtros, además solo muestra 20 elementos por pagina ( no tiene que hacer 20 elementos para demostrar la idea) solo el paginado.

Los cantones se filtran por provincia y los distritos se filtran por cantón y provincia, es importante notar existen 81 cantones en Costa Rica.

Buena Suerte :)
