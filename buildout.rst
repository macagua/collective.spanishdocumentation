*****************
¿Qué es buildout?
*****************

.. contents :: :local:

Una herramienta para administrar, a través de un archivo de configuración
declaratoria, las partes y componentes de un desarrollo con Python.  Dichas
partes no están limitadas a componentes o código Python.

La parte más poderosa de buildout es que puede extenderse con el uso de
"recetas" que pueden instalar componentes más complicados simplemente
agregando nuevas secciones a la configuración. Buildout puede instalar
diversos paquetes de Python fácilmente porque está conectado con el índice
de paquetes de Python (http://www.python.org/pypi).

Algunos términos importantes
----------------------------

**Instalación de Zope**.
    El software propio del servidor de aplicaciones.

**Instancia de Zope**.
    Un directorio específico que contiene una configuración completa de Zope.

**Paquete de Python**.
    Básicamente, una carpeta con código Python que contiene un archivo
    __init__.py.

**Producto de Zope**.
    Un paquete de Python especial para extender Zope.

**Huevo (Python egg)**.
    Un mecanismo para empaquetar y distribuir paquetes de Python.

**Cheese shop (PYPI)**.
    Un repositorio de paquetes de Python.

**easy_install**.
    Un script de línea de comando que permite instalar a través de la red
    paquetes del PYPI.

Requisitos previos
------------------

Existen instrucciones detalladas para la instalación de requisitos, pero en
general se necesita lo siguiente:

* Python 2.4.x.
* Python setuptools (easy_install)
* Para Zope, ZopeSkel (egg).
* Para Plone, Python Imaging Library (PIL) instalado en ese Python.

Creación de un buildout
-----------------------

Se puede generar un buildout utilizando un template de paster::

    $ paster create -t plone3_buildout buildout

El template hace varias preguntas::

    Selected and implied templates:
      ZopeSkel#plone3_buildout  A buildout for Plone 3 projects

    Variables:
      egg:      buildout
      package:  buildout
      project:  buildout

    Enter zope2_install (Path to Zope 2 installation; leave blank to fetch one) ['']:
    <si ya se tiene una instalación de Zope se puede usar poniendo aquí el path>
    Enter plone_products_install (Path to directory containing Plone products; leave blank to fetch one) ['']:
    <lo mismo aquí si ya se tienen los productos de Plone>
    Enter zope_user (Zope root admin user) ['admin']:
    <el usuario administrador del sitio>
    Enter zope_password (Zope root admin password) ['']:
    <el password para este usuario>
    Enter http_port (HTTP port) [8080]:
    <el puerto donde escuchará el servicio de Zope>
    Enter debug_mode (Should debug mode be "on" or "off"?) ['off']:
    <'on' para activar el modo de debug>
    Enter verbose_security (Should verbose security be "on" or "off"?) ['off']:
    <'on' para presentar detalles cuando ocurran errores de privilegios>
    ...
    ...
    ...
    -----------------------------------------------------------
    Generation finished
    You probably want to run python bootstrap.py and then edit
    buildout.cfg before running bin/buildout -v

    See README.txt for details
    -----------------------------------------------------------

Activación de un buildout
-------------------------

Para activar un buildout hay que ejecutar el script `bootstrap.py` con el
mismo python con que se desea trabajar::

    $ cd unam.buildout
    $ python2.4 bootstrap.py
    ...
    ...
    ...
    $ bin/buildout
    ...
    ...
    ...
    $ bin/instance start

Directorios creados
-------------------

**bin**.
    Ejecutables de buildout y producidos por las partes.

**eggs**.
    Los eggs obtenidos e instalados de PYPI.

**downloads**.
    Software adicional descargado. 

**var**.
    Logs y archivo de ZODB de Zope (buildout nunca sobreescribe estos archivos).

**src**.
    Código fuente de nuestros desarrollos.

**products**.
    Productos tradicionales de zope.

**parts**.
    Todo el código, configuración y datos manejados por buildout.

Ejemplo
-------

Un ejemplo de un buildout funcional se muestra a continuación:

.. code-block:: ini

    # definicion de las partes que va a tener el buildout, cada parte es una
    # sección de configuración y generalmente utiliza una receta específica
    [buildout]
    parts =
        zope2
        productdistros
        instance
        zopepy

    # ligas adicionales a pypi.python.org donde pueden encontrarse eggs
    find-links =
        http://dist.plone.org
        http://download.zope.org/ppix/
        http://download.zope.org/distribution/
        http://effbot.org/downloads

    # Agregar eggs adicionales aquí
    # elementtree es requerido por Plone
    eggs =
        elementtree
    
    # Por cada paquete en desarrollo (dentro de src) se debe agregar una línea
    # e.g.: develop = src/my.package
    develop =

    # Esta receta instala zope 2. Para usar la misma url que requiere plone se
    # utiliza ${plone:zope2-url}. Es posible referirse con esta sintaxis a
    # cualquier variable de una de las partes, así: ${parte:variable}
    [zope2]
    recipe = plone.recipe.zope2install
    url = ${plone:zope2-url}

    # Ligas a distribuciones de productos tradicionales de Zope.
    # En nested-packages se pone el nombre del archivo (sin path) cuando
    # una distribución incluye varios productos.
    [productdistros]
    recipe = plone.recipe.distros
    urls =
    nested-packages =
    version-suffix-packages = 

    # esta receta inicializa la instancia de zope y utiliza los datos de las
    # respuestas que se dieron al crear el buildout
    [instance]
    recipe = plone.recipe.zope2instance
    zope2-location = ${zope2:location}
    user = admin:admin
    http-address = 8080
    debug-mode = on
    verbose-security = on

    # Aquí se deben listar todos los eggs que zope debe poder ver
    # incluyendo los de desarrollo que se definen arriba
    # e.g. eggs = ${buildout:eggs} ${plone:eggs} my.package
    eggs =
        Plone
        ${buildout:eggs}
        ${plone:eggs}

    # Activar la inicialización de zcml de los paquetes que lo requieran
    # e.g. zcml = my.package my.other.package
    zcml = 

    # Directorios donde zope buscará productos
    products =
        ${buildout:directory}/products
        ${productdistros:location}
        ${plone:products}

    # Interpreté de python generado con todos los paquetes activados en 
    # el path
    [zopepy]
    recipe = zc.recipe.egg
    eggs = ${instance:eggs}
    interpreter = zopepy
    extra-paths = ${zope2:location}/lib/python
    scripts = zopepy

En los comentarios en el codigo se explican las secciones del buildout.

Utilización de buildout para instalación de todas las partes de un sitio
========================================================================

Buildout permite no solamente instalar Zope y Plone, sino cualquier parte de
la arquitectura de un sitio, desde el servidor web de front end hasta el
balanceador de carga o la base de datos. Un sitio plone poderoso requiere
muchas partes distintas y mediante buildout podemos instalarlas todas de una
sola vez. El beneficio adicional de esto es que obtenemos un solo script de
configuración con el cual se puede repetir la instalación completa de todas
las partes del sitio. Para conocer ejemplos de esto de una manera práctica,
revisaremos paso por paso un script completo de buildout, comentando las
diferentes partes que utilizaremos.

.. image:: highavail.png

Lo primero es definir las secciones de construcción del software necesario.
Lxml y xdv son componentes que forman parte de deliverance, que es un
mecanismo para generar los temas visuales de los sitios de Plone mediante
reglas de XSLT, evitando que el diseñador requiera conocer a fondo Plone y sus
mecanismos de temas. Lxml tiene su propia receta y xdv utiliza la receta
básica de instalación de paquetes de Python:

.. code-block:: ini

    [lxml]
    recipe = z3c.recipe.staticlxml
    egg = lxml
    force = false
    [xdv]
    recipe = zc.recipe.egg
    eggs =
       lxml
       PasteScript
       dv.xdvserver
    scripts =
       paster
       xdvcompiler

La construcción de Zope y el servidor de ZEO utilizan asímismo sus propias
recetas. Algunas declaraciones es mejor definirlas como variables para poder
reutilizarlas en otras partes del buildout sin tener que definirlas más de una
vez. Estas definiciones de variables constan de una cadena encerrada entre
llaves y precedida por el símbolo $, de esta manera: ${parte:nombre}. En esta
sintaxis, parte se refiere a la sección del buildout definida entre corchetes
[] donde se define la variable y nombre corresponde a la variable definida
dentro de esa sección:

.. code-block:: ini

    [zope2]
    recipe = plone.recipe.zope2install
    fake-zope-eggs = true
    additional-fake-eggs =
       ZConfig
       pytz
    skip-fake-eggs =
       zope.testing
       zope.i18n
    url = ${downloads:zope}
    [zeoserver]
    recipe = plone.recipe.zope2zeoserver
    zope2-location = ${zope2:location}
    zeo-address = ${ports:zeo-server}
    effective-user = ${users:zope}
    zeo-var = ${buildout:directory}/var
    blob-storage = ${zeoserver:zeo-var}/blobstorage
    eggs = plone.app.blob

Como según nuestro diagrama de arquitectura del sitio deseamos tener cuatro
clientes en un cluster, lo mejor es utilizar la receta existente para generar
cluster de Plone en lugar de la típica receta de zope2instance. La parte
importante aquí es la definición de instance-clone, que representa una
definición de molde que contendrá valores de configuración que serán
utilizados por los cuatro clientes. Siempre se recomienda utilizar variables
para la definición de hosts y puertos, de tal forma que puedan configurarse en
una sección separada:

.. code-block:: ini

    [instance1]
    recipe = collective.recipe.zope2cluster
    instance-clone = instance-settings
    http-address = ${hosts:instance1}:${ports:instance1}
    zope-conf-additional =
       <icp-server>
          address ${ports:instance1-icp}
       </icp-server>
    [instance2]
    recipe = collective.recipe.zope2cluster
    instance-clone = instance-settings
    http-address = ${hosts:instance2}:${ports:instance2}
    zope-conf-additional =
       <icp-server>
          address ${ports:instance2-icp}
       </icp-server>
    [instance3]
    recipe = collective.recipe.zope2cluster
    instance-clone = instance-settings
    http-address = ${hosts:instance3}:${ports:instance3}
    zope-conf-additional =
       <icp-server>
          address ${ports:instance3-icp}
       </icp-server>
    [instance4]
    recipe = collective.recipe.zope2cluster
    instance-clone = instance-settings
    http-address = ${hosts:instance4}:${ports:instance4}
    zope-conf-additional =
       <icp-server>
          address ${ports:instance4-icp}
       </icp-server>

Es recomendable también incluir una instancia de debug que no sea iniciada
automáticamente para poder conectarse al sitio sin interferir con el cluster
de producción:

.. code-block:: ini

    [instance-debug]
    recipe = collective.recipe.zope2cluster
    instance-clone = instance-settings
    http-address = ${hosts:instance-debug}:${ports:instance-debug}
    debug-mode = on
    verbose-security = on

Nginx es un servidor web de alto desempeño, que es cada vez más utilizado en
el mundo de Plone. La receta cmmi que se utiliza baja el paquete, lo
configura, lo compila y lo instala. Esto significa que dicha receta puede
utilizarse en realidad para instalar cualquier paquete de Unix que utilice
este mecanismo de compilación e instalación:

.. code-block:: ini

    [nginx-build]
    recipe = hexagonit.recipe.cmmi
    url = ${downloads:nginx}
    patches =
       ${buildout:directory}/patches/nginx-xslt.patch
       ${buildout:directory}/patches/nginx-xslt-options.patch
       ${buildout:directory}/patches/nginx-xslt-conf.patch
    configure-options =
       --with-http_xslt_module
       --with-http_stub_status_module
       --with-libxml2=${buildout:directory}/parts/libxml2
       --with-libxslt=${buildout:directory}/parts/libxslt
       --conf-path=${buildout:directory}/production/nginx/default.conf
       --error-log-path=${buildout:directory}/var/log/main-error.log
       --pid-path=${buildout:directory}/var/main.pid
       --lock-path=${buildout:directory}/var/main.lock

Varnish es un motor de cacheo que guarda las respuestas de las peticiones
dinámicas que se hacen a Plone y las sirve directamente de disco para mejorar
el desempeño:

.. code-block:: ini

    [varnish-build]
    recipe = hexagonit.recipe.cmmi
    url = ${downloads:varnish}

HAProxy es un balanceador de carga que distribuye las peticiones al sitio
entre los cuatro clientes definidos:

.. code-block:: ini

    [haproxy-build]
    recipe = plone.recipe.haproxy
    url = http://dist.jarn.com/public/haproxy-1.3.15.7.zip
    cpu = ${build:cpu}
    target = ${build:target}

La configuración del servidor web principal de Nginx se hace utilizando como
template un archivo almacenado en el buildout. La configuración de Varnish
funciona de la misma manera:

.. code-block:: ini

    [main-config]
    recipe = collective.recipe.template
    input = ${buildout:directory}/production/main.conf.template
    output = ${buildout:directory}/production/main.conf
    [compile-theme]
    recipe = plone.recipe.command
    command = ${buildout:directory}/bin/xdvcompiler -t ${theme:theme} -r ${theme:rules} -a ${theme:absolute-prefix} ${theme:output-xslt}
    update-command = ${compile-theme:command}
    [cache-config]
    recipe = collective.recipe.template
    input = ${buildout:directory}/production/cache.conf.template
    output = ${buildout:directory}/production/cache.conf
    [cache]
    recipe = plone.recipe.varnish
    daemon = ${buildout:directory}/parts/varnish-build/sbin/varnishd
    mode = foreground
    bind = ${hosts:cache}:${ports:cache}
    cache-size = 1G
    user = ${users:cache}
    config = ${buildout:directory}/production/cache.conf

Las transformaciones del tema visual con Deliverance se realizan configurando
un servidor adicional de Nginx que ejecuta las reglas de los temas:

.. code-block:: ini

    [transform-config]
    recipe = collective.recipe.template
    input = ${buildout:directory}/production/transform.conf.template
    output = ${buildout:directory}/production/transform.conf

El balanceador de carga también utiliza un archivo de template ubicado dentro
del buildout:

.. code-block:: ini

    [balancer-config]
    recipe = collective.recipe.template
    input = ${buildout:directory}/production/balancer.conf.template
    output = ${buildout:directory}/production/balancer.conf

Supervisor es un administrador de procesos que se encarga de mantener
funcionando todas las piezas del sitio y proporciona un punto único de control
para iniciar y detener los servicios, así como consultar su status y logs:

.. code-block:: ini

    [supervisor]
    recipe = collective.recipe.supervisor
    port = ${ports:supervisor}
    user = ${supervisor-settings:user}
    password = ${supervisor-settings:password}
    serverurl = http://${hosts:supervisor}:${ports:supervisor}
    programs =
       10 zeo     ${zeoserver:location}/bin/runzeo
                      true ${users:zope}
       20 instance1 ${buildout:directory}/parts/instance1/bin/runzope
                      true ${users:zope}
       20 instance2 ${buildout:directory}/parts/instance2/bin/runzope
                      true ${users:zope}
       20 instance3 ${buildout:directory}/parts/instance3/bin/runzope
                      true ${users:zope}
       20 instance4 ${buildout:directory}/parts/instance4/bin/runzope
                      true ${users:zope}
       30 balancer ${buildout:directory}/bin/haproxy
          [-f ${buildout:directory}/production/balancer.conf -db]
          true ${users:balancer}
       40 transform ${nginx-build:location}/sbin/nginx
          [-c ${buildout:directory}/production/transform.conf]
          true ${users:transform}
       50 cache ${buildout:directory}/bin/cache
          true ${users:cache}
       60 main ${nginx-build:location}/sbin/nginx
          [-c ${buildout:directory}/production/main.conf]
          true

Se genera una configuración de logrotate para poder incluirla fácilmente en el
directorio de configuración de esta herramienta en Unix:

.. code-block:: ini

    [logrotate.conf]
    recipe = collective.recipe.template
    input = ${buildout:directory}/production/logrotate.conf.template
    output = ${buildout:directory}/production/logrotate.conf

Un intérprete de Python y algunas otras herramientas de desarrollo se incluyen
en las siguientes seciones. El intérprete de Python es especial porque en su
path de ejecución están todos los paquetes utilizados en el buildout:

.. code-block:: ini

    [zopepy]
    recipe = zc.recipe.egg
    eggs = ${instance-settings:eggs}
    interpreter = zopepy
    extra-paths = ${zope2:location}/lib/python
    scripts = zopepy
    [omelette]
    recipe = collective.recipe.omelette
    eggs = ${instance-settings:eggs}
    products = ${instance-settings:products}
    packages = ${zope2:location}/lib/python ./
    [xdv-setup]
    recipe = collective.recipe.template
    input = ${buildout:directory}/devel/server.ini.template
    output = ${buildout:directory}/devel/server.ini

Esta configuración de construcción se integra después en una configuración
base del sitio. La base contiene la mayoría de los servicios y configuraciones
compartidas entre los demás buildouts. El buildout contiene los siguientes
servidores:

* `main`
    el servidor web Nginx que puede correr en el puerto principal
* `cache`
    un cache Varnish configurado para servir un sitio Plone
* `transform`
    un servidor web Nginx que realiza transformaciones
* `balancer`
    un cluster de HAproxy que balancea los clientes ZEO
* `instance1`
    Clientge de ZEO 1
* `instance2`
    Clientge de ZEO 2
* `instance3`
    Clientge de ZEO 3
* `instance4`
    Clientge de ZEO 4
* `instance-debug`
    un cliente ZEO que no forma parte del cluster y esta siempre en modo de
    desarrollo
* `zeoserver`
    un servidor ZEO para la base de datos de Zope común

Se incluye la configuración para rotación de logs con logrotate, excepto para
Varnish. La configuración queda en el directorio production/logrotate.conf y
debe integrarse a la configuración general de logrotate usando un symlink.

En la configuración de transformación de Nginx, solo se incluye un servidor
Plone, pero es posible agregar mas si es necesario.

Para controlar todos los servicios, se incluye Supervisor::

    $ ./bin/supervisord

En http://localhost:9001 puede consultarse el estado de los servicios. Desde
ahí es posible iniciar o detener cualquiera de ellos.

La configuración esta contenida enteramente en este buildout, con patrones
para los archivos de configuración en production/\*.template. Los nombres de
servidores, puertos y otras opciones comunes pueden cambiarse en las secciones
que se encuentran al inicio de este archivo. Estos son los valores que se
utilizan en la sección de construcción definida arriba:

.. code-block:: ini

    [buildout]
    extensions = buildout.dumppickedversions
    # Copiar las versiones mas recientes de los paquetes utilizados a un archivo,
    # para poder "congelarlas" después en producción.
    dump-picked-versions-file = versions/known-good-versions.cfg
    # Extender la configuración de versiones para obtener la versión de Plone
    # requerida, desde http://dist.plone.org/release/<version>/versions.cfg
    extends =
       build.cfg
       versions/plone-3.3rc4.cfg
    newest = false
    unzip = true
    versions = versions
    # Las partes del buildout son todos los servicios que se instalaran
    parts =
       lxml
       xdv
       zope2
       zeoserver
       instance1
       instance2
       instance3
       instance4
       instance-debug
       nginx-build
       varnish-build
       haproxy-build
       cache
       main-config
       cache-config
       transform-config
       balancer-config
       compile-theme
       logrotate.conf
       supervisor
       zopepy
       omelette
       backup
       cron-pack
       cron-backup
    develop =
       src/*
    # Se requieren versiones especificas de algunos proyectos
    [versions]
    zc.buildout = 1.2.1
    zc.recipe.testrunner = 1.1.0
    elementtree = 1.2.6-20050316
    ZODB3 = 3.8.1
    z3c.blobfile = 0.1.2
    lxml = 2.1.5
    ###
    # URLs de las versiones de Zope, Varnish y Nginx que se utilizaran
    [downloads]
    zope = ${versions:zope2-url}
    varnish = http://downloads.sourceforge.net/varnish/varnish-2.0.4.tar.gz
    nginx = http://sysoev.ru/nginx/nginx-0.7.43.tar.gz
    # configuración básica de los clientes ZEO
    [instance-settings]
    eggs =
    #   mynamespace.policy
       Plone
       plone.app.blob
       plone.app.ldap
       Products.CacheSetup
    zcml =
    # mynamespace.policy
    # mynamespace.policy-meta
    # mynamespace.policy-overrides
       plone.app.ldap
       plone.app.blob
    products =
    user = admin:admin
    zodb-cache-size = 10000
    zeo-client-cache-size = 300MB
    debug-mode = off
    zope2-location = ${zope2:location}
    zeo-client = true
    shared-blob = on
    blob-storage = ${zeoserver:zeo-var}/blobstorage
    zeo-address = ${zeoserver:zeo-address}
    effective-user = ${users:zope}
    # configuración básica de supervisor
    [supervisor-settings]
    user = admin
    password = admin
    # Nombre del sitio Plone que se usara para configurar virtual hosting
    [plone-sites]
    main = plone-site
    # Nombres o ips de los diversos servidores, main es el principal
    [hosts]
    main = 127.0.0.1
    cache = 127.0.0.1
    supervisor = 127.0.0.1
    balancer = 127.0.0.1
    transform = 127.0.0.1
    instance1 = 127.0.0.1
    instance2 = 127.0.0.1
    instance3 = 127.0.0.1
    instance4 = 127.0.0.1
    instance-debug = 127.0.0.1
    xdv = 127.0.0.1
    syslog = 127.0.0.1
    # Puertos de los servidores, main es el principal
    [ports]
    main = 8000
    cache = 8101
    balancer = 8201
    transform = 8301
    instance1 = 8401
    instance2 = 8402
    instance3 = 8403
    instance4 = 8404
    instance1-icp = 8401
    instance2-icp = 8402
    instance3-icp = 8403
    instance4-icp = 8404
    instance-debug = 8499
    zeo-server = 8501
    supervisor = 9001
    xdv = 5000
    # Usuarios del sistema a los que se asignaran los servicios
    [users]
    main = www
    cache = www
    transform = www
    balancer = www
    zope = www
    supervisor = www
    # configuración del tema
    [theme]
    root = ${buildout:directory}/theme
    theme = ${theme:root}/theme.html
    rules = ${theme:root}/rules/default.xml
    absolute-prefix = /static
    output-xslt = ${theme:root}/theme.xsl
    # configuración de compilación
    [build]
    cpu = i686
    target = linux26
    # Creación de scripts para backup
    [backup]
    recipe = collective.recipe.backup
    # Compresión semanal de la base de datos
    [cron-pack]
    recipe = z3c.recipe.usercrontab
    times = 0 2 1 * *
    command = ${buildout:directory}/bin/zeopack
    # Backups diarios
    [cron-backup]
    recipe = z3c.recipe.usercrontab
    times = 0 1 * * *
    command = ${buildout:directory}/bin/backup

