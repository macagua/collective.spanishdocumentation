.. -*- coding: utf-8 -*-

*****************************************
Desarrollo avanzado de sitios con Plone 3
*****************************************

Un sitio basado en Plone es muy complejo y se compone de una colección de
elementos como contenido, configuración y recursos de presentación. La
tendencia en Plone 3 es separar lo más posible todas estas áreas, para
permitir un desarrollo organizado y estructurado. La base de datos de Zope,
ZODB, debe en lo posible almacenar únicamente el contenido generado por los
usuarios. Todo el código y configuración del sitio deben estar en el
filesystem, de manera que puedan editarse y versionarse con las herramientas
comunes de desarrollo y no queden encerrados en la ZODB. Esto también permite
una distribución e instalación más sencillas.

La estructura del código que se recomienda incluye las siguientes partes:

`Producto guía (policy product)`
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
        * Workflows generales de la organización.

`Producto de tema`
    Incluye uno o más productos que definan un "skin" de Plone que especifique
    la presentación visual del sitio. Cada uno puede incluir:

        * Estilos de CSS.
        * Javascript.
        * Imágenes.
        * Templates de Plone modificados.
        * Templates originales del tema.
        * Vistas y viewlets especiales.

`Productos de contenido`
    Uno o varios productos que definen los tipos de contenido que representan
    la base del sitio web.

        * Definición de tipos y campos.
        * Workflows específicos para un tipo de contenido.
        * Vistas y viewlets especiales para un tipo de contenido.
        * Imágenes y estilos propios del contenido.
        * Portlets propios del contenido.
        * Índices y metadatos del catálogo para cada tipo utilizado.

`Productos de apoyo`
    Uno o varios productos que realicen funciones no específicamente
    asociadas al contenido.

        * Utilerías (herramientas tipo portal_xxx).
        * Portlets generales.
        * Vistas y viewlets especiales.
        * Funcionalidades que extiendan Plone.

