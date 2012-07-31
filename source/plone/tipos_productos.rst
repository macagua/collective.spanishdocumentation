.. -*- coding: utf-8 -*-

.. _desarrollar_productos:

==========================================
Desarrollar diversos productos con Plone 3
==========================================

:Autor(es): Carlos de la Guardia, Leonardo J. Caballero G.
:Correo(s): carlos.delaguardia@gmail.com, leonardocaballero@gmail.com
:Lanzamiento: |version|
:Fecha: |today|

En esta articulo busca explicar los tipos desarrollos de productos / módulos 
disponibles para Plone 3.

Introducción
============

Un sitio basado en Plone es muy complejo y se compone de una colección de
elementos como contenido, configuración y recursos de presentación. La
tendencia en Plone 3 es separar lo más posible todas estas áreas, para
permitir un desarrollo organizado y estructurado. La base de datos de Zope,
ZODB, debe en lo posible almacenar únicamente el contenido generado por los
usuarios. Todo el código y configuración del sitio deben estar en el
filesystem, de manera que puedan editarse y versionarse con las herramientas
comunes de desarrollo y no queden encerrados en la ZODB. Esto también permite
una distribución e instalación más sencillas.

Tipos de productos
==================

La estructura del código que se recomienda incluye las siguientes partes:

.. glossary::

  Producto de configuración (policy product)
    Incluye toda la configuración general del sitio. Representa las reglas
    generales de manejo de sitios Plone de una organización y puede incluir:

      * Configuraciones del sitio y propiedades de navegación.
      * Productos propios y de terceros que deben instalarse automáticamente
        con el sitio.
      * Configuraciones de viewlets.
      * Estructura inicial de contenido del sitio.
      * Pasos adicionales a la instalación del producto, como creación de
        cuentas de usuarios y contenido personalizado.
      * Portlets utilizados en el sitio.
      * Flujo de trabajos generales de la organización.
      
    Para crear este producto consulte el articulo :ref:`Creación de un producto de configuración <producto_policy>`.

  Producto de tema (plone theme)
    Incluye uno o más productos que definan un "skin" de Plone que especifique
    la presentación visual del sitio. Cada uno puede incluir:

      * Estilos de CSS.
      * Archivos de Javascript.
      * Archivos de Imágenes.
      * Plantillas de Plone modificados.
      * Plantillas originales del tema.
      * Vistas y viewlets especiales.
      
    Para crear este producto consulte el articulo :ref:`Creación de un paquete de tema <producto_tema>`.

  Productos de contenido (content types)
    Uno o varios productos que definen los tipos de contenido que representan
    la base del sitio web.

      * Definición de tipos y campos.
      * Flujo de trabajos específicos para un tipo de contenido.
      * Vistas y viewlets especiales para un tipo de contenido.
      * Imágenes y estilos propios del contenido.
      * Portlets propios del contenido.
      * Índices y metadatos del catálogo para cada tipo utilizado.

  Productos de apoyo
    Uno o varios productos que realicen funciones no específicamente
    asociadas al contenido.

      * Utilerías (herramientas tipo *portal_xxx*).
      * Portlets generales.
      * Vistas y viewlets especiales.
      * Funcionalidades que extiendan Plone.


Referencia
==========

- `Desarrollo avanzado de sitios con Plone 3`_ desde la comunidad Plone Mexico.

.. _Desarrollo avanzado de sitios con Plone 3: http://www.plone.mx/docs/productos.html

