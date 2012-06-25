.. -*- coding: utf-8 -*-

.. _skel_openerp:

===============================
Esqueletos de proyectos OpenERP
===============================

:Autor(es): Leonardo J. Caballero G.
:Correo(s): leonardocaballero@gmail.com
:Lanzamiento: |version|
:Fecha: |today|

.. contents:: :local:

Introducción
============

`OpenERP`_, es un sistema ERP y CRM. Tiene componentes separados en esquema Cliente-servidor. 
Dispone de interfaces XML-RPC, y SOAP. Emplea a Postgresql como sistema manejador de bases de 
datos y ha sido programado con Python, lo cual permite que su adecuación e implantación sea 
limpia y pueda tener una curva bastante menor que otras soluciones ERP existentes. 

Entonces para su desarrollo existen una serie de colecciones de plantillas *esqueletos* de módulos 
y temas basados en :ref:`Paster <skel_python>`, para proyectos que permiten iniciar rápidamente 
el desarrollo en OpenERP.

Requerimientos previos
======================
Se requiere instalar las siguientes dependencias con el siguiente comando: 

.. code-block:: sh

  # aptitude install bzr bzr-gtk bzrtools bzr-explorer python-dev python-setuptools tree

Instalación
===========

Dentro de su entorno virtual activado debe instalar el paquete `openerp_bootstrap`_, ejecutando el siguiente comando: 

.. code-block:: sh

  (python) pip install openerp_bootstrap

.. note::

  No olvidar que estos paquetes han sido instalados con el :ref:`entorno virtual <por_que_virtualenv>` 
  que previamente usted activo, eso quiere decir que los paquetes previamente instalados con 
  :ref:`Easy Install <que_es_easyinstall>` o :ref:`PIP <que_es_pip>` están instalados en el directorio 
  ``~/virtualenv/python/lib/python2.x/site-packages/`` en ves del directorio de su versión de Python 
  del sistema ``/usr/lib/python2.x/site-packages/``

Al finalizar la instalación podrá opcionalmente consultar cuales plantillas
tiene disponible para usa, ejecutando el siguiente comando: 

.. code-block:: sh

  (python)$ paster create --list-templates
    Available templates:
      basic_package:      A basic setuptools-enabled package
      openerp_newmodule:  Template for creating a basic openerp package skeleton
      openerp_theme:      Template for creating a basic openerp theme skeleton
      paste_deploy:       A web application deployed through paste.deploy

Usted puede usar el comando paster para crear paquetes Python. 

.. code-block:: sh

  (python)$ paster create -t openerp_newmodule openerp_mimodulo
    Selected and implied templates:
      openerp-bootstrap#openerp_newmodule  Template for creating a basic openerp package skeleton

    Variables:
      egg:      openerp_mimodulo
      package:  openerp_mimodulo
      project:  openerp_mimodulo
    Enter module_name (Module name (like "Project Issue")) ['My Module']: Mi modulo OpenERP
    Enter description (One-line description of the module) ['']: Mi modulo de OpenERP de pruebas
    Enter version (Version) ['1.0']: 0.1
    Enter author (Author name) ['']: Leonardo J. Caballero G.
    Enter author_email (Author email) ['']: leonardocaballero@gmail.com
    Enter category (Category) ['']: modulos openerp demo pruebas       
    Enter website (Website) ['']: http://about.me/macagua
    Enter depends (Dependencies [space-separated module names]) ['']: account
    Enter is_web (Is web addon? [yes/no]) ['no']: 
    Creating template openerp_newmodule
    Creating directory ./openerp_mimodulo
      Copying __init__.py to ./openerp_mimodulo/__init__.py
      Copying __openerp__.py_tmpl to ./openerp_mimodulo/__openerp__.py

Usted puede verificar el paquete previamente creado con el siguiente comando:

.. code-block:: sh

  (python)$ tree openerp_mimodulo/
    openerp_mimodulo/
    |-- __init__.py
    `-- __openerp__.py

Hasta este punto tiene creado la estructura del nuestro modulo y puede 
consultar la información del manifiesto de su modulo en el archivo 
``__openerp__.py``, con el siguiente comando:

.. code-block:: python

  $ cat ./openerp_mimodulo/__openerp__.py
  # -*- coding: utf-8 -*-
  
  {
      'name': 'Mi modulo OpenERP',
      'version': '0.1',
      'category': 'modulos openerp demo pruebas',
      'description': """Mi modulo de OpenERP de pruebas""",
      'author': 'Leonardo J. Caballero G. (leonardocaballero@gmail.com)',
      'website': 'http://about.me/macagua',
      'license': 'AGPL-3',
      'depends': ['account'],
      'init_xml': [],
      'update_xml': [],
      'demo_xml': [],
      'active': False,
      'installable': True,
  }

Ahora proceda a crear un nuevo tema, con el siguiente comando:

.. code-block:: sh

  (python)$ paster create -t openerp_theme
    Selected and implied templates:
      openerp-bootstrap#openerp_theme  Template for creating a basic openerp theme skeleton
    
    Enter project name: openerp_mitema
    Variables:
      egg:      openerp_mitema
      package:  openerp_mitema
      project:  openerp_mitema
    Enter module_name (Module name (like "My Theme")) ['My Theme']: Mi tema OpenERP
    Enter description (One-line description of the module) ['']: Mi tema OpenERP de pruebas
    Enter version (Version) ['1.0']: 0.1
    Enter author (Author name) ['']: Leonardo J. Caballero G.
    Enter author_email (Author email) ['']: leonardocaballero@gmail.com
    Enter category (Category) ['']: tema openerp demo pruebas
    Enter website (Website) ['']: http://about.me/macagua
    Enter depends (Dependencies [space-separated module names]) ['']: project
    Enter has_css (Needs CSS? [yes/no]) ['yes']: 
    Enter has_js (Needs Javascript? [yes/no]) ['yes']: 
    Enter has_xml (Needs QWeb XML? [yes/no]) ['no']: 
    Creating template openerp_theme
    Creating directory ./openerp_mitema
      Copying __init__.py to ./openerp_mitema/__init__.py
      Copying __openerp__.py_tmpl to ./openerp_mitema/__openerp__.py
      Recursing into static
        Creating ./openerp_mitema/static/
        Recursing into css
          Creating ./openerp_mitema/static/css/
          Copying +normalized_name+.css_tmpl to ./openerp_mitema/static/css/openerp_mitema.css
        Recursing into js
          Creating ./openerp_mitema/static/js/
          Copying +normalized_name+.js_tmpl to ./openerp_mitema/static/js/openerp_mitema.js
        Recursing into xml
          Creating ./openerp_mitema/static/xml/
          Copying +normalized_name+.xml_tmpl to ./openerp_mitema/static/xml/openerp_mitema.xml
    xml not required, removed dir ./openerp_mitema/static/xml

Usted puede verificar el paquete previamente creado con el siguiente comando:

.. code-block:: sh

  (python)$ tree openerp_mitema/
    openerp_mitema/
    |-- __init__.py
    |-- __openerp__.py
    `-- static
        |-- css
        |   `-- openerp_mitema.css
        `-- js
            `-- openerp_mitema.js

Este creara un modulo Web con todos los archivos estáticos que usted ya tiene listo para personalizar.

.. code-block:: python

  $ cat ./openerp_mitema/__openerp__.py
  # -*- coding: utf-8 -*-
  
  {
      'name': 'Mi tema OpenERP',
      'version': '0.1',
      'category': 'tema openerp demo pruebas',
      'description': """Mi tema OpenERP de pruebas""",
      'author': 'Leonardo J. Caballero G. (leonardocaballero@gmail.com)',
      'website': 'http://about.me/macagua',
      'license': 'AGPL-3',
      'depends': ['project', 'web'],
      'init_xml': [],
      'update_xml': [],
      'demo_xml': [],
      'active': False,
      'installable': True,
      'web':True,
      'css': [
          'static/css/openerp_mitema.css',
      ],
      'js': [
          'static/js/openerp_mitema.js',
      ],
  }


Descarga código fuente
======================

Para descargar el código fuente de este ejemplo ejecute el siguiente comando:

.. code-block:: sh

  $ bzr branch lp:~macagua/macagua-stuff/openerp_mimodulo
  $ bzr branch lp:~macagua/macagua-stuff/openerp_mitema


Recomendaciones
===============

Si desea trabajar con algún proyecto de desarrollo basado en esqueletos o plantillas ``paster`` 
y Buildout simplemente seleccione cual esqueleto va a utilizar para su desarrollo y proceso a 
instalarlo con Easy Install o PIP (como se explico anteriormente) y siga sus respectivas 
instrucciones para lograr con éxito la tarea deseada.

.. seealso:: Artículos sobre :ref:`Esqueletos de proyectos Python <skel_python>`.

Referencias
===========

- `How to create an OpenERP module`_.
- http://planet.domsense.com/en/2011/12/quickly-get-and-run-openerp-6-1-trunk/
- http://planet.domsense.com/en/2012/04/how-to-create-an-openerp-module-the-easy-way/trackback/

.. _OpenERP: http://es.wikipedia.org/wiki/OpenERP
.. _How to create an OpenERP module: the easy way: http://planet.domsense.com/en/2012/04/how-to-create-an-openerp-module-the-easy-way/
.. _Installing OpenERP on Linux – the quick & dirty way: livesin.digitalmalaya.net/2011/10/10/installing-openerp-on-linu-quick-dirty-way/
.. _openerp_bootstrap: http://pypi.python.org/pypi/openerp_bootstrap
