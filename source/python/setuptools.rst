.. -*- coding: utf-8 -*-

.. _easyinstall_setuptools:

========================
Setuptools y EasyInstall
========================

:Autor(es): Carlos de la Guardia
:Correo(s): carlos.delaguardia@gmail.com
:Lanzamiento: |version|
:Fecha: |today|

.. contents :: :local:

.. _que_es_setuptools:

¿Qué es Setuptools?
===================

`Setuptools`_, es una colección de mejoras para el módulo distutils de Python,
que permiten a un desarrollador construir y distribuir paquetes de Python de
forma sencilla, en especial cuando dependen de otros paquetes de Python para
funcionar. 

Entre sus características principales están:

* Por defecto, utiliza PyPI para buscar los paquetes, lo que permite acceso
  inmediato e instalación transparente de miles de paquetes.

* Permite crear Python Eggs, que son paquetes de Python empaquetados en un
  sólo archivo para su distribución.

* Incluye archivos de configuración y todos los archivos que forman parte del
  directorio de trabajo, sin necesidad de listarlos individualmente o crear
  archivos de manifiesto.

* La instalación es muy sencilla, solo se necesita bajar de internet el
  archivo ``ez_setup.py`` y ejecutarlo con el Python que se desea utilizar
  (versión 2.3.5 o superior). Esto instalará un programa llamado ``easy_install``
  junto a los demás ejecutables de Python.

.. _que_es_easyinstall:

¿Qué es EasyInstall?
====================

`easy_install`_, es una herramienta que se basa en `Setuptools` para automáticamente encontrar y 
descargar desde internet las dependencias, para instalarlas o actualizarlas 
al momento de construir, que además esta herramienta es capaz de bajar 
de internet las dependencias utilizando HTTP, FTP, Subversion o SourceForge. 

.. _uso_easyinstall:

Ejemplos de uso
===============

El programa ``easy_install`` ofrece varias formas de uso, para instalar los paquetes
de diversas fuentes.

Ejemplo 1. Instalar un paquete por nombre, buscando en PyPI la versión más
reciente: 

.. code-block:: sh

    $ easy_install SQLObject

Ejemplo 2. Instalar o actualizar un paquete por nombre y versión utilizando
los enlaces encontrados en una "página de descargas": 

.. code-block:: sh

    $ easy_install -f http://pythonpaste.org/package_index.html SQLObject

Ejemplo 3. Descargar e instalar una distribución de código fuente: 

.. code-block:: sh

    $ easy_install http://example.com/path/to/MyPackage-1.2.3.tgz

Ejemplo 4. Instalar un Python .egg ya descargado: 

.. code-block:: sh

    $ easy_install /my_downloads/OtherPackage-3.2.1-py2.3.egg

Ejemplo 5. Instalar un paquete con una versión especifica: 

.. code-block:: sh

    $ easy_install "ZopeSkel==2.21.2"

Ejemplo 6. Actualizar un paquete ya instalado con la versión más reciente de
PyPI: 

.. code-block:: sh

    $ easy_install --upgrade PyProtocols


.. _easy_install_zope_plone:

Utilización con Zope/Plone
==========================

El mecanismo más moderno para la instalación de distribuciones de Zope y
Plone, llamado buildout, hace uso de ``easy_install`` para obtener e instalar
todas las dependencias. Adicionalmente, existe una herramienta llamada
ZopeSkel que permite crear fácilmente "esqueletos" de distintos tipos de
proyectos de Zope y Plone, mediante una herramienta llamada ``paster`` y un
sistema de plantillas. Es recomendado instalar esta última herramienta para
proyectos nuevos, de la siguiente manera:

.. code-block:: sh

    $ easy_install ZopeSkel

Una vez instalado, ``ZopeSkel`` se utiliza mediante el comando de sistema ``paster``,
pasando la opción ``create``. ZopeSkel ofrece una buena variedad de esqueletos
para diversos tipos de proyectos, como temas visuales, componentes de Plone,
buildouts o tipos de contenido con Archetypes. Para ver las opciones
disponibles, se utiliza la opción ``--list-templates``:

.. code-block:: sh

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


Referencia
==========

- `Instalación de setuptools y EasyInstall para Python`_ desde la comunidad Plone México.

.. _Setuptools: http://pypi.python.org/pypi/setuptools/
.. _easy_install: http://peak.telecommunity.com/DevCenter/EasyInstall
.. _Instalación de setuptools y EasyInstall para Python: http://plone.org/countries/mx/instalacion-de-setuptools-y-easyinstall-para-python
