.. -*- coding: utf-8 -*-

.. _instalar_config_propio_mirror_pypi:

===================================================
Instalar y configurar su propio repositorio de PyP­I­
===================================================

:Autor(es): Leonardo J. Caballero G.
:Correo(s): leonardocaballero@gmail.com
:Lanzamiento: |version|
:Fecha: |today|

.. contents:: :local:

Este manual intenta ayudar a como implementar un servidor espejo (mirror) de paquetes 
Egg Python del servidor central ``PyPI`` local en su organización.

.. toctree::
   :maxdepth: 1

.. _creando_propio_repositorio_pypi:

Creando su propio repositorio de PyPI
=====================================

Una de las características principales que ha popularizado a los sistemas operativos Linux, 
son los diversos esquemas de distribución de software implementados en la Web para compartir 
y distribuir software, todo esto gracias a la libertad 2 del software libre.

En la actualidad existen varios tipos de paquetes de software para Linux de los cuales dos 
son los principales formatos de paquetes los **.rpm** de Redhat Linux y los archivos **.deb** 
de Debian GNU/Linux, con estos formatos se pueden descargar, instalar, configurar y dejar listo 
un paquete de software para que usted solo lo ejecutes y lo utilices.

Una parte importante que va de la mano del sistema de paquetes, es el repositorio de software 
y es, en pocas palabras, un sitio (lugares / servidores) en internet donde se almacenan un espejo 
(lo mismo) que tiene el repositorio original pero que puede ayudar a que las personas que 
estén mas cerca (geográficamente hablando) puedan acceder al software más rápidamente.

Los repositorios de software de Linux se almacenan literalmente en cientos de servidores 
espejos “mirrors” distribuidos en muchos países, por ejemplo: 

La lista de mirrors de Debian incluye cientos de servidores unos alojados por empresas, 
otros por universidades, gobiernos, etc.

-   http://www.debian.org/mirror/list

En el caso de ubuntu la lista también es larga y abarca países de la A a la Z.

-   https://launchpad.net/ubuntu/+archivemirrors

Repositorio de PyPI
-------------------

En el caso de Python existe el sistema de ``paquetes Egg`` y estos se disponen para ser 
distribuidos como aplicaciones y librerías Python en un repositorio principal dispuesto por la 
fundación Python en la siguiente dirección:

-   http://pypi.python.org/simple/

Que no es mas que la interfaz que consultan la herramientas :ref:`easy_install <que_es_easyinstall>` / :ref:`pip <que_es_pip>` 
para realizar las instalaciones de ``paquetes Egg``.

Este repositorio principal posee sus mirror o espejos como se listan a continuación:

-   http://b.pypi.python.org/simple/

-   http://c.pypi.python.org/simple/

-   http://d.pypi.python.org/simple/

-   http://e.pypi.python.org/simple/

-   http://f.pypi.python.org/simple/

-   http://g.pypi.python.org/simple/

Para mas información sobre nuevo repositorios consulte la siguiente dirección:

-   http://pypi.python.org/mirrors


Si desea saber el estatus actual de sincronización de los repositorios oficiales 
puede consultar la siguiente dirección:

-   http://www.pypi-mirrors.org/

Además existen otros repositorios públicos generados con el paquete ``z3c.pypimirror`` 
disponibles a continuación:

-   http://pypi.it.uwosh.edu/

-   http://pypi.inqbus.de/

-   http://pypi.python.jp/

-   http://pypi.blitzen.unc.edu/

-   http://pypi.pbs.org/pypi/simple/

-   http://pypi.upc.edu/mirror/

-   http://pypi.affinitic.be/

-   http://kambing.ui.ac.id/pypi/

Ahora si usted desea tener su propio servidor espejo del servidor PyPI por un tema de 
mayor eficiencia en los recursos de ancho de banda local de su organización, pues bien 
requiere tener servidor espejo de sus paquetes privados, entonces necesita instalar el 
paquete ``z3c.pypimirror``.

Instalando z3c.pypimirror
=========================

Para instalar el paquete `z3c.pypimirror`_, su instalación es muy simple, por eso
estoy partiendo del principio de que tenemos instalado en el sistema los siguientes 
requerimientos:

-   El interprete `Python`_ 2.4 o superior.
-   Opcionalmente la herramienta :ref:`virtualenv <que_es_virtualenv>`, si requiere hacer 
    la instalación en un entorno virtual Python.
-   Los paquetes :ref:`distribute <que_es_distribute>` / :ref:`setuptools <que_es_setuptools>`.
-   Disponer al menos **13 GB de espacio libre** para los paquetes Egg.
-   Disponer de un servidor Web como Apache2 o Nginx para hacer publico su repositorio.
-   Habilidad de ejecutar un script vía tarea de crontab en el servidor.

Existen dos formas de instalar el paquete usando el :ref:`paquete Egg <install_egg_z3c_pypimirror>` 
o usando la configuración :ref:`buildout <install_buildout_z3c_pypimirror>`. Para ambas es recomendable 
que instale ciertas dependencias en su sistema operativo como las que se muestran a continuación: 

.. code-block:: sh

  # aptitude install python-setuptools python-dev build-essential

.. _install_egg_z3c_pypimirror:

A continuación se muestra como puede instalar el paquete, con el siguiente ­comando:

Instalando con pip
------------------

Opcionalmente con la herramienta :ref:`pip <que_es_pip>`, se realiza con el siguiente ­comando:

.. code-block:: sh

  # pip install z3c.pypimirror

Instalando con easy_install
---------------------------

Con la herramienta :ref:`easy_install <que_es_easyinstall>`, se realiza con el siguiente ­comando:

.. code-block:: sh

  # easy_install-2.4 z3c.pypimirror


.. _install_buildout_z3c_pypimirror:

Instalando con buildout
-----------------------

Existe un :ref:`proyecto buildout <que_es_zcbuildout>` disponible que automatiza todo el proceso de instalación 
y configuración de tu propio repositorio PyPI, se realiza con los siguientes ­comandos:

.. code-block:: sh

  $ git clone git://github.com/macagua/macagua.buildout.pypimirror.git
  $ python bootstrap.py
  $ ./bin/buildout -vN

Configurando z3c.pypimirror
===========================

Después de ejecutar la instalación comando anterior, tenemos que configurar 
nuestro repositorio PyPI, para eso hay crear un usuario en el sistema llamado
``pypimirror`` es un criterio, en el directorio **home** de usuario pypimirror, 
es en donde pretendo centralizar los paquetes, archivos de registros (.log) 
y entre otros... entonces cree una carpeta el nombre de paquetes con el siguiente 
comando:

.. code-block:: sh

  # mkdir -p /home/pypimirror/paquetes

Este será el directorio en donde iremos a mantener nuestros paquetes
procedentes de PyPI, los archivos de registros (*.log) y temporales podemos
mantenerlos en el directorio ``/home/pypimirror``, ahora tenemos que crear el
fichero de configuración, lo llamé ``pypimirror.cfg``, tendrá la siguiente
configuración:

.. code-block:: cfg

  [DEFAULT]
  # the root folder of all mirrored packages.
  # if necessary it will be created for you
  mirror_file_path = /home/pypimirror/paquetes
  
  
  # where's your mirror on the net?
  base_url = http://pypi.sudominio.com
  
  # lock file to avoid duplicate runs of the mirror script
  lock_file_name = /home/pypimirror/pypi-poll-access.lock
  
  # Pattern for package files, only those matching will be mirrored
  filename_matches =
      *.zip
      *.tgz
      *.egg
      *.tar.gz
      *.tar.bz2
  
  # Pattern for package names; only packages having matching names will
  # be mirrored
  package_matches =
  #   zope.*
  #   plone.*
  #   Products.*
  #   collective.*
     *.*
  
  # remove packages not on pypi (or externals) anymore
  cleanup = True
  
  # create index.html files
  create_indexes = True
  
  # be more verbose
  verbose = True
  
  # resolve download_url links on pypi which point to files and download
  # the files from there (if they match filename_matches).
  # The filename and filesize (from the download header) are used
  # to find out if the file is already on the mirror. Not all servers
  # support the content-length header, so be prepared to download
  # a lot of data on each mirror update.
  # This is highly experimental and shouldn't be used right now.
  #
  # NOTE: This option should only be set to True if package_matches is not
  # set to '*' - otherwise you will mirror a huge amount of data. BE CAREFUL
  # using this option!!!
  external_links = False
  
  # similar to 'external_links' but also follows an index page if no
  # download links are available on the referenced download_url page
  # of a given package.
  #
  # NOTE: This option should only be set to True if package_matches is not
  # set to '*' - otherwise you will mirror a huge amount of data. BE CAREFUL
  # using this option!!!
  follow_external_index_pages = False
  
  # logfile
  log_filename = /home/pypimirror/pypimirror.log


Esta configuración, es una copia del archivo **pypimirror.cfg.sample**
localizado en ``$PYTHON/site-packages/z3c.pypimirror-1.0.14-py2.4.egg/z3c/pypimirror``, 
un detalle importante durante la configuración es que en la variable
**package_matches**, se indique para descargar los espacios de nombre de
paquetes **zope**, **plone**, **Products** y **collective**, de siendo así
mismo el propio paquete z3c.pypimirror lo cual de esta forma estaría siendo
descartado, así que para conseguir cualquier paquete desde PyPI, usted puede
comentar las lineas y decir como se muestra a continuación:

.. code-block:: cfg

    package_matches =
    #   zope.*
    #   plone.*
    #   Products.*
    #   collective.*
       *.*

Ahora que tenemos nuestro repositorio PyPI debidamente configurado, para
iniciar la replicación del repositorio de PyPI, ejecute el siguiente comando:

.. code-block:: sh

  $ /usr/bin/pypimirror --initial-fetch --follow-external-links --follow-external-index-pages /home/pypimirror/pypimirror.cfg

Puedes supervisar los avances analiazndo el logfile de z3c.pypimirror:

.. code-block:: sh

  $ tail -f /home/pypimirror/pypimirror.log

Cabe resaltar que **NO** es necesario preocuparse en crear la página índice
como el archivo **index.html**, para el servidor Web, porque en el archivo de
configuración anterior, le estamos indicado que este será creado
automáticamente **(create_indexes = True)**.

Publicación de repositorio con un Web Server
============================================

Luego de haber replicado localmente su repositorio PyPI en su servidor, 
usted debe configurar un virtual host en un servidor Web para publicar 
su repositorio previamente replicado.


Configuración con Nginx Web Server
----------------------------------

Opcionalmente si usted utiliza un `Nginx Web Server`_ debe crear un sitio
disponible, con el siguiente comando:

.. code-block:: sh

  # vim /etc/nginx/sites-available/pypimirror

y entonces agrega la siguiente configuración:

.. code-block:: cfg

  server {
            listen IP-ADDRESS;
            server_name MIDOMINIO.TLD/pypi;
            location /pypi {
                root /home/pypimirror/paquetes;
            }
  }

Realice un enlace simbólico desde el directorio de Nginx ``sites-available/`` 
al directorio ``sites-enabled/``, para que su configuración previa este disponible:

.. code-block:: sh

  # ln -s /etc/nginx/sites-available/pypimirror /etc/nginx/sites-enabled/pypimirror



Para finalizar debe carga de la nueva configuración, con el siguiente comando:

.. code-block:: sh

  # /etc/init.d/nginx reload

Configuración con Apache Web Server
-----------------------------------

Mientras se sincroniza el repositorio, usted puede configurar su servidor
Web, por ejemplo, `Apache Web Server`_ debe crear un sitio disponible con el
siguiente comando:

.. code-block:: sh

  # vim /etc/apache2/sites-available/pypimirror


Debe indicarle en su directiva ``DocumentRoot``, que apunte hacia el
directorio directorio,  y entonces agrega la siguiente configuración:

.. code-block:: cfg

  <VirtualHost IP-ADDRESS:80>
      ServerName MIDOMINIO.TLD
      CustomLog /home/pypimirror/pypimirror.log combined
      DocumentRoot /home/pypimirror/paquetes
  </VirtualHost>


Realice un enlace simbólico desde el directorio de Apache2 ``sites-available/`` 
al directorio ``sites-enabled/``, para que su configuración previa este disponible:

.. code-block:: sh

  # ln -s /etc/apache2/sites-available/pypimirror /etc/apache2/sites-enabled/pypimirror


Luego debe habilitar esta configuración del sitio llamado "pypimirror", con el siguiente comando:

.. code-block:: sh

  # a2ensite pypimirror

Y por ultimo recargamos la configuración en el servicio de Apache2, con el
siguiente comando:

.. code-block:: sh

  # /etc/init.d/apache2 reload

Programar actualizaciones con crontab
=====================================

Usted automatizar la sincronización de los paquetes adicionando una tarea en
el ``crontab`` del sistema con la siguiente linea:

.. code-block:: sh

  $ crontab -e

y entonces agregue la siguiente linea:

.. code-block:: cfg

  */6 * * * * pypimirror /usr/bin/pypimirror --update-fetch --follow-external-links --follow-external-index-pages /home/pypimirror/pypimirror.cfg

Usando z3c.pypimirror
=====================

Posterior a su instalación / configuración ya puede usar el repositorio previamente 
instalado, para esto existen varias formas de utilizarlo según sea su caso como se 
describen a continuación:

Usando pip
-----------

Si usted necesita usar la herramienta :ref:`pip <que_es_pip>` es posible 
especificar el servidor de donde usted desea bajar el paquete, con lo 
muestra el siguiente comando:

.. code-block:: sh

  pip install -i http://pypi.sudominio.com mipaquete


Usando easy_install
-------------------

Opcionalmente con la herramienta :ref:`easy_install <que_es_easyinstall>` 
del SetupTools usted puede especificar el servidor de donde usted desea bajar 
el paquete, con lo muestra el siguiente comando:

.. code-block:: sh

  easy_install -i http://pypi.sudominio.com mipaquete

­


Usando buildout
---------------

Después de que todo este hecho, usted solo necesita decir en su archivo de
configuraciones locales buildout ``~/.buildout/default.cfg`` (si no esta creado 
créalo o edite un archivo) cual es la dirección HTTP del repositorio por 
defecto (el que previamente configuro) de donde debería buscar y descargase
los paquetes y coloque lo siguiente:

.. code-block:: cfg

  [buildout]
  index =  http://pypi.sudominio.com


Guarde los cambios y ahora de esta forma cada ves que se ejecuta buildout
busca inicialmente este repositorio ;)

Ver también
===========

-   `Buildout de z3c.pypimirror`_.
-   `The PyPI Replication Project`_.
-   `What to do when PyPI goes down`_.
-   `Plone en la Plataforma de Desa­rrollo de Software Libre de CENDITEL`_.


Referencias
===========

-   El articulo `Instalar y configurar su propio repositorio de PyP­I­`_ desde la comunidad Plone Venezuela.
-   `Criando seu próprio repositório do Pypi`_.
-   `Repositorios de software para Linux`_.


Reconocimientos
---------------

Agradecimientos `Cleber J Santos`_ de la empresa `Simples Consultoria`_ por
escribir inicialmente este tutorial en Portugues, y a los compañeros `Dhionel Diaz`_ 
y `Leonardo J. Caballero G.`_ de la `fundación CENDITEL`_, por
traducir al Español y poner en practica `z3c.pypimirror`_ con el cual
crearon esta completa receta :D


.. _z3c.pypimirror: http://pypi.python.org/pypi/z3c.pypimirror
.. _Python: http://www.python.org/
.. _Apache Web Server: http://httpd.apache.org/
.. _Nginx Web Server: http://wiki.nginx.org/Main
.. _Cleber J Santos: http://twitter.com/cleberjsantos
.. _Simples Consultoria: http://www.simplesconsultoria.com.br/
.. _Dhionel Diaz: mailto:ddiaz@cenditel.gob.ve
.. _Leonardo J. Caballero G.: http://wiki.cenditel.gob.ve/wiki/lcaballero
.. _fundación CENDITEL: http://www.cenditel.gob.ve/
.. _Buildout de z3c.pypimirror: http://bluedynamics.com/articles/jens/setup-z3c.pypimirror
.. _The PyPI Replication Project: http://www.coactivate.org/projects/pypi-mirroring/project-home
.. _Plone en la Plataforma de Desa­rrollo de Software Libre de CENDITEL: http://plataforma.cenditel.gob.ve/wiki/Plone
.. _Criando seu próprio repositório do Pypi: http://www.simplesconsultoria.com.br/blog/criando-seu-proprio-repositorio-do-pypi-1
.. _Instalar y configurar su propio repositorio de PyP­I­: http://www.coactivate.org/projects/ploneve/instalar-y-configurar-su-propio-repositorio-de-pypi
.. _What to do when PyPI goes down: http://jacobian.org/writing/when-pypi-goes-down/
.. _Repositorios de software para Linux: http://www.comoinstalarlinux.com/repositorios-de-software-para-llinux/
