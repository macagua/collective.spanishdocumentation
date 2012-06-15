.. -*- coding: utf-8 -*-

.. _buildout_holamundo:

=========================
Hola mundo en zc.buildout
=========================

:Autor(es): Leonardo J. Caballero G.
:Correo(s): leonardocaballero@gmail.com
:Lanzamiento: |version|
:Fecha: |today|

.. contents :: :local:

Descripción general
===================

Este es una configuración básica de :ref:`buildout <python_buildout>` que explica como generar un
programa típico `Hola Mundo`_ en Bash script llamado **"hola"** dentro del
directorio ``bin/`` local a tu entorno de desarrollo y otorgar permisos
necesarios para la ejecución de este programa.


Instalación
===========

Puedes instalar zc.buildout usando :ref:`pip <que_es_pip>` (es recomendable 
hacerlo dentro de un :ref:`entorno virtual <creacion_entornos_virtuales>`):

.. code-block:: sh

  $ pip install zc.buildout

Ahora crea una nueva configuración zc.buildout así:

.. code-block:: sh

  $ mkdir holamundo ; $ cd holamundo

Inicializar el proyecto 

.. code-block:: sh

  $ buildout init

Ahora el nuevo directorio holamundo es un proyecto buildout. El archivo de
configuración predeterminado de este proyecto es ``buildout.cfg``. Después de la
inicialización, tendrá el siguiente contenido:

.. code-block:: cfg

  [buildout]
  parts =

Puedes cambiarlo a:

.. code-block:: cfg

  [buildout]

  parts =
      hola-mundo
      chmod

  # Este récipe ayuda a generar un programa Bash script llamado "hola"
  # dentro del directorio "bin" local a tu entorno de desarrollo
  # Para mayor información consulte http://pypi.python.org/pypi/collective.recipe.template
  [hola-mundo]
  recipe = collective.recipe.template
  output = ${buildout:bin-directory}/hola
  input = inline:
    echo 'hola mundo'

  # Este récipe ayuda otorgar permisos de ejecución al programa generado en la sección "hola-mundo"
  # Para mayor información consulte http://pypi.python.org/pypi/plone.recipe.command
  [chmod]
  recipe = plone.recipe.command
  command = chmod u+x ${hola-mundo:output}


Ahora ejecuta el comando buildout con el argumento ``-v`` (verbose mode), esto ayudará a que
muestre todo los detalles de la construcción del mismo. 

.. code-block:: sh

  $ ./bin/buildout -v

Esto creará un nuevo programa Bash script dentro del directorio ``bin/hola``. Ejecute 
el programa Bash script generado con el siguiente comando:

.. code-block:: sh

  $ ./bin/hola
    hola mundo

Y de esta forma ya tiene generado un programa típico `Hola Mundo`_ en Bash
script con :ref:`zc.buildout <que_es_zcbuildout>`.


Descarga código fuente
======================

Para descargar el código fuente de este ejemplo ejecute el siguiente comando:

.. code-block:: sh

  $ svn co https://svn.plone.org/svn/collective/spanishdocs/trunk/src/buildout/leccion2 holamundo


Conclusiones
============

Este ejemplo intenta mostrar las capacidades del :ref:`zc.buildout <que_es_zcbuildout>` como
herramienta alternativa al `Makefile`_ y al `Apache Ant`_.


Artículos relacionados
======================

.. seealso:: Artículos sobre :ref:`replicación de proyectos Python <python_buildout>`.


Referencias
===========

- `Buildout - How to maintain big app stacks without losing your mind`_.


.. _Hola Mundo: http://es.wikipedia.org/wiki/Hola_Mundo
.. _Makefile: http://es.wikipedia.org/wiki/Makefile
.. _Apache Ant: http://es.wikipedia.org/wiki/Apache_Ant
.. _Buildout - How to maintain big app stacks without losing your mind: http://www.slideshare.net/djay/buildout-how-to-maintain-big-app-stacks-without-losing-your-mind
