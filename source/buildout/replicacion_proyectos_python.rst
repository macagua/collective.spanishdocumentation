.. -*- coding: utf-8 -*-

.. _python_buildout:

===============================
Replicación de proyectos Python
===============================

:Autor(es): Leonardo J. Caballero G.
:Correo(s): leonardocaballero@gmail.com
:Lanzamiento: |version|
:Fecha: |today|

.. contents :: :local:

.. _que_es_zcbuildout:

¿Qué es zc.buildout?
====================

Es una herramienta que replica todo un entorno de trabajo aislado. Esto es
una buena práctica para experimentar con código y el estar familiarizado con
estas herramientas será beneficioso para desarrollar e implantar
aplicaciones.

Características
---------------
Estas son sus principales características:

- Permite definición de buildouts de forma declarativa.
- Basado en Python.
- Orientado a desarrollador.
- Se puede replicar.
- Es fácil trabajar con los formatos de paquetes eggs.


Vocabulario
-----------

.. glossary::

  buildout
    Un conjunto de partes que describe como ensamblar una aplicación.

  part
    Un conjunto opciones que le permite a usted construir una pieza de la aplicación.

  recipe
    El software usado para crear una parte basada en sus opciones. 


Instalación
===========
Puedes instalar zc.buildout usando :ref:`pip <que_es_pip>` (es recomendable 
hacerlo dentro de un :ref:`entorno virtual <creacion_entornos_virtuales>`):

.. code-block:: sh

  $ pip install zc.buildout


Configuraciones genéricas
=========================
Usted puede agregar las configuraciones genéricas para todos sus proyectos 
Buildout, para esto debe ejecutar los siguientes comandos:

.. code-block:: sh

  $ mkdir $HOME/.buildout ; mkdir $HOME/.buildout/{eggs,downloads,zope}
  $ nano $HOME/.buildout/default.cfg

Luego de crear el archivo ``default.cfg`` defina algunas configuraciones de 
usuario predeterminadas para cualquier parte de su configuración buildout:

.. code-block:: cfg

  [buildout]
  eggs-directory = /path/to/home/.buildout/eggs
  download-cache = /path/to/home/.buildout/downloads
  zope-directory = /path/to/home/.buildout/zope

.. note::

  Esto solamente proveerá valores predeterminados, ¡estos no sobreescribirán 
  las configuraciones en su configuraciones buildout!


Creación de proyectos buildout
==============================
Ahora crea una nueva configuración zc.buildout así:

.. code-block:: sh

  $ mkdir mibuildout ; cd mibuildout
  $ buildout init

Ahora el nuevo directorio ``mibuildout`` es un proyecto **buildout**. El archivo de
configuración predeterminado del buildout es ``buildout.cfg`` . Después de la
inicialización, tendrá el siguiente contenido:

.. code-block:: cfg

  [buildout]
  parts =

Puedes cambiarlo a:

.. code-block:: cfg

  [buildout]

  parts = py

  [py]
  recipe = zc.recipe.egg
  interpreter = python
  eggs = zope.component

Ahora ejecuta el comando buildout disponible dentro del directorio
``mibuildout/bin`` sin ningún argumento. Esto creará un nuevo interprete Python
dentro del directorio ``mibuildout/bin``:

.. code-block:: sh

  $ ./bin/buildout

Esto creará un nuevo intérprete Python dentro del directorio
``mibuildout/bin``:

.. code-block:: sh

  $ ./bin/python

Y luego tendrá a disposición en su ``PYTHONPATH`` el paquete que instalo
`zope.component`_, como se demuestra a continuación: 

.. code-block:: python

  >>> import zope.component

Utilizando ``zc.buildout`` con la ``recipe`` llamado `zc.recipe.egg`_ se puede crear un
intérprete de Python con los paquetes Egg Python especificados.


Este comando ejecutará un intérprete de Python que puedes usar para ejecutar
el código de su proyecto.


Descarga código fuente
======================

Para descargar el código fuente de este ejemplo ejecute el siguiente comando:

.. code-block:: sh

  $ git clone https://github.com/plone-ve/buildout.basic.git


Conclusiones
============

Este ejemplo intenta mostrar las capacidades del `zc.buildout`_ con el
interprete Python de su entorno de desarrollo.


Referencias
===========

-   :ref:`Arquitectura de componentes Zope <zca-es>`.

.. _zc.buildout: http://pypi.python.org/pypi/zc.buildout/
.. _zope.component: http://pypi.python.org/pypi/zope.component
.. _zc.recipe.egg: http://pypi.python.org/pypi/zc.recipe.egg
