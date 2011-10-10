.. -*- coding: utf-8 -*-

Esqueletos de proyectos Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Son una serie de colecciones de plantillas *esqueletos* que permiten iniciar
rápidamente proyectos, existente diversos *esqueletos* orientados a tipos de
desarrollos específicos, a continuación se muestran algunos esqueletos
útiles:

-   `ZopeSkel`_, es una colección de esqueletos para crear
    automáticamente paquetes e instancias en Zope.
-   `zopeproject`_, Tools and scripts for creating development
    sandboxes for web applications that primarily use Zope.
-   `grokcore.startup`_,  Soporte a Paster para proyectos Grok.
-   `grokproject`_, Script that sets up a grok project directory,
    installs Zope 3 and grok and creates a template for a grok application.
-   `django-project-templates`_, plantillas Paster para crear proyectos Django.
-   `fez.djangoskel`_, es una colección de plantillas Paster para
    crear aplicaciones Django como paquetes eggs.
-   `django-harness`_, es una aplicación destinada a simplificar las
    tareas típicas relacionadas con la creación de un sitio web hechos con
    Django, el mantenimiento de varias instalaciones (local, producción, etc)
    y cuidando su instalación global y su estructura de "esqueleto"
    actualizado del sitio de manera fácil.
-   `lfc-skel`_, Plantillas Paster para django-lfc. lfc-skel provee
    una plantilla para crear una aplicación LFC.
-   `Pylons`_,  un Framework Web Pylons, que al instalarse con Easy
    Install instala dos plantillas de proyectos Pylons.
-   `PylonsTemplates`_, Plantillas extras de paster para Pylons,
    incluyendo implementación de repoze.what. PylonsTemplates le ofrece
    plantillas adicionales paster para aplicaciones Pylons.
-   `BlastOff`_, Una plantilla de aplicación Pylons que proporciona
    un esqueleto de entorno de trabajo configurado con SQLAlchemy, mako,
    repoze.who, ToscaWidgets, TurboMail, WebFlash y (opcionalmente)
    SchemaBot. La aplicación generada esta previamente configurada con
    autenticación, inicio de sesión y formularios de registro, y
    (opcionalmente) confirmación de correo electrónico. BlastOff ayudar a
    acelerar el desarrollo de aplicaciones en Pylons por que genera un
    proyecto con una serie de dependencias configuraciones previamente.
-   `CherryPaste`_, Usar CherryPy dentro Paste.
-   `TracLegosScript`_, TracLegos es un software diseñado para
    ofrecer plantillas para proyectos Trac y asiste con la creación de
    proyecto trac.
-   `trac_project`_, Plantilla de proyecto Trac de software de código
    abierto.

Instalando dependencias en distribuciones basadas en Debian GNU/Linux
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Para para distribuciones basadas en Debian GNU/Linux, debe instalar los
requisitos previos con el siguiente comando: 

.. code-block:: sh

  # aptitude install python python-dev python-profiler python-setuptools python-virtualenv libc6-dev


Activar el entorno virtual creado previamente, ejecutando el siguiente
comando: 

.. code-block:: sh

  $ source .virtualenv/python/bin/activate

Luego de activar el entorno virtual creado previamente, ejecutando el
siguiente comando: 

.. code-block:: sh

  (python) easy_install pip
  (python) pip install PasteScript

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
      basic_package:       A basic setuptools-enabled package
      paste_deploy:        A web application deployed through paste.deploy

Usted debe usar el comando paster para crear el proyecto Buildout. 

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
paquete básico ha habilitado el setuptools 

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

  (python)$ cd mipaquetepython/
  (python)$ python setup.py install

Para comprabar su instalación ejecute el siguiente comando:

.. code-block:: sh

  (python)$ python

Y realice una importación del paquete mipaquetepython ejecutando el siguiente comando: 

.. code-block:: python

  >>> import mipaquetepython


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
