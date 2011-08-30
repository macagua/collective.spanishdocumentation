Introducción
============

Este es una configuración básica de buildout que explica como instalar una librería zope.component en el Python para tu entorno de desarrollo, además que genera un interprete Python llamado "python" local a tu entorno de desarrollo que incluye la librería zope.component en su PYTHONPATH

Instalación
-----------

  $ pip install zc.buildout
  $ svn co https://svn.plone.org/svn/collective/spanishdocs/trunk/src/buildout/leccion2 holamundo
  $ cd holamundo
  $ buildout init
  $ ./bin/buildout
  $ ./bin/hola
  $ hola mundo
