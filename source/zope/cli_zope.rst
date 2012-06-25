.. -*- coding: utf-8 -*-

.. _linea_comando_zope:

==========================
Comando de control de Zope
==========================

:Autor(es): Leonardo J. Caballero G.
:Correo(s): leonardocaballero@gmail.com
:Lanzamiento: |version|
:Fecha: |today|

.. contents :: :local:

Descripción general
===================

El comando para las tareas de Zope tasks es ``./bin/instance`` en su instalaciones 
Plone basada en configuraciones buildout.

Para mostrar la lista de comandos disponible ejecute el siguiente comando: 

.. code-block:: sh

  ./bin/instance help

  Documented commands (type help <topic>):
  ========================================
  EOF      debug       help       logtail  restart  show    stop
  adduser  fg          kill       quit     run      start   test
  console  foreground  logreopen  reload   shell    status  wait

  ./bin/instance help kill
  kill [sig] -- Send signal sig to the daemon process.
                The default signal is SIGTERM.
  ./bin/instance help reload
  reload [options] -- Reload the configuration.
      Without options, this reparses the command line.
      With options, this substitutes 'options' for the
      command line, except that if no -C option is given,
      the last configuration file is used.


Para instalaciones antiguas de Plone, el comando es ``zopectl``.

Iniciar la instancia Zope en modo foreground
============================================

En este modo se ejecuta el servidor Zope *foreground* y tiene un alias *fg*

.. code-block:: sh

  ./bin/instance fg

Para cancelar este modo de ejecución use **Ctrl-C** (ej. EOF) para salir.

Iniciar la instancia Zope en modo debug
=======================================

En este modo se ejecuta el servidor Zope en modo *depuración* para inspeccionar su 
base de datos objeto manualmente usando el shell interactivo de Python, con el 
siguiente comando:

.. code-block:: sh

  ./bin/instance debug

Al ejecutar este comando debe mostrar un interprete interactivo de Python al 
contexto de Zope y Plone

.. code-block:: python

  Starting debugger (the name "app" is bound to the top-level Zope object)
  >>> dir(app.Plone.acl_users)
  ['COPY', 'COPY__roles__', 'DELETE', 'DELETE__roles__', 'HEAD', 'HEAD__roles__', 'LOCK', 'LOCK__roles__', 'MKCOL', ...

Para salir de la consola interactiva ejecute la siguiente instrucción:

.. code-block:: python

  >>> quit
Use quit() or Ctrl-D (i.e. EOF) to exit


Iniciar la instancia Zope en modo servicio / demonio
====================================================

En este modo se ejecuta el servidor Zope *demonio* en este modo se utiliza para 
entornos de producción, ejecute con el siguiente comando:

.. code-block:: sh

  ./bin/instance start
  . daemon process started, pid=14643


Detener la instancia Zope en modo servicio / demonio
====================================================

Para esto debió previamente iniciado el servidor Zope *en modo servicio / demonio* 

.. code-block:: sh

  ./bin/instance stop
  . daemon process stopped


Agregando usuarios desde la linea de comandos
=============================================

Usted necesita hacer esto cuando usted olvido la contraseña del usuario 'admin' 
de Zope o la base de datos esta dañada.

Agregar usuario con permisos de Administración en Zope: 

.. code-block:: sh

  ./bin/instance stop # detener primero su instancia de Zope
  ./bin/instance adduser <nombre_usuario> <contraseña_usuario>
  ./bin/instance start


Usted necesita detener primero su instancia de Zope.

Usted no puede sobre escribir el usuario ``admin`` existente, pero 
usted probablemente quiera agregar un usuario adicional ``admin2``.


Referencias
===========

-   `Plone Hosting`_

.. _Plone Hosting: http://collective-docs.readthedocs.org/en/latest/hosting/
