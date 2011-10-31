.. -*- coding: utf-8 -*-

==========================================
Importar y exportar contenido desde el ZMI
==========================================

El servidor de aplicaciones Zope ofrece copia las partes de la estructura de árbol a través de
de importación / exportación. Archivo exportado es básicamente un pickle Python que contiene
el nodo seleccionado y todos los nodos secundarios.

Los archivos .zexp importables debe ser colocado en el directorio ``/parts/instance/import`` 
de su carpeta buildout en el servidor. Si está utilizando ZEO cluster definido, siempre se ejecutan
las importaciones a través de un específico front-end de instancia, utilizando el acceso directo al puerto.
Tenga en cuenta que las estructura de carpetas ``parts`` se poda en cada ejecución buildout.

Cuando los archivos se colocan en el servidor en la carpeta correcta, la pestaña Import/Export 
ZMI los recogerá en la selección de hacia abajo. No es necesario reiniciar Zope.

Más información
===============

-   `http://quintagroup.com/services/support/tutorials/import-export-plone/`_

.. _http://quintagroup.com/services/support/tutorials/import-export-plone/: http://quintagroup.com/services/support/tutorials/import-export-plone/
