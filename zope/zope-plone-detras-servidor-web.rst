.. -*- coding: utf-8 -*-

=================================================
Ejecutando Zope y Plone detrás de un Servidor Web
=================================================

Este documento busca explicar los conceptos intrínsecos para instalar y configurar un servidor Web en frente del servidor Zope/Plone.

.. contents :: :local:

¿Por que detrás de un Servidor Web?
===================================

Cuando se configura el servidor Zope y Plone detrás de un servidor Web generalmente se hace como **servidor proxy reverso** y existentes varias razones para este tipo de configuración:

* **Seguridad**: el servidor proxy es una capa adicional de defensa y por lo tanto protege los servidores web. Para el servidor Zope permite enmascarar el puerto de publicación del mismo, a través del patrón de diseño "Front-controler" que permite aplicar nuevos direccionamientos a todas las peticiones del puerto 80 aplicando reglas de reescritura de direcciones URLs.
* **Configurar un firewall en su servidor Web**, esta configuración tiene la finalidad es reforzar la seguridad de aplicaciones Web.
* **Cifrado / Aceleración SSL**, cuando se crea un sitio web seguro, habitualmente el cifrado SSL no lo hace el mismo servidor web, sino que es realizado por el "proxy reverso", el cual está equipado con un hardware de aceleración SSL (Security Sockets Layer).
* **Distribución de Carga**, con el "proxy reverso" puede distribuir la carga entre varios servidores web. En ese caso, el "proxy reverso" puede necesitar reescribir las direcciones URLs de cada página web (traducción de la dirección URL externa a la dirección URL interna correspondiente, según en qué servidor se encuentre la información solicitada).
* **Caché de contenido estático**, con un "proxy reverso" puede descargar los servidores web almacenando contenido estático como imágenes u otro contenido gráfico.


Servicio de Virtual hosting en Zope
===================================
El servidor Zope viene con un objeto llamado "Virtual Host Monster" que le ayuda a hacer configuraciones de hosting virtual. 
La técnica de hosting virtual es una forma de servir a muchos sitios web con un servidor Zope.


Terminología general
--------------------

Hay que entender varios conceptos antes de continuar:

.. glossary::

  vhost
    Es una nomenclatura del Ingles "Hosting Virtual" que hace referencia del Hosting Virtual.

  Hosting Virtual
    Según la documentación sobre `Hosting Virtual`_ en Apache Versión 2.0 `'El término Hosting Virtual se refiere a hacer funcionar más de un sitio web (tales como www.company1.com y www.company2.com) en una sola máquina. Los sitios web virtuales pueden estar "basados en direcciones IP", lo que significa que cada sitio web tiene una dirección IP diferente, o "basados en nombres diferentes", lo que significa que con una sola dirección IP están funcionando sitios web con diferentes nombres (de dominio). El hecho de que estén funcionando en la misma máquina física pasa completamente desapercibido para el usuario que visita esos sitios web'`.

  VHM
    Es una nomenclatura del Ingles "Virtual Host Monster" que hace referencia al objeto encargado de Hosting Virtual del servidor Zope.

  Virtual Host Monster
    Según la documentación sobre `VirtualHostMonster`_ en la Wiki de Zope2 `'Es un objeto, usualmente encontrado en la carpeta raíz de la instancia de Zope, el cual hace trabajar a los hosts virtual'`.

  Proxy inverso
    Según la documentación sobre Proxy en su sección Reverse Proxy/`Proxy inverso`_ en Wikipedia Español `'Un reverse proxy es un servidor proxy instalado en el domicilio de uno o más servidores web. Todo el tráfico entrante de Internet y con el destino de uno de esos servidores web pasa a través del servidor proxy'`.

  Reescritura de URL
    Según la documentación sobre `URL rewriting`_ (Rewrite engine) en Wikipedia Ingles `'La reescritura de direcciones URL (a veces conocida como dirección URL de adornadas, cortas o amigable a los motores de buscadores) le permite modificar la apariencia de las dirección URL Web, para esto usa un motor de reescritura de URL, por lo generar incorporado en un Servidor Web. Esta técnica es usada para proveer enlaces web cortos y de mayor entendimiento y relevancia a páginas Web. La técnica añade un grado de separación entre los archivos que se utilizan para generar una página web y la dirección URL que se presenta al mundo.'`.

  Servidores Web
    Según la documentación sobre `Servidor web`_ en Wikipedia Español `'es un programa informático que procesa una aplicación del lado del servidor realizando conexiones bidireccionales y/o unidireccionales y síncronas o asíncronas con el cliente generando o cediendo una respuesta en cualquier lenguaje o Aplicación del lado del cliente. El código recibido por el cliente suele ser compilado y ejecutado por un navegador web. Para la transmisión de todos estos datos suele utilizarse algún protocolo. Generalmente se utiliza el protocolo HTTP para estas comunicaciones, perteneciente a la capa de aplicación del modelo OSI. El término también se emplea para referirse al ordenador que ejecuta el programa.'`.

  Servidor HTTP Apache
    Según la documentación sobre `Servidor HTTP Apache`_ en Wikipedia Español `'es un servidor web HTTP de código abierto, para plataformas Unix (BSD, GNU/Linux, etc.), Microsoft Windows, Macintosh y otras, que implementa el protocolo HTTP/1.1 y la noción de sitio virtual'`.

  Nginx
    Según la documentación sobre `Nginx en Wikipedia Español`_ `'es un servidor web/proxy inverso ligero de alto rendimiento y un proxy para protocolos de correo electrónico (IMAP/POP3).'`.


¿Como trabaja Virtual Host Monster?
-----------------------------------

EL objeto `Virtual Host Monster`_ enmascara la dirección URL devuelta por el servidor Zope como response la cual es publicada como **http://www.cliente1.com/** en lugar de **http://127.0.0.1:8080/**. Está instalado previamente en el servidor Zope (este objeto se llama **virtual_hosting** y se encuentra en el directorio del raíz del servidor Zope y puede ser consultado desde la interfaz administrativa de Zope) y no necesita ninguna configuración en Zope. 

Su configuración sólo se produce a través de una regla de reescritura de la dirección URL, adicionalmente se debe configurar su servidor web como un proxy inverso hacia el servidor Zope. 

La regla de reescritura de la dirección URL de VHM luce algo así: ::

    ^/(.*) \ 
    http://127.0.0.1:8080/VirtualHostBase/http/intranet.cliente1.com:80/cliente1_intranet/VirtualHostRoot/$1

Esta dirección URL de VHM previa tiene siete partes:

.. glossary::

  ^/(.*) \ 
    ¿Qué significa eso? Bueno, esto es una `expresión regular`_, que coincide con casi todo. Voy a explicarlo con calma:

    * El carácter ``^`` significa empezar por el principio, el principio es donde está justo después del nombre de dominio (por ejemplo, después de http://www.cliente1.com).
    * El carácter ``/`` significa que coincida con el primer ``/`` que venga (después del nombre de dominio, por ejemplo, http://www.cliente1.com/).
    * El carácter ``(`` significa recordar todo lo que allá coincidido entre este carácter y ``)`` y lo llaman como \$1
    * El carácter ``.`` significa que coincida con cualquier carácter simple que no sea un espacio en blanco (espacios o tabulaciones).
    * El carácter ``*`` significa en realidad el operador de la izquierda puede ser igualado a 0 o más veces - en otras palabras, coinciden con el texto continuo hasta llegar a una línea final o espacio en blanco.
    * El carácter ``\`` significa salto de linea en la configuración del servidor Web y se utiliza para hacer las configuraciones del servidor Web más legibles por humanos.

    En pocas palabras ``^/(.*)`` significa **Coincidir todo lo que empieza con un ``/`` y guardar todos los caracteres después del carácter ``/``,** esto luego es procesado por la variable \$1 que mas adelante se explica que función cumple.

  http://127.0.0.1:8080
    Esto es para el aplicar el proxy reverso en su servidor Web. Esto configura a cual servidor debería acceder, además incluir el protocolo, host y puerto. En este ejemplo el proxy reverso accede al servidor Zope en el puerto 8080 en el mismo host usando el protocolo http. En Apache 2.2 se hace con el módulo **mod_proxy** y Nginx con su configuración **por defecto**. 

  VirtualHostBase
    Esta es la palabra clave mágica para iniciar el hosting virtual. ¡Usted no debe agregar un objeto llamado VirtualHostBase en el directorio raíz de su Zope!

  http
    Es el primer segmento de ruta después del VirtualHostBase define el protocolo del la dirección URL del vhost.

  intranet.cliente1.com:80
    Es el segundo elemento después del VirtualHostBase y define el servidor y el puerto. Junto con el protocolo es la parte base de la dirección URL, en este ejemplo **http://intranet.cliente1.com:80**. Como el VirtualHostBase el protocolo y servidor no son objetos reales. Ellos son solo colocados dentro de la dirección URL para propósitos de configuración y estos son despojados de la dirección URL después de la configuración del host virtual para cada solicitud.

  cliente1_intranet
    Ahora el verdadero recorrido a través de servidor Zope es que inicia. Después de configurar la parte de protocolo y el servidor de la nueva dirección URL que esta atravesando a través de Zope a la nueva raíz virtual para el host virtual. Usted puede agregar cero o más objetos aquí.

  VirtualHostRoot
    Finalmente la palabra clave mágica con la que se ha llegado al nuevo raíz virtual para el vhost. Cada cosa después del VirtualHostRoot es visible en el navegador Web.

  Caso especial _vh_documentos
    Imagine que usted quiere tener **http://intranet.cliente1.com/documentos/** como la dirección URL de su dirección URL virtual. Entonces usted puede obtener el efecto usando la declaración especial ``_vh_``. Cualquier segmento de ruta iniciando con ``_vh_`` es despojado de la dirección URL para ser recorrido a través de Zope y volver a ser agregado sin ``_vh_`` después de recorrido.

    Un ejemplo: ::

      ^/documentos/(.*) \
      http://127.0.0.1:8080/VirtualHostBase/http/intranet.cliente1.com:80/cliente1_intranet/VirtualHostRoot/_vh_documentos/$1

  \$1
    Así mismo como el ``^/(.*)`` y el ``\$1`` ambos son tipos de `expresión regular`_ hacia alguna sección especifica de su sitio, un ejemplo, puede ser una sección llamada **documentos**. Entonces el valor obtenido de la expresión ``^/(.*)`` se almacena en la variable \$1".


.. note::

  Usted no puede crear un objeto llamado VirtualHostBase o VirtualHostRoot en su Zope 
  ni debe agregar un objeto con el mismo ID de su VHM. Es posible que funcione, 
  pero también puede dañar el sitio.


Servidor Web Nginx y Zope
=========================

A continuación se explica como instalar el servidor Web `Nginx`_ y configurarlo con Zope, a través de técnicas de **reescritura URL**.

Instalar y configurar Servidor Web Nginx
----------------------------------------

Para instalar debe iniciar sesión como usuario "root" ejecute el siguiente
comando:  

.. code-block:: sh

  # aptitude install nginx

Luego se debe agregar la configuración respectiva en Nginx con el siguiente
comando: 

.. code-block:: sh

  # vim /etc/nginx/nginx.conf

Y agregue la siguiente configuración: 

.. code-block:: cfg

    user www-data;
    worker_processes  1;

    error_log  /var/log/nginx/error.log;
    pid        /var/run/nginx.pid;

    events {
        worker_connections  1024;
    }

    http {
        include       /etc/nginx/mime.types;
        default_type  application/octet-stream;

        access_log      /var/log/nginx/access.log;

        sendfile        on;
        #tcp_nopush     on;

        #keepalive_timeout  0;
        keepalive_timeout  65;
        tcp_nodelay        on;

        gzip  on;

        server_names_hash_bucket_size 64;

        server_name_in_redirect off;
        server_tokens           off;

        include /etc/nginx/conf.d/*.conf;
        include /etc/nginx/sites-enabled/*;
    }


Regla de Reescritura de URL para Zope
-------------------------------------

Y defina la política de virtual host del sitio, con el siguiente comando: 

.. code-block:: sh

  # vim /etc/nginx/sites-available/cliente1-intranet

Agregue la siguiente configuración: 

.. code-block:: cfg

    server {
        # DNS/IP y Puerto en que escucha la aplicación
        listen   *:80;

        # Nombre del servidor
        server_name  intranet.cliente1.com;

        # Tamaño máximo de subida de archivos
        client_max_body_size 24M;

        # Tamaño máximo de buffer de archivos
        client_body_buffer_size 128K;

        # Archivo de registro de acceso del sitio web
        access_log  /var/log/nginx/cliente1-intranet.access.log;

        # Archivo de registro de error del sitio web
        error_log  /var/log/nginx/cliente1-intranet.error.log error;

        # Interfaz Administrativa de Zope
        location /manage {
                proxy_pass       http://127.0.0.1:8080/VirtualHostBase/http/intranet.cliente1.com:80/manage_main/VirtualHostRoot/;
                proxy_set_header Host $host;
            }

        # Intranet del cliente1
        location / {
                proxy_pass       http://127.0.0.1:8080/VirtualHostBase/http/intranet.cliente1.com:80/cliente1_intranet/VirtualHostRoot/;
                proxy_set_header Host $host;
        }

        # redirect server error pages to the static page /50x.html
        #
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
                root   /var/www/nginx-default;
        }

    }


Realice un enlace simbólico desde el directorio de Nginx **sites-available/**
al directorio **sites-enabled/**, para que su configuración previa este
disponible: 

.. code-block:: sh

  # ln -s /etc/nginx/sites-available/cliente1-intranet /etc/nginx/sites-enabled/cliente1-intranet


Reinicie el servidor Web
------------------------

Luego reinicie su servidor Nginx con el siguiente comando: 

.. code-block:: sh

  # /etc/init.d/nginx reload


Servidor Web Apache2 y Zope
===========================

A continuación se explica como instalar el servidor Web `Apache 2`_ y configurarlo como un **Proxy inverso** con Zope, además aplicando técnicas de **reescritura URL**.

Terminología en Apache2
-----------------------

Hay que entender varios conceptos antes de continuar:

.. glossary::

  Módulos Apache 2
    Una lista de todos los módulos de Apache 2.2 con sus opciones. Más información http://httpd.apache.org/docs/2.2/es/mod/

  Como reescribir dirección URL
    Un buen sobre la técnica de reescritura de direcciones URL con las reglas de reescritura. Más información http://httpd.apache.org/docs-2.0/misc/rewriteguide.html 

  Referencias de módulo mod_proxy
    La referencias oficial desde la documentación de Apache 2.2. Más información http://httpd.apache.org/docs/2.2/es/mod/mod_proxy.html

  Referencias de módulo mod_ssl
    Cifrado SSL con apache 2. Más información http://httpd.apache.org/docs/2.2/es/mod/mod_ssl.html


Instalar y configurar Servidor Web Apache2
------------------------------------------

Para instalar debe iniciar sesión como usuario "root" ejecute el siguiente
comando: 

.. code-block:: sh

  # aptitude install apache2


Habilitar módulos de mod_rewrite y mod_proxy
--------------------------------------------

Próximo paso es habilitar ``mod_proxy`` y ``mod_rewrite``.

-   Módulo `mod_rewrite`_: Es usado como un motor de reescritura
    basado en reglas para reescribir direcciones URL solicitadas en tiempo de
    ejecución, es decir le permite a usted apuntar a una dirección URL en
    otra dirección URL. Para habilitar ese módulo debe ejecutar el siguiente comando:

    .. code-block:: sh

      # a2enmod proxy
      Enabling module proxy.
      Run '/etc/init.d/apache2 restart' to activate new configuration!

-   Módulo `mod_proxy`_: Es un `Proxy inverso`_ que le permite apuntar
    a una dirección URL en otro servidor en otro puerto. Este sirve como un
    traductor, para que el usuario nunca se comunique con cualquier otro
    servicio que use otro puerto que no sea el 80, es decir es un
    intermediario transparente hacia otro sitio. Con este módulo los usuarios
    pueden ir de Plone hacia una aplicación PHP, y luego a una aplicación
    Java y nunca saberlo. Para habilitar ese módulo debe ejecutar el siguiente comando: 

    .. code-block:: sh

      # a2enmod rewrite
      Enabling module rewrite.
      Run '/etc/init.d/apache2 restart' to activate new configuration!


Luego puede editar la configuración del módulo **mod_proxy**, con el
siguiente comando: 

.. code-block:: sh

  # vim /etc/apache2/mods-enabled/proxy.conf


Ahora, encontramos los siguientes ajustes y coinciden con lo que tengo aquí.
Siga exactamente esto, o usted podría terminar con teniendo un proxy abierto
que permite a otros rebote a través de su máquina para llegar a cualquier
lugar que desee de forma anónima, enviar spam, etc. Hagas lo que hagas, nunca
active su ***ProxyRequests On***. 

.. code-block:: cfg

    ProxyRequests Off
    ProxyPreserveHost On
    <Proxy *>
         Order deny,allow
         #Deny from all
         Allow from all
    </Proxy>

Regla de Re-escritura de Zope
-----------------------------

Y defina la política de virtual host del sitio, con el siguiente comando: 

.. code-block:: sh

  # vim /etc/apache2/sites-available/cliente1-intranet

Agregue la siguiente configuración: 

.. code-block:: cfg

    <VirtualHost *:80>
      ServerName    www.cliente1.com
      ServerAlias   intranet.cliente1.com
      ServerAdmin   webmaster@intranet.cliente1.com
      ServerSignature On

      CustomLog     /var/log/apache2/cliente1-intranet-access.log combined
      ErrorLog      /var/log/apache2/cliente1-intranet-error.log
      LogLevel warn

      # registro del rebajar la tasa de compresión a un archivo
      #CustomLog /var/log/apache2/deflate_log deflate

      <IfModule mod_rewrite.c>
        RewriteEngine On

        # uso RewriteLog para la depuración de problemas con sus reglas de reescritura 
        # debe desactivar después de encontrar el error, ya que el disco duro se llenaría *muy rápido*
        # RewriteLog "/var/log/apache2/rewrite_log"
        # RewriteLogLevel 2

        # sirviendo los iconos desde el servidor Apache 2
        RewriteRule ^/icons/ - [L]

        # reescribir cualquier acceso al ZMI en un servidor seguro
        # RewriteRule ^/(.*)/manage(.*) \
        # https://secure.cliente1.com/Zope/cliente1_instance/cliente1_com/$1/manage$2 [NC,R=301,L]
        # RewriteRule ^/manage(.*) \
        # https://secure.cliente1.com/Zope/cliente1_instance/cliente1_com/manage$1  [NC,R=301,L]


       # reescribir cualquier otro acceso al servidor Zope usando un proxy [P] 
       # y añadir las palabras claves mágicas del VMH. 
       # usar la variable de servidor %{SERVER_NAME} en lugar de cliente1.com 
       # para evitar que se desborde la directiva ServerAlias​​, 
       # usar la variable de servidor %{HTTP_HOST} no es recomendable ya que puede contener el puerto

       RewriteRule ^/manage/(.*) \
           http://127.0.0.1:8080/VirtualHostBase/http/%{SERVER_NAME}:80/manage_main/VirtualHostRoot/$1 [L,P]

       RewriteRule ^/(.*) \
           http://127.0.0.1:8080/VirtualHostBase/http/%{SERVER_NAME}:80/cliente1_intranet/VirtualHostRoot/$1 [L,P]

      </IfModule>

      <IfModule mod_proxy.c>
        ProxyVia On

        # evitar que el servidor web sea utilizado como proxy
        <LocationMatch "^[^/]">
          Deny from all
        </LocationMatch>
      </IfModule>

      # almacenamiento en caché (inhabilitado)
      # esto cacheará todos los archivos con la información correcta de caché a partir /
      <IfModule mod_mem_cache.c>
      # CacheEnable mem /
      </IfModule>

      # compresión (inhabilitado)
      <IfModule mod_deflate.c>
       SetOutputFilter DEFLATE
      </IfModule>
    </VirtualHost>


Realice un enlace simbólico desde el directorio de Apache2 **sites-available/** al directorio **sites-enabled/**, para que su configuración previa este disponible 

.. code-block:: sh

  # ln -s /etc/apache2/sites-available/cliente1-intranet /etc/apache2/sites-enabled/cliente1-intranet

A continuación, algunas configuraciones muy características:


Plone como un domino completo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tener un nombre de host completo (es decir, todo bajo "/") que es servido por
un único sitio Plone, añade esto a su configuración de VirtualHost de Apache
la siguiente configuración: 

.. code-block:: sh

  RewriteEngine On
  RewriteRule ^/(.*)$
    http://127.0.0.1:8080/VirtualHostBase/http/%{SERVER_NAME}:80/cliente1_intranet/VirtualHostRoot/$1 [L,P]

Plone como una porción de su sitio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Alternativamente, usted podría mapear su sitio Plone dentro de un sub-
directorio de un sitio existente sin subsumirlo como todo el sitio. ¿Para
hacer esto hay es usar una regla de reescritura ligeramente diferente?. En
primer lugar, lo mejor es crear un sitio Plone con un ID que coincida con el
nombre de directorio en el que desea que el sitio este publicado. Por
ejemplo, si desea que la dirección URL de su sitio Plone sea así: ::

  http://cliente1.com/cliente1_intranet


Entonces debería crear su sitio Plone con el identificador **cliente1_intranet**. 
Para aparejar eso a este sitio que se muestra cuando usted navega a la dirección 
`http://cliente1.com/cliente1_intranet`_, debe especificar la reescritura de 
la siguiente forma: 

.. code-block:: sh

  RewriteEngine On
  RewriteRule ^/cliente1_intranet($|/.*) http://127.0.0.1:8080/VirtualHostBase/http/%{SERVER_NAME}:80/VirtualHostRoot/cliente1_intranet$1 [L,P]

Soporte HTTPS
~~~~~~~~~~~~~

Si usted quiere soportar acceso seguro HTTPS a su sitio Plone, es algo
parecida la regla de reescritura anterior para su VirtualHost. Cambie "http"
a "https" y cambiar los números de puerto de "80" a "443", de esta forma: 

.. code-block:: sh

  RewriteRule ^/(.*)$ \
   http://127.0.0.1:8080/VirtualHostBase/https/%{SERVER_NAME}:443/VirtualHostRoot/$1 [L,P]

Más información http://plone.org/documentation/kb/apache-ssl

Reglas más elegantes
~~~~~~~~~~~~~~~~~~~~

Si usted tiene necesidades mas exóticas, tome un tiempo y lea la página de
`Virtual Host Monster`_, y considere tener a la mano el `RewriteRule Witch`_,
el cual es un generador de directivas RewriteRule de Apache para Virtual Host
en Zope.

Recomendaciones
~~~~~~~~~~~~~~~

- Si tienes problemas raros con sus reglas, es recomendado activar el
  `RewriteLog`_ y alzar el `RewriteLogLevel`_ a tu conveniencia, consulte
  la documentación de `Mod_rewrite`_.


Reinicie el servidor
--------------------

Luego reinicie su servidor Nginx con el siguiente comando: 

.. code-block:: sh

  # /etc/init.d/apache2 reload


Suprimiendo virtual host monster
================================

En el caso de que usted ha establecido reglas de virtual hosting de modo 
que ya no se Zope le permiten acceder a la interfaz de gestión, puede agregar
``_SUPPRESS_ACCESSRULE"`` a la dirección URL para desactivar VirtualHostMonster.



Ver también
===========

-   `Zope Virtual Hosting Services`_
-   `Running Plone and Zope behind an Apache 2 web server`_
-   `Mapping the Virtual Host`_


Referencias
===========

-   `Integración de Plone con el Servidor Web Nginx de la fundación CENDITEL`_.
-   `Definir Virtual Host y Reescritura de Servidor Web`_. 
-   `Proxy Apache a Zope`_.
-   `How VHM works`_.

.. _Hosting Virtual: http://httpd.apache.org/docs/2.0/es/vhosts/
.. _VirtualHostMonster: http://wiki.zope.org/zope2/VirtualHostMonster
.. _Nginx: http://wiki.nginx.org/NginxEs
.. _Apache 2: http://httpd.apache.org/
.. _mod_rewrite: http://httpd.apache.org/docs/2.2/mod/mod_rewrite.html
.. _mod_proxy: http://httpd.apache.org/docs/2.2/mod/mod_proxy.html
.. _Proxy inverso: http://es.wikipedia.org/wiki/Proxy#Reverse_Proxy_.2F_Proxy_inverso
.. _URL rewriting: http://en.wikipedia.org/wiki/URL_rewriting
.. _Servidor web: http://es.wikipedia.org/wiki/Servidor_web
.. _Servidor HTTP Apache: http://es.wikipedia.org/wiki/Servidor_HTTP_Apache
.. _Nginx en Wikipedia Español: http://es.wikipedia.org/wiki/Nginx
.. _http://cliente1.com/cliente1_intranet: http://cliente1.com/cliente1_intranet
.. _Virtual Host Monster: https://weblion.psu.edu/trac/weblion/wiki/VirtualHostMonster
.. _RewriteRule Witch: http://betabug.ch/zope/witch
.. _RewriteLog: http://httpd.apache.org/docs/2.2/mod/mod_rewrite.html#rewritelog
.. _RewriteLogLevel: http://httpd.apache.org/docs/2.2/mod/mod_rewrite.html#rewriteloglevel
.. _Zope Virtual Hosting Services: http://www.zope.org/Documentation/Books/ZopeBook/2_6Edition/VirtualHosting.stx
.. _Running Plone and Zope behind an Apache 2 web server: http://plone.org/documentation/kb/plone-apache/tutorial-all-pages
.. _Mapping the Virtual Host: http://www.insmallsteps.com/lessons/lesson-hosting-install/mapping-the-virtual-host
.. _Integración de Plone con el Servidor Web Nginx de la fundación CENDITEL: http://plataforma.cenditel.gob.ve/wiki/Plone%3APloneVHostWebServer
.. _Definir Virtual Host y Reescritura de Servidor Web: http://wiki.canaima.softwarelibre.gob.ve/wiki/Definir_Virtual_Host_y_Reescritura_de_Servidor_Web
.. _Proxy Apache a Zope: https://weblion.psu.edu/trac/weblion/wiki/ProxyApacheToZope
.. _How VHM works: http://plone.org/documentation/kb/plone-apache/vhm
.. _expresión regular: http://es.wikipedia.org/wiki/Expresión_regular
