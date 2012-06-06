.. -*- coding: utf-8 -*-

.. highlight:: rest

.. _deliverance_introduccion:

===================
Descripción general
===================

`Deliverance`_, es una herramienta para hacer temas de aplicaciones Web la cual 
reescribe `HTML`_ usando selectores `CSS`_ (hojas de estilo en cascada) basado 
en un conjunto de reglas. El único requerimiento es que el diseño Web estático 
y que la aplicación Web ofrezcan soporte ``HTML`` y selectores "ID" ``CSS`` en 
el código fuente.

Funcionamiento
==============

``Deliverance`` hace transformaciones `HTML`_ para diseños estáticos de páginas Web, 
similar en funcionamiento a la `XSLT`_ pero usando un simple lenguaje basado en XML 
para expresar la transformación. Esta coloca porciones o secciones del código ``HTML`` 
generado por la fuente de datos aquí se llamará **contenido** dentro las secciones del 
código de los diseños estáticos de páginas Web aquí llamado **tema** el cual sirven de 
contenedor para emplazar la HTML generado, por ejemplo se pueden añadir desde estructuras 
de navegación, hojas de estilo desde el **contenido** al **tema**, entre otros. 

A diferencia de los típicos sistemas de plantillas Web, los cuales implementan una 
combinación de técnicas y tecnologías estáticas (HTML(CSS/Javascript) con estructuras 
de programación dinámicos (``ASP``, ``JSP``, ``PHP``, ``Python``, entre otros en cuestión) 
Deliverance le evita no usar ninguna variable de servidor / estructuras de programación 
para sustituir. Solo se necesitan definir un conjunto simple de reglas que se aplican 
en el código ``HTML``.


Componentes de Deliverance
==========================

.. glossary::

   Contenidos
      Es la información a la que quiere aplicar un estilo a través del tema. Este puede ser un 
      sitio Web dinámico o un archivo estático, especificado a  través de una dirección ``URL`` 
      por medio de reglas de `reescritura direcciones URL`_ y `proxy inverso`_.

   Tema
      Este contiene los estilos e información de diagramación/presentación de contenidos que se 
      quiere aplicar al contenido. Este puede ser un sitio Web dinámico o un archivo estático, 
      especificado a través de una dirección ``URL``. El **tema** en si es una pagina ``HTML`` 
      con poco código en ella. Es simplemente un ejemplo de lo que debería ser la pagina, lo que 
      lo hace accesible a los diseñadores o a cualquier tipo de herramienta e incluso se pueden 
      generar de forma dinámica.

   Reglas
      Las reglas especifican al servicio de ``Deliverance`` como aplicar el tema al contenido. 
      Hay 4 tipos de reglas: `replace`_ , `append, prepend`_ y `drop`_ (reemplazar, agregar, 
      anteponer y quitar). Las reglas son especificadas en un documento `XML`_.

Los atributos en cada regla contienen identificadores `CSS`_ o expresiones `XPath`_ que describen 
secciones en el tema y contenido en la cual ejecutara la regla.

¿Por que Deliverance?
=====================
- Muchas veces el diseño Web ya existe dentro de la organización.
- Mantiene la separación entre la presentación y el contenido.
- Rendimiento y flexibilidad.
- Porque permite trabajar sin un lenguaje de programación (para usuarios no-programadores).
- Debido a su concepto puede ser usado por diseñadores, integradores, desarrolladores, usuarios.

Conocimiento necesario
======================
Es recomendable poseer conocimiento en las siguientes conceptos/tecnologías/herramientas: 

* Lenguaje de marcado de Hipertexto ``HTML``.
* Lenguaje de estilos en Cascada ``CSS``.
* La extensión del navegador Web Mozilla Firefox llamada ``Firebug``.
* Uso de un editor simple de archivos ``XML``.

Beneficios
==========
- Los diseñadores Web no necesitan aprender el sistema manejador de contenidos ``CMS``, 
el ``Framework`` o sistema de temas de un sitio/aplicación Web.

- Se puede unificar el diseño de múltiples aplicaciones Web con un diseño unificado 
aplicado a wikis, blogs, contenido estático ``HTML``, entre otros.

.. note::

    Una explicación detallada sobre esta tecnología la puedes encontrar en la conferencia 
    dictada en la Plone Conference 2010 llamada: `Easier and faster Plone theming with 
    Deliverance and xdv`_ por `Nate Aune`_ de la empresa Jazkarta.
    
   .. figure::  Ploneconf2010-PloneConf_MARLBOROUGH_DAY1_SESSION3Recording1Computer226-129.jpg
      :align:   center

      Conferencia Easier and faster Plone theming with Deliverance and xdv por `Nate Aune`_.

.. _Deliverance: http://pypi.python.org/pypi/Deliverance
.. _XSLT: http://es.wikipedia.org/wiki/XSLT
.. _HTML: http://es.wikipedia.org/wiki/HTML
.. _CSS: http://es.wikipedia.org/wiki/Hojas_de_estilo_en_cascada
.. _proxy inverso: http://es.wikipedia.org/wiki/Proxy#Reverse_Proxy_.2F_Proxy_inverso
.. _reescritura direcciones URL: http://plone-spanish-docs.readthedocs.org/en/latest/zope/zope-plone-detras-servidor-web.html#terminologia-general
.. _replace: http://packages.python.org/Deliverance/rules.html#behavior-replace
.. _append, prepend: http://packages.python.org/Deliverance/rules.html#behavior-append-prepend
.. _drop: http://packages.python.org/Deliverance/rules.html#behavior-drop
.. _XML: http://es.wikipedia.org/wiki/Extensible_Markup_Language
.. _XPath: http://es.wikipedia.org/wiki/XPath
.. _Easier and faster Plone theming with Deliverance and xdv: http://ploneconference2010.blip.tv/file/4314435/
.. _Nate Aune: http://twitter.com/natea
