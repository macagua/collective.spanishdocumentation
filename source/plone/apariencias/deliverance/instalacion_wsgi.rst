.. -*- coding: utf-8 -*-

.. highlight:: rest

.. _instalacion_wsgi:

Instalación como middleware WSGI
================================

Una de las caracteristicas de ``Deliverance`` es que soporta ejecución con un `middleware WSGI`_.

Conceptos básicos
-----------------

.. glossary:

  WSGI 
    Es una Interfaz de Entrasa de Servidor, del Ingles `Web Server Gateway Interface`. 
    Esto es una especificación para servidores web y servidores de aplicación para 
    comunicarse con aplicaciones web (aunque también se puede utilizar para más que eso). 
    Este es un estandar Python, descrito en detalles en `PEP 333`_.


Entonces si usted quiere usar el filtro `middleware WSGI`_, debe agregar esta configuración 
zc.buildout a su archivo ``buildout.cfg``, a continuación un ejemplo:

.. code-block:: cfg

    [buildout]
    versions = versions
    parts =
        lxml
        deliverance

    [versions]
    Deliverance = 0.5.0
    WebOb = 0.9.8
    PasteScript = 1.7.5
    PasteDeploy = 1.5.0

    [lxml]
    recipe = z3c.recipe.staticlxml
    egg = lxml

    [deliverance]
    recipe = zc.recipe.egg
    dependent-scripts = true
    eggs =
        Deliverance
        PasteScript
        PasteDeploy

Además debe crea el archivo ``proxy.ini`` en el directorio de su proyecto 
zc.buidlout con el siguiente comando:

.. code-block:: console

    $ nano ./proxy.ini

Y agregar la siguiente configuración:

.. code-block:: ini

    [server:main]
    use = egg:Paste#http
    host = 0.0.0.0
    port = 5000

    [composite:main]
    use = egg:Paste#urlmap
    /static = static
    / = default

    [app:static]
    use = egg:Paste#static
    document_root = %(here)s/theme

    [pipeline:default]
    pipeline = theme
               content

    [filter:deliverance]
    use = egg:Deliverance
    rule_filename = %(here)s/etc/deliverance.xml
    theme_uri = %(here)s/theme/theme.html
    execute_pyref = true
    debug = true

    # Proxy: por ejemplo, Plone, cuyo nombre es Plone en localhost:8080.
    [app:content]
    use = egg:Paste#proxy
    address = http://localhost:8080/VirtualHostBase/http/localhost:5000/Plone


Si aun no a comenzado de arranque de proyecto, entonces ejecute el siguiente comando:

.. code-block:: console

    $ python bootstrap.py

Como ha realizado cambios a su configuración zc.buildout, debe iniciar 
ejecutar la construcción de su configuración zc.buildout, con el 
siguiente comando:

.. code-block:: console

    $ ./bin/buildout -vN

Al finalizar la construcción de su proyecto más archivos se agregan a los 
scripts disponibles en el directorio ``bin/``, incluyendo ``bin/paster``, ``bin/deliverance-proxy``. 

Una ves terminada la instalación puede iniciar el arranque del mismo con el siguiente comando:

.. code-block:: console

    $ ./bin/paster serve --reload ./proxy.ini

A continuación, puede tener acceso a nuestra página en http://localhost:5000 .

.. _middleware WSGI: http://en.wikipedia.org/wiki/Python_Paste#WSGI_middleware
.. _PEP 333: http://www.python.org/dev/peps/pep-0333/
