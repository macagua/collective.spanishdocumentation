.. -*- coding: utf-8 -*-

==================================
Esqueletos de proyectos Zope/Plone
==================================

Son una serie de colecciones de plantillas *esqueletos* que permiten iniciar
rápidamente proyectos, existente diversos *esqueletos* orientados a tipos de
desarrollos específicos, a continuación se muestran algunos esqueletos
útiles:

- `ZopeSkel`_, es una colección de esqueletos para crear
  automáticamente paquetes e instancias en Zope.
- `zopeproject`_, Tools and scripts for creating development
  sandboxes for web applications that primarily use Zope.
- `grokcore.startup`_,  Soporte a Paster para proyectos Grok.
- `grokproject`_, Script that sets up a grok project directory,
  installs Zope 3 and grok and creates a template for a grok application.

Instalando paquete egg de esquetos
==================================

Para ralizar este paso debe tener creado previamente y activado un entorno virtual creado, ejecutando el siguiente comando: 

.. code-block:: sh

  (python) pip install 'ZopeSkel==2.21.2'

No olvidar que estos paquetes han sido instalados con el entorno virtual que
previamente usted activo, eso quiere decir que los paquetes previamente
instalados con Easy Install están instalados en el directorio
``~/virtualenv/python/lib/python4/site-packages/`` en ves del directorio de
su versión de Python de sistema ``/usr/lib/python2.x/site-packages/``

Al finalizar la instalación podrá opcionalmente consultar cuales plantillas
tiene disponible para usa, ejecutando el siguiente comando: 

.. code-block:: sh

  (python)$ paster create --list-templates
    Available templates:
      archetype:          A Plone project that uses Archetypes content types
      basic_buildout:     A basic buildout skeleton
      basic_namespace:    A basic Python project with a namespace package
      basic_package:      A basic setuptools-enabled package
      basic_zope:         A Zope project
      kss_plugin:         A project for a KSS plugin
      nested_namespace:   A basic Python project with a nested namespace (2 dots in name)
      paste_deploy:       A web application deployed through paste.deploy
      plone:              A project for Plone add-ons
      plone2.5_buildout:  A buildout for Plone 2.5 projects
      plone2.5_theme:     A theme for Plone 2.5
      plone2_theme:       A theme for Plone 2.1
      plone3_buildout:    A buildout for Plone 3 installation
      plone3_portlet:     A Plone 3 portlet
      plone3_theme:       A theme for Plone 3
      plone4_buildout:    A buildout for Plone 4 developer installation
      plone_app:          A project for Plone add-ons with a nested namespace (2 dots in name)
      plone_basic:        A project for Plone products
      plone_hosting:      Plone hosting: buildout with ZEO and Plone versions below 3.2
      plone_pas:          A project for a Plone PAS plugin
      recipe:             A recipe project for zc.buildout
      silva_buildout:     A buildout for Silva projects

Usted debe usar el comando paster para crear el proyecto Buildout. 

.. code-block:: sh

  (python)$ paster create -t plone4_buildout cliente1-portal.buildout
    Selected and implied templates:
      ZopeSkel#plone4_buildout  A buildout for Plone 4 developer installation

    Variables:
      egg:      cliente1-portal.buildout
      package:  cliente1-portal.buildout
      project:  cliente1-portal.buildout

    **************************************************************************
    **   *** NOTE: This template is for developers.
    
    **  If you just want to install Plone, the preferred way to get a
    **  buildout-based setup for Plone is to use the standard installer
    **  for your operating system (the Windows installer, the Mac
    **  installer, or the Unified Installer for Linux/Unix/BSD). These
    **  give you a best-practice, widely-used setup with an isolated
    **  Python and a well-documented buildout.
    **************************************************************************

    Plone Version (Plone version # to install) ['4.1']: 
    Creating template plone4_buildout
    Creating directory ./cliente1-portal.buildout
      Copying README.txt to ./cliente1-portal.buildout/README.txt
      Copying bootstrap.py to ./cliente1-portal.buildout/bootstrap.py
      Copying buildout.cfg_tmpl to ./cliente1-portal.buildout/buildout.cfg
      Recursing into src
        Creating ./cliente1-portal.buildout/src/
        Copying README.txt to ./cliente1-portal.buildout/src/README.txt
      Recursing into var
        Creating ./cliente1-portal.buildout/var/
        Copying README.txt to ./cliente1-portal.buildout/var/README.txt
    
    **************************************************************************
    **   Generation finished.
    
    **  Now run bootstrap and buildout:
    
    **  python bootstrap.by
    
    **  bin/buildout
    
    **  See ZopeSkel add-on page for more details:
    
    **  http://plone.org/products/zopeskel
    
    **************************************************************************

Usted puede verificar el paquete previamente creado y observará como este
paquete básico ha habilitado el setuptools 

.. code-block:: sh

  (python)$ tree cliente1-portal.buildout
    cliente1-portal.buildout
    |-- README.txt
    |-- bootstrap.py
    |-- buildout.cfg
    |-- src
    |   `-- README.txt
    `-- var
    `-- README.txt


Para iniciar el proyecto Plone ejecute los siguientes comandos:

.. code-block:: sh

  (python)$ cd cliente1-portal.buildout/
  (python)$ python bootstrap.py

Y realice una importación del paquete mipaquetepython ejecutando el siguiente comando: 

.. code-block:: sh

  (python)$ tree .
    .
    |-- README.txt
    |-- bin
    |   `-- buildout
    |-- bootstrap.py
    |-- buildout.cfg
    |-- develop-eggs
    |-- eggs
    |   |-- distribute-0.6.19-py2.4.egg
    |   |   |-- EGG-INFO
    |   |   |   |-- PKG-INFO
    |   |   |   |-- SOURCES.txt
    |   |   |   |-- dependency_links.txt
    |   |   |   |-- entry_points.txt
    |   |   |   |-- entry_points2.txt
    |   |   |   |-- not-zip-safe
    |   |   |   `-- top_level.txt
    |   |   |-- easy_install.py
    |   |   |-- pkg_resources.py
    |   |   |-- setuptools
    |   |   |   |-- __init__.py
    |   |   |   |-- archive_util.py
    |   |   |   |-- cli.exe
    |   |   |   |-- command
    |   |   |   |   |-- __init__.py
    |   |   |   |   |-- alias.py
    |   |   |   |   |-- bdist_egg.py
    |   |   |   |   |-- bdist_rpm.py
    |   |   |   |   |-- bdist_wininst.py
    |   |   |   |   |-- build_ext.py
    |   |   |   |   |-- build_py.py
    |   |   |   |   |-- develop.py
    |   |   |   |   |-- easy_install.py
    |   |   |   |   |-- egg_info.py
    |   |   |   |   |-- install.py
    |   |   |   |   |-- install_egg_info.py
    |   |   |   |   |-- install_lib.py
    |   |   |   |   |-- install_scripts.py
    |   |   |   |   |-- register.py
    |   |   |   |   |-- rotate.py
    |   |   |   |   |-- saveopts.py
    |   |   |   |   |-- sdist.py
    |   |   |   |   |-- setopt.py
    |   |   |   |   |-- test.py
    |   |   |   |   |-- upload.py
    |   |   |   |   |-- upload_docs.py
    |   |   |   |-- depends.py
    |   |   |   |-- dist.py
    |   |   |   |-- extension.py
    |   |   |   |-- gui.exe
    |   |   |   |-- package_index.py
    |   |   |   |-- sandbox.py
    |   |   |   `-- tests
    |   |   |       |-- __init__.py
    |   |   |       |-- doctest.py
    |   |   |       |-- server.py
    |   |   |       |-- test_build_ext.py
    |   |   |       |-- test_develop.py
    |   |   |       |-- test_easy_install.py
    |   |   |       |-- test_packageindex.py
    |   |   |       |-- test_resources.py
    |   |   |       |-- test_sandbox.py
    |   |   |       |-- test_upload_docs.py
    |   |   |-- site.py
    |   `-- zc.buildout-1.4.4-py2.4.egg
    |       |-- EGG-INFO
    |       |   |-- PKG-INFO
    |       |   |-- SOURCES.txt
    |       |   |-- dependency_links.txt
    |       |   |-- entry_points.txt
    |       |   |-- namespace_packages.txt
    |       |   |-- not-zip-safe
    |       |   |-- requires.txt
    |       |   `-- top_level.txt
    |       |-- README.txt
    |       `-- zc
    |           |-- __init__.py
    |           `-- buildout
    |               |-- __init__.py
    |               |-- allowhosts.txt
    |               |-- bootstrap.txt
    |               |-- buildout.py
    |               |-- buildout.txt
    |               |-- debugging.txt
    |               |-- dependencylinks.txt
    |               |-- distribute.txt
    |               |-- download.py
    |               |-- download.txt
    |               |-- downloadcache.txt
    |               |-- easy_install.py
    |               |-- easy_install.txt
    |               |-- extends-cache.txt
    |               |-- repeatable.txt
    |               |-- rmtree.py
    |               |-- runsetup.txt
    |               |-- setup.txt
    |               |-- testing.py
    |               |-- testing.txt
    |               |-- testing_bugfix.txt
    |               |-- testrecipes.py
    |               |-- tests.py
    |               |-- testselectingpython.py
    |               |-- unzip.txt
    |               |-- update.txt
    |               |-- upgrading_distribute.txt
    |               `-- windows.txt
    |-- parts
    |   `-- buildout
    |-- src
    |   `-- README.txt
    `-- var
    `-- README.txt


Iniciar la construcción de proyecto Plone:

.. code-block:: sh

  (python)$ ./bin/buildout -vN


Recomendaciones
~~~~~~~~~~~~~~~

-   Si desea trabajar con algún proyecto de desarrollo basado en
    esqueletos o plantillas paster y Buildout simplemente seleccione cual
    esqueleto va a utilizar para su desarrollo y proceso a instalarlo con
    Easy Install o PIP (como se explico anteriormente) y siga sus respectivas
    instrucciones para lograr con éxito la tarea deseada.

Referencias
-----------

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
