.. -*- coding: utf-8 -*-

.. highlight:: rest

.. _deliverance_instalacion:

===========
Instalación
===========

Para instalar Deliverance, usted podría instalar la distribución de `Deliverance`_ de PyPI.

.. note::

    El paquete Deliverance sólo se requiere para obtener el comando para manipular el `servidor proxy`_ Deliverance.

Usted puede instalar la distribución de `Deliverance`_ usando `easy_install`_, `pip`_ 
o `zc.buildout`_. Por ejemplo, usando ``easy_install`` (sería ideal si se ejecuta dentro 
de un `entorno virtual`_ Python):

.. code-block:: console

    $ easy_install -U Deliverance

Usted también puede instalar con la herramienta ``pip`` si es su preferencia, 
puede realizarlo con el siguiente comando:

.. code-block:: console

    $ pip install Deliverance


Modos de instalación
====================

Para este caso se instalara el ejemplo de instalación llamado `DeliveranceDemo`_

.. toctree::
   :maxdepth: 2

   instalacion_buildout
   instalacion_wsgi


.. _Deliverance: http://pypi.python.org/pypi/Deliverance
.. _easy_install: http://plone-spanish-docs.readthedocs.org/en/latest/python/setuptools.html
.. _pip: http://plone-spanish-docs.readthedocs.org/en/latest/python/distribute-y-pip.html
.. _zc.buildout: http://plone-spanish-docs.readthedocs.org/en/latest/buildout/replicacion-de-proyectos-python.html#que-es-zc-buildout
.. _entorno virtual: http://plone-spanish-docs.readthedocs.org/en/latest/python/creacion-de-entornos-virtuales-python.html
.. _middleware WSGI: http://en.wikipedia.org/wiki/Python_Paste#WSGI_middleware
.. _DeliveranceDemo: http://svn.plone.org/svn/collective/deliverancedemo/trunk/
.. _servidor proxy: http://es.wikipedia.org/wiki/Servidor_proxy
