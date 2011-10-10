.. -*- coding: utf-8 -*-

===============================
Replicación de proyectos Python
===============================

¿Que es zc.buildout?
--------------------

Es una herramienta que replica todo un entorno de trabajo aislado. Esto es
una buena práctica para experimentar con código y el estar familiarizado con
estas herramientas será beneficioso para desarrollar e implantar
aplicaciones.


Puedes instalar `zc.buildout`_ usando `pip`_ (es recomendable hacerlo dentro
de un `entorno virtual`_):

.. code-block:: sh

  $ pip install zc.buildout

Ahora crea una nueva configuración zc.buildout asi:

.. code-block:: sh

  $ mkdir mibuildout ; cd mibuildout
  $ buildout init

Ahora el nuevo directorio *mibuildout* es un buildout. El archivo de
configuración predeterminado de buildout es **buildout.cfg** . Después de la
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
*mibuildout/bin* sin ningún argumento. Esto creará un nuevo interprete Python
dentro del directorio *mibuildout/bin*:

.. code-block:: sh

  $ ./bin/buildout

Esto creará un nuevo intérprete Python dentro del directorio
*mibuildout/bin*:

.. code-block:: sh

  $ ./bin/python

Y luego tendrá a disposición en su PythonPath el paquete que instalo
`zope.component`_, como se demuestra a continuación: 

.. code-block:: python

  >>> import zope.component

Utilizando zc.buildout con la receta `zc.recipe.egg`_ se puede crear un
intérprete de Python con los huevos Python especificados.


Este comando ejecutará un intérprete de Python que puedes usar para ejecutar
el código de su proyecto.


Descarga código fuente
~~~~~~~~~~~~~~~~~~~~~~

Para descargar el código fuente de este ejemplo ejecute el siguiente comando:

.. code-block:: sh

  $ svn co https://svn.plone.org/svn/collective/spanishdocs/trunk/src/buildout/leccion1 mibuildout


Conclusiones
~~~~~~~~~~~~

Este ejemplo intenta mostrar las capacidades del `zc.buildout`_ con el
interprete Python de su entorno de desarrollo.


Referencias
~~~~~~~~~~~

-   `Arquitectura de componentes Zope`_.

.. _zc.buildout: http://pypi.python.org/pypi/zc.buildout/
.. _pip: http://coactivate.org/projects/ploneve/distribute-y-pip
.. _entorno virtual: http://coactivate.org/projects/ploneve/creacion-de-entornos-virtuales-python
.. _zope.component: http://pypi.python.org/pypi/zope.component
.. _zc.recipe.egg: http://pypi.python.org/pypi/zc.recipe.egg
.. _Arquitectura de componentes Zope: http://www.muthukadan.net/docs/zca-es.html
