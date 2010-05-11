********
ZCatalog
********

.. contents :: :local:

Uso del ZCatalog de Zope:

* Permite indexar contenido y realizar búsquedas.
* Todos los objetos de Zope son potencialmente catalogables.
* Ofrece varios índices para diversos tipos de búsqueda.
* Plone lo utiliza a fondo para manejar el contenido.
* Hacer una busqueda es sencillo: resultados = catalog(portal_type='Document')

Tipos de índices
================

`ZCTextIndex`
    Texto, para búsquedas de texto completo.

`FieldIndex`
    Almacena valores específicos, para búsquedas más exactas.

`KeywordIndex`
    Similar a FieldIndex, pero permite buscar listas de valores, como
    palabras clave.

`PathIndex`
    Para hacer búsquedas por path absoluto de los objetos.

`TopicIndex`
    Índice especial para buscar en colecciones prefiltradas.

`DateIndex`
    Parecido a FieldIndex, pero especializado para buscar fechas.

`DateRangeIndex`
    Especial para buscar entre dos fechas dadas.

`ExtendedPathIndex`
    Similar al PathIndex default de Zope, pero con extensiones pensadas para
    Plone. Permite las siguientes operaciones:

    * catalog(path="some/path") - buscar todos los objetos bajo un path.
    * catalog(path={"query":"some/path", "depth":2) - igual que la expresión
      anterior pero limitando los resultados a dos niveles de profundidad bajo
      el path.
    * catalog(path={"query":"some/path", "navtree":1) - igual que la expresión
      anterior pero regresa también los parientes de ese path, para formar un
      árbol de navegación.

Metadata
========

* Los índices únicamente se utilizan para realizar las búsquedas.
* Para almacenar información acerca de los objetos en el catálogo, se utiliza
  metadata.
* En la metadata de catálogo se dan de alta los nombres de los campos de los
  objetos indexados que se quieran almacenar en el catálogo.
* Se recomienda utilizar objetos pequeños como metadata.
* Esta información será incluída en los resultados de la búsqueda.

Resultados de una búsqueda
==========================

Las búsquedas en catálogo no devuelven los objetos buscados, sino un objeto
especial llamado `brain` por cada objeto encontrado. Este objeto especial
contiene el metadata del objeto almacenado en el catálogo. También permite
utilizar los siguientes métodos:

* `has_key(llave)`, para determinar si el brain contiene esa llave.
* `getPath()`, para obtener el path físico del objeto indexado.
* `getURL()`, obtiene el URL del objeto indexado, puede ser distinto del path
  si se utiliza virtual hosting.
* `getObject()`, obtiene el objeto mismo, para poder realizar operaciones con
  él. En Plone se recomienda limitar su uso lo más posible, pues es más lento
  y ocupa más recursos que el objeto brain.
* `getRID()`, regresa el ID del objeto en el catálogo.

Búsquedas avanzadas con records
===============================

Casi todos los campos permiten buscar utilizando como parámetro un diccionario
con uno o más valores. Dentro del diccionario, dependiendo del tipo de índice,
pueden estar incluídos los siguientes campos:

* `operator`, puede ser 'and' o 'or', para KeywordIndex y TopicIndex.
* `range`, puede ser max,min o minmax, para FieldIndex o DateIndex.
* `query`, una lista de valores o un solo valor, para FieldIndex, KeywordIndex,
  PathIndex, DateIndex y DateRangeIndex.
* `level`, número con el nivel inicial de búsqueda, para PathIndex.

Ordenamiento
============

Por default, solo el ZCTextIndex regresa los resultados en algún orden
específico, por relevancia. Para los demás tipos de índices es necesario
especificar si se desea un orden, utilizando los siguientes parámetros en la
búsqueda:

* `sort_on`, el nombre del campo para hacer el sort.
* `sort_order`, ascending o descending, para cambiar el orden en que se realiza
  el sort.
* `sort_limit`, para limitar el número de resultados ordenados y evitar
  procesamiento inútil.

Otros datos acerca del ZCatalog
===============================

* En Plone, se puede definir dentro de un objeto el método SearchableText para
  colocar el texto de todos los campos que quieran incluirse en las búsquedas
  de texto completo. Lo mismo se puede hacer con objetos de Zope fuera de
  Plone utilizando el método PrincipiaSearchSource.
* Es posible indexar un mismo campo en dos índices distintos. Por ejemplo con
  un ZCTextIndex para búsquedas de texto menos exactas y en un FieldIndex para
  resultados más controlados.
* Un objeto no necesariamente tiene que estar en la ZODB para ser catalogado.

