Introducción
============

Este es una configuración básica de buildout que explica como generar un programa Python llamado "hola" dentro del directorio "bin" local a tu entorno de desarrollo y otorgar permisos necesarios para la ejecución de este programa Python

Instalación
-----------

  $ pip install zc.buildout
  $ svn co https://svn.plone.org/svn/collective/spanishdocs/trunk/src/buildout/leccion2 holamundo
  $ cd ./holamundo
  $ buildout init
  $ ./bin/buildout
  $ ./bin/hola
  $ hola mundo
