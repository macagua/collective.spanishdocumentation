.. -*- coding: utf-8 -*-

.. _1_seccion:

Introducción
============

Objetivos, prerrequisitos, visión general del manual y una definición rápida
de lo que es un tema de Plone.


Objetivos y Prerrequisitos
---------------------------

El objetivo de este manual es presentarle una vista general de la teoría,
herramientas, y técnicas utilizadas en la personalización de la apariencia de
Plone o la creación de su propio tema.


Objetivos
.........

No lea este manual de principio a fin. Véalo como una guía o un libro de
frases que le ayudaran a orientarse en el complejo mundo de temas de Plone.

Le presentaremos la teoría, pero realmente no hay substituto para la
práctica; así que le señalaremos varias tutoriales excelentes, libros, y
recursos encontrados en este sitio y otras locaciones, las cuales le guiarán
a través de los distintos aspectos de temas de Plone 3. Nosotros apuntamos a
complementar esos recursos llenando los vacíos, proporcionando una visión
general breve de la teoría, colocando las cosas en contexto, y dando un
referencia rápida de esos detalles que son confusos o que no puede recordar
desde la última vez que utilizó algún elemento.


Prerrequisitos
..............

Este manual está escrito para integradores y personas encargadas de la
personalización, y no asumimos todas las experiencias de desarrollo. Sin
embargo sí imaginamos que tiene experiencia con XHTML y CCS, conoce algo de
XML, y tiene algún conocimiento respecto a lenguajes scripting. Trabajamos de
la premisa que usted no tiene experiencia con Plone, no obstante, si está
familiarizado con Plone 2, descubrirá un par de cosas nuevas.

será de ayuda si usted al instalar Plone le echó un vistazo a los directorios
de instalaciones en su sistema de archivos. De la misma manera es útil haber
investigado las opciones en el enlace de Configuración del sitio de su sitio
web, y navegado por la Zope Management Interface (Interfaz de Administración
de Zope) para una ojeada en el tras bambalinas.


¿Qué es un tema Plone?
-----------------------

Breve descripción de lo que estamos hablando.

Un tema es una colección de plantillas de páginas, hojas de estilo,
componentes, y opciones de configuración que crean la apariencia y diseño
personalizado de su sitio Plone.

Plone le proporciona la opción de incrustar sus cambios de tema y adicionales
en un sólo sitio trabajando a través de la web. O mediante la alternativa de
crear paquetes de sus temas dentro de su propio producto, para que pueda
instalarlo de desinstalarlo, como también aplicarlo a varios sitios. Ambos
caminos tienen su pros y contras, y este manual los recorre en secciones
presentadas más adelante.

Plone 3 viene con dos temas:

-   un tema listo e incorporado - predeterminado de Plone
-   y un sustituto adicional - NuPlone.


En Plone 4 las cosas son algo distintas:

-   Dos temas disponibles -  Plone Classic y Sunburst (este último es el
    predeterminado de Plone cuando se instala por primera vez)
-   Plone Default sigue existiendo como el cimiento en el que Plone
    Classic y Sunburst están construidos y debería ser una base provechosa
    para cualquier producto de tema.
-   NuPlone se ha removido pero sigue estando disponible para su descarga
    si es necesario.

Si se siente escéptico o tiene dudas de lo que se puede lograr, revise la
riqueza de los distintos sitios mostrados en `plone.net`_ o los temas
descargables disponibles en la `Products section`_ (Sección de productos) de
este sitio.

Si usted ya posee un tema de Plone 3 y desea actualizarlo para que trabaje
con Plone 4, pues la `guía de actualización`_ tiene más información y
orientación.


Resumen
--------

Esta es una vista rápida de lo temas de este manual.

.. image: ./image_mini.png
  :width: 200px
  :alt: Mapa conceptual del Manual de referencia
  :align: center

  Mapa conceptual de este manual, haga clic para agrandar

.. glossary::

  Sección 1: Introducción
    Un tema es una apariencia de diseño distinta para
    Plone, la cual es estructuralmente basada en el tema por defecto de Plone.

  Sección 2: Enfoques 
    ¿Cual es la manera de aproximarse? ¿Cuales son los pros y
    contras de trabajar a través de la web o por el sistema de archivos?

  Sección 3: Herramientas 
    ¿Qué herramientas se necesitan y que está disponible para ayudarle a 
    construir su tema? 

  Sección 4: Bloques para Construcción 
    Existen tres "bloques para construcción" 
    principales en un tema de Plone 3. Si bien hay algunos solapamientos
    entre ellos, en general, ayuda a verlos como entidades separadas.

      - skin
      - componentes
      - configuración

    Esta sección provee una vista general de

      - la terminología relacionada a cada uno de estos bloques para
        construcción
      - los lenguajes necesarios para trabajar con cada una de ellas
      - las técnicas y enfoques requeridos para personalizar estos bloques
        para construcción o la creación de nuevos.
      - ¿cómo puede encontrar los archivos que necesita?

  Sección 5: armar una página 
    ¿Cómo se arregla y se junta todo para crear una página? Observaremos

      - la construcción de una página
      - ¿cómo el contenido llega a la página?
      - ¿cómo las hojas de estilo y JavaScript se agregan a la página?
      - ¿cómo puede obtener información adicional de su sitio?

  Sección 6: Referencia de Elementos 
    Breve referencia a los elementos de páginas y resumen de como hacer 
    frente a la personalización y creación de componentes. 

  Sección 7: ¿Dónde está qué? 
    A menudo es difícil identificar la ubicación de los archivos que necesita. 
    Esta sección le ofrece una referencia rápida del esquema de archivos de 
    un producto de tema. También hay algunos consejos para otros diagramas 
    en la web, los cuales le ayudan a hacer un mapa de los elementos de 
    contenido de página para componentes, plantillas y estilos.


.. _plone.net: http://plone.net/
.. _Products section: http://plone.org/documentation/products
.. _guía de actualización: http://plone.org/documentation/manual/upgrade-guide
