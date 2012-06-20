.. -*- coding: utf-8 -*-

.. _creando_temas_diazo:

=======================
Creando Temas con Diazo
=======================

:Autor(es): Leonardo J. Caballero G.
:Correo(s): leonardocaballero@gmail.com
:Lanzamiento: |version|
:Fecha: |today|

.. contents :: :local:

¿Como funciona?
===============

 * Con un simple XML usted substituye elementos de su 'template' o 'plantilla' html por contenido generado por el Plone.

 * Este concepto se basa en la técnica de programación `Screen scraping`_.

 * Se implementa de forma sencilla en Plone usando el motor de temas `Diazo`_ y el producto `plone.app.theming`_.

¿Qué es Diazo?
==============

 * Es la nueva manera de crear temas para el Plone.
 * Permite aplicar cualquier HTML en Plone.
 * Es un motor de temas.

Requisitos
==========

 * Plone 4.1.x y `plone.app.theming`_
 * Plone 4.2


Instalación
===========

El paquete ``plone.app.theming`` trabaja con Plone 4.1 o superior.

Para instalar ``plone.app.theming`` dentro de su instancia Plone, ubique el archivo 
``buildout.cfg`` en el directorio de su instancia Plone en el sistema de archivo, 
y ábralo con un editor de texto. Ubique la sección que luce así:

.. code-block:: cfg

    # extends = http://dist.plone.org/release/4.1/versions.cfg
    extends = versions.cfg
    versions = versions

Y agregue ``plone.app.theming`` a su configuración, para esto es necesario cambiar 
algunas versiones de paquetes a instalar, con esto se extiende las configuraciones 
base desde una lista de versiones desde el servicio `good-py`_, entonces se cambia 
esta parte de la configuración de la siguiente forma:

.. code-block:: cfg

    extends =
        versions.cfg
        http://good-py.appspot.com/release/plone.app.theming/1.0b1

    versions = versions

.. note::
    Note que la ultima parte de la URL es el numero de versión de Diazo. Tal ves si 
    hay una nueva versión en el tiempo se aplicaran las nuevas versiones definiéndola 
    allí, si quiere verificar esto consulte la `página de la información`_ para conocer 
    las configuraciones adecuadas.

Lo que sucede aquí es que la lista dependencias para el producto ``plone.app.theming`` 
especifica algunas nuevas versiones de paquetes a instalar vía la dirección URL de 
`good-py`_. De esta forma, no tendrá problemas con conflicto de versiones, ya que 
Buildout manipulara esto por ti.

El próximo paso es agregar el paquete ``plone.app.theming`` en la sección "eggs"
del archivo ``buildout.cfg``. Vea que por defecto la sección luce así:

.. code-block:: cfg

    eggs =
        Plone

Esta sección podrá tener muchas lineas adicionales, si usted ya tiene otros productos 
adicionales instalados previamente. Solo agregue el ``plone.app.theming`` en una linea 
aparte, de la siguiente forma:

.. code-block:: cfg

    eggs =
        Plone
        plone.app.theming

Una ves que tenga esas lineas agregadas en su archivo de configuración, es tiempo de 
ejecutar el script buildout, y el agregara e instalara en su sistema ``plone.app.theming`` 
por usted. Vaya a la linea de comando, y desde el directorio raíz de su instancia Plone 
(el mismo directorio donde esta localizado su buildout.cfg) ejecute buildout 
de la siguiente forma:

.. code-block:: sh

    $ bin/buildout -vN

Usted vera en la salida estándar de la consola algo similar a esto:

.. code-block:: sh

    Getting distribution for 'plone.app.theming==1.0b1'.
    Got plone.app.theming 1.0b1.
    ...

Si todo ha ido según el plan, ahora tienen ``plone.app.theming`` instalado en su 
instancia de Zope.

Próximo paso, iniciar el servidor Zope, con el siguiente comando:

.. code-block:: sh

    $ bin/instance fg

Entonces valla al panel de control de los **Complementos** en 
:menuselection:`Configuración de sitio --> Complementos` como un usuario 
Administrador Plone, y marque la casilla del producto "Diazo theme support" 
y haga clic en el botón ``Habilitar``. 

Usted notara que ahora tiene un nuevo elemento dentro del panel de control llamado "Diazo theme".


Estructura básica del paquete
=============================

 * Un tema es un simple archivo .zip conteniendo una carpeta con al menos dos archivos:

    .. code-block:: sh

        tema-diazo/
        |-- index.hyml
        `-- rules.xml

 * Normalmente, el paquete es más complejo.

 * Contiene archivos CSS, las imágenes, Javascripts.

Crear una carpeta
-----------------

Crear una carpeta con el nombre de su tema. En esta carpeta irá a guardar 
los archivos de su tema:

.. code-block:: sh

    $ mkdir NOMBRE-TEMA
    
.. warinig:

    Donde **NOMBRE-TEMA** es el nombre de paquete de su tema.

Creando el archivo index.html
.............................

Puede crear el archivo ``index.html`` con los siguientes comandos:

.. code-block:: sh

    $ cd NOMBRE-TEMA ; nano index.html 

Debe al menos tener la estructura HTML siguiente:

.. highlight:: html

::

    <html>
      <head>
       <title>Mi primer tema Diazo</title> 
      </head>
      <body>
       <h1 id="titulo">Mi primer tema Diazo</h1>
       <div id="menu">menú del sitio</div>
       <div id="contenido">Lorem ipsum... </div>
      </body> 
    </html>



Creando el archivo rules.xml
............................

Puede crear el archivo ``rules.xml`` con los siguientes comandos:

.. code-block:: sh

    $ nano rules.xml

Debe crear al menos la siguiente estructura HTML:

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>

    <rules
    xmlns="http://namespaces.plone.org/diazo"
    xmlns:css="http://namespaces.plone.org/diazo/css"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    
    <theme href="index.html" css:if-content="#visual-portal-wrapper" />
    <replace css:content="#portal-globalnav" css:theme="#menu" />
    <replace css:content="#portal-columns" css:theme="#contenido" />
    
    </rules>

**Define a cual template va a utilizar**:

Usted puede establecer cual plantilla HTML usara para este tema con la 
siguiente sentencia Diazo:

.. code-block:: xml

    <theme href=“index.html" css:if-content="#visual-portal-wrapper" />

**Adiciona la navegación de Plone**:

Usted puede importar estructura de la navegación de Plone con la 
siguiente sentencia Diazo:

.. code-block:: xml

    <replace css:content="#portal-globalnav" css:theme="#menu" />

**Adiciona el Contenido**:

Usted puede agregar el contenido del sitio Plone con la 
siguiente sentencia Diazo:

.. code-block:: xml

    <replace css:content="#portal-columns" css:theme="#contenido" />

Colocando en práctica
=====================

Para probar el paquete de tema diazo que lleva hecho hasta ahora puede 
seguir los siguientes pasos:

 * Crear un archivo ZIP con su carpeta del tema.
 * Agregue al sitio Plone
    * :menuselection:`Configuración del sitio --> Diazo Theme`. 
    * Haga clic en la pestaña 'Import Theme' y agregue a su archivo.
    
Es importante destacar que la página de configuración diazo no son 
modificado por seguridad.

Después de aplicar el tema, usted debe tener el código HTML, con 
el menú y el contenido de Plone.

Sin embargo, los estilos no se aplican Plone.

Agregando los estilos
=====================

**Importando el CSS de Plone**:

Usted puede reusar los estilos CSS de Plone con la siguiente sentencia Diazo:

.. code-block:: xml

    <replace css:content="head" css:theme="head" />

Esta llamada substituye todo el HEAD de su HTML por el HEAD de Plone

Reglas Diazo
============

A continuación se describen algunas las reglas diazo mas comunes.

La regla <replace />
---------------------

A continuación el siguiente ejemplo:

.. code-block:: xml

    <replace css:theme="title" css:content="title"/>

El resultado aquí es que el elemento <title /> en el tema será substituido 
por el elemento <title /> del  contenido (dinámico).

La regla <before /> y <after />
-------------------------------

A continuación el siguiente ejemplo:

.. code-block:: xml

    <after css:content="#portal-searchbox" css:theme="#contenido" />

Este ejemplo colocara la búsqueda de Plone al final de la página.

La regla <drop />
-----------------

A continuación el siguiente ejemplo:

.. code-block:: xml

    <drop css:content="#portal-searchbox .searchSection" />

Se utiliza para eliminar los elementos del tema o del contenido 
que no se utilizan.

El ejemplo anterior se eliminará el mensaje "Sólo en esta sección" que 
viene con la búsqueda de Plone.

La regla <merge />
------------------

A continuación el siguiente ejemplo:

.. code-block:: xml

    <merge attributes="class" css:theme="body" css:content="body" />

Se utiliza para combinar los valores de atributos, especialmente usado para 
combinar las clases CSS.

 * Si el tema tiene en su etiqueta body de esta manera:

    .. code-block:: xml

        <body class="alpha beta">

 * Y el contenido posee una etiqueta body como:

    .. code-block:: xml

        <body class="delta gamma">

 * el resultado del ejemplo anteriormente seria:

    .. code-block:: xml

        <body class="alpha beta delta gamma">


Orden de ejecución
------------------

El motor Diazo ejecutará las reglas según un orden propio y no necesariamente 
en el orden escrito. No hay necesidad de decorar, pero es bueno que sea señalado:

1º lugar: <before>

2º lugar: <drop />

3º lugar: <replace> 

4º lugar: Reglas que usan attributes.

5º lugar: Reglas usando "theme-children" 

6º y último lugar: <after /> 

Tema mas completo
=================

Usted podrá encontrar un ejemplo de tema mas completo en la siguiente dirección:

http://plone.org/products/beyondskins.responsive

Mas ejemplos consulte el índice de paquetes Python en búsqueda de `temas basados en diazo`_.

Referencias
===========

-   `Diazo documentation`_.
-   `Construindo temas para Plone com Diazo`_ por la empresa `Simples Consultoria`_.

.. _Diazo: http://pypi.python.org/pypi/diazo/1.0.1
.. _Screen scraping: http://es.wikipedia.org/wiki/Screen_scraping
.. _plone.app.theming: http://pypi.python.org/pypi/plone.app.theming
.. _good-py: http://good-py.appspot.com/
.. _página de la información: http://good-py.appspot.com/release/plone.app.theming
.. _temas basados en diazo: http://pypi.python.org/pypi?%3Aaction=search&term=diazo+theme&submit=search
.. _Construindo temas para Plone com Diazo: http://www.slideshare.net/simplesconsultoria/constuindo-temas-para-plone-com-diazo
.. _Simples Consultoria: http://www.simplesconsultoria.com.br/
.. _Diazo documentation: http://docs.diazo.org/en/latest/index.html

