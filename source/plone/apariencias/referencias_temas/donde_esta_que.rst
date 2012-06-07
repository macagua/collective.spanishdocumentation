.. -*- coding: utf-8 -*-

.. _8_seccion:

8. ¿Dónde está qué?
===================

Cómo localizar las partes y piezas que usted necesita. Enlaces a ayudas
visuales útiles para la identificación de elementos de página, referencias a
la localización de su producto y directorios de huevos, diagramas de un huevo
de tema en el sistema de archivos.


8.1. ¿Dónde está qué en una página?
===================================

¿Cómo puede localizar a los archivos relacionados a un elemento de página
individual?

En este momento (de escribir esto), no hay una varita mágica incorporada para
apuntar a un elemento en una página Web de Plone y saber exactamente que
plantillas y código están involucrados en su creación. No obstante puede que
la haya pronto, y los aventureros gustarían de explorar `Weblion's Gloworm tool`_.

Si no está listo para una aventura todavía, entonces hay una serie de buenos
tutoriales disponibles con diagramas y guías para dónde está qué.


Comprendiendo cómo CSS traza mapas a la página
----------------------------------------------

El proyecto Weblion tiene una página Wiki excelente para ayudarle con esto

-   `https://weblion.psu.edu/trac/weblion/wiki/PloneThreeWhereIsWhat`_

Firebug (producto adicional para Firefox), obviamente, es una herramienta
esencial para la inspección de código y CSS de una página.

-   `http://www.getfirebug.com/`_


Elementos de página
--------------------

Los elementos de página son constantemente mencionados en Plone, así que una
vez que conozca el nombre de un área de página, usted está en buen camino
para localizar los archivos relevantes.

-   usted puede encontrar una clave visual para elementos de página en la
    sección Elementos de este manual
-   también encontrará un excelente resumen en el tutorial 
    `What Controls What You See (¿Qué controla lo que se ve?)`_ en Plone.org
-   y un mapeo de los administradores de viewlet y portlet en `Weblion wiki`_


8.2. ¿Dónde está mi Instancia Zope?
===================================

La ubicación de su instancia Zope depende del instalador de Plone o el
proceso de instalación que haya utilizado.


De Plone 3.1.2 en adelante
--------------------------

Buildout  En una instalación basada en Buildout, no tiene que preocuparse
mucho acerca de su instancia Zope. Si realmente quiere investigar encontrará
su instancia en [your buildout]/parts/instance. Sin embargo la mayoría de los
detalles clave (sus productos Plone, productos de terceros , y Data.fs) no se
alojan allá. Todos ellos están reunidos de varias partes de su sistema de
archivos por el archivo zope.conf que se genera cuando ejecuta Buildout.

Plone 3.1.1 o anteriores
------------------------

Instalador de Plone Los instaladores de Plone (aparte del Instalador
Universal de Plone 3.1 Universal) suele situar un directorio de instancia
Zope junto a los directorios de software Zope y Python. Así que por ejemplo,
una instalación estándar de Windows, localiza la instancia de Zope en
c:\Program Files\Plone 3\Data. En una Mac, llamará "instance" y probablemente
será ubicada en una carpeta Plone en la carpeta de aplicaciones.
Sin embargo el instalador Universal de Plone 3.1, le dará una instalación
basada en Buildout. Paquete de producto Plone Si ha instalado Zope usted
mismo, se le habrá pedido crear (por terminal) una instancia Zope, por lo que
debe tener una buena idea de dónde está en el sistema.


8.3. ¿Dónde está mi directorio de productos?
============================================

Cómo localizar su directorio de productos. Esto varia de acuerdo al
instalador de Plone o el proceso de instalación que haya utilizado.

El directorio de productos es donde los productos 2.5 de viejo estilo se
ubican. Para encontrar este, primero tendrá que saber dónde está su instancia
Zope o su Buildout.

Para fines de creación de temas, la razón principal para tener que buscar el
directorio de productos es para localizar los archivos de Plone Default - ya
que partes de Plone todavía siguen en el formulario viejo-estilo de
productos.


De Plone 3.1.2 en adelante
--------------------------

En una instalación basada en Buildout, usted encontrará los productos en
varios directorios.Productos en el Core de Plone (tal como CMFPlone) Para
estos, revise


-   [su buildout]/parts/plone.

Productos que descargé usted mismo Estos deberían estar en


-   [su buildout]/products.

If you find you haven't got a products directory there, then it is OK to
create one yourself.  Productos que le pidió a Buildout que descargara Si le
pidió buildout a Buildout que buscara algunos productos viejo-estilo,
entonces estos se ubicaran en


-   [su buildout]/parts/[nombre de directorio].

(Buildout también creará el directorio y lo llamará algo así como
"productdistros").

Plone 3.1.1 o anteriores
------------------------

Instalador de Plone y paquete de producto Plone  debería ser fácil de
localizar todos los productos (aquellos que pertenecen a la instalación de
núcleo de Plone y aquellos que se han descargado) en

-   [su instancia zope]/products

Sin embargo, si usted utiliza el Instalador Universal de Plone 3.1 su
instalación será basada en Buildout.

.. _84_seccion:

8.4. ¿Dónde se encuentra mi locación de Huevo?
==============================================

Es lo suficientemente fácil para Zope encontrar los huevos, más difícil para
humanos.


De Plone 3.1.2 en adelante
--------------------------

Productos Core (núcleo) de Plone Default Para los productos de núcleo
utilizados en el tema Plone Default, buildout tiene un directorio de huevos

-   [su buildout]/eggs

que es donde los huevos se ubican automáticamente cuando se instala Plone. Su
propio producto de tema Debido a que su propio producto de tema estará bajo
desarrollo, esto estará en un lugar distinto en su Buildout

-   [su buildout]/[zinstance|zeocluster|]/src

(Tenga en cuenta que para compartir huevos entre Buildouts puede especificar
una ubicación diferente para esto en un archivo buildout por defecto, revise
`buildout tutorial en plone.org`_ para más información).


Usando Omelette para obtener sus huevos rápidamente.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Es más o menos una navegación de arrastre a través de todos los huevos usados
por Plone. La receta de Omelette por David Glick crea una estructura de
directorio unificado de todos los paquetes de espacio de nombres, realizando
enlaces simbólicos a los contenidos, a través de Buildout. Instrucciones
completas y documentación sobre esto se puede encontrar aquí:

`http://pypi.python.org/pypi/collective.recipe.omelette`_

Una vez que haya ejecutado nuevamente Buildout con la receta de omelette, se
dará cuenta que tiene una nueva sección aquí:

-   [su buildout]/[zinstance|zeocluster]/parts/omelette

y huevos tales como plone.app.layout se pueden encontrar aquí:

-   [su buildout]/[zinstance|zeocluster]/parts/omelette/plone/app/layout


Plone 3.1.1 o anteriores
------------------------

Instalador de Plone Si ha instalado Plone con un instalador, entonces los
huevos probablemente se habrán situado en


-   [su instalación plone]/Python/Lib/site-packages.

Sin embargo, si usted utiliza el Instalador Universal de Plone 3.1 su
instalación será basada en Buildout. El paquete de producto Plone Si ha
utilizado el paquete de producto (es decir, instalado desde el código
fuente), entonces es muy posible encontrarlos en

-   [su instancia zope]/lib/python.


8.5. Ubicación de archivos en su propio producto de tema
========================================================

El huevo creado para usted por la plantilla paster de plone3_theme debe tener
un diseño de sistema de archivos muy similar a este diagrama.

Si el diagrama no funciona, consulte las siguientes páginas donde las
secciones del diagrama están combinadas con una explicación textual.

.. image:: ./your_theme_egg.gif
  :alt: su huevo de tema

8.6. Archivos para el skin
==========================

Estos archivos y directorios serán relevantes cuando se trabaja en la parte
del skin de su tema.

.. glossary ::

  /skins/[su espacio de nombre de tema].

    [su espacio de tema]_custom_templates | custom_images | styles 
    Estos directorios formarán las capas de skins. Sus plantillas, imágenes, 
    y hojas de estilo pueden ir aquí. Si usted pidió por esto, la plantilla de 
    pegado plone3_theme proveerá una hoja de estilo en blanco para sustituir 
    los por defecto de Plone. 

  /skins.zcml 
    Cuando la instancia de Zope arranca, esto convierte sus directorios en 
    las capas de skin. 

  /profiles/default/skins.xml | cssregistry.xml | jsregistry.xml 
    Cuando su tema está instalado en el sitio Plone, este configura la 
    jerarquía de las capas de skin, y registra sus hojas de estilo y JavaScript 
    con los registros

.. image:: ./your_theme_egg_skin.gif
  :alt: su huevo de tema; archivos del skin

8.7. Archivos para componentes
==============================

Estos archivos y directorios serán relevantes cuando se trabaja en la parte
de Componentes de su tema.

.. glossary ::

  /browser/viewlet.py | viewlet.pt 
    Un ejemplo de un componente viewlet

  /browser/interfaces.py
    Esto se utiliza para crear su interfaz de tema (y cualquier otra interfaz 
    que pueda necesitar)

  /profiles/default/viewlets.xml
    Utilice este archivo para ordenar sus viewlets dentro de los administradores 
    de viewlets /browser/configure.zcml 
    
    Utilice este archivo para conectar los componentes 

  /browser/templates | styles 
    Estos directorios pueden usarse para plantillas, estilos, e imágenes. Usted 
    tendrá que registrar estos como directorios para recursos en configure.zcml.


.. image:: ./your_theme_egg_components.gif
  :alt: su huevo de tema; archivos de componentes

8.8. Archivos para configuración
=================================

Estos archivos y directorios serán relevantes cuando se trabaja en la parte
de Configuración de su tema.

.. glossary ::

  /profiles/default/
    Este directorio contiene el código XML para Generic Setup.
    La plantilla paster plone3_theme le proporcionará algunos archivos ya hechos;
    para definir sus capas de skin, registrar sus hojas de estilo y JavaScript, y
    ordenar los viewlets.

  /profiles.zcml
    Cuando la instancia de Zope inicia, este archivo hace que el
    perfil esté disponible para el uso de Generic Setup.

.. image:: ./your_theme_egg_config.gif
  :alt: su huevo de tema; archivos de configuración

8.9. Archivos para la instalación de su huevo
==============================================

Estos son los archivos y directorios necesarios para instalar el huevo en la
ruta de python y ponerlo a disposición en el arranque de Zope.

.. image:: ./your_theme_egg_egg_installation.gif
  :alt: su huevo de tema; archivos utilizados para la instalación de su huevo

8.10. Archivos para la instalación de su tema
==============================================

Estos son los archivos que se usan cuando se instala el producto de tema
mediante :menuselection:`Configuración del sitio --> Agregar/Quitar productos` o 
:menuselection:`Interfaz de Administración de Zope --> portal_quickinstaller`

.. glossary ::

  /profiles/default/
    Generic Setup instalará su perfil de tema cuando su tema
    se haya instalado. import_steps.xml apunta a un "controlador" para pasos de
    instalación los cuales no son parte aún de Generic Setup o no pueden ser
    expresados como XML.

  /setuphandlers.py
    Esto contiene el "controlador" para pasos no genéricos de la instalación Generic Setup

.. image:: ./your_theme_egg_qi_installation.gif
  :alt: su huevo de tema; archivos utilizados por el quick installer


.. _Weblion's Gloworm tool: http://weblion.psu.edu/blog/esteele/gloworm-0-1-alpha1-now-available
.. _https://weblion.psu.edu/trac/weblion/wiki/PloneThreeWhereIsWhat: https://weblion.psu.edu/trac/weblion/wiki/PloneThreeWhereIsWhat
.. _Weblion wiki: https://weblion.psu.edu/trac/weblion/wiki/PloneThreeWhereIsWhat
.. _http://www.getfirebug.com/: http://www.getfirebug.com/
.. _What Controls What You See (¿Qué controla lo que se ve?): http://plone.org/documentation/tutorial/where-is-what/introduction
.. _buildout tutorial en plone.org: http://plone.org/documentation/tutorial/buildout/creating-a-buildout-defaults-file
.. _http://pypi.python.org/pypi/collective.recipe.omelette: http://pypi.python.org/pypi/collective.recipe.omelette
.. _http://plone.org/products/collective.xdv/documentation: http://plone.org/products/collective.xdv/documentation
