.. -*- coding: utf-8 -*-

.. _zpt_lenguage:

===================
Zope Page Templates
===================

.. contents :: :local:

¿Qué es un Page Template de Zope?
=================================

* Herramienta para generar HTML dinámico.
* Pensado para permitir a diseñadores y desarrolladores trabajar en conjunto.
* Utiliza etiquetas de HTML con atributos extra.
* Permite utilización de macros para reutilizar templates.

Principios regidores de los ZPT
===============================

* Permitir al diseñador trabajar con sus herramientas de edición.
* Poder visualizar la página en edición tal como se verá en el sitio (WYSIWYG).
* Mantener el código separado de los templates.

Funcionamiento de los templates
===============================

* Ejemplo:

.. code-block:: html

      <h1 tal:content="context/title">Título del template</h1>

* Se presenta como: <h1>Biblioteca del Congreso Nacional de Chile</h1>
* Los templates utilizan el lenguaje TAL (Template Attribute Language).
* Las instrucciones de TAL se indican como atributos dentro de las etiquetas
  de HTML normales.
* Todas las instrucciones comienzan con tal: y son ignoradas por editores
  visuales.

Primer page template
--------------------

.. code-block:: html

    <html>
      <body>
         <p>
           Hola, <b tal:content="template/title">título</b>!
         </p>
      </body>
    </html>

Tipos de expresiones
--------------------

* Expresiones Path, que siguen un camino a partir de un objeto inicial hasta
  un resultado:
  
.. code-block:: html

       <p tal:content="context/objectValues"></p>

* Expresiones Python, que evalúan una expresión en Python:
  
.. code-block:: html

        <p tal:content="python:context.objectValues(['Folder'])"></p>

* Expresiones String, que permiten insertar cadenas de texto con iterpolación
  simple:
  
.. code-block:: html

        <p tal:content="string:El usuario actual es ${user/getUserName}."></p>

Insertar texto
==============

Tal:content nos permite sustituir el texto completo de un tag de HTML. Si
queremos insertar texto dentro de una frase, la práctica común es utilizar la
etiqueta span para colocar el texto de reemplazo:

.. code-block:: html

    <p>El URL es <span tal:replace="request/URL">
       http://www.example.com</span>.</p>

Repetición de estructuras
=========================

Repeat nos permite repetir una etiqueta, de manera similar a un ciclo for:

.. code-block:: html

    <table border="1" width="100%">
      <tr>
          <th>Id</th>
          <th>Meta-Type</th>
          <th>Título</th>
      </tr>
      <tr tal:repeat="item context/objectValues">
          <td tal:content="item/getId">Id</td>
          <td tal:content="item/meta_type">Meta-Type</td>
          <td tal:content="item/title">Título</td>
      </tr>
    </table>

Etiquetas condicionales
=======================

Condition nos permite evaluar una condición y mostrar o no un tag dependiendo
de si es falsa o verdadera:

.. code-block:: html

    <table tal:condition="python: context.objectValues(['Folder'])"
           border="1" width="100%">
      <tr>
          <th>Id</th>
          <th>Meta-Type</th>
          <th>Título</th>
      </tr>
      <tr tal:repeat="item python: context.objectValues(['Folder'])">
          <td tal:content="item/getId">Id</td>
          <td tal:content="item/meta_type">Meta-Type</td>
          <td tal:content="item/title">Título</td>
      </tr>
    </table>

Cambio de atributos
===================

En ocasiones no es el texto dentro de la etiqueta lo que queremos cambiar,
sino uno de los atributos de la misma:

.. code-block:: html

    <td><img src="/misc_/OFSP/File_icon.gif"
             tal:attributes="src item/icon" />
       <span tal:replace="item/meta_type">Meta-Type</span></td>

Macros
======

Para reutilización de templates:

* Definen una parte de la página que puede ser usada en otros templates.
* Permiten insertar elementos dinámicos dentro de los macros.
* Utilizados ampliamente por Plone.

Definición de un macro
----------------------

* Se definen utilizando atributos, en un lenguaje llamado METAL (Macro
  Expansion Tag Attribute Language).
* Puden definirse varios dentro de un template, dentro de cualquier etiqueta.
* Se almacenan dentro del atibuto 'macros' de la página:

.. code-block:: html

    <p metal:define-macro="copyright">
       Copyright 2007, <em>Biblioteca del Congreso Nacional de Chile</em> Inc.
    </p>

Uso de un macro
---------------

* El atributo use-macro se incluye dentro de cualquier etiqueta de HTML con el
  macro apropiado.
* La etiqueta donde se incluye es completamente reemplazada por el código del
  macro.
* El macro se identifica con una expresión de tipo path:

.. code-block:: html

      <b metal:use-macro="container/master_page/macros/copyright">
         Aquí va el macro
      </b>

Slots
=====

Los slots definen espacios que pueden llenarse dinámicamente dentro de un
template:

.. code-block:: html

    <div metal:define-macro="sidebar">
       <div metal:define-slot="links">
       Links
       <ul>
         <li><a href="http://www.bcn.cl/lc/tinterna/index_html">Tratados
             Internacionales</a></li>
         <li><a href="http://www.bcn.cl/siit/">Información Territorial</a></li>
         <li><a href="http://www.bcn.cl/bcn_legislativa/index_html">
             Boletín Legislativo</a></li>
         <span metal:define-slot="additional_links"></span>
      </ul>
      </div>
      <span metal:define-slot="additional_info"></span>
    </div>

Utilización de slots
--------------------

.. code-block:: html

    <span metal:use-macro="container/master_page/macros/sidebar">
      <p metal:fill-slot="additional_links">
        <li><a href="http://asiapacifico.bcn.cl/">Portal Asia-Pacífico</a></li>
      </p>
      <p metal:fill-slot="additional_info">
        Gracias por visitar nuestro sitio web.
      </p>
    </span>

Combinación de METAL y TAL
==========================

ZPT evalúa primero los macros y después cualquier expresión dentro de ellos.

.. code-block:: html

    <ul metal:define-macro="links"
        tal:repeat="link context/getLinks">
      <li>
        <a href="url del link"
            tal:attributes="href link/url"
            tal:content="link/name">nombre del link</a>
      </li>
    </ul>

Macros de página completa
-------------------------

.. code-block:: html

    <html metal:define-macro="page">
      <head>
        <title>BCN: <span tal:replace="context/title">Título</span></title>
      </head>
      <body>
        <h1 metal:define-slot="headline"
             tal:content="context/title">título</h1>
        <p metal:define-slot="body">
           Cuerpo del documento.
        </p>
        <span metal:define-slot="footer">
           <p>Copyright 2007 Biblioteca del Congreso Nacional de Chile</p>
        </span>
      </body>
    </html>


Referencias
===========

-   `Zope Page Templates`_ desde la comunidad Plone Mexico.

.. _Zope Page Templates: http://www.plone.mx/docs/zpt.html
