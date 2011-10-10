.. -*- coding: utf-8 -*-

====================================================
Configurar puntos de montajes para Data.fs separadas
====================================================

El montaje de un sitio Plone con la base de datos objetos **Data.fs** separadas puede ser muy útil si se
están ejecutando varios sitios Plone en una sola instancia de Zope.


¿Por qué?
~~~~~~~~~

Esto significa que usted puede tomar ese sitio y moverlo a otro lugar, o
migrarlo, sin afectar a nadie más. También puede restaurarlo sólo este sitio
si ocurre algo desastroso.

¿Que es un punto de montaje ZODB?
----------------------------------

Es la capacidad de montar diferentes bases de datos de objetos Zope - ZODB separadas,
y así poder definir parámetros específicos para cada ZODB.


Casos de usos
--------------

Existen diversos procedimientos para establecer puntos de montajes que a
continuación se describen:


Establecer puntos de montaje a una instalación predeterminada
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Este es el procedimiento para cambiar una configuración predeterminada en una
instalación con un punto de montaje para un ZODB.


1.  Crear una instancia Plone en una máquina de desarrollo en alguna
    parte. Debe ser la misma versión de Plone de su versión de producción
    (por ejemplo, Plone 3.3.6 o la que sea).
2.  Elimine el sitio por defecto de Plone que creado en esta instancia y
    crear un nuevo sitio Plone - le da un **identificador**. (Es posible que
    desee agregar un usuario administrador para el sitio en este punto).
3.  `Compacte la base de datos`_ y detenga la instancia.
4.  Copie el archivo *Data.fs* de esta instancia en un directorio con el
    mismo **identificador** como el sitio que ha creado.
5.  Acceda a este directorio creado en la carpeta *var/filestorage* en su
    instancia de producción.
6.  Utilice el récipe de zc.buildout llamado
    `collective.recipe.filestorage`_ en su configuración buildout para crear
    los puntos de montaje (donde las piezas se muestra una lista de los
    identificador de nombres de sitio):

    .. code-block:: cfg

      [mountpoints]
      recipe = collective.recipe.filestorage
      location = var/filestorage/%(fs_part_name)s/Data.fs
      parts =
          cliente-1-sitio-web
          cliente-2-intranet

7.  Detenga el servidor Zope de producción y ejecute de nuevo su
    buildout.
8.  Iniciar el servidor Zope de producción, acceda a través de la **ZMI** 
    y utilice la lista desplegable en la parte superior derecha y seleccione 
    la opción **Plone site** para crear un sitio Plone nuevo con el mismo 
    **identificador** como su sitio de montaje.
    A continuación, elimine este sitio (sí, yo sé que es raro, pero es algo
    que tiene que ver con el nivel superior de carpetas **acl_users**).
9.  Utilice la lista desplegable en la parte superior derecha y seleccione 
    la opción **ZODB mount points** para crear un nuevo punto de montaje 
    de ZODB. Usted debe ver a sus **puntos de montaje** listo para crearlos.


Establecer nuevos puntos de montajes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Utilizando el récipe de zc.buildout llamado `collective.recipe.filestorage`_ es muy facil ya que solo necesita agregar una nueva linea en su configuración buildout, cada linea representa un punto de montaje para cada sitios, a continuación se muestra un ejemplo de esto:

.. code-block:: cfg
  
  [mountpoints]
  recipe = collective.recipe.filestorage
  location = var/filestorage/%(fs_part_name)s/Data.fs
  parts =
      cliente-1-sitio-web/Data
      cliente-2-intranet/Data
      cliente-2-sitio-web/Data
      cliente-3-blog/Data

Luego debe guardar los cambios y ejecutar de nuevo el script buildout, con el siguiente comando:

.. code-block:: sh
  
  ./bin/buildout -vN


Hacer copias de seguridad con Data.fs separadas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Al hacer copias de seguridad es un poco complejo usando las
herramientas generadas por el buildout del `Instalador Unificado`_ (por
el hecho de que cada Data.fs esta en su propio directorio), pero este
punto trabaja en su configuración buildout de la siguiente forma:

.. code-block:: cfg

  [backup]
  additional_filestorages =
      cliente-1-sitio-web/Data
      cliente-2-intranet/Data


Consejos
--------

Los siguientes consejos le ofrecerán una serie de recomendaciones para evitar
problemas al establecer puntos de montajes:

Problemas de memoria
~~~~~~~~~~~~~~~~~~~~

El uso de archivos separados Data.fs requiere mucha memoria, en la que cada
Data.fs, en cada cliente, se creará un objeto cache en la memoria RAM. Usted
puede reducir el número de objetos almacenados para todas las bases de datos
a la vez en la parte de los puntos de montaje de su buildout, utilizando la
opción de tamaño **zodb-cache**. Alternativamente, usted puede definir el
número de objetos de un Data.fs particular usando una configuración adicional
buildout con el prefijo **filestorage_**.

Ver el récipe `collective.recipe.filestorage`_ para más
detalles.

En versiones posteriores ZODB, también es posible controlar el tamaño de la
memoria, en bytes, en lugar de números de los objetos. Usted también puede
buscar en el almacenamiento de blob (en el sistema de archivos) para cuando
requiera almacenar objetos de gran tamaño en la ZODB.

¡Nunca jamás haga esto!
~~~~~~~~~~~~~~~~~~~~~~~

Nunca copiar y pegar objetos entre los puntos de montajes de sus sitios.
Usted puede hacer esto a través de la ZMI y es muy tentador. Zope simplemente
copia un puntero al objeto, no el objeto en sí mismo, así que cuando el
objeto se elimina en la base de datos de origen, se obtiene una referencia
pendiente y, finalmente, base de datos de errores poskey en el base de datos
destino muestra una serie de errores horribles para arreglar.

Eso también puede ser un gran dolor, porque el error, probablemente no
aparecerá hasta que usted compacte su base de datos de origen, que pueden ser
muy pocos días después de que en realidad se elimino el objeto - y por
supuesto que usted necesita para hacer un roll back en la base de datos de
origen (la cual no aparecerá dañada), sino la base de datos de destino.

Creo que las versiones posteriores de ZODB tienen algún tipo de bandera o
marca "flag" que establezcan para evitar que esto no suceda, pero me gustaría
tener cuidado.

Referencias
-----------

- `How to mount a Plone Site as a separate Data.fs`_.
- `Multiple Plone sites per zope instance - using separate Data.fs files for each one`_.

.. _collective.recipe.filestorage: http://pypi.python.org/pypi/collective.recipe.filestorage
.. _Instalador Unificado: http://plone.org/countries/conosur/documentacion/instalando-plone-3-con-el-instalador-unificado
.. _How to mount a Plone Site as a separate Data.fs: http://webteam.medsci.ox.ac.uk/integrators-developers/separatedatafs
.. _Multiple Plone sites per zope instance - using separate Data.fs files for each one: http://plone.org/documentation/kb/multiple-plone-sites-per-zope-instance-using-separate-data-fs-files-for-each-one
