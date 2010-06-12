EasyInstall y Setuptools
========================

.. contents :: :local:

Setuptools es una colección de mejoras para el módulo distutils de Python,
que permiten a un desarrollador construir y distribuir paquetes de Python de
forma sencilla, en especial cuando dependen de otros paquetes de Python para
funcionar. Entre sus características principales están:

* Por default, utiliza PyPI para buscar los paquetes, lo que permite acceso
  inmediato e instalación transparente de miles de paquetes.
* Automáticamente encuentra y baja de internet las dependencias, para
  instalarlas o actualizarlas al momento de construir, mediante la herramienta
  EasyInstall. EasyInstall es capaz de bajar de internet las dependencias
  utilizando HTTP, FTP, Subversion o SourceForge. 
* Permite crear Python Eggs, que son paquetes de Python empaquetados en un
  sólo archivo para su distribución.
* Incluye archivos de configuración y todos los archivos que forman parte del
  directorio de trabajo, sin necesidad de listarlos individualmente o crear
  archivos de manifiesto.
* La instalación es muy sencilla, solo se necesita bajar de internet el
  archivo ez_setup.py y ejecutarlo con el Python que se desea utilizar
  (versión 2.3.5 o superior). Esto instalará un script llamado `easy_install`
  junto a los demás ejecutables de Python.

Ejemplos de uso
---------------

El script easy_install ofrece varias formas de uso, para instalar los paquetes
de diversas fuentes.

Ejemplo 1. Instalar un paquete por nombre, buscando en PyPI la versión más
reciente::

    $ easy_install SQLObject

Ejemplo 2.Instalar o actualizar un paquete por nombre y versión utilizando las
ligas encontradas en una "página de descargas"::

    $ easy_install -f http://pythonpaste.org/package_index.html SQLObject

Ejemplo 3. Descargar e instalar una distribución de código fuente::

    $ easy_install http://example.com/path/to/MyPackage-1.2.3.tgz

Ejemplo 4. Instalar un Python .egg ya descargado::

    $ easy_install /my_downloads/OtherPackage-3.2.1-py2.3.egg

Ejemplo 5. Actualizar un paquete ya instalado con la versión más reciente de
PyPI::

    $ easy_install --upgrade PyProtocols

Utilización con Zope/Plone
--------------------------

El mecanismo más moderno para la instalación de distribuciones de Zope y
Plone, llamado buildout, hace uso de easy_install para obtener e instalar
todas las dependencias. Adicionalmente, existe una herramienta llamada
ZopeSkel que permite crear fácilmente "esqueletos" de distintos tipos de
proyectos de Zope y Plone, mediante una herramienta llamada paster y un
sistema de templates. Es recomendado instalar esta última herramienta para
proyectos nuevos, de la siguiente manera::

    $ easy_install ZopeSkel

Una vez instalado, ZopeSkel se utiliza mediante el comando de sistema paster,
pasando la opción create. ZopeSkel ofrece una buena variedad de esqueletos
para diversos tipos de proyectos, como temas visuales, componentes de Plone,
buildouts o tipos de contenido con Archetypes. Para ver las opciones
disponibles, se utiliza la opción --list-templates::

    $ paster create --list-templates
    Available templates:
      archetype:          A Plone project that uses Archetypes
      basic_namespace:    A project with a namespace package
      basic_package:      A basic setuptools-enabled package
      basic_zope:         A Zope project
      kss_plugin:         A KSS plugin template
      nested_namespace:   A project with two nested namespaces.
      paste_deploy:       A web application deployed through paste.deploy
      plone:              A Plone project
      plone2.5_buildout:  A buildout for Plone 2.5 projects
      plone2.5_theme:     A Theme for Plone 2.5
      plone2_theme:       A Theme Product for Plone 2.1 & Plone 2.5
      plone3_buildout:    A buildout for Plone 3 projects
      plone3_portlet:     A Plone 3 portlet
      plone3_theme:       A Theme for Plone 3.0
      plone_app:          A Plone App project
      plone_hosting:      Plone hosting: buildout with ZEO and any Plone version
      plone_pas:          A Plone PAS project
      recipe:             A recipe project for zc.buildout
      silva_buildout:     A buildout for Silva projects
      zope_app:           Package that contains a Zope application
      zope_deploy:        (Paste) deployment of a Zope application

