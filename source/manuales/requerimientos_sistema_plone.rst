.. -*- coding: utf-8 -*-

.. highlight:: rest

.. _requerimientos_sistema:

­­Requerimientos de sistema de Plone
==================================

:Traductor(es): Leonardo J. Caballero G.
:Correo(s): leonardocaballero@gmail.com
:Lanzamiento: |version|
:Fecha: |today|

En esta es una traducción del articulo llamado `Plone system requirements`_.

­Este documento busca definir que tipo de requerimientos de ejecución 
de una instalación Plone necesita tanto en hardware y sistema operativo.


Requisitos instalar Plone
-------------------------

Para ejecutar un sitio Web basado en Plone usted necesita:


1.  Un computador en modo servidor conectado a Internet (para sitios
    públicos) o en intranet (para sitios corporativos).
2.  Acceso a consola de comando para instalar Plone (acceso por FTP, no
    es suficiente).
3.  Habilidad de ejecutar en procesos como un servicio en el servidor de
    hospedaje.
4.  Habilidad para abrir puertos arbitrariamente. Zope quiere abrir su
    propio puerto para recibir solicitudes.

Los proveedores de hospedaje de gama baja no le ofrecen por lo general las
opciones número 3 ni número 4. Usted necesita tener proveedor de hospedaje
específico para Plone o un servidor dedicado con acceso administrativo
exclusivo.

-   Para servidores privados virtuales baratos con acceso root ver 
    http://www.lowendbox.com - Los precios comienzan tan bajo como 7 USD / mes.

-   Si no desea mantener su propio servidor y necesitas una solución de un 
    "solo clic" en nube consulte el servicio Ploud http://www.ploud.com

Requisitos del sistema operativo
--------------------------------

-   MS Windows XP o superior.
-   Apple OSX 10.4.x o superior.
-   GNU/Linux 2.6.x o superior.
-   Python 2.6 (opcionalmente Python 2.7, para Plone 4.2 y superior).

Plone requiere tener las herramientas de desarrollo (como el compilador GCC) 
y otros dependencias para Mac OS X y GNU/Linux instalado previamente para 
instalar Plone. Estas incluyen las siguientes:

-   libjpeg
-   readline
-   zlib
-   libbz2
-   libxslt
-   libxml2
-   librería de desarrollo python

Se recomienda utilizar el administrador de paquetes de su sistema para implementar 
estas dependencias. Si necesita más instrucciones para instalar estos paquetes 
favor de referencia: :ref:`Instalación de Plone <instalando_plone>`.

.. note::
    Plone requiere Python 2.6 o 2.7. Las herramientas de Desarrollo son requerida para Linux (GCC).

Requisitos del Hardware
-----------------------

Los requerimientos de Hardware a continuación dar una estimación aproximada
de qué tipo de configuración mínimas de Hardware se necesita para un servidor
de Plone.

Los productos adicionales y soluciones de caching puede incrementar los
requerimientos de memoria RAM.

Un servidor de aplicación Zope esta disponible para ejecutar muchos sitios
Plone con la misma configuración de Software. Esto baja los requerimientos
cuando hospedas múltiples sitios en el mismo servidor.


Requisitos mínimos de hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   Mínimo 256 MB RAM y 512 MB de memoria de intercambio por cada sitio
    de Plone.
-   Mínimo 512 MB de espacio de disco duro.


Hardware recomendado
~~~~~~~~~~~~~~~~~~~~

-   512 MB o más RAM por cada sitio Plone.
-   2 GB o más de espacio de disco duro.

.. note::
    Plone `escala`_ fácilmente. Si está desarrollando un sitio de alto tráfico, 
    su plan de infraestructura para aprovechar sus tecnologías clave, tales 
    como el `servidor ZEO`_ y otras estrategias, incluyendo balanceo de carga 
    y almacenamiento en caché.


Soluciones de hospedaje
-----------------------

Por favor, consulte con fines comerciales el sitio `plone.net`_ para buscar
proveedores de hospedaje o elija cualquier solución de servidor o maquina
virtual de hospedaje cumpliendo con los requerimientos de hardware.

Referencias
-----------

-   `Requerimientos de sistema de Plone`_ desde la comunidad de Plone Venezuela.
-   `Plone system requirements`_.

.. _Requerimientos de sistema de Plone: http://www.coactivate.org/projects/ploneve/~xad~xadrequerimientos-de-sistema-de-plone
.. _plone.net: http://plone.net/hosting-providers
.. _Plone system requirements: http://plone.org/documentation/kb/plone-system-requirements
.. _Hosting providers from plone.net website: http://plone.org/support/hosting-providers
.. _escala: http://plone.org/documentation/faq/scalability
.. _servidor ZEO: http://plone.org/documentation/glossary/zeo-server
