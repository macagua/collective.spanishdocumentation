.. -*- coding: utf-8 -*-

.. _skel_python:

==============================
Esqueletos de proyectos Python
==============================

:Autor(es): Leonardo J. Caballero G.
:Correo(s): leonardocaballero@gmail.com
:Lanzamiento: |version|
:Fecha: |today|

.. contents:: :local:

Introducción
============

Son una serie de colecciones de plantillas *esqueletos* que permiten iniciar
rápidamente proyectos, existente diversos *esqueletos* orientados a tipos de
desarrollos específicos.

.. _que_es_pastescript:

¿Qué es PasteScript?
--------------------

Es una herramienta de linea de comando basada en plugins que le 
permiten crear estructuras de paquetes de proyectos Python ademas sirve aplicaciones 
web, con configuraciones basadas en `paste.deploy`_.

Instalación
===========

Dentro de su :ref:`entorno virtual <creacion_entornos_virtuales>` activado debe 
instalar el paquete `PasteScript`_, ejecutando el siguiente comando: 

.. code-block:: sh

  (python) pip install PasteScript

.. note::

  No olvidar que estos paquetes han sido instalados con el entorno virtual que
  previamente usted activo, eso quiere decir que los paquetes previamente
  instalados con Easy Install están instalados en el directorio
  ``~/virtualenv/python/lib/python2.x/site-packages/`` en ves del directorio de
  su versión de Python de sistema ``/usr/lib/python2.x/site-packages/``

Al finalizar la instalación podrá opcionalmente consultar cuales plantillas
tiene disponible para usa, ejecutando el siguiente comando: 

.. code-block:: sh

  (python)$ paster create --list-templates
    Available templates:
      basic_package:       A basic setuptools-enabled package
      paste_deploy:        A web application deployed through paste.deploy

Usted puede usar el comando paster para crear paquetes Python. 

.. code-block:: sh

  (python)$ paster create -t basic_package mipaquetepython

    Selected and implied templates:

      PasteScript#basic_package  A basic setuptools-enabled package

    Variables:
      egg:      mipaquetepython
      package:  mipaquetepython
      project:  mipaquetepython
    Enter version (Version (like 0.1)) ['']: 0.1
    Enter description (One-line description of the package) ['']: My Basic Package
    Enter long_description (Multi-line description (in reST)) ['']: My Basic Package to show how use PasteScript
    Enter keywords (Space-separated keywords/tags) ['']: PasteScript Basic Package Demo
    Enter author (Author name) ['']: Pedro Picapiedra
    Enter author_email (Author email) ['']: pedro@acme.com
    Enter url (URL of homepage) ['']: http://www.acme.com/equipo/pedro
    Enter license_name (License name) ['']: GPL
    Enter zip_safe (True/False: if the package can be distributed as a .zip file) [False]:
    Creating template basic_package
    Creating directory ./mipaquetepython
      Recursing into +package+
        Creating ./mipaquetepython/mipaquetepython/
        Copying __init__.py to
        ./mipaquetepython/mipaquetepython/__init__.py
      Copying setup.cfg to ./mipaquetepython/setup.cfg
      Copying setup.py_tmpl to ./mipaquetepython/setup.py
    Running /home/macagua/virtualenv/python/bin/python setup.py egg_info


Usted puede verificar el paquete previamente creado y observará como este
paquete básico ha habilitado el ``setuptools`` 

.. code-block:: sh

  (python)$ tree mipaquetepython/
    mipaquetepython/
    |-- mipaquetepython
    |   `-- __init__.py
    |-- mipaquetepython.egg-info
    |   |-- PKG-INFO
    |   |-- SOURCES.txt
    |   |-- dependency_links.txt
    |   |-- entry_points.txt
    |   |-- not-zip-safe
    |   `-- top_level.txt
    |-- setup.cfg
    `-- setup.py

Para instalar este paquete ejecute el siguiente comando:

.. code-block:: sh

  (python)$ cd mipaquetepython/mipaquetepython/
  (python)$ vim app.py

Escriba un simple código que solicita un valor y luego lo muestra: 

.. code-block:: python

  var = raw_input("Introduzca alguna frase: ")
  print "Usted introdujo: ", var

Guarde los cambios en el archivo ``app.py``

Luego importe su aplicacion ``app.py`` en el archivo ``__init__.py`` 
con el siguiente código fuente: 

.. code-block:: python

  from mipaquetepython import app

Para comprabar su instalación ejecute el siguiente comando:

.. code-block:: sh

  (python)$ python

Y realice una importación del paquete mipaquetepython ejecutando 
el siguiente comando: 

.. code-block:: python

  >>> import mipaquetepython
  Introduzca alguna frase: Esta cadena
  Usted introdujo:  Esta cadena
  >>> exit()


Descarga código fuente
======================

Para descargar el código fuente de este ejemplo ejecute el siguiente 
comando:

.. code-block:: sh

  $ svn co https://svn.plone.org/svn/collective/spanishdocs/trunk/src/mini-tutoriales/mipaquetepython mipaquetepython


Esqueletos en diversos proyectos Python
=======================================

A continuación se muestran algunos esqueletos útiles:

- :ref:`Esqueletos de proyectos Zope/Plone <skel_plone>`.
- **Esqueletos de proyectos Django**:

  - `django-project-templates`_, plantillas Paster para crear proyectos Django.

  - `fez.djangoskel`_, es una colección de plantillas Paster para crear aplicaciones Django como paquetes eggs.

  - `django-harness`_, es una aplicación destinada a simplificar las tareas típicas relacionadas con la creación de un sitio web hechos con Django, el mantenimiento de varias instalaciones (local, producción, etc) y cuidando su instalación global y su estructura de "esqueleto" actualizado del sitio de manera fácil.

  - `lfc-skel`_, Plantillas Paster para django-lfc. lfc-skel provee una plantilla para crear una aplicación LFC.

- **Esqueletos de proyectos Pylons**:

  - `Pylons`_,  un Framework Web Pylons, que al instalarse con EasyInstall instala dos plantillas de proyectos Pylons.

  - `PylonsTemplates`_, Plantillas extras de paster para Pylons, incluyendo implementación de repoze.what. PylonsTemplates le ofrece plantillas adicionales paster para aplicaciones Pylons.

  - `BlastOff`_, Una plantilla de aplicación Pylons que proporciona un esqueleto de entorno de trabajo configurado con SQLAlchemy, mako, repoze.who, ToscaWidgets, TurboMail, WebFlash y (opcionalmente) SchemaBot. La aplicación generada esta previamente configurada con autenticación, inicio de sesión y formularios de registro, y (opcionalmente) confirmación de correo electrónico. BlastOff ayudar a acelerar el desarrollo de aplicaciones en Pylons por que genera un proyecto con una serie de dependencias configuraciones previamente.

- **Esqueletos de proyectos CherryPy**:

  - `CherryPaste`_, Usar CherryPy dentro Paste.

- **Esqueletos de proyectos Trac**:

  - `TracLegosScript`_, TracLegos es un software diseñado para ofrecer plantillas para proyectos Trac y asiste con la creación de proyecto trac.

  - `trac_project`_, Plantilla de proyecto Trac de software de código abierto.


Recomendaciones
===============

Si desea trabajar con algún proyecto de desarrollo basado en esqueletos o plantillas paster y Buildout simplemente seleccione cual esqueleto va a utilizar para su desarrollo y proceso a instalarlo con Easy Install o PIP (como se explico anteriormente) y siga sus respectivas instrucciones para lograr con éxito la tarea deseada.

Referencias
===========

- `Gestión de proyectos con Buildout, instalando Zope/Plone con este mecanismo`_ desde la comunidad de Plone Venezuela.

.. _PasteScript: http://pypi.python.org/pypi/PasteScript
.. _paste.deploy: http://pypi.python.org/pypi/PasteDeploy
.. _django-project-templates: http://pypi.python.org/pypi/django-project-templates
.. _fez.djangoskel: http://pypi.python.org/pypi/fez.djangoskel
.. _django-harness: http://pypi.python.org/pypi/django-harness
.. _lfc-skel: http://pypi.python.org/pypi/lfc-skel/
.. _ZopeSkel: http://pypi.python.org/pypi/ZopeSkel
.. _zopeproject: http://pypi.python.org/pypi/zopeproject/
.. _grokcore.startup: http://pypi.python.org/pypi/grokcore.startup
.. _grokproject: http://pypi.python.org/pypi/grokproject/
.. _Pylons: http://pypi.python.org/pypi/Pylons/1.0
.. _PylonsTemplates: http://pypi.python.org/pypi/PylonsTemplates/
.. _BlastOff: http://pypi.python.org/pypi/BlastOff/
.. _CherryPaste: http://pypi.python.org/pypi/CherryPaste
.. _TracLegosScript: http://trac-hacks.org/wiki/TracLegosScript
.. _trac_project: http://trac-hacks.org/browser/traclegosscript/anyrelease/example/oss
.. _Gestión de proyectos con Buildout, instalando Zope/Plone con este mecanismo: http://coactivate.org/projects/ploneve/gestion-de-proyectos-con-buildout
