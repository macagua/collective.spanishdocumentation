.. -*- coding: utf-8 -*-

=====================================
Creando instancias adicional de debug
=====================================

Es posible que desee mantener su buildout.cfg para producción y sincronizar 
la configuración de desarrollo de forma automática como sea posible.

Una buena idea es utilizar buildout.cfg misma en cada entorno. Si con cosas condicionales, 
como poner el modo de depuración activo, como es requerido, usted puede ampliar las
secciones buildout, que a su vez crear "Zopes adicionales" bajo carpeta bin/ 
con la siguiente configuración:

.. code-block:: cfg

  [instance]
  recipe = plone.recipe.zope2instance
  zope2-location = ${zope2:location}
  user = admin:x
  http-address = 8080
  debug-mode = off
  verbose-security = off

  ...

  environment=
      PTS_LANGUAGES=en es pt

  # Crear un script lanzado el cual iniciará una 
  # instancia Zope en modo debug
  [debug-instance]
  # Extend the main production instance
  <= instance

  # Aquí sobre escribes configuraciones especifica 
  # para hacer la instancia que se ejecute en modo debug
  debug-mode = on
  verbose-security = on
  event-log-level = DEBUG

Y ahora usted puede iniciar si instancia de **desarrollo** Zope como: 

.. code-block:: sh

  ./bin/debug-instance fg

Y su instancia principal de Zope stays en modo de producción: 

.. code-block:: sh

  ./bin/instance

.. note::

    Usando el modo fg focus siempre de Zope a modo depuración, pero no registra en el nivel de log.

Referencias
===========

-   `Plone Hosting`_

.. _Plone Hosting: http://collective-docs.readthedocs.org/en/latest/hosting/
