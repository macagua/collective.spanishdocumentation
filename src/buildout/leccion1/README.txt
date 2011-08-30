Introducción
============

Este es una configuración básica de buildout que explica como instalar la librería zope.component generando un interprete Python llamado "python" local a tu entorno de desarrollo que incluye esta librería en su PYTHONPATH

Instalación
-----------

  $ pip install zc.buildout
  $ svn co https://svn.plone.org/svn/collective/spanishdocs/trunk/src/buildout/leccion1 replicar-python
  $ cd replicar-python
  $ buildout init
  $ ./bin/buildout
  $ ./bin/python
  >>> import zope.component
