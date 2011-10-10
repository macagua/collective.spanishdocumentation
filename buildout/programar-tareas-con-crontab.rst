.. -*- coding: utf-8 -*-

Programar tareas con crontab
============================

Introducción
------------

Este es una configuración básica de `buildout`_ que explica como generar un
programa típico `Hola Mundo`_ en Bash script llamado **"hola"** dentro del
directorio **"bin"** local a tu entorno de desarrollo y otorgar permisos
necesarios para la ejecución de este programa.


Instalación
~~~~~~~~~~~

Puedes instalar zc.buildout usando `pip`_ (es recomendable hacerlo dentro de
un `entorno virtual`_):

.. code-block:: sh

  $ pip install zc.buildout

Ahora crea una nueva configuración zc.buildout así:

.. code-block:: sh

  $ mkdir holamundo ; $ cd holamundo

Inicializar el proyecto 

.. code-block:: sh

  $ buildout init

Ahora el nuevo directorio  holamundo es un buildout. El archivo de
configuración predeterminado de buildout es buildout.cfg . Después de la
inicialización, tendrá el siguiente contenido:

.. code-block:: cfg

  [buildout]
  parts =

Puedes cambiarlo a:

.. code-block:: cfg

  [buildout]

  parts =
      ...
      restart-zope-daily
      ...


  # Este récipe ayuda a configurar una tarea de crontab de rotación de archivos log.
  # Para mayor información ver http://pypi.python.org/pypi/z3c.recipe.usercrontab
  [restart-zope-daily]
  recipe = z3c.recipe.usercrontab
  times = 0 6 * * *
  command = ${buildout:bin-directory}/instance restart


Ahora ejecuta el comando buildout disponible dentro del directorio
*holamundo/bin* con el argumento -v (verbose mode), esto ayudará a que
muestre todo los detalles de la construcción del mismo. Esto creará un nuevo
programa Bash script dentro del directorio *holamundo/bin/hola*:

.. code-block:: sh

  $ ./bin/buildout -v


Ejecute el programa Bash script generado con el siguiente comando:

.. code-block:: sh

  $ ./bin/hola
    hola mundo

Y de esta forma ya tiene generado un programa típico `Hola Mundo`_ en Bash
script con `zc.buildout`_.


Descarga código fuente
~~~~~~~~~~~~~~~~~~~~~~

Para descargar el código fuente de este ejemplo ejecute el siguiente comando:

.. code-block:: sh

  $ svn co https://svn.plone.org/svn/collective/spanishdocs/trunk/src/buildout/leccion2 holamundo


Conclusiones
~~~~~~~~~~~~

Este ejemplo intenta mostrar las capacidades del `zc.buildout`_ como
herramienta alternativa al `Makefile`_ y al `Apache Ant`_.


Referencias
~~~~~~~~~~~

-   `Buildout - How to maintain big app stacks without losing your mind`_.


.. _buildout: http://coactivate.org/projects/ploneve/replicacion-de-proyectos-python
.. _Hola Mundo: http://es.wikipedia.org/wiki/Hola_Mundo
.. _pip: http://coactivate.org/projects/ploneve/distribute-y-pip
.. _entorno virtual: http://coactivate.org/projects/ploneve/creacion-de-entornos-virtuales-python
.. _Makefile: http://es.wikipedia.org/wiki/Makefile
.. _Apache Ant: http://es.wikipedia.org/wiki/Apache_Ant
.. _Buildout - How to maintain big app stacks without losing your mind: http://www.slideshare.net/djay/buildout-how-to-maintain-big-app-stacks-without-losing-your-mind
.. _zc.buildout: http://coactivate.org/projects/ploneve/replicacion-de-proyectos-python
