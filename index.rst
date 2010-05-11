==========================
Mejores Practicas de Plone
==========================

Desarrollar un sitio con Plone requiere de la combinacion de una serie de
tecnologias y conocimientos, desde HTML hasta desarrollo avanzado con Python.
A lo largo del tiempo, la comunidad de Plone ha ido experimentando y
adoptando diversas formas de trabajar un proyecto, las cuales hoy en dia
pueden considerarse como las mejores practicas de desarrollo con Plone.

Algunas de estas practicas se refieren por supuesto a la programacion con
Python y a la construccion de aplicaciones administracion de contenido con
Plone, pero hay algunas otras que rebasan el ambito de Plone y son utiles
para cualquier ambiente de desarrollo.

En este texto vamos a abordar una por una diversas practicas que consideramos
invaluables para el trabajo profesional con Plone. La intencion es demostrar
la manera en que se integra un ambiente de desarrollo ideal para desarrollar
con Plone.

Ademas de las mejores practicas, conoceremos en detalle algunas de las
principales tecnologias de Zope y Plone.

En particular, conoceremos:

Python
------

Python es el lenguaje con el que estan desarrollados tanto Zope como Plone,
por lo que es muy importante conocerlo para poder tomar maxima ventaja de
estos sistemas. Es imprescindible programar en Python para poder crear
productos y tipos de contenido para Plone.

En esta seccion tenemos el tutorial oficial de Python, preparado por la
asociacion de Python de Argentina y la fundacion de Python.

.. toctree::
   :maxdepth: 2

   Tutorial de Python <python/python-tutorial/index>

Tutorial de Subversion
----------------------

Para tener un ambiente de desarrollo productivo, en especial cuando se
trabaje en equipo, es muy importante contar con un sistema de control de
versiones. Subversion es el utilizado por plone.org y el plone collective,
por lo que consideramos necesario conocerlo, aunque recientemente la
popularidad de sistemas distribuidos como Git y Mercurial ha aumentado.

.. toctree::
   :maxdepth: 2

   subversion

Buildout y setuptools
---------------------

Buildout es un sistema que permite definir ambientes de desarrollo
repetibles, incluyendo dependencias y configuracion. Buildout se apoya
fuertemente en setuptools, que permite instalar paquetes de Python a traves
de Internet. Es recomendable utilizar buildout para cualquier proyecto de
Plone que se quiera emprender.

.. toctree::
   :maxdepth: 2

   setuptools
   buildout

Tecnologias de Zope
-------------------

Plone esta basado en el servidor de aplicaciones Zope y en un toolkit de
desarrollo de portales llamado CMF. Para trabajar con Plone es necesario
conocer diversas tecnologias provenientes de estos sistemas.

.. toctree::
   :maxdepth: 2

   zpt
   zcatalog
   workflow
   gs

Temas varios de Plone
---------------------

Existen muchos temas importantes para el desarrollo con Plone, en esta
seccion tocaremos algunos de ellos.

.. toctree::
   :maxdepth: 2

   productos
   policy
   tema
   minituts

Otros recursos
--------------

.. toctree::
   :maxdepth: 2

   links
   presentaciones
   
Indices y tablas
================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

