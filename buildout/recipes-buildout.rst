.. -*- coding: utf-8 -*-

================
Récipes Buildout
================

Los récipes son los mecanismos de plugin proveídos por Buildout para agregar
nuevas funcionalidades para construir su software. Una parte del Buildout es
creado por un récipe. Los récipes son siempre instalado como un paquete eggs
de Python. Ellos pueden ser descargados desde un servidor de paquetes, como
el Python Package Index (PyPI), otro ellos pueden ser desarrollados como
parte de un proyecto usando un paquete egg de desarrollo.
Un paquete egg de desarrollo es un tipo especial de paquete egg que se
instala como un vínculo de huevo que contiene el nombre de un directorio de
origen. Los paquetes eggs de desarrollo no tienen que ser empaquetados para
distribución para ser usados y se puede modificar en en sitio, lo cual es
especialmente útil cuando se están desarrollando.

A continuación describo una serie de récipes útiles para la construcción de
Python/Zope/Plone:

- `collective.recipe.plonesite`_, es un récipe buildout para crear
  y actualizar un sitio plone. Este récipe le permite habilitar de crear y
  actualizar un sitio Plone como parte de una ejecución buildout. Este
  récipe sólo tiene por objeto ejecutar perfiles y productos QuickInstall.
  Se supone que los métodos de instalación, setuphandlers, pasos de
  actualización, y otras recetas se encargará del resto del trabajo: 

  .. code-block:: cfg

     parts =
         ...
         plonesite
         ...

     # For options see http://pypi.python.org/pypi/collective.recipe.plonesite
     [plonesite]
     recipe = collective.recipe.plonesite
     site-id = Plone
     instance = instance
     profiles =
         collective.flowplayer:default


- `plone.recipe.command`_, es un récipe buildout para ejecutar
  instrucciones desde linea de comando arbitrariamente desde buildout.

- `mr.developer`_, es una extensión de **zc.buildout** la cual
  hace fácil trabajar con buildouts que contiene muchos paquetes que
  contienen gran cantidad de paquetes de los cuales sólo desea desarrollar
  algunos.

- `collective.recipe.backup`_, proporciona parámetros por defecto
  para las tareas de respaldo de datos comunes. El script ``./bin/repozo`` es
  un script zope para hacer copias de seguridad de ``Data.fs``. 

- `collective.recipe.updateplone`_, es un récipe buildout para actualizar sitios Plone.

- `plone.recipe.apache`_, es un récipe buildout para compilar,
  instalar un servidor Web Apache desde los archivos fuentes con la
  configuración adecuada.

- `zest.recipe.mysql`_, es un récipe buildout para definir una base de datos MySQL.

- `z3c.recipe.ldap`_, es un récipe buildout para desplegar una servidor OpenLDAP.


Existe una lista de récipes buildout disponibles en los siguientes enlaces:

- `Lista de recipes Buildout`_.
- `Recipes Buidout en PYPI`_.


Referencias
-----------

- `Gestión de proyectos con Buildout`_.

.. _collective.recipe.plonesite: http://collective.recipe.plonesite/
.. _collective.recipe.backup: http://collective.recipe.backup/
.. _plone.recipe.apache: http://plone.recipe.apache/
.. _z3c.recipe.ldap: http://z3c.recipe.ldap/
.. _collective.recipe.updateplone: http://collective.recipe.updateplone/
.. _zest.recipe.mysql: http://zest.recipe.mysql/
.. _plone.recipe.command: http://plone.recipe.command/
.. _mr.developer: http://pypi.python.org/pypi/mr.developer
.. _Lista de recipes Buildout:  http://www.buildout.org/docs/recipelist.html
.. _Recipes Buidout en PYPI: http://pypi.python.org/pypi?:action=search&term=recipe+buildout&submit=search
.. _Gestión de proyectos con Buildout: http://coactivate.org/projects/ploneve/gestion-de-proyectos-con-buildout
