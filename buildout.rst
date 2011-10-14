.. -*- coding: utf-8 -*-

==================
Buildout y Plone 3
==================

.. contents :: :local:

Una herramienta para administrar, a través de un archivo de configuración
declaratoria, las partes y componentes de un desarrollo con Python.  Dichas
partes no están limitadas a componentes o código Python.

La parte más poderosa de buildout es que puede extenderse con el uso de
"recetas" que pueden instalar componentes más complicados simplemente
agregando nuevas secciones a la configuración. Buildout puede instalar
diversos paquetes de Python fácilmente porque está conectado con el índice
de paquetes de Python (http://www.python.org/pypi).

Algunos términos importantes
============================

.. glossary::

  Paquete de Pythons.
    Básicamente, una carpeta con código Python que contiene un archivo
    ``__init__.py``.

  Huevo (Python egg).
    Un mecanismo para empaquetar y distribuir paquetes de Python.

  Instalación de Zope.
    El software propio del servidor de aplicaciones.

  Instancia de Zope.
    Un directorio específico que contiene una configuración completa de Zope.

  Producto de Zope.
    Un paquete de Python especial para extender Zope.

  easy_install.
    Un script de línea de comando que permite instalar a través de la red
    paquetes del PYPI.

  Cheese shop (PYPI).
    Un repositorio de paquetes de Python.


Requisitos previos
------------------

Existen instrucciones detalladas para la instalación de requisitos, pero en
general se necesita lo siguiente:

* Python 2.4.x.
* Python setuptools (easy_install)
* Para Zope, ZopeSkel (egg).
* Para Plone, Python Imaging Library (PIL) instalado en ese Python.


Creación de un buildout
=======================

Se puede generar un buildout utilizando un template de paster:

.. code-block:: sh

  $ paster create -t plone3_buildout unam.buildout

El template hace varias preguntas:

.. code-block:: sh

  Selected and implied templates:
    ZopeSkel#plone3_buildout  A buildout for Plone 3 projects

    Variables:
      egg:      unam.buildout
      package:  unam.buildout
      project:  unam.buildout

    Enter zope2_install (Path to Zope 2 installation; leave blank to fetch one) ['']:
    <si ya se tiene una instalación de Zope se puede usar poniendo aquí el path>
    Enter plone_products_install (Path to directory containing Plone products; leave blank to fetch one) ['']:
    <lo mismo aquí si ya se tienen los productos de Plone>
    Enter zope_user (Zope root admin user) ['admin']:
    <el usuario administrador del sitio>
    Enter zope_password (Zope root admin password) ['']:
    <el password para este usuario>
    Enter http_port (HTTP port) [8080]:
    <el puerto donde escuchará el servicio de Zope>
    Enter debug_mode (Should debug mode be "on" or "off"?) ['off']:
    <'on' para activar el modo de debug>
    Enter verbose_security (Should verbose security be "on" or "off"?) ['off']:
    <'on' para presentar detalles cuando ocurran errores de privilegios>
    ...
    ...
    ...
    -----------------------------------------------------------
    Generation finished
    You probably want to run python bootstrap.py and then edit
    buildout.cfg before running bin/buildout -v

    See README.txt for details
    -----------------------------------------------------------

Activación de un buildout
=========================

Para activar un buildout hay que ejecutar el script `bootstrap.py` con el
mismo python con que se desea trabajar:

.. code-block:: sh

  $ cd unam.buildout
  $ python2.4 bootstrap.py
  ...
  ...
  ...
  $ bin/buildout -v
  ...
  ...
  ...
  $ bin/instance fg

Directorios creados
-------------------

.. glossary::

  bin/
    Ejecutables de buildout y producidos por las partes.

  eggs/
    Los eggs obtenidos e instalados de PYPI.

  downloads/
    Software adicional descargado. 

  var/
    Logs y archivo de ZODB de Zope (buildout nunca sobreescribe estos archivos).

  src/
    Código fuente de nuestros desarrollos.

  products/
    Productos tradicionales de zope.

  parts/
    Todo el código, configuración y datos manejados por buildout.

Descripción de este ejemplo
---------------------------

Un ejemplo de un buildout funcional se muestra a continuación:

.. code-block:: cfg

  # definicion de las partes que va a tener el buildout, cada parte es una
  # sección de configuración y generalmente utiliza una receta específica
  [buildout]
  parts =
      zope2
      productdistros
      instance
      zopepy

  # ligas adicionales a pypi.python.org donde pueden encontrarse eggs
  find-links =
      http://dist.plone.org
      http://download.zope.org/ppix/
      http://download.zope.org/distribution/
      http://effbot.org/downloads

  # Agregar eggs adicionales aquí
  # elementtree es requerido por Plone
  eggs =
      elementtree
    
  # Por cada paquete en desarrollo (dentro de src) se debe agregar una línea
  # e.g.: develop = src/my.package
  develop =

  # Esta receta instala zope 2. Para usar la misma url que requiere plone se
  # utiliza ${plone:zope2-url}. Es posible referirse con esta sintaxis a
  # cualquier variable de una de las partes, así: ${parte:variable}
  [zope2]
  recipe = plone.recipe.zope2install
  url = ${plone:zope2-url}

  # Ligas a distribuciones de productos tradicionales de Zope.
  # En nested-packages se pone el nombre del archivo (sin path) cuando
  # una distribución incluye varios productos.
  [productdistros]
  recipe = plone.recipe.distros
  urls =
  nested-packages =
  version-suffix-packages = 

  # esta receta inicializa la instancia de zope y utiliza los datos de las
  # respuestas que se dieron al crear el buildout
  [instance]
  recipe = plone.recipe.zope2instance
  zope2-location = ${zope2:location}
  user = admin:admin
  http-address = 8080
  debug-mode = on
  verbose-security = on

  # Aquí se deben listar todos los eggs que zope debe poder ver
  # incluyendo los de desarrollo que se definen arriba
  # e.g. eggs = ${buildout:eggs} ${plone:eggs} my.package
  eggs =
      Plone
      ${buildout:eggs}
      ${plone:eggs}

  # Activar la inicialización de zcml de los paquetes que lo requieran
  # e.g. zcml = my.package my.other.package
  zcml = 

  # Directorios donde zope buscará productos
  products =
      ${buildout:directory}/products
      ${productdistros:location}
      ${plone:products}

  # Interpreté de python generado con todos los paquetes activados en 
  # el path
  [zopepy]
  recipe = zc.recipe.egg
  eggs = ${instance:eggs}
  interpreter = zopepy
  extra-paths = ${zope2:location}/lib/python
  scripts = zopepy

En los comentarios en el codigo se explican las secciones del buildout.


Referencias
===========

-   `¿Qué es buildout?`_.

.. _¿Qué es buildout?: http://www.plone.mx/docs/buildout.html
