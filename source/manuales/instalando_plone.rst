.. -*- coding: utf-8 -*-

.. _instalando_plone:

====================
Instalación de Plone
====================

:Traductor(es): Luis Sumoza, Leonardo J. Caballero G.
:Correo(s): lsumoza@gmail.com, leonardocaballero@gmail.com
:Lanzamiento: |version|
:Fecha: |today|

En esta es una traducción del articulo llamado `Installing Plone`_ donde se ofrece 
la información básica para la instalación de Plone en Windows, OS X, Linux, BSD
(distribución de software Berkeley) y prácticamente cualquier otra
plataforma.

.. contents :: :local:

.. _1_guia_instalacion:

1. Guía rápida de Instalación
=============================

Como instalar Plone, paso a paso. Versión corta


Linux/BSD
---------


Requisitos previos
..................

Antes de instalar Plone en Linux, BSD, o cualquier otro sistema operativo
basado en Unix, debería asegurarse que tiene los siguientes paquetes
instalados:

-   Compilador gcc, a C

-   Software g++, extensión de gcc para compilar código C++

-   GNU make, una herramienta de compilación

-   GNU tar, paquete para crear archivos tar

-   Paquetes para descomprimir: bzip2 y gzip

Los siguientes paquetes también son recomendados, pero no son necesarios para
construir Plone

-   libssl, le permite usar TSL como su servidor de correo electrónico.

-   readline, un paquete GNU que incrementa la capacidad de las
    aplicaciones para editar los comandos de Terminal.


Obtener el instalador de Plone
..............................

El instalador para Linux/BSD/Unix, denominado Unified Installer (Instalador
Unificado), se puede descargar de `esta página`_ en el sitio web de Plone.

1.  Haga clic en *Download Plone* (descargar Plone), y este le llevará a
    la página que contiene los distintos instaladores de Plone .
2.  Haga clic en el enlace Unified Installer para comenzar la descarga de
    Plone.
3.  Después que la descarga haya finalizado, abra la Terminal y cambie
    los directorios donde el archivo del instalador que usted descargó está
    localizado.
4.  Descomprima el instalador escribiendo ``tar xzf InstallerName``, donde
    InstallerName es el nombre del instalador de Plone que usted descargó.
5.  En su Terminal de comandos introduzca el directorio de la carpeta que
    usted acaba de extraer.


Configurando su Instalación Plone
.................................

Lo primero que debe decidir al momento de instalar Plone es si quiere una
instalación ZEO o una instalación autónoma. Probablemente debería escoger ZEO
si va a usar Plone para cualquier producción. Sin embargo, si simplemente
está probando Plone o lo va a usar para formación, la opción autónoma se
adecuaría mejor. Para un discusión más profunda de este tema lea la 
sección llamada :ref:`¿Ser ZEO o no ser ZEO? <ser-zeo-o-no-ser-zeo>`.

Para comenzar la instalación escriba ``./install.sh method`` donde *method* es
"standalone" (autónoma) o "zeo". Si desea instalar Plone en modo servidor
escriba ``sudo ./install.sh method`` o ejecute el script de instalación
como root de alguna otra manera. Una lista completa de opciones de líneas de
comando la puede encontrar `aquí`_.


Últimos pasos
.............

Cercano del final de la instalación, el instalador debió haber mostrado su
nombre de usuario y contraseña para su instalación Plone en la Terminal. Si
tiene problemas encontrándolos, estos están también listados en un archivo de
texto llamado ``adminPassword.txt`` (el cual se puede encontrar en la carpeta
``zinstance`` o ``zeoserver`` de la instalación de Plone, dependiendo de con 
que opción usted allá ejecutado el instalador unificado "standalone" o "zeo").

Para iniciar Plone:

1.  Haga un "cd" al directorio de su instalación Plone.

2.  Entre en su carpeta ``zinstance`` o ``zeoserver``.

3.  Ejecute ``./bin/plonectl start``. (El puerto que usa Plone se puede
    ajustar en el archivo ``buildout.cfg`` para luego ejecutar ``./bin/buildout``).

4.  Navegue a su instancia visitando `http://localhost:8080/ <http://localhost:8080/>`_ 
    en su navegador web. Si usted estableció otro puerto, use ese en vez del
    *8080*.

5.  Haga clic en "Create a new Plone site" (Crear un nuevo sitio Plone) e
    introduzca su información de inicio de sesión para comenzar a usar Plone.
    Introduzca la información requerida y luego envíe el formulario para
    finalizar la creación de su sitio. Usted puede encontrar su sitio en
    http://localhost:8080/*SiteName*, donde **SiteName** es la identificación
    de su sitio Plone.

Para detener el proceso Plone ejecute ``./bin/plonectl stop``. ¡Diviértase
usando Plone!


OS X
----

Si usted quiere usar Plone en un escritorio Mac, el instalador binario OS X
es una buena opción. Este proporciona el instalador para OS X y contiene un
controlador visual. Sin embargo, ya que provee binarios pre-compilados, es
muy difícil agregar nuevos componentes que requieran construcciones binarias.
Si usted tiene la necesidad realizar esa acción, pues entonces agregue XCode
a su sistema y use el instalador Unificado.


MS Windows (2000, 2003, XP, Vista, 7)
-------------------------------------


Obtener Plone
.............

Puede descargar Plone para Windows de `esta página`_.

1.  Haga clic en el botón **Download Plone** (Descargar Plone).
2.  Haga clic en el enlace para el instalador de Windows y guárdelo en
    una locación que sea fácil de recordar tal como su Escritorio.
3.  Haga doble-clic en el instalador para iniciar el proceso de
    instalación.


Asistente de instalación de Plone
.................................

1.  Introduzca el directorio donde le gustaría instalar Plone. La mayoría
    de personas están de acuerdo con la ubicación predeterminada. (Haga clic
    en "Next" (Siguiente) al finalizar cada paso para continuar)
2.  Introduzca el nombre de usuario y contraseña que desee para la cuenta
    del administrador.
3.  Revise las opciones de configuración actual.
4.  Durante el proceso de instalación una barra mostrará que tan cerca
    está la instalación de completarse.  Marque las casillas de confirmación
    para determinar si usted quiere agregar Plone como un servicio para que
    se inicie automáticamente con el inicio de Windows.
    
    .. note::
        esto se puede cambiar en cualquier momento ejecutando ``bin\\instance.exe remove`` 
        en su directorio de instalación o si desea ejecutar Plone después de que la
        instalación haya culminado.


Iniciando Plone
...............

Si usted decidió no hacer de Plone un servicio, usted lo puede iniciar y
detener a través del directorio de Plone en su línea de comandos y a
continuación ejecutar:

.. code-block:: sh

    bin/instance.exe fg

o mediante el uso del Controlador GUI (interfaz gráfica de usuario) de Plone.

El Controlador de Plone se puede encontrar en su menú de 
:menuselection:`Inicio --> Todos los programas --> Plone --> Plone Controller`. 
Este se usa para modificar la configuración de Plone, así como para iniciarlo 
o detenerlo. Ahora si usted decide hacer de Plone un servicio ejecute: 

.. code-block:: sh

    bin/instance.exe install

Del mismo modo, para la desinstalación ejecute: 

.. code-block:: sh

    bin/instance.exe remove

Una vez que usted haya iniciado una instancia de Plone, la puede ver
visitando http://localhost:8080/ en su navegador web. Si no se carga,
asegúrese de que su Firewall no ha bloqueado el puerto TCP 8080.

Haga clic en "Create a new Plone site" (Crear un nuevo sitio Plone) e
introduzca su información de inicio de sesión para comenzar a usar Plone.
Ingrese la información solicitada y luego envíe el formulario para finalizar
la creación de su sitio. Puede encontrar su sitio en
http://localhost:8080/*SiteName*, donde **SiteName** es la identificación de su
sitio Plone. ¡Diviértase con Plone!


.. _2_instalando_linux_unix_bsd:

2. Instalando en Linux / Unix / BSD
===================================

El instalador Unificado en un kit de código fuente-distribución que incluye
prácticamente todo lo necesario para construir Plone en Linux, OS X, BSD y la
mayoría de sistemas Unix.

.. _21_que_instalador_unificado:

2.1. ¿Qué es el instalador Unificado?
-------------------------------------

Breve introducción al instalador, el caso para utilizarlo, sus opciones y
cambios recientes.

El instalador unificado es un kit de instalación de código fuente para
instalar Python, Zope, Plone y sus dependencias en plataformas de tipo Unix.
Posee dos componentes principales:

-   Los paquetes de código fuente para Python, Zope, Plone, un par de
    librerías de sistema y unas librerías de Python;
-   Un script de instalación que usa paquetes para crear una instalación
    lista-para-usarse, relativamente autocontrolada, de Python/Zope/Plone que
    cumple con los estándares de prácticas recomendadas en la comunidad
    Plone.

La nueva instalación Zope/Plone usará, luego de terminada la instalación, su
propia copia de Python que no remplazará su copia de Python en el sistema. Si
lo desea, puede usar el Python de su sistema (o algún otro), y el instalador
Unificado lo usará sin tener que modificarlo en las librerías de su sitio.


¿Por qué el instalador Unificado?, ¿Por qué no un sistema de Paquetes/Puertos?
..............................................................................

En las listas de ayuda y canales IRC de Plone, la sugerencia "simplemente use
el instalador Unificado", generalmente resulta en una de dos reacciones:

    *Yo prefiero controlar la instalación de código fuente por mí mismo, y 
    escoger todos los directorios de destinos;*

No hay nada malo en eso, sin embargo, si usted utiliza los directorios de
destinos del instalador Unificado podrá ver que le facilitará obtener ayuda
de la comunidad de Plone.

Si aún así elige instalarlos manualmente, está bien. Usted todavía puede
encontrar conveniente descargar el instalador Unificado con el fin de obtener
todos los paquetes juntos, y puede que le resulte útil leer el escrito de la
interfaz de usuario ``install.sh`` para ideas sobre la construcción de componente
particulares.

    *Yo prefiero usar mi mecanismo de plataformas de puertos/paquetes.*

La historia de paquetes de plataforma para Zope y Plone es una problemática.
Paquetes de plataforma han sido de calidad desigual y han utilizado árboles
de instalación que dificultan la ayuda que pueda ofrecer la comunidad cuando
los problemas se presentan. Igualmente, los paquetes de plataforma han sido
históricamente vulnerables a cambios en el sistema de Python. Zope/Plone es
muy exigente al escoger la versión de Python con la cual ejecutarse, además
cualquier actualización del sistema Python, cuando otro elemento está
instalado, puede fácilmente afectar o dañar a Zope/Plone. En este punto,
puede que este pensando que esto simplemente quiere decir que los paquetes
tienen deficiencias con respecto a las dependencias especificadas. El
instalador Unificado se creó porque generación tras generación de paquetes no
resolvieron este problema.


Opciones principales del instalador Unificado
.............................................

El instalador Unificado para Plone posee tres características principales:

-   Instalar como root o como usuario normal;
-   Instalar como un Cluster de objetos empresariales Zope - ZEO, o una
    instancia autónoma de Zope;
-   Instalar el kit completo, o una simple instancia de ejecución.

Cada una de estas opciones están descritas en secciones separadas.

.. note::

    Las versiones anteriores del instalador Unificado no vienen con estas opciones


Cambios en Plone 4
..................

-   El instalador ahora incluye un archivo de configuración
    *develop.cfg*, el cual puede usar después de la instalación inicial para
    configurar un entorno común de desarrollo. Para usarlo, ejecute buildout
    con el comando: 

    .. code-block:: sh

        bin/buildout -c develop.cfg

-   El instalador ahora requiere que las librerías de desarrollo SSL sean
    instaladas previamente en su sistema (usualmente se hace con openSSL) Si
    no las puede encontrar, este se detendrá. Si lo desea puede omitir este
    requerimiento, lo que resultará en una instalación que no puede usar el
    servicio ESMTP (extensión del Protocolo Simple de Transferencia de
    Correo) para correo electrónico.

Cambios en Plone 3.1
....................

-   El instalador Unificado ahora usa :ref:`buildout <que_es_zcbuildout>` 
    para configurar las instancias de Plone, lo que hace más fácil controlar 
    productos adicionales y actualizaciones de su instalación Plone.
-   Es mucho más sencillo agregar instancias adicionales de Zope/Plone a
    una base de instalación existente.
-   Existen opciones adicionales para:

-   Controlar el directorio de destino de la instalación;
-   Establecer un usuario aparte del "admin" y/o configurar la contraseña
    de su elección;
-   El uso de una versión instalada de Python 2.4 (posiblemente una copia
    del sistema). Se usa :ref:`virtualenv <que_es_virtualenv>` para aislar 
    la instalación nueva y así su sistema de Python no es tocado.

-   Si se requiere la instalación de libjpeg o libz, se hace localmente a
    la nueva instalación. Incluso en un modo instalación root, sus librerías
    en el sistema no son tocadas.


Cambios en Plone 3
..................

Si usted ha usado el instalador Unificado para versiones anteriores de Plone,
ya sabrá que las opciones anteriores son nuevas. Hay algunos cambios
adicionales:

-   El script de instalación trata de determinar si necesita o no nuevas
    construcciones de libz y libjpeg. Si no las necesita, no las construirá.
-   La Interfaz de Usuario ahora trabaja más cómoda con plataformas odd-
    duck como Solaris, donde la herramientas GNU pueden estar en locaciones
    inusuales.
-   Esta versión omite algunos productos adicionales (TextIndexNG#,
    ReportLab) incluidos en versiones anteriores.
-   Aunque esta versión trae el nuevo kit de fácil instalación de Python,
    no lo usa.

.. _22_instalacion_root_normal:

2.2. ¿Instalación como root o usuario normal?
---------------------------------------------

Casos donde se recomienda o no la instalación como usuario root.

El script ``install.sh`` para el instalador Unificado puede ser ejecutado como
root (típicamente usando el comando sudo) o como un usuario normal. Las
diferencias claves son:


**La instalación root (usada para producción):**

-   Instala por defecto en ``/usr/local/Plone``;
-   Crea un usuario "plone" y establece este usuario como propietario de
    los archivos de datos (Data.fs). Configura Zope para correr como el
    usuario efectivo "plone".
-   Los archivos de programa y configuración son propiedad del usuario
    root, y no deberían modificarse por los procesos de Zope.


**La instalación de usuario normal (no root):**

-   Instala por defecto en ``$HOME/Plone``;
-   Esta destinada a ser ejecutada por y bajo el identificador efectivo
    de usuario de la persona que instala.


¿Por qué escoger entre instalación normal o root?
.................................................

Instalar como root (o con privilegios root a través de sudo) puede ser la
mejor opción para instalaciones de producción de Plone. Ya que la instalación
se ejecuta bajo el identificador de un usuario creado específicamente para
este propósito, debería tener un nivel de control de acceso más alto a los
recursos. Generalmente esto es aceptado como la "mejor practica"; ejecutar
procesos persistentes (como Zope) por medio de usuarios únicos con permisos
limitados.

De igual forma al instalar como root, tenga cuidado y no ejecute 
``sudo bin/buildout`` excepto cuando esté trabajando ``offline`` (sin conexión), 
ya que si no lo hace inmediatamente ejecutara una setup (instalación) de los
programas descargados. En lugar de esto, obtenga archivos de distribución de
fuentes validadas, colóquelas en ``buildout-cache/download/dist`` y ejecute
``bin/buildout -o`` en el modo sin conexión.

La instalación como usuario normal (quizás con su propia identificación de
usuario) puede ser la mejor opción para una instancia de prueba o desarrollo.
Se hace muy sencillo instalar y editar productos personalizados sin tener que
preocuparse por los derechos o identidades de los usuarios.


.. _ser-zeo-o-no-ser-zeo:

2.3. ¿Ser ZEO o no ser ZEO?
============================

El instalador Unificado instalará Zope ya sea para ejecutarse en una
configuración Cliente/Servidor o en una configuración autónoma. Aquí están
los méritos de ambas.

El instalador Unificado ofrece dos estrategias distintas para la
configuración de Zope:

-   Una configuración ZEO de Cliente/Servidor. ZEO (del inglés Zope
    Enterprise Objects) le permite tener varios procesos de clientes Zope (o
    servidores separados) que comparten una base común de datos de objetos de
    procesos de servidores.
-   Una instancia autónoma de Zope.


**La instancia autónoma de Zope** es más fácil de entender, integrar y
controlar, y probablemente es la mejor opción para un entorno sencillo o de
prueba.

**La configuración ZEO Cliente/Servidor**, no obstante, posee algunas
ventajas para el uso de producción y también desarrollo.

-   Mejores opciones de balanceo de carga. Incluso sin un proxy de
    balanceo de cargas, clientes independientes y procesos de servidores
    pueden distribuir mejor las cargas en servidores modernos multi-núcleo.
    Con un proxy de balanceo de carga, mejores resultados son posibles.
-   La capacidad de ejecutar scripts contra un sitio en producción. Usted
    puede usar ``zopectl run`` para ejecutar scripts en alguno de los clientes
    mientras que otros sirven el sitio a internet.
-   Mejor depuración. Usted puede correr un cliente en modo depuración
    mientras que el resto corre en modo producción. De esta manera puede
    mejorar los diagnósticos para la instancia de depuración. También podrá
    usar herramientas de introspección como Clouseau y el comando ``zopectl debug`` 
    en contra de un sitio en producción.
-   Usted puede reservar un cliente para acceso administrativo (tendrá su
    propio puerto). Luego si usted tiene un incremento súbito en la demanda
    del sitio antes de que esté listo, podrá realizar cambios a través del
    cliente administrativo, incluso cuando su cliente público se ralentice.

.. _24_ejecutando_instalacion:

2.4. Ejecutando el instalador Unificado
---------------------------------------

Preparar la ejecución y ejecutar el instalador Unificado.


Preparaciones
.............

Verifique su plataforma de administrador de paquetes y asegúrese que tenga
los siguientes instalados:

-   gcc, La colección del Compilador GNU.
-   g++, Las extensiones de C++ para gcc.
-   GNU make, la herramienta fundamental de control y construcción.
-   GNU tar. Esta es la versión de tar para todos las plataformas Linux,
    BSD y OS X, pero no Solaris.
-   Paquetes para descomprimir: bzip2 y gzip. Paquetes para descompresión
    bzip2 y gzip. gzip es casi estándar; en algunas plataformas será
    requerida la instalación del paquete bzip2.


    Idealmente debería tener también las librerías *libssl* y *readline*, 
    y los encabezados de desarrollo cargados (usualmente los paquetes 
    libssl-dev y readline-dev). Realmente estos no son requeridas, pero 
    agregan una funcionalidad deseable. *libssl* se requiere para usar TLS 
    (Seguridad de la Capa de Transporte) con su servidor de correo electrónico, 
    lo cual puede ser vital si este no es local. Para detalles lea el 
    instalador Unificado ``README.txt``

Ahora escoja un directorio conveniente de trabajo para extraer el archivo 
.tar.gz (tarball) del instalador Unificado:

.. code-block:: sh

    tar zxf Plone-VERSION-UnifiedInstaller.tar.gz

Luego vaya al nuevo directorio creado:

.. code-block:: sh

    cd Plone-VERSION-UnifiedInstaller
    
.. note::

    *VERSION* - cambiara con cada versión.


Ejecutando install.sh
.....................

Si usted se decidió por la instalación con privilegios root; ya sea por el
comando su a root o precediendo estos comandos con el comando sudo.

**Instalación ZEO:**

.. code-block:: sh

    ./install.sh zeo

**Instalación autónoma de Zope:**

.. code-block:: sh

    ./install.sh standalone

Pues ahora acomódese y observe los mensajes de progreso.

**Si los mensajes de progreso no comienzan,** generalmente significa que
falta alguna herramienta vital de instalación. Use su administrador de
paquetes para instalar la herramienta, y trate nuevamente.

**Si la instalación tiene éxito,** usted verá un conjunto de instrucciones
para la nueva instalación de Zope/Plone. Haga una nota de la contraseña usada
para el usuario "admin". Estas instrucciones también estarán disponibles en
el archivo ``README.txt``, y la contraseña en el archivo ``adminPassword.txt`` 
de su nueva instalación.

**Si la instalación falla,** no entre en pánico. Anote los mensajes de
errores y diagnósticos para que en el caso de que usted no pueda resolverlos
por sí mismo, pida ayuda en la `lista de correo de plone-setup`_ o en el canal
`IRC #plone`_. Nosotros necesitaremos información precisa sobre su plataforma y
toda la información de diagnostico posible para ayudarlo. Además asegúrese de
revisar la sección :ref:`Notas de plataforma <28_notas_plataforma>` en el 
archivo ``README.txt`` que viene con el instalador para ver si hay algún tipo 
de trabajo o requerimiento especial en relación a su plataforma.

.. tip::

    El programa de instalación crea un archivo detallado de registro, llamado 
    ``install.log``, que puede ayudar al diagnostico de una instalación fallida.


Revisando su instalación
------------------------

Si su instalación fue exitosa, trate de iniciarla siguiendo las instrucciones
que se muestran al final del proceso de instalación (o en el archivo
README.txt que está en el directorio de instalación). Los problemas de
arranque no son comunes pero de vez en cuando aparecen; la causa más común es
que otros procesos ya están usando el puerto 8080 (o uno o más de los puertos
8100, 8080 y 8081 si está usando ZEO). Si es así, puede detener o eliminar
ese proceso en el caso de que sea una instalación vieja de Zope/Plone. Si no
también puede reasignar los puertos usados por su instalación de Plone al
editar el archivo buildout.cfg y ejecute el comando ``bin/buildout`` para 
reasignar los puertos.

Si su arranque es exitoso, compruebe su instalación abriendo un navegador web
y navegando a http://localhost:8080/. (Si esta haciendo la prueba en otra
computadora, substituya el nombre (ip o url) de su servidor host por
"localhost".)

Se debería mostrar un mensaje de bienvenida de Zope. Un sitio de prueba
debería estar disponible en http://localhost:8080/Plone, y la Interfaz de
Administración de Zope (Zope Management Interface -ZMI) en
http://localhost:8080/manage

Si aparentemente Zope está ejecutándose, pero no puede conectarse, compruebe
si tal vez un cortafuegos (firewall) está emplazado y bloqueando la conexión.


.. _25_creando_nuevas_instancias:

2.5. Creando nuevas instancias
------------------------------

El instalador Unificado puede usarse para crear instancias adicionales de
Zope/Plone.

Una vez que ha usado el instalador Unificado para realizar completamente una
instalación de Plone, quizás usted quiera crear instancias de trabajo
adicionales para ejecutar otros sitios (o conjunto de sitios). El instalador
Unificado hace posible establecer nuevas instancias que usarán el código base
de Python y Zope de la instalación principal.

Para instalar una nueva instancia, primero decida si quiere una instalación
root o de usuario normal. Usted puede usar el código base de instalaciones
con nivel root para una nueva instancia con nivel root, o una instalación no-
root para una instancia no-root. Además la nueva instancia que puede ser una
instalación ZEO o autónoma, es independiente a la elección que haya hecho
para la instalación principal.


Los Comandos
............

Ubíquese en el directorio que contiene el archivo ``install.sh`` de su instalador
Unificado desempaquetado.

Preceda los siguientes comandos con "sudo" o "su -" para cambiar al usuario
root.

**Para una instancia de clúster de ZEO:**

.. code-block:: sh

    ./install.sh zeo --instance=nuevo_nombre_instancia

**Para una instancia autónoma de Zope.**

.. code-block:: sh

    ./install.sh standalone --instance=nuevo_nombre_instancia


.. glossary::

  nuevo_nombre_instancia
    debería ser un nombre de directorio simple - y no un nombre de ruta completo. 
    El nuevo directorio se creara como un nuevo subdirectorio de la instalación 
    completa y compartirá su respectivo Python y el cache de buildout.


Definiendo nuevos Puertos
.........................

La nueva instancia aún no está lista para ejecutarse, ya que está configurada
para usar los puertos por defecto y entrará en conflicto con la instalación
previa. Afortunadamente esto es fácil arreglar.

Vaya al directorio que contiene su nueva instancia y abra el archivo ``buildout.cfg`` 
con su editor de texto favorito.

Si esta es una instancia autónoma, solo necesitará definir un puerto nuevo en
un lugar solamente:

.. code-block:: cfg

    http-address = 8080

Para la instancia ZEO se requiere un poco mas de trabajo. Usted necesitará
cambiar dos entradas de ``http-address`` (una para cada cliente) y el puerto para
el servidor de ZEO, el cual se define en la línea:

.. code-block:: cfg

    zeo-address = 127.0.0.1:8100

Solo cambie el numero de puerto (8100); y no modifique la dirección IP.


Constrúyalo
...........

Guarde sus cambios y ejecute :ref:`buildout <que_es_zcbuildout>` para actualizar 
todas las partes de la instalación:

.. code-block:: sh

    bin/buildout


Si esta es una instalación root, anteponga el comando "sudo" o use "su -"
para cambiar al usuario root.

Ahora ya está listo para correr la nueva instancia.

.. _26_opciones_cli_instalador:

2.6. Opciones de líneas de Comando
----------------------------------

Algunas opciones poco frecuentes del instalador Unificado, pero de igual
manera siguen siendo útiles para usted.

Puede agregar la siguientes opciones a su línea de comando ``install.sh`` para un
control más refinado de su instalación:

--target=pathname
    Úsela para especificar rutas de nivel superior para las instalaciones. 
    Las instancias de Plone y Python se construirán dentro de este directorio.

--user=user-name
    En una instalación root, define el usuario efectivo para ejecutar la instancia. 
    Por defecto es el usuario "plone". Ignorado para las instalaciones no-root.

--with-python=/fullpathtopython2.x
    Si usted ya tiene una construcción Python adecuada para ejecutar Zope/Plone, 
    lo puede especificar aquí. :ref:`virtualenv <que_es_virtualenv>` se usara para 
    crear un entorno aislado de Python para la instalación. La librería del sistema 
    de su sitio no se tocara. Se requiere Python 2.4 para Plone 3.x, y Python 2.6 
    para Plone 4. Su Python debe satisfacer las necesidades de Plone, y el 
    instalador pondrá a prueba el soporte para las librerías zlib, *libssl* y xml 
    antes de construir para ellas.

--password=InstancePassword
    Si no se especifica, una contraseña aleatoria sera generada.

--without-ssl
    Las librerías de desarrollo SSL (generalmente OpenSSL) se necesitan al construir 
    Python para que soporten SSL (protocolo de capa de conexión segura) y TLS (protocolo 
    para seguridad de la capa de transporte). Sin ellas Plone no podrá utilizar TLS en 
    SMTP (Protocolo Simple de Transferencia de Correo). El instalador Unificado habitualmente 
    se detendrá si no puede encontrar el encabezado SSL y sus librerías. Use esta opción 
    para indicarle al instalador que usted sabe lo que esta haciendo y que desea continuar 
    sin las SSL.

--without-lxml
    ``lxml``, un wrapper (empaquetador) de Python para ``libxml2`` y ``libxslt``, no es 
    requerido para Plone 4.1. Pero se necesita por algunos programas populares adicionales 
    como plone.app.theming. A menos que usted especifique esta opción, el instalador tratara 
    de construir ``lxml`` con las librerías estáticas ``libxml2`` y ``libxslt``. Puede que 
    esto no funcione en todas las plataformas.

--nobuildout 
    Saltar la ejecución de ``bin/buildout``. Usted debería saber que esta haciendo. El uso 
    principal para esta opción se refiere a cuando usted desea que el instalador Unificado 
    junte todas las piezas, para luego activar su propio archivo buildout.cfg.

El instalador Unificado averiguara si usted tiene o no, las librerías ``libz``,
``libjpeg`` y ``readline`` en su sistema. Si las tiene: genial. Si no las tiene, el
instalador tratará de construirlas en el subdirectorio lib/ del destino de su
instalador y hacer un enlace directamente a ellas. En el caso de que esto no
sea lo que quiere, use las siguientes opciones de líneas de comando para
ajustar este comportamiento.

**--libz=auto|yes|no**

**--libjpeg=auto|yes|no**

**--readline=auto|yes|no**

auto
     Tener este programa determina si necesita o no la librería instalada. 
     Si es necesaria, sera instalada en ``$PLONE_HOME``. Esta es el 
     comportamiento por defecto.

yes
    para forzar la instalación en ``$PLONE_HOME`` (o ``$LOCAL_HOME``) para 
    enlaces estáticos, incluso si una copia en el sistema de la librería 
    esta disponible.

no
    para no forzar la instalación de la librería.


.. _27_paquete_instalador_ubuntu_debian:

2.7. Paquetes de instalación Ubuntu / Debian
--------------------------------------------

¿Cómo instalar los paquetes requeridos en los estilos de sistemas
Debian/Ubuntu?

Antes de comenzar el proceso debería instalar los paquetes del sistema
requeridos para la ejecución:

.. code-block:: sh

    sudo apt-get install build-essential
    sudo apt-get install libssl-dev
    sudo apt-get install libxml2-dev
    sudo apt-get install libxslt1-dev
    sudo apt-get install libbz2-dev
    sudo apt-get install zlib1g-dev

En vez de permitir al instalador usar su propios paquetes, es muy conveniente
usar los paquetes del sistema para librerías comunes.

.. code-block:: sh

    sudo apt-get install libjpeg62-dev
    sudo apt-get install libreadline-gplv2-dev

Y si usted quiere habilitar la anexión de documentos de Word y PDF:

.. code-block:: sh

    sudo apt-get install wv
    sudo apt-get install poppler-utils


.. _28_notas_plataforma:

2.8. Notas de Plataformas
-------------------------

Notas de contribución de usuarios que usan el instalador Unificado en
plataformas particulares


Instalando en Solaris 10 (x86)
..............................


*Publicado por Michael Bobzin el 15 de Febrero de 2008 03:12 PM*

Hola,

para completar la instalación en Solaris 10 (x86) tengo que
cambiar algunas líneas en ``install.sh``

.. code-block:: sh

    #!/bin/bash
    ...
    #Build Python
    ...
    if [ $NEED_LOCAL -eq 1 ]
    then
     ...
    else
        export LD_LIBRARY_PATH=/usr/local/lib
            ./configure \
                    --prefix=$PY_HOME \
                    --with-readline \
                    --with-zlib \
                    --disable-tk \
                    --with-gcc="$GCC" \
                    --with-cxx="$GPP"
    fi


Instalando en Solaris 10 (SPARC)
................................

*Publicado por Joni Barnoff el 5 de abril de 2008 07:31 PM* 

.. code-block:: sh

    LD_LIBRARY_PATH=/usr/local/ssl/lib


Esto es necesario para incluir *libssl* en la construcción de Python.


Instalando en Solaris 10 (SPARC)
................................

*Publicado por Jim Leek el 20 de Marzo de 2009 04:21 PM*

Los inconvenientes principales en Solaris se deben al hecho de que el script
del instalador (``install.sh``) no siempre puede obtener las rutas correctas para
la versión correcta del software en Solaris. También tiene problemas para
encontrar las librerías correctas en el entorno de Solaris. Para agregar a
este ``install.sh`` se usa el shell básico Bourne (#!/bin/sh), lo que significa
que algunos de los comandos que son parte del shell Bourne de Linux y que no
están presentes en el shell Bourne de Solaris simplemente no funcionan. Cabe
destacar que el interruptor e-(existe) no esta presente en el shell Bourne de
Solaris: 

.. code-block:: sh

    if [ -e $INSTALL_LOG ]       # Does not work in Solaris.


Para resolver esto haga lo siguiente:

1. Se necesita que las locaciones de todas las dependencias se ubiquen en Solaris:

 (a) gcc - /usr/local/bin/gcc (gcc-3.4.6 proveniente de www.sunfreeware.com - por defecto en solaris 10 es /opt/sfw/bin/gcc)
 (b) g++ - /usr/local/bin/g++ (Instalado con gcc-3.4.6 - por defecto en solaris 10 = /opt/sfw/bin/g++)
 (c) gmake - /opt/sfw/bin/gmake
 (d) gtar - /usr/sfw/bin/gtar
 (e) gzip - /usr/bin/gzip
 (f) bzip2 - /usr/bin/bzip2

Además ``install.sh`` usa el comando shell ``whoami`` , el cual en Solaris se encuentra en:

 (g) whoami - /usr/ucb/whoami

2. Garantice que todas las Rutas anteriores se encuentren en la ruta del sistema: 

.. code-block:: sh

        PATH=$PATH:/opt/sfw/bin:/usr/sfw/bin:/usr/ucb:/usr/ccs/bin
        export PATH

(Si /usr/ccs/bin no es agregado, la compilación de Python fallara con "gmake:ar: Command not found".)

3. Debido a que el interruptor -e no esta presente en el shell Bourne de Solaris, 
el script ``install.sh``, y todos los otros scripts, este se debe cambiar a bash: 

.. code-block:: sh

        #!/usr/bin/bash

4. El script ``install.sh`` utiliza el comando shell ``which`` para localizar el software 
que necesita para la construcción. Para garantizar que las versiones correctas del software 
fueron utilizadas (en lugar de las predeterminadas de Solaris), ``install.sh`` fue modificado 
explícitamente para definir las locaciones de cada pieza del software: 

.. code-block:: sh

        GCC=/usr/local/bin/gcc
        GPP=/usr/local/bin/g++
        GNU_MAKE=/opt/sfw/bin/gmake
        GNU_TAR=/usr/sfw/bin/gtar
        GUNZIP=/usr/bin/gunzip
        BUNZIP2=/usr/bin/bunzip2


5. Durante la construcción se necesitan ambas librerías: "libssl" y "readline". 
Agréguelas a la ruta de la librería del sistema. 

.. code-block:: sh

        LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/ssl/lib:/opt/sfw/lib
        export LD_LIBRARY_PATH

Para mas información: `http://www.eng.ox.ac.uk/Plone/solaris/plone-installation`_


Solaris 10 x86
..............

*Publicado por Coopertino el 9 de Septiembre de 2008 02:03 PM* 

.. code-block:: sh

    cat /etc/release
    Solaris 10 8/07 s10x_u4wos_12b X86

La instalación se ejecuto sin problemas, después de estas dos modificaciones:

En el script ``install.sh`` en la línea 1 

.. code-block:: sh

    from #! /bin/sh  --> #! /bin/bash

En el script ``install.sh`` en la línea 81 

.. code-block:: sh

    from GNU_TAR=`which tar` --> GNU_TAR=`which gtar`

.. _3_instlando_windows:

3. Instalando en Windows
========================

¿Cómo preparar y ejecutar Plone en Windows?; no para desarrollo considerable.

El instalador binario para Windows es la opción a escoger si quiere probar
Plone en Windows o para ser el host de un sitio, pero no para desarrollo
considerable. Si considera desarrollar formalmente en Windows, consulte `este
documento`_.

**Este documento fue actualizado para Plone-4.1.2.**


Lo Básico
----------

**Esta sección explica cómo para hacer una instalación básica de Plone.**


Descargue e instale Plone
-------------------------

1.  Descargue el instalador desde esta página en plone.org:
    `http://plone.org/download`_.

2.  Guárdelo en un sitio que pueda recordar, tal como su Escritorio.

3.  Después que la descarga haya finalizado, haga doble clic en archivo
    del instalador para ejecutarlo.

4.  Encamínese por el asistente de instalación. El instalador crea una
    carpeta en ``C:\Plone41`` e instala allí el Plone.

5.  Aguarde mientras el instalador extrae los archivos y crea su
    instancia de Plone.

6.  El instalador más nuevo automáticamente instala servicios de Windows
    para Plone y empieza los servicios de tal manera no allá ninguna
    necesidad de iniciar el servicio de Plone manualmente. Si usted necesita
    iniciar o parar los nuevos servicios ellos son llamados "Plone 4.1" y
    "Plone 4.1 Zeo" y están listado en la ventana de controlador de
    Servicios.


Accediendo a Plone
------------------

*Nota: Quizás tenga que indicarle a su Firewall (cortafuegos) que abra el
puerto TCP 8080, antes de que pueda acceder a la interfaz web de Plone.*

1.  Abra un navegador web y vaya a http://localhost:8080/ y haga clic en
    el botón "Create a new Plone site".

2.  Lo próximo es iniciar sesión de usuario. El nombre de usuario por
    defecto de Zope "admin" y la contraseña es también "admin" (sin las
    comillas dobles).

3.  En la página "Create a Plone site" desplace hacia abajo y clic el
    botón "Create Plone Site".

4.  Después de que el sitio está creado usted será redirigido al sitio en
    la dirección http://localhost:8080/Plone. Usted puede utilizar esta
    dirección URL la próxima ves que usted quiera visitar su sitio.


Iniciando y Deteniendo su servicio Plone
----------------------------------------

**En este caso usted necesita parar o iniciar sus servicios Plone a mano
usted puede acceder de esta forma:**

* Haga clic en el botón de "Inicio" de Windows .

* Escriba "servicios" (sin comillas dobles) dentro de la barra de búsquedas que
  parecerá al final del menú de Inicio.

* Haga clic en la entrada llamada "Servicios" en la categoría "Programas" de
  los resultados de búsqueda.

* En la ventana de Servicios, desplace hacia abajo para buscar los servicios
  "Plone 4.1" y "Plone 4.1 Zeo".

De aquí usted puedes iniciar y parar los servicios siempre que usted
necesite.

Si usted solamente probando Plone y usted no quiere que se inicie cada ves
que usted inicie su computadora, haga los ajustes en la opción "Propiedades"
de cada uno de los servicios Plone y establezca el valor "Tipo de arranque" a
"Manual."


Los detalles
------------

**Esta sección da más información sobre el instalador de Windows y cómo
personalizarlo si fuera necesario.**

Como de Plone 4.0.9 y Plone 4.1 hay nuevos instaladores de Windows que se
prestan a la comunidad. Estos instaladores se comportan de manera diferente
que las versiones anteriores. Este documento explica los cambios y las
razones detrás de ellos.


Visión general
..............

Anteriormente, el instalador de Windows Plone de corriendo con el buildout
después le permite al usuario introducir varias variables, incluyendo un
directorio de instalación. Aun así, debido a la manera en que Python, Windows
y buildout interaccionan, mucho tiempo o directorios de instalación compleja
no siempre trabajo de una, y la los principales errores fatales suceden
durante la ejecución del proceso de instalación de buildout. De esta falla
puede ser muy difícil que un usuario nuevo de Plone se pueda recuperar,
creando así una mala "primera Impresión" para un nuevo usuario.

La nueva instalación de Plone en Windows opera algo de esta flexibilidad para
una fiabilidad mucho mayor. Buildout se ejecuta cuando la construcción de la
instalación, no "en vivo" durante el proceso de instalación. Esto significa
que buildout nunca puede fallar durante instalación. Aun así, esto también
significa que el instalador de Windows sólo instalará Plone a las rutas
``C:\Plone41`` (para 4.1) y ``C:\Plone42`` (para 4.2).

Para los usuarios que requieren más flexibilidad en las rutas de instalación,
hemos proporcionado la posibilidad de copiar y pegar un directorio de
instalación a una nueva ubicación, así como una nueva instalación para crear
instaladores personalizados de Windows para Plone (que se incluye con el
instalador de Windows Plone). Ahora, usted puede modificar sus buildouts y
regenerar nuevos instaladores de Windows con configuraciones diferentes (por
ejemplo, el uso de múltiples clientes ZEO, bases de datos múltiples o
productos diferentes), que se pueden utilizar en la producción o distribución
a los clientes.


Predeterminados
...............

Los servicios Plone en Windows ahora utilizan una receta llamada
``enfold.recipe.winservice`` que es un fork de la receta ``z3c.winservice`` 
para usar en Zope 2. El nuevo instalador Plone de Windows tiene tres 
diferencias fundamentales respecto a las versiones anteriores:

-   Credenciales predeterminadas para Plone

    -   Anteriormente usted se puede crear a partir de ellas dentro del
        instalador.
    
    -   Ahora está predefinido el nombre de usuario como "admin" y la
        contraseña: "admin". Esto hace que el instalador de Windows compatible
        con el instalador unificado y el instalador de Mac OS X.
        
        Esto puede ser cambiado editando el archivo ``buildout.cfg``, ver la sección
        ``[shared]`` la cual contenga la línea parecida a esta:

        .. code-block:: cfg

            user = login:password

-   Nombre de Servicio del Windows

    -   Anteriormente, esto se ha generado automáticamente durante la
        instalación.
        
    -   Ahora es definido en el archivo ``buildout.cfg`` vea la secciones 
        ``[service]`` y ``[service-zeo]``

        .. code-block:: cfg

            name = Unique Service Name

-   Ubicación de instalación

    -   Anteriormente, el usuario puede seleccionar / crear una carpeta nueva para instalar Plone.
        
    -   Ahora se instala en ``C:\Plone41`` o ``C:\Plone40`` (según la versión).


Cómo cambiar la ubicación de Instalación
........................................

El nuevo instalador de Plone para Windows no le deja para cambiar la ubicación 
de instalación cuándo te corrido el instalador. Aun así, es todavía posible al 
instalar Plone ingresar una ubicación diferente después de la instalación inicial, 
bien que es una vía del proceso más manual. Por ejemplo, suponga que se ha instalado 
Plone en la ruta ``C:\Plone41`` y después de su evaluación usted lo quieres mover 
hacia una ubicación más permanente, digamos en la ruta ``Z:\Plone41-Intranet\``.

La buena noticia es que el directorio de instalación, ``C:\Plone41``, es 100% 
auto-contenido. No hay dependencias externas instaladas en cualquier otro 
lugar de su sistema. Usted puede sencillamente copiar / pegar este directorio, 
modificar su archivo buildout.cfg (descrito abajo), y reconstruir su entorno 
personalizado. Para una implementación de calidad en producción de Plone, usted 
casi siempre tiene que hacer esto porque la configuración por defecto de la 
instalación Plone para Windows son muy básicas, y destinada más para la 
evaluación de los escenarios de despliegue de producción.

He aquí un ejemplo simple para mover Plone desde su instalación por defecto directorio 
(``C:\Plone41``) a un nuevo directorio ``Z:\Plone41-Intranet``

-   Cambie a la unidad ``Z:\`` y ejecute los siguiente comandos:

    .. code-block:: cfg

        mkdir Plone41-Intranet
        cd Plone41-Intranet
        copy C:\Plone41\* .
        
-   Cambie de ubicación a ``Z:\Plone41-Intranet``
-   edite el archivo ``buildout.cfg``

-   valla a la sección ``[shared]``
-   cambie la variable de usuario ``login:password`` que quieran usar
-   cambie la variable ``http-address`` a un único puerto, que diga ``9090``
-   cambie la variable ``zeo-address`` a un único puerto, que diga ``9999``

    .. code-block:: cfg

        [shared]
        user = administrator:s3kr1t
        http-address = 9090
        zeo-address = 9999
        debug-mode = off
        verbose-security = off

-   valla a la sección ``[service]``
-   cambie la variable ``name`` a "Plone 4.1 Intranet"

    .. code-block:: cfg

        [service]
        recipe = enfold.recipe.winservice:service
        name = Plone 4.1 Intranet
        runzope = run-instance

-   valla a la sección ``[service-zeo]``
-   cambie la variable ``name`` a "Plone 4.1 Intranet Database"

    .. code-block:: cfg

        [service-zeo]
        recipe = enfold.recipe.winservice:service
        name = Plone 4.1 Intranet Database
        runzope = run-zeo


-   ejecute de nuevo la construcción de los archivos configuración, con
    el siguiente comando:

    .. code-block:: sh

        bin\buildout.exe
        
-   Ahora instale sus nuevo servicio

    .. code-block:: sh

        bin\instance.exe install
        bin\zeo_service.exe install
        
-   Ahora usted puede iniciar su servicio de servidor de la base de
    datos, con el siguiente comando:

    .. code-block:: sh

        bin\zeo_service.exe start
        
-   Esa es siempre la mejor forma de iniciar su cliente/instancia en modo
    foreground. Si esto le falla, una falta de configuración sustancial 
    o una falta de coincidencia sustancial del código fuente de su sistema.

    .. code-block:: sh

        bin\instance.exe fg

Su terminal se conectará al servidor. Si dice "Zope Ready to Serve Requests" 
usted anda en buen camino. Presione la combinación de teclas
Control-C o la tecla Break y inicie el servicio desde el panel de servicios
panel o por la línea de comando, de la siguiente forma:

    .. code-block:: sh

        bin\instance.exe start

.. note::

    Yo creo que hay un problema con el registro y python. Desde entonces nosotros
    *no* registramos en el python del sistema, usted lo tendrá que tener
    instalado en su directorio de trabajo actual dentro de una carpeta llamada
    Python. 
    
Así que el comando será como siguiente:

.. code-block:: sh

    Z:\\Plone41-Intranet> bin\buildout
    Z:\\Plone41-Intranet> cd python
    Z:\\Plone41-Intranet\Python> python ..\bin\service.py --startup auto install
    Z:\\Plone41-Intranet\Python> python ..\bin\service-zeo.py --startup auto install
    
    
Construyendo un Instalador de Windows personalizado
...................................................

La característica más grande del nuevo instalador es la capacidad de crear
unos instaladores de Windows personalizados, con el cual usted puede utilizar
o distribuir. Anteriormente, construyendo un instalador de Windows
personalizado usted requería un conocimiento sustancial de otros cuántos
diferentes sub-sistemas que trabajan en conjunto. Ahora usted sencillamente
edite el archivo ``installer.cfg`` del recipe buildout. Ejecute de nuevo buildout
con el parámetro de la siguiente forma ``bin\buildout -c installer.cfg`` y usted 
conseguirá un nuevo instalador de Windows ejecutable en el directorio actual de trabajo.

Vea el enlace sobre los "Detalles de los paquetes Windows" a continuación
para mayor información.

Accediendo a Plone
------------------

Quizás tenga que transmitirle a su Firewall (cortafuegos) que abra el puerto
8080, antes de que pueda acceder a la interfaz web de Plone.

Abra un navegador web y vaya a http://localhost:8080/. Haga clic en el botón
que contiene el texto "Create a new Plone site" (Crear un nuevo sitio Plone)
Se le pedirá que introduzca el nombre de usuario y contraseña: aquellos que
escribió anteriormente.

Otórguele a su sitio una identificación como "Plone", y un titulo como "Mi
sitio Plone". Además puede seleccionar el idioma del sitio y algunos
productos adicionales para su instalación. Luego haga clic en el botón "Add
Plone Site" (Agregar nuevo sitio Plone) cerca del final de la pagina. Tomara
unos segundos crear su sitio Plone

Después de que su sitio se haya creado puede acceder a el mediante esta URL:
*http://localhost:8080/Plone*, donde "Plone" es la identificación de su
sitio.

Referencias
===========

- `Instalando Plone con el Instalador Unificado`_.
- `Installing Plone`_.
- `Detalles de los paquetes Windows`_.
- `Sitio Web de Buildout`_.

.. _esta página: http://plone.org/products
.. _aquí: http://plone.org/documentation/kb/installing-plone-with-the-unified-installer/command-line-options
.. _http://www.eng.ox.ac.uk/Plone/solaris/plone-installation: http://www.eng.ox.ac.uk/Plone/solaris/plone-installation
.. _este documento: http://plone.org/documentation/kb/using-buildout-on-windows
.. _http://plone.org/download : http://plone.org/download
.. _Instalando Plone con el Instalador Unificado : http://plone.org/countries/conosur/documentacion/instalando-plone-3-con-el-instalador-unificado
.. _Installing Plone: http://plone.org/documentation/manual/installing-plone
.. _Detalles de los paquetes Windows: http://package.enfoldsystems.com/docs/windows.html
.. _Sitio Web de Buildout: http://www.buildout.org/
.. _lista de correo de plone-setup: http://plone.org/support/forums/setup
.. _IRC #plone: http://webchat.freenode.net/?channels=plone
