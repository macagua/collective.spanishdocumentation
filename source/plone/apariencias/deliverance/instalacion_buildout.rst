.. -*- coding: utf-8 -*-

.. highlight:: rest

.. _instalacion_buildout:

Instalando con buildout
=======================

Si estas usando zc.buildout, usted puede usar la siguiente configuración 
dentro de ``buildout.cfg`` como punto de arranque. Este asegura que el 
script de consola ``deliverance-proxy`` esté instalado, lo cual es importante 
si usted necesita ejecutar manualmente el `servidor proxy`_ Deliverance:

.. code-block:: cfg

    [buildout]
    versions = versions
    parts =
       ...
       deliverance-server
       ...
    [versions]
    Deliverance = 0.5.0
    WebOb = 0.9.8
    PasteScript = 1.7.5
    PasteDeploy = 1.5.0

    [deliverance-server]
    recipe = zc.recipe.egg
    eggs =
        Deliverance
        PasteScript

.. note::
    
    Opcionalmente, en algunos sistemas operativos, en particular, Mac OS X la instalación 
    de un "buen" paquete (Python egg) de ``lxml`` puede ser problemático, debido a una 
    falta de coincidencia en las versiones del sistema operativo de las librerías ``lxml`` 
    con respecto a la ``libxml2`` y ``libxslt``. Para resolver esto, se puede compilar 
    un ``lxml`` estático de paquete egg usando la siguiente receta buildout:

    .. code-block:: cfg

        [buildout]
        versions = versions
        # lxml debería estar de primero en la lista ``parts``
        parts =
           lxml
           deliverance-server
        
        [versions]
        Deliverance = 0.5.0
        WebOb = 0.9.8
        PasteScript = 1.7.5
        PasteDeploy = 1.5.0
        
        [lxml]
        recipe = z3c.recipe.staticlxml
        egg = lxml
        
        [deliverance-server]
        recipe = zc.recipe.egg
        eggs =
            Deliverance
            PasteScript


Entonces usted tiene que comenzar de arranque:

.. code-block:: console

    $ python bootstrap.py

Luego ejecute la construcción de su configuración zc.buildout, con el siguiente comando:

.. code-block:: console

    $ ./bin/buildout -vN


.. note::
    
    Note que el paquete lxml es una dependencia de Deliverance, usted podría 
    necesitar instalar los paquetes de desarrollo de libxml2 y libxslt para 
    poder construir esta configuración zc.buildout. En Debian/Ubuntu Linux usted puede ejecutar:

    .. code-block:: console
        
        $ sudo apt-get install build-essential python-dev libxml2-dev libxslt1-dev

    Luego vuelva a ejecutar la construcción de su configuración zc.buildout como en paso anterior

Usted debería ver algo como esto:

.. code-block:: console
 
    Generated script '/home/user/deliverancedemo/bin/paster'.
    Generated script '/home/user/deliverancedemo/bin/deliverance-proxy'.

Una ves instalado, usted debería buscar el script ``deliverance-proxy`` en el directorio ``bin``.


Creando una configuración
-------------------------

Luego de finalizar la intalación correctamente debe tener disponible 
en el script ``bin/paster`` el cual tiene disponible dos plantillas 
PasteScript para construir sitios con configuraciones Deliverance, 
para comprobar esto ejecute el siguiente comando:

.. code-block:: console

    $ ./bin/paster create --list-templates
    Available templates:
      archetype:          A Plone project that uses Archetypes content types
      basic_buildout:     A basic buildout skeleton
      basic_namespace:    A basic Python project with a namespace package
      basic_package:      A basic setuptools-enabled package
      basic_zope:         A Zope project
      nested_namespace:   A basic Python project with a nested namespace (2 dots in name)
      paste_deploy:       A web application deployed through paste.deploy
      plone_basic:        A project for Plone products
      recipe:             A recipe project for zc.buildout
      deliverance:        Basic template for a deliverance-proxy setup
      deliverance_plone:  Plone-specific template for deliverance-proxy


Debería tener disponible la plantilla Paster ``deliverance`` y ``deliverance_plone`` 
la primera le permite crear una configuración básica para la instalación del 
servidor proxy Deliverance y la segunda permite crear una configuración especifica 
de Plone con un servidor proxy Deliverance.

A continuación se demostra cada creación de cada una de las plantillas Paster descritas 
anteriormente, con el siguiente comando:

.. code-block:: console

    $ ./bin/paster create -t deliverance mi-ejemplo-basico
    Selected and implied templates:
      Deliverance#deliverance  Basic template for a deliverance-proxy setup

    Variables:
      egg:      mi_ejemplo_basico
      package:  miejemplobasico
      project:  mi-ejemplo-basico
    Enter host (The host/port to serve on) ['localhost:8000']: localhost:5000
    Enter proxy_url (The main site to connect/proxy to) ['http://localhost:8080']: localhost:8000
    Enter proxy_rewrite_links (Rewrite links from sub_host?) ['n']: y
    Enter password (The password for the deliverance admin console) ['']: secret
    Enter theme_url (A URL to pull the initial theme from (optional)) ['']: 
    Creating template deliverance
    Creating directory ./mi-ejemplo-basico
      Recursing into etc
        Creating ./mi-ejemplo-basico/etc/
        Copying deliv-users.htpasswd_tmpl to ./mi-ejemplo-basico/etc/deliv-users.htpasswd
        Copying deliverance.xml_tmpl to ./mi-ejemplo-basico/etc/deliverance.xml
        Recursing into supervisor.d
          Creating ./mi-ejemplo-basico/etc/supervisor.d/
          Copying deliverance.conf_tmpl to ./mi-ejemplo-basico/etc/supervisor.d/deliverance.conf
        Copying supervisord.conf_tmpl to ./mi-ejemplo-basico/etc/supervisord.conf
    Creating ./mi-ejemplo-basico/theme
    Creating ./mi-ejemplo-basico/theme/theme.html
    Creating ./mi-ejemplo-basico/theme/style.css


En el caso que requiera aplicar configuraciones Deliverance con sitios web Plone, 
para hacer esto ejecute el siguiente comando:

.. code-block:: console

    $ ./bin/paster create -t deliverance_plone mi-ejemplo-plone
    Selected and implied templates:
      Deliverance#deliverance        Basic template for a deliverance-proxy setup
      Deliverance#deliverance_plone  Plone-specific template for deliverance-proxy

    Variables:
      egg:      mi_ejemplo_plone
      package:  miejemploplone
      project:  mi-ejemplo-plone
    Enter site_name (The name of your Plone site (no /'s)) ['']: Plone
    Enter host (The host/port to serve on) ['localhost:8000']: localhost:5000
    Enter proxy_url (The main site to connect/proxy to) ['http://localhost:8080']: 
    Enter proxy_rewrite_links (Rewrite links from sub_host?) ['n']: y
    Enter password (The password for the deliverance admin console) ['']: secret
    Enter theme_url (A URL to pull the initial theme from (optional)) ['']: 
    Creating template deliverance
    Creating directory ./mi-ejemplo-plone
      Recursing into etc
        Creating ./mi-ejemplo-plone/etc/
        Copying deliv-users.htpasswd_tmpl to ./mi-ejemplo-plone/etc/deliv-users.htpasswd
        Copying deliverance.xml_tmpl to ./mi-ejemplo-plone/etc/deliverance.xml
        Recursing into supervisor.d
          Creating ./mi-ejemplo-plone/etc/supervisor.d/
          Copying deliverance.conf_tmpl to ./mi-ejemplo-plone/etc/supervisor.d/deliverance.conf
        Copying supervisord.conf_tmpl to ./mi-ejemplo-plone/etc/supervisord.conf
    Creating ./mi-ejemplo-plone/theme
    Creating ./mi-ejemplo-plone/theme/theme.html
    Creating ./mi-ejemplo-plone/theme/style.css
    Creating template deliverance_plone
      Recursing into etc
    Replace 1601 bytes with 2062 bytes (3/49 lines changed; 9 lines added)
        Copying deliverance.xml_tmpl to ./mi-ejemplo-plone/etc/deliverance.xml

Usted debe iniciar la instancia Zope, con el siguiente comando:

.. code-block:: console

    $ ./bin/instance start

Y para finzalizar, sin importar la plantilla usada para crear la configuración, 
igualmente debe ejecutar manualmente el `servidor proxy`_ Deliverance, puede 
hacerlo ejecutando el siguiente comando:

.. code-block:: console

    $ ./bin/deliverance-proxy ./etc/deliverance.xml
    To see logging, visit http://localhost:5000/.deliverance/login
        after login go to http://localhost:5000/?deliv_log
    serving on http://localhost:5000

Como puede ver le esta indicando que Deliverance esta siendo servido por la 
dirección URL http://localhost:5000/ aplicando su estilo y tema HTML al contenido 
como se define en la archivo deliverance.xml

Para acceder a la consola depuración de iniciar sesión por la dirección URL http://localhost:5000/.deliverance/login y luego acceder a la dirección URL http://localhost:5000/?deliv_log

.. _Deliverance: http://pypi.python.org/pypi/Deliverance
.. _DeliveranceDemo: http://svn.plone.org/svn/collective/deliverancedemo/trunk/
.. _servidor proxy: http://es.wikipedia.org/wiki/Servidor_proxy
