.. -*- coding: utf-8 -*-

.. _6_seccion:


6. Armando una página
=====================

¿Cómo todas estas partes y piezas van de la mano para hacer una página web?
Y, más importante aún, ¿cómo se obtiene el contenido sobre la página?


6.1. Contenido a plantilla
==========================

Contenido a plantilla


6.1.1. Contenido a plantilla
============================

Cómo el contenido llega a una plantilla de página.

Hay tres caminos por el cual el contenido de sus elementos de contenido puede
llegar a una página.

-   directamente desde un elemento de contenido
-   desde el catalogo
-   vía un componente de vista (usando Python)

Obtener el contenido directamente desde un elemento de contenido
----------------------------------------------------------------

Una plantilla de página puede extraer datos directamente desde el elemento de
contenido que está visualizando. Aquí hay un fragmento de la plantilla RSS,
llamando el campo de descripción de una elemento de colección de contenido:

.. code-block:: xml

    <description>
        <metal:block define-slot="description">
           <tal:block content="*context/Description*">
              Default rss description goes here
           </tal:block>
        </metal:block>
    </description>

-   *context* se refiere al elemento actual de contenido
-   *Description* es el accessor (acceso) del campo de descripción


Accessors
~~~~~~~~~

Un accessor es simplemente el método por el cual los datos en un campo son
extraídos. En la mayoría de los casos el nombre de un accessor es el nombre
del campo con la primera letra en mayúscula y precedido por "get" (por
ejemplo, getStartTime). Hay una excepción a la regla El título y campo de
descripción, común para la mayoría de los tipos de contenido, tienen "Title"
y "Description" como los accessors (es decir, sin 'get', pero la primera
letra igual se pone en mayúscula).


Widgets
~~~~~~~

Este fragmento de la plantilla de un elemento de noticia hace exactamente lo
mismo, pero llama a un macro "widget" especifico de visualización para el
campo en lugar de sólo los datos.

.. code-block:: xml

    <p class="documentDescription">
     <metal:field use-macro="python:here.widget('description', mode='view')">
         .....
    </metal:field>
    </p>

Obteniendo contenido del catálogo
----------------------------------

Cada elemento de contenido está catalogado en la creación y edición. Algunos
de sus campos están indexados para búsqueda rápida y clasificación, mientras
que los valores de los demás se almacenan en lo que se llama el "cerebro" o
"metadatos" para rápido acceso.

páginas reuniendo un conjunto de tipos de contenido; una carpeta o colección
listando. A menudo reciben su contenido de una consulta de catálogo y
cerebro, en vez de despertar cada elemento de contenido. Normalmente
encontrará una variable definida en alguna parte que contiene los resultados
de una consulta de catálogo:

.. code-block:: python

    folderContents here.queryCatalog(contentFilter);

Luego la plantilla hará bucles a través de los resultados y los valores de
llamada desde el cerebro/metadatos:

.. code-block:: python

    item_url item/getURL;
    item_id item/getId;

Estos se parecen mucho a los accessors normales, de hecho, son los nombres de
campos en el cerebro/metadatos del catálogo. Esto puede tornarse confuso, si
usted trata de acceder a un campo que no está en el cerebro/metadatos
obtendrá un error.

Usted puede ver qué campos están disponibles para usted a través de

-   :menuselection:`Configuración del sitio --> Interfaz de Administración de Zope --> portal_catalog --> metadata tab`

Si quiere entender más del catalogo, hay una visión general útil en el `Zope book`_, 
un recorrido más específico de Plone en `The Definitive Guide to Plone`_ 
(Este libro es sólo para Plone 2, pero la sección de catálogo sigue
siendo relevante para Plone 3).


Obteniendo contenido vía Python (usando un componente de vista)
----------------------------------------------------------------

Usualmente es más eficiente usar una vista para procesar los datos desde un
elemento de contenido (o un grupo de elementos de contenido) y luego situarlo
dentro de la plantilla de página. En este caso, por view (vista) queremos
decir un componente específico definido en ZCML.

Aquí hay un fragmento que llama una vista para renderizar el sitemap (mapa
del sitio):

.. code-block:: html

    <ul id="portal-sitemap"
        class="navTreeLevel0 visualNoMarker"
        tal:define="view context/@@sitemap_view;">
         <tal:sitemap replace="structure view/createSiteMap" />
    </ul>

-   *context/@@sitemap_view* es asignado a un variable llamada
    (amablemente) "view"
-   *createSiteMap* es un método de @@sitemap_view
-   @@ indica que esto es un componente de vista

Aquí está la estructuración o conexión en ZCML que crea @@sitemap_view:

.. code-block:: xml

    <browser:page
         for="*" <!-- there's no restriction on where I can be used -->
         name="sitemap_view" <!-- this is my name -->
         class=".sitemap.SitemapView" <!-- this is where you can find the code to deliver my content -->
         permission="zope.Public" <!-- you can see me if you have the Public permission -->
         allowed_interface=".interfaces.ISitemapView"
    />

En resumen

-   El contenido es procesado por una clase Python
-   ZCML conecta esta clase en un componente
-   la plantilla llama este componente


.. _62_seccion:

6.2. Plantillas y componentes a la página
==========================================

Plantillas y componentes a la página


6.2.1. Plantillas y componentes a la página
============================================

Una visión general de cómo las plantillas, viewlets y portlets trabajan
juntos para crear una página.

Al principio las plantillas de página pueden ser un poco frustrantes.
Pareciera que no hay ni una sola plantilla que contenga todo lo que usted
necesita.


Vistas de contenido
-------------------

Ya que es probable que cada tipo de contenido tenga una combinación diferente
de campos, cada tipo de contenido requiere una plantilla independiente para
su visualización. Como hemos visto en la sección `Plantillas y el lenguaje de plantillas`_, 
estas usualmente tienen _view agregado a sus nombres. Usted
puede encontrar estos tipos de contenido estándar de Plone en

-   [su instancia zope]/Products/CMFPlone/Skins/plone_content.


main_template
-------------

Sin embargo, conocer sobre las vistas de contenido sólo lo trae hasta aquí.
Es la plantilla principal (main_template.pt) la que junta el contenido de la
página junto con la decoración y diseño. Usted puede encontrar esto en

-   [su instancia de zope]/Products/CMFPlone/skins/plone_templates.

Es importante recordar que las plantillas de vista de contenidos no son
completas en sí mismas, ella apenas proporcionan una parte de contenido
situada dentro de un "slot" ("ranura") en el main_template, llamado "main"
("principal)

Si no se siente seguro acerca de las ranuras, entonces vuelva a revisar
`Plantillas y el lenguaje de plantillas`_.

Alrededor del la ranura (slot) principal, los componentes; viewlets y
portlets entran en juego, suministrando los elementos de decoración para el
contenido. La plantilla principal simplemente trae estos a través de los
administradores de viewlets y portlets.

Los viewlets son tan flexibles que incluso pueden ser traídos a la vista de
contenido. Por ejemplo, el administrador de contenido de arriba se utiliza en
un número de vistas de contenido, y se ocupa, entre otras cosas, el viewlet
de presentación que vimos en las secciones anteriores.


Con más detalle
----------------

Puede que le resulte útil observar un ejemplo en contexto.

Eche un vistazo a:

-   Products/CMFPlone/Skins/plone_templates/main_template

y

-   Products/CMFPlone/Skins/plone_content/document_view


Acerca de document_view (una plantilla de vista de contenido)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Aunque document_view luce como una página HTML completa, ignore esto.
    Note que justo en la parte superior llama a main_template.

.. code-block:: xml

    metal:use-macro="here/main_template/macros/master"

El código que se usa desde document_view es en realidad el pedacito entre
estas etiquetas:

.. code-block:: xml

    <metal:main fill-slot="main"> ...... </metal:main>

Esto se sitúa en un slot en el the main_template:

.. code-block:: xml

    <metal:bodytext metal:define-slot="main"
                    tal:content="nothing">
    ...
    </metal:bodytext>

2. Si regresamos al fill-slot (slot-para llenar) en el document_view
    podrá ver algunas etiquetas que llaman campos relevantes desde el tipo de
    contenido, como este:

.. code-block:: xml

    <metal:field
           use-macro="python:here.widget('title', mode='view')">
    </metal:field>

También verá algunas etiquetas como llamar a los administradores viewlet que,
a su vez, convocará grupos de viewlets:

.. code-block:: xml

    <div tal:replace="structure provider:plone.abovecontentbody" />

Estos le permiten colocar piezas extra de decoración de página alrededor del
contenido específico desde los campos (ejemplo, el enlace de modo de
presentación).


Acerca de la plantilla principal (main template)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Regrese a main_template y verá llamadas similares a otros
    administradores viewlet manejando grupos de viewlets para más decoración
    de página:

    .. code-block:: xml

        <div tal:replace="structure provider:plone.portaltop" />

2. Y las llamadas a los administradores para traer los portlets definidos
    para esa página en particular:

    .. code-block:: xml

        <tal:block replace="structure provider:plone.leftcolumn" />

3. verá también un numero de slots adicionales (define-slot), los cuales
    pueden ser llenados (fill-slot) desde la plantilla de vista de contenido.
    Aquí hay una que puede utilizar para añadir un poco de css:

    .. code-block:: xml

        <metal:styleslot define-slot="style_slot" />

Regrese a su plantilla de vista de contenido y simplemente agregue un fill-
slot adicional (fuera de los fill-slot principales):

.. code-block:: xml

    <metal:mystyleslot fill-slot="style_slot">
     .....
    </metal:mystyleslot>

Revisaremos otras maneras de proporcionar estilos con más detalle en la
siguiente sección.


6.2.2. ¿Cómo mostrar el contenido completo en las vistas de carpeta sí
=======================================================================

Esta parte sólo tiene sentido para las carpetas, carpeta inteligente, u otros
puntos de vista similares con un número bastante reducido de elementos.
Muestra cómo presentar una vista completa de los contenidos en los listados
mediante el uso de macros ya definidos para los tipos de contenido. El mismo
método puede ser utilizado para definir viewlets para los productos de diseño
como compositepack.

Yo estaba buscando un producto de diseño para la portada de un sitio en el
que estoy trabajando, y los productos existentes no satisfacían mis
necesidades, ya que sólo mostraban vistas de resumen de contenido en lugar de
la vista completa. En vez de escribir viewlets para diferentes tipos de
contenido desde cero, utilicé los macros de vista existentes de los tipos de
contenido de la siguiente manera, en una nueva vista de carpeta que llamé
folder_full_view (esto es sólo un fragmento de código):

.. code-block:: xml

            <tal:listing condition="folderContents">

                    <div tal:repeat="item folderContents">
                    <tal:block tal:define="here item/getObject;
                                           actions nothing;
                                           view here/defaultView;
                                           object_title item/pretty_title_or_id"
                               tal:on-error="nothing">
                       <div metal:use-macro="here/?view/macros/main"/>
                    </tal:block>
                    </div>

            </tal:listing>

El establecimiento de acciones a "nothing" (nada) es para que los iconos de
acción no se muestren en cada elemento de contenido. El on-error="nothing"
puede que no aparezca con usted. Yo lo tengo porque permití que el catálogo
devolviera resultados para los cuales no hay permiso de Vista.

De igual manera para el producto CompositePack, yo definí un viewlet.

.. code-block:: xml

    <div class="viewlet default_view">
    <tal:block on-error="nothing"
         tal:define="here nocall: context;
                     actions nothing;
                     view here/defaultView;
                     object_title
                     here/pretty_title_or_id">
      <metal:block use-macro="context/global_defines/macros/defines" />
      <div metal:use-macro="context/?view/macros/main"/>
    </tal:block>
    </div>


para que el contenido completo se puede mostrar en un diseño.

Use estas ideas bajo su propio riesgo. Hasta ahora a mí me han funcionado.

6.2.3. ¿Cómo cambiar el tamaño de imágenes usando PiL en Plantillas de página?
==============================================================================

Una breve descripción de cómo cambiar el tamaño de imágenes (image field)
desde un campo de imagen utilizando la biblioteca de imágenes de Python en
sus Plantillas de página mediante el uso de TAL.

PROBLEMA:

Tengo un tipo personalizado con un ImageField. Estoy personalizando un
listado de carpeta de estos tipos y yo quería una vista miniatura de cada
imagen en el listado de carpetas. Esto es muy sencillo usando PiL (Python
Imaging Library - librería para imágenes en Python), si sabe qué hacer.
También se me presentó el problema de trabajar con el cerebro y no con el
objeto en sí.

SUPOSICIONES:

-   Usted tiene PiL instalado y funcionando.
-   Usted sabe cómo hacer un Arquetipo personalizado

RESUMEN:

Al obtener los contenidos de carpeta para una lista de carpeta, los objetos
de cerebro son devueltos e iterados para elaborar la lista. Esto es, por
supuesto, mucho más eficiente que despertar cada objeto. El problema es que
usted no puede ir a su campo de imagen en el cerebro (que yo sepa). El
siguiente es un fragmento de "folder_listing.pt" que muestra esto.

.. code-block:: xml

    <tal:foldercontents define="contentFilter contentFilter|request/contentFilter|nothing;
                                contentsMethod python:test(here.portal_type=='Topic',
                                here.queryCatalog, here.getFolderContents);
                                folderContents folderContents|python:contents
                                Method(contentFilter);">

        <tal:entry tal:repeat="item folderContents">

        <tal:block tal:define="item_url item/getURL|item/absolute_url;">

Como puede ver, mientras que se itera sobre "item" (elemento) usted está
accediendo a las cosas del cerebro de una manera cerebro, como "item/getURL".
Pero se dará cuenta de que no se puede hacer "item/my_image" porque no está
en el cerebro. ¿Qué hacer? podría aclamar. Bueno puede despertar los objetos,
obtener el campo de imagen, y luego llamar el cambio de tamaño de imagen de
una manera "pythonica", pero esto es un impacto en el rendimiento, ya que
pone Python en su TAL, cosa que debería evitar.

En lugar de esto usted va a ser astuto. Ya tiene "item_url" y sabe el nombre
de su campo de imagen (my-image) así que coloque estas juntas y llegará justo
a la imagen. Pruebe esto en su navegador:

http://full/url/to/your/object/my-image

y ¡debería ver su imagen! Al traducir esto en TAL, será de la siguiente
manera:

.. code-block:: xml

    <img src="#" tal:attributes="src string:${item_url}/my-image" />

Ahora añadir la parte de modificar el tamaño de la imagen, y aquí es donde me
equivoqué. Mucha de la documentación sobre PiL de Plone asume que usted está
trabajando con un objeto ATImage, pero no es así. Está trabajando con un
ATImageField. ATImageField sólo define UN solo tamaño de escala de la imagen
por defecto:

.. code-block:: python

    sizes = {'thumb': (80,80)}

Donde ATImage define un montón:

.. code-block:: python

      sizes = {'large'   : (768, 768),
               'preview' : (400, 400),
               'mini'    : (200, 200),
               'thumb'   : (128, 128),
               'tile'    :  (64, 64),
               'icon'    :  (32, 32),
               'listing' :  (16, 16),
              },

Para empeorar el asunto, note que los tamaños definidos para el mismo tamaño
clave son diferentes. ¡Perro malo, no hay galleta! De cualquier forma, lo que
esto significa es que para acceder al tamaño que quiere, tiene que definirlo
en su esquema por adelantado, de esta manera:

.. code-block:: python

        ImageField(
            name='my-image',
            widget=ImageWidget(
                label="My Image",
                description="An image!",
            ),
            storage=AttributeStorage(),
            sizes= {'large'   : (768, 768),
               'preview' : (400, 400),
               'mini'    : (200, 200),
               'thumb'   : (128, 128),
               'tile'    :  (64, 64),
               'icon'    :  (32, 32),
               'listing' :  (16, 16),
              },
        ),



Bien, ahora que ha definido los tamaños que quiere en su tipo de esquema
(schema) personalizado, está listo para usarlo en su Plantilla de página.
¿Recuerda la manera en que accedimos a esto antes?

.. code-block:: xml

    <img src="#" tal:attributes="src string:${item_url}/my-image" />

Para acceder a los tamaños definidos en su esquema, simplemente agregue el
nombre al final de su imagen, precedida por un guión.

.. code-block:: xml

    <img src="#" tal:attributes="src string:${item_url}/my-image_mini" />

Es así de simple, y debería ser así. No debería tener que acceder y por
consiguiente ¡despertar sus objetos!. Hay también otras maneras de obtener
PiL, pero considero que esta es la manera más fácil y sin arrojar ningún
error bizarro como "Unauthorized" o "TypeError:a float is required"

¡Disfrute!
~Spanky

TAMBIÉN VEA:

 * `http://plone.org/kb/manual/archetypes-developer-manual/fields/fields-reference`_
 * `http://plone.org/documentation/kb/richdocument/pil`_

.. _63_seccion:

6.3. CSS y JavaScript a la página
==================================

CSS y JavaScript a la página


6.3.1. CSS y JavaScript a la página
====================================

Cómo las hojas de estilo y JavaScript llegan a la página.

Los archivos JavaScript y hojas de estilo están incluidos en la sección skin
del tema Plone Default, así que el proceso de personalización o reescritura
en general sigue el concepto de orden de precedencia descrito en la sección
`Skin`_ de este manual (es decir, situar un remplazo en una capa más alta del
Skin).

Si crea su propia hoja de estilo, puede ponerla en la carpeta personalizada
de portal_skins a través de la web o en el directorio de skins de su tema en
el sistema de archivos.

Si gusta, y se siente ambicioso, puede activar la hoja de estilos en un
componente de tipo de recurso al ponerlo en el directorio del navegador y
registrandolo en ZCML. De hecho, esto se hace por usted si crea su propio
producto de tema usando el plone3_template. Con respecto al último enfoque
existen pros y contras, revise de nuevo la sección `Skin o Componentes`_ si
quiere explorar estos un poco más..


Registros de recursos
~~~~~~~~~~~~~~~~~~~~~

Antes que la CSS y JavaScript lleguen a la página atraviesan un paso
adicional. Usted notará que hay bastantes hojas de estilo y archivos
JavaScript disponibles (y no todos son siempre requeridos). Por lo tanto una
herramienta de registro señala y escoge como es requerido y asocia sólo
aquellos que necesitan para velocidad y eficiencia.

Hay un tutorial detallado sobre cómo utilizar estos registros en el 
`siguiente sección`_.

incluyendo el uso de condiciones para especificar que sólo desea un recurso
en particular cargado en un contexto particular (por ejemplo, con la vista de
documento).


Registrando hojas de estilo y JavaScript
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   A través de la web puede agregar o eliminar hojas de estilo y
    JavaScript yendo a la interfaz de :menuselection:`Configuración del sitio --> Interfaz de Administración de Zope --> portal_css` o :menuselection:`Configuración del sitio --> Interfaz de Administración de Zope --> portal_javascripts`.
-   En el sistema de archivos, el registro de hojas de estilo y JavaScript es parte de la configuración. Por lo que tendrá que buscar en
    profiles/default/jssregistry.xml and cssregistry.xml.


DTML (Document Template Markup Language - Lenguaje de Marcado de Documento de Plantilla)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Algunos de los archivos por defecto en la hojas de estilo de Plone poseen una
extensión .dtml, y la CSS que está adentro está empaquetada.

.. code-block:: xml

    /* <dtml-with base_properties> */
     .......
    /* </dtml-with> */

DTML es otro lenguaje de plantillas de Zope, que en este caso se ha
implementado de manera que ciertas variables puedan ser recogidas a partir de
una hoja de propiedades (base_properties.props), por ejemplo:

.. code-block:: xml

    #portal-column-one {
        vertical-align: top;
        *width: <dtml-var columnOneWidth missing="16em">;*
        border-collapse: collapse;
        padding: 0;
    }


Nosotros no recomendamos el uso de esta técnica, ya que es probable que
desaparezca, pero es bueno saber que está allí. A veces puede quedarse
atrapado al estar personalizando una hoja de estilo existente y
accidentalmente borra la parte superior o inferior de la sentencia "dtml-
with".


6.3.2. Utilizando los Registros de recursos para controlar CSS y JavaScript
===========================================================================

Plone tiene dos herramientas claras para la gestión de hojas de estilo en
cascada y JavaScript en una forma práctica. Este tutorial explica algunos
porqués y cómo e incluso tiene un mínimo ejemplo práctico de cómo funciona.


6.3.2.1. ¿Por qué tenemos estos registros?
==========================================

¿Por qué los registros de recursos fueron escritos, qué hacen, y por qué son
útiles?

Los ResourceRegistries brotan fuera (como la mayoría de características en
Plone) de frustraciones con el estado del mundo ante su existencia: si desea
agregar una hoja de estilo CSS o una librería JavaScript a su sitio Plone,
más allá de usar Custom.css-file, usted tendrá que sustituir las plantillas
de encabezado. Esto era doloso desde el punto de vista de mantenimiento, y
tampoco permitía que ocurriera más de una vez. No había manera de que
Productos suministraran sus propios archivos css sin grandes conflictos en el
caso de que más de un producto intentara hacer lo mismo. Tener varias hojas
de estilo y archivos JavaScript para hacer las cosas más manejables en el
sistema de archivos fue doloroso también.

Con la existencia de ResourceRegistries también hemos sido capaces de dividir
CSS de Plone y JavaScript en partes más manejables que pueden ser activadas o
desactivadas con el clic de un botón. No hubiéramos podido hacer esto en
versiones anteriores de Plone ya que la división de las hojas de estilo
hubiera aumentado el número de peticiones separadas HTTP necesarias para
mostrar una página de manera increíble.


Los registros de recursos deberían:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   Trabajar más fácil con y suministrar sus propias CSS y JavaScript en
    Plone
-   Hacer posible/fácil añadir condiciones a sus CSS y JavaScript para
    que apliquen cuando quiera que se apliquen
-   Facilitar a los autores de Productos el abastecimiento de CSS y
    JavaScript para sus productos sin tener conflictos con otros productos
-   Reducir el número de peticiones HTTP (http-requests) necesarias para
    mostrar una página Plone en un navegador Web
-   Empaquetar CSS y JavaScript para reducir el tamaño de la descarga de
    archivos para los usuarios y el uso de ancho de banda para el tema del
    servidor de un sitio Plone.
-   Facilitar el cambio de prioridades entre las CSS y JavaScripts
-   Facilitar la desactivación de todas o algunas partes de las CSS de
    Plone por defecto y JavaScripts


¿Qué son los registros?
~~~~~~~~~~~~~~~~~~~~~~~

Los registros de recursos actualmente consisten en dos herramientas Plone que
están en la ZMI en el root de su sitio Plone. Ellos han sido parte del
paquete/instaladores de Plone desde Plone 2.1. (Se pueden usar con Plone
2.0.x también. Hay un archivo especial readme en el producto para
instrucciones de instalación para Plone 2.0.x)


¿Cómo funcionan los registros?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cada registro tiene una lista ordenada de los recursos, archivos CSS o
JavaScript, y cada uno con su propio conjunto de atributos. Las entradas de
los registros serán conectadas automáticamente en páginas Plone en las
plantillas estándar cuando el navegador solicite una página. Los registros se
han configurado para que tengan defaults bastante sensibles; así que para
casi todos los casos de uso (probablemente el 90%+) no es más que la cuestión
de añadir la identificación del recurso que desea utilizar.

.. note::
    Para experimentación, por ejemplo, al leer este documento, asegúrese de
    marcar la casilla de verificación "modo de depuración/desarrollo" en la parte
    superior del panel de configuración. (Lea más acerca del por qué en la parte 2.)


6.3.2.2. Condiciones, la fusión, almacenamiento en caché y depuración
=====================================================================

otros detalles sobre cómo ResourceRegistries funciona


Condiciones
-----------

Cuando un agente de usuario (es decir, un navegador) hace una solicitud de
página, todos los recursos registrados en el registro son evaluados en contra
de su campo de condición. Si la condición es verdadera, el recurso es servido
en el navegador. Si la condición se evalúa como falsa, el recurso no se
sirve.

Esto le da la capacidad de servir condicionalmente diferentes hojas de estilo
o scripts basados ??en lógica como si el usuario está conectado o no, si
usted está en la sección "Recursos Humanos" de su intranet o si el tipo de
contenido es un elemento de noticias.

Las Condiciones tienen que ser expresiones `TALES`_. Y puede usar 
`global template variables (variables globales de plantilla)`_ dentro de ellas.


Fusionando
----------

Cada vez que haga clic en el botón de guardar en un registro, un nuevo
conjunto de archivos CSS o JavaScript se crean. El registro tratará de reunir
los diferentes recursos en grandes bultos/archivos para servirlos al
explorador Esto es para reducir el número de peticiones http necesarias y
puede mejorar considerablemente el rendimiento.


Reglas para la fusión de los recursos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.  El registro sólo trata de combinar recursos que están adyacentes en
    la lista. De lo contrario hay riesgo de que el orden de operaciones en el
    navegador sea afectado (orden de código en JavaScript y el orden de la
    cascada en CSS). Esto posiblemente podría afectar la renderización o
    ejecución en el navegador de una manera negativa, y por tanto no
    disponible.
2.  Dos recursos adyacentes sólo fusionan si su condición es exactamente
    la misma (más información sobre condiciones en el próximo capítulo)
3.  Dos recursos adyacentes no se mezclan, si no tienen la casilla de
    verificación "permitir fusión" confirmada.


Los "Archivos" mágicamente ensamblados se les asigna al azar un nuevo número
como sus nombres. Por lo que encontrará entradas como 
``<link rel=\"stylesheet\" href=\"plone2341.css\" />`` en su código HTML. 
Puede examinar cómo los recursos se fusionan si hace clic en la segunda pestaña 
en el registro, "composición". Se le presentará una lista de archivos "mágicos",
como 'plone2341.css, y en su interior los recursos de componentes que se usan
para su respectiva construcción. Puede hacer clic en cada entrada para
inspeccionar lo que se verá cuando sea servido.


La UI (interfaz de usuario) de composición-CSS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./image_preview.png
  :alt: La UI de composición de css-registry (registro-css)


Cada recurso combinado tendrá un pequeño fragmento en el código identificando
su origen para que pueda hacerse con el código no modificado en el caso de
necesitarlo.

El asunto de comentario generalmente luce así.

.. code-block:: css

    /* ----- base.css ----- */
    @media screen {
    /* http://yourhost/plone/portal_css/base.css?original=1 */
    /* */


El almacenamiento en caché y HTTP
----------------------------------

Los recursos fusionados de forma automática se sirven con encabezados-HTTP
optimizados para que están en la memoria caché por largo tiempo. Dado que el
número auto-generado se cambia cada vez que guarde las configuraciones del
registro, el explorador solicitará los nuevos "archivos" y no utilizará los
viejos valores almacenados en caché. El esquema es en realidad bastante
inteligente.

El problema potencial con el esquema de almacenamiento en caché es que el
registro no sabe si usted cambia los archivos en los directorios del skin a
menos que toque el botón de guardar en el registro. Esto es sólo un problema
mientras se trabaja en el CSS (o JavaScript) para tenerlos funcionando de
manera correcta, pero también puede causar confusión masiva si realiza
cambios y sólo ve los estilos/scripts almacenados en caché en en el
explorador. Para evitar este problema, hemos añadido un modo de "depuración y
desarrollo" para los registros.


Modo de depuración y desarrollo
--------------------------------

Para activar el modo de depuración y desarrollo, marque la casilla
correspondiente en la página de configuración de registro y haga clic en
"Guardar".

Esto:

-   Desactiva la fusión de recursos (ideal para encontrar errores y
    declaraciones específicas con las herramientas de inspectores y
    desarrollo como Firebug)
-   Define encabezados-HTTP para que no entren en memoria caché y así
    obtener una copia fresca cada vez.
-   Desactiva la compresión



Estos valores afectan el rendimiento de una manera adversa, así que asegúrese
de desactivar el modo de depuración cuando su Plone está en línea.


6.3.2.3. Parámetros de recursos
===============================

Los parámetros para una entrada de registro en el registro CSS (y
JavaScript).

Cada entrada en los registros de CSS y JavaScript tiene algunos parámetros
que pueden ser ajustados.

.. glossary::

  id
    La id de la hoja de estilo o JavaScript que será utilizada. De Plone 3.3 
    en adelante, puede especificar un recurso alojado externamente mediante 
    la introducción de la URL completa aquí.

  expression
    Una expresión `TALES`_ a ser evaluada para comprobar si la hoja de
    estilo o JavaScript debe ser incluida en la producción o no. Puede usar
    `global template variables (variables globales de plantilla)`_ aquí.

  conditionalcomment (disponible de Plone 3.3 en adelante)
    Una pequeña cadena para ser incluida en un comentario condicional alrededor
    del recurso. Por ejemplo, si escribe simplemente "IE" en el campo se
    traducirá en un comentario condicional de: ::
    
      <!--[if IE]>...<![endif]--
    
    Este comportamiento está actualmente habilitado para los registros de CSS y 
    JavaScript. El registro KSS es el único registro que no tiene soporte completo 
    para comentarios condicionales. 
    
    Para más información vea: `http://msdn.microsoft.com/en-us/library/ms537512.aspx`_ 
    
  media
    Los medios (media) para los cuales la hoja de estilo se debería aplicar, 
    normalmente vacía o "all" (todos). otros posibles valores son "screen" (pantalla), 
    "print" (impresión) etc. `Lea más acerca de las configuraciones de medios de CSS en w3.org`_ 

  rel
    Relación de enlace. defaults to 'stylesheet', y casi siempre debería permanecer de esa manera.
    Para la designación de las hojas de estilo alternativas. Esto se utiliza para
    alternar entre las fuentes grandes, medianas y pequeñas, en Plone por
    defecto. No cambie esto a menos que sepa realmente lo que está
    haciendo.

  title
    el título de una hoja de estilo alternativa.

  rendering
    Cómo la hoja de estilo es enlazada desde la página html. Esta es una configuración
    avanzada. Deje su valor por defecto "import" a menos que conozca los efectos
    que tienen las diferentes formas de renderizar y vincular hojas de estilo

  import
    El predeterminado. normal importación css
    
  link funciona mejor con
    navegadores antiguos y es necesario para alternar hojas de estilo
    
  inline
    renderizar la stylesheet en línea en lugar de vincularla de forma
    externa. ¡No se debería utilizar en absoluto! no es posible crear sitios que
    la validen si lo hace.
    
    Para más información: `http://developer.mozilla.org/en/docs/Properly_Using_CSS_and_JavaScript_in_XHTML_Documents`_ 
    
  compression
    Si y en qué medida el recurso debería ser comprimido
    
  none
    el contenido original no se modificará safe el contenido se comprime de una 
    manera que debe ser seguro para cualquier método de solución alternativa para 
    errores en el explorador. El código condicional para Internet Explorer se 
    mantiene desde ResourceRegistries 1.2.3 y 1.3.1.
  
  full
    el contenido se comprime con algunas reglas adicionales. Para css todos
    los comentarios y la mayoría de saltos de línea se eliminan, esto puede
    romper hacks de navegador especiales, así que utilice con cuidado. Para
    JavaScript esto codifica variables con prefijos especiales de acuerdo a las
    reglas descritas aquí (caracteres especiales):
    ` http://dean.edwards.name/packer/usage/`_ El código fuente tiene que estar
    escrito de acuerdo a esas reglas, de lo contrario, es más que probable que se rompa.

  safe-encode
    - sólo disponible para JavaScript.
    - 'full-encode' - sólo disponible para JavaScript. Además codifica palabras
      clave. Esto en gran medida comprime el JavaScript, pero necesita ser
      decodificado en el proceso en el navegador en cada carga. Dependiendo del
      tamaño de los scripts esto podría conducir a timeouts en Firefox. ¡Use con
      especial cuidado!applyPrefix - sólo disponible para CSS.
    - Si su stylesheet usa URL relativas en una sentencia ``url()``, por ejemplo
      para hacer referencia a otro stylesheet o imagen, puede experimentar
      problemas cuando utiliza el registro en modo-no-depuración, ya que
      *portal_css* altera la URL que se ve en el explorador. Si es así, configure
      esta opción a *True (Verdadero)* o marque la opción de "Replace relative
      paths in url() statements with absolute paths? (reemplazar rutas relativas
      en sentencias url () con rutas absoluta sí" en la pantalla de administración
      *portal_css* para remplazar cualquier ruta alternativa dentro de una
      sentencia ``url()`` con una ruta absoluta (con el prefijo de la ruta de root
      del sitio Plone) durante la etapa de fusión de recursos. Esto no modifica la
      stylesheet original. Puede tener un ligero impacto en el rendimiento, pero no
      debería ser un problema si los recursos se almacenan en caché de manera
      apropiada. No tiene ningún efecto en modo de depuración.


6.3.2.4. Práctico: Agregar una hoja de estilo al registro a través de la Web
============================================================================

Operaciones básicas de los registros CSS y Javascript. Y un ejemplo
verdaderamente mínimo de cómo usarlos en la vida real. Como un simple ejemplo
de la funcionalidad más básica, vamos a agregar y registrar una mínima
stylesheet que agregue al fondo de su Plone un horripilante color rojo.

Para utilizar uno de los registros, usted tiene que

1.  Contar con un recurso (por ejemplo un Archivo) en su Skin con un poco
    de CSS o JavaScript en él (lo que podría, por ejemplo, estar en la
    carpeta personalizada de portal_skins).

2.  Realizar una entrada en el registro correspondiente (por ejemplo
    portal_css) con la id del recurso.


Hacer una hoja de estilo
------------------------

-   Vaya a la :menuselection:`Configuración del sitio --> Interfaz de Administración de Zope --> portal_skins --> custom`.
-   Desde el menú de agregar elementos, seleccione Archivos
-   Dele a su nuevo archivo una id de "*css-demo.css*"
-   Pegue el siguiente contenido dentro del archivo:

.. code-block:: css

    body{ background-color : red }

-   ...y guárdelo


Agréguela al Registro CSS
--------------------------

Los registros son dos herramientas que están sólo en la Interfaz de
Administración de Zope (ZMI); estas no tiene ninguna interfaz en la interfaz
de usuario Plone como tal. Sin embargo, usted las puede encontrar fácilmente
cuando navega por la ZMI de su sitio Plone. Busque por *portal_css* y
*portal_javascript*

-   Vaya a la :menuselection:`Configuración del sitio --> Interfaz de Administración de Zope`
    y haga clic en portal_css. Una vez seleccionado, el Registro CSS
    (aquel que utilizamos para este ejemplo. El de JavaScript es exactamente
    igual) presentará una interfaz mostrando todo los recursos registrados
    (en el caso del Registro CSS, los recursos son archivos CSS).

-   Asegúrese de marcar la casilla de verificación para modo de
    depuración. Esto asegurará que usted vea los cambios inmediatamente.

-   Desplácese hasta la parte inferior del formulario, donde hay un
    formulario para agregar una hoja de estilo

-   En el campo de id introduzca "*css-demo.css*" (Deje los demás valores
    por defecto como están por ahora)

-   ¡Eureka!. Vea su sitio Plone y fácilmente se dará cuenta de su (la
    verdad es bastante horripilante) ¡brillante color rojo de fondo!


La explicación técnica
----------------------

Cada entrada en los registros tiene un identificador que hace referencia a un
recurso que se puede encontrar en el contexto actual de adquisición de Plone.
Técnicamente podría ser una herramienta o una utilidad o cualquier cosa que
tenga un nombre y este disponible, pero más frecuente es que sea un objeto de
Archivo (por CSS y JS estático) o un Método DTML (para reemplazo de variable
dinámica). Los registros de recursos no hacen ninguna diferencia en cuanto a
qué es el objeto, siempre y cuando se pueda encontrar y llamar, renderizar o
imprimir como una cadena.


6.3.2.5. Práctico: Agregar una hoja de estilo al Registro en su propio producto de tema
=======================================================================================

Las hojas de estilo y JavaScript se añaden a los registros de instalación de
su producto de tema, a través de la Generic Setup. Usted simplemente tiene
que escribir el código XML de Generic Setup


Crea su hoja de estilo
----------------------

-   Cree un archivo normal CSS [mytheme.css] usando su editor CSS
    favorito.
-   Ahora tiene dos opciones:


-   El lugar más simple para poner su hoja de estilo se encuentra en el
    directorio de skins de su producto de tema. Paster habrá creado un
    directorio de estilos para usted (skins/plonetheme_mytheme_styles).

-   Paster también habrá creado un directorio de stylesheets para usted
    en el directorio del navegador de su producto de tema y habrá registrado
    esto como un recurso en el archivo configure.zcml. Usted puede, si desea,
    poner su hoja de estilo en ese directorio.


Escriba su archivo de Generic Tool
----------------------------------

Los archivos relevantes para la configuración de sus registros son
profiles/default/cssregistry.xml and profiles/default/jsregistry.xml. Paster
debería haber creado esto para usted, pero si no están allá, créelos usted
mismo.

Una entrada para una hoja de estilo en el directorio de skins de su producto
de tema, se verá así:

.. code-block:: xml

    <?xml version="1.0"?>
    <object name="portal_css" meta_type="Stylesheets Registry">
     <stylesheet title="" cacheable="True" compression="safe"
        cookable="True"
        enabled="1" expression="" id="mytheme.css" media="screen"
        rel="stylesheet" rendering="import"/>
    </object>

Tenga en cuenta que los parámetros son los mismos que por la forma a-través-
de-la-Web. Usted sólo tendrá que dar el ID de la hoja de estilo, Plone, la
encontrará, ya que es parte del skin.

Una entrada para una hoja de estilo en el directorio del explorador de su
producto de tema se verá así:

.. code-block:: xml

    <?xml version="1.0"?>
    <object name="portal_css">
     <stylesheet title=""
        id="++resource++plonetheme.mytheme.stylesheets/mytheme.css"
        media="screen" rel="stylesheet" rendering="import"
        cacheable="True" compression="safe" cookable="True"
        enabled="1" expression=""/>
    </object>

Note la sintaxis especial de ++resource++plonetheme.mytheme.stylesheets para
referirse al directorio registrado como un recurso en browser/configure.zcml

Una vez escrita, se puede volver a importar el archivo cssregistry.xml
utilizando la herramienta portal_setup en la ZMI para que este cambio surta
efecto. Asegúrese de elegir el perfil correcto (su producto de tema) antes de
importar el step CSS. Reinstalar el producto de tema también funcionará,
aunque hay que tener cuidado para evitar enfrentamientos de GenericSetup. Es
más seguro importar el step individual si su tema se ha instalado
previamente.


De la versión Plone 3.3 en adelante
------------------------------------

De Plone 3.3 en adelante también le puede decir al Registro CSS poner
comentarios condicionales alrededor del stylesheet:

.. code-block:: xml

    <stylesheet title="" cacheable="False" compression="none" cookable="False"
     rel="stylesheet" expression="" id="IEFixes.css" media="all"
     enabled="1" rendering="import" **conditionalcomment="IE"** />

También puede especificar un recurso externo:

.. code-block:: xml

    <javascript cacheable="False" compression="none" cookable="False"
     enabled="True" expression=""
     **id="http://ajax.googleapis.com/ajax/libs/jquery/1.2.6/jquery.min.js"**
     inline="False" insert-before="jquery-integration.js" />

Si está usando SSL y especificando un recurso externo, puede verse en la
necesidad de especificar el protocolo http y una entrada ssl en el registro.
Usted puede utilizar el parámetro de expresión para decidir cuál será
utilizado:

.. code-block:: xml

    <javascript cacheable="False" compression="none" cookable="False"
     enabled="True" **expression="python:request.get('ACTUAL_URL','').st
     artswith('https://')"**
     id="**https://**jqueryjs.googlecode.com/files/jquery-1.2.6.min.js"
     inline="False" insert-before="jquery-integration.js" />

    <javascript cacheable="False" compression="none" cookable="False"
     enabled="True" **expression="python:request.get('ACTUAL_URL','').st
     artswith('http://')"**
     id="**http://**jqueryjs.googlecode.com/files/jquery-1.2.6.min.js"
     inline="False" insert-before="jquery-integration.js" />


6.3.2.6. Ejemplo de Condiciones
===============================

Algunos ejemplos de limitación para Hojas de Estilo por el parámetro de
condición, que le ayudarán a empezar.

En estos ejemplos hemos dado la condición como aparecería en
profiles/default/jsregistry.xml and cssregistry.xml. Si usted está trabajando
a través de la web, el texto dentro de las comillas "...." simplemente se
puede situar en la casilla de condición para la CSS relevante o el archivo
JavaScript en portal_css portal_javascripts.


Tipo de contenido
-----------------

Si su CSS, o JavaScript, sólo es relevante para un determinado tipo de
contenido:

.. code-block:: xml

    expression = "python:object.meta_type == 'ATFolder'"

Vista
-----

Usted puede revisar una vista de navegador específica para una propiedad (en
este ejemplo es de Products.Maps):

.. code-block:: xml

    <javascript
        cacheable="True"
        ...
        expression="object/@@maps_googlemaps_enabled_view/enabled | nothing" />

Así es como se busca una de las vistas globales (vea la 
`Sección - Utilizando otra información sobre su sitio`_ para más 
información sobre estas vistas).

En este ejemplo se ofrece la Hoja de estilo Plone RTL:

.. code-block:: xml

    <stylesheet
        ...
        expression="python:portal.restrictedTraverse ('@@plone_portal_state').is_rtl()"
        id="RTL.css"
        ...
    />

Rol
---

Lo siguiente comprobará si el visitante ha iniciado sesión o no; en este caso
entrega el estándar member.css si el visitante no es anónimo:

.. code-block:: xml

    <stylesheet
        ...
        expression="not: portal/portal_membership/isAnonymousUser"
        id="member.css"
        .../>

En este ejemplo se hace lo mismo, pero utiliza la vista plone_portal_state

.. code-block:: xml

    expression="python: not here.restrictedTraverse ('@@plone_portal_state').anonymous()"

Sección y/o lugar en el sitio
------------------------------

Tenga en cuenta que el cuerpo de la etiqueta de cada página tiene una sección
y clase de plantilla CSS. Así que puede que no tenga que usar los registros
de recursos en absoluto.

Sin embargo, si desea cambiar los estilos para una carpeta que no está en el
nivel superior de su sitio, o si desea proporcionar algún JavaScript en un
punto específico en el sitio, entonces tendrá que escribir un script y
llamarlo a través de la expresión resource-registry (recurso-registro.) La
clase de sección en el cuerpo de la etiqueta en main_template es generada por
un script Python getSectionFromURL. Este es un buen punto de partida para su
propio script.

He aquí un ejemplo de expresión y script Este devolverá True (verdadero) para
una carpeta de su sitio el nombre corto "news" (noticias) y cualquier objeto
que este dentro. En este caso, a diferencia de la configuración por defecto
de Plone, la carpeta de news es un nivel por debajo del nivel superior:

.. code-block:: xml

    expression="python: here.getSectionInTree(object,1)=='news'"

.. code-block:: python

    ## Script (Python) "getSectionInTree"
    ##bind container=container
    ##bind context=context
    ##bind namespace=
    ##bind script=script
    ##bind subpath=traverse_subpath
    ##parameters=object, position
    ##title=Returns a section name
    ##
    contentPath = object.portal_url.getRelativeContentPath(context)
    if not contentPath:
        return ''
    else:
        if len(contentPath)-1 >= position:
             return contentPath[position]
        else:
             return ''


6.3.3. ¿Cómo agregar nuevos estilos de clase para Kupu?
=======================================================

Este documento explica cómo agregar y definir nuevos estilos de clase
personalizado para su uso en Kupu.

 Prerrequisitos: conocimiento CSS

1. Vaya a la Configuración de sitio en su sitio Plone.

2. Seleccione el icono de configuración del producto adicional para el
    editor visual Kupu, como se ve a continuación:

.. image:: ./image_preview_003.png
  :alt: Site-setup kupu


3. Vaya a la caja de estilos de párrafo.

.. image:: ./image_preview_011.png
  :alt: Kupu paragraph styles


4. Agregue su nuevo estilo de párrafo en la caja. 
   Format is title|tag or title|tag|className, one per line. Por ejemplo:

.. code-block:: cfg

    Smalltext|p|smalltext

5. Abra su ZMI.

6. Asegúrese de que su sitio está en `el modo de depuración`_ la primera
    vez que se hacen cambios. Esto le permitirá ver los cambios de inmediato.

7. Vaya a *http://yoursite/portal_skins/plone_styles/ploneCustom.css/manage_main*.

8. Haga clic en el botón de personalización.

9. Ingrese su nuevo estilo de párrafo, donde dice "add your custom stuff here" (agregue sus elementos personalizados aquí)

    .. code-block:: css

        .smalltext {font-size: 70%;}

.. note::
    desplazarse por la página para revisar elementos disponibles. Vea
    *base_properties* para definiciones de estos elementos


6.4. Utilizando otra información sobre su sitio en una página
=============================================================

Cómo obtener información sobre el estado de su sitio y otras variables
globales.

En algún momento u otro se dará que necesita utilizar el título de su sitio
en una plantilla, o usted querrá que su plantilla ofrezca algo en función de
los roles o permisos de su visitante o usuario. Hay dos métodos para obtener
esta información:


1. Vistas del explorador (recomendado)
--------------------------------------

El primer enfoque, más reciente, y recomendado es utilizar los métodos
disponibles en una de las tres vistas del explorador:

-   @@plone_portal_state
-   @@plone_context_state
-   @@plone_tools

Estos se mantienen en

-   [locación de su huevo]/plone/app/layout/globals 

OR

-   [locación de su huevo]/plone.app.layout-[version]/plone/app/layout/globals


Puede encontrar una descripción de cada método en interfaces.py en ese
directorio, pero los métodos principales se describen a continuación Este
extracto de main_template en el núcleo de plantillas de Plone Default en
Plone 4, muestra cómo estas vistas, o sus métodos individuales, están a
disposición de cada página:

.. code-block:: xml

    <html xmlns="http://www.w3.org/1999/xhtml"
          ...
          tal:define="portal_state context/@@plone_portal_state;
                      context_state
                      context/@@plone_context_state;
                      ...
                      lang portal_state/language;
                      ...
                      portal_url
                      portal_state/portal_url;
                      ..."
         ...
    >


Aquí hay un fragmento de la plantilla newsitem_view en el núcleo de
plantillas de Plone Default ilustrando cómo @@plone_context_state se puede
utilizar para establecer si un elemento es editable o no:

.. code-block:: xml

            <p tal:define="**is_editable context/@@plone_context_state/is_editable**"
               tal:condition="python: not len_text and
               is_editable"
               i18n:translate="no_body_text"
               class="discreet">
                This item does not have any body text, click
                the edit tab to change it.
            </p>

--


2.  Global Define (en desuso)
-----------------------------

El segundo enfoque ha estado en uso por un tiempo largo, pero se está
remplazando gradualmente (ya que es más lento) en Plone 3 y ha sido casi
eliminado en Plone 4. Este es el uso de un conjunto de variables que están
disponibles para cada página.

En Plone 3:

Estas son llamadas main_template:

.. code-block:: xml

    <metal:block use-macro="here/global_defines/macros/defines" />

Si quiere investigarlas más a fondo, las encontrará en

-   [su directorio de productos]/CMFPlone/browser/ploneview.py.

Estas variables se utilizan en un número de plantillas de Plone Default en
Plone 3 y a continuación son listadas junto a sus equivalentes en las vistas
disponibles.

En Plone 4:

El macro global_defines no se utiliza en absoluto y las variables han sido
sustituidas completamente en todas las plantillas de Plone. Sin embargo, en
caso de ser necesario, el macro global_defines sigue estando disponible en
las capas de núcleo del skin en Plone Default en la carpeta plone_deprecated.
Para más información sobre cómo crear un tema de Plone 3 compatible con Plone
4, consulte la `Guía de actualización`_ .


Vistas y métodos disponibles
----------------------------

Acerca del sitio
~~~~~~~~~~~~~~~~

View @@plone_portal_state

+----------------------+---------------------------------+---------------------+
| Método               |  Lo que se obtiene              | global define       |
+======================+=================================+=====================+
| portal               | Portal Object                   | portal              |
+----------------------+---------------------------------+---------------------+
| portal_title         | El título de su sitio           | portal_title        |
+----------------------+---------------------------------+---------------------+
| portal_url           | La dirección URL de su sitio    | portal_url          |
+----------------------+---------------------------------+---------------------+
| navigation_root_path | Ruta del root de navegación     |                     |
+----------------------+---------------------------------+---------------------+
| navigation_root_url  | La dirección URL del root de    | navigation_root_url |
|                      | navegación                      |                     |
+----------------------+---------------------------------+---------------------+
| default_language     | El idioma por defecto del sitio |                     |
+----------------------+---------------------------------+---------------------+
| language             | El idioma actual                |                     |
+----------------------+---------------------------------+---------------------+
| locale               | La localización actual          |                     |
+----------------------+---------------------------------+---------------------+
| is_rtl               | Si el sitio se está viendo en   | RTLisRTL            |
|                      | un lenguaje                     |                     |
+----------------------+---------------------------------+---------------------+
| member               | El actual miembro autenticado   | member              |
+----------------------+---------------------------------+---------------------+
| anonymous            | Si el visitante actual es       | isAnon              |
|                      | anónimo                         |                     |
+----------------------+---------------------------------+---------------------+
| friendly_types       | Obtener una lista de tipos que  |                     |
|                      | se pueden implementar por un    |                     |
|                      | usuario                         |                     |
+----------------------+---------------------------------+---------------------+


Sobre el contexto actual
~~~~~~~~~~~~~~~~~~~~~~~~

View @@plone_context_state

+----------------------+---------------------------------+---------------------+
| Método               |  Lo que se obtiene              | global define       |
+======================+=================================+=====================+
| current_page_url     | La dirección URL de la página   | current_page_url    |
|                      | actual                          |                     |
+----------------------+---------------------------------+---------------------+
| current_base_url     | La dirección URL real de la     |                     |
|                      | página actual                   |                     |
+----------------------+---------------------------------+---------------------+
| canonical_object     | El objeto actual en sí          |                     |
+----------------------+---------------------------------+---------------------+
| canonical_object_url | La dirección URL del objeto     |                     |
|                      | actual                          |                     |
+----------------------+---------------------------------+---------------------+
| view_url             | La URL utilizada para           |                     |
|                      | visualizar el objeto            |                     |
+----------------------+---------------------------------+---------------------+
| view_template_id     | La id de la plantilla de vista  |                     |
+----------------------+---------------------------------+---------------------+
| is_view_template     | Verdadero si el URL actual se   |                     |
|                      | refiere a la vista estándar     |                     |
+----------------------+---------------------------------+---------------------+
| object_url           | La dirección URL del objeto     |                     |
|                      | actual                          |                     |
+----------------------+---------------------------------+---------------------+
| object_title         | El título "embellecido" del     |                     |
|                      | objeto actual                   |                     |
+----------------------+---------------------------------+---------------------+
| member               | El actual miembro autenticado   | member              |
+----------------------+---------------------------------+---------------------+
| workflow_state       | El estado de flujo de trabajo   | wf_state            |
|                      | del objeto actual               |                     |
+----------------------+---------------------------------+---------------------+
| friendly_types       | Obtener una lista de tipos que  |                     |
|                      | se pueden implementar por un    |                     |
|                      | usuario                         |                     |
+----------------------+---------------------------------+---------------------+
| parent               | El "padre" directo del objeto   |                     |
|                      | actual                          |                     |
+----------------------+---------------------------------+---------------------+
| folder               | La carpeta actual               |                     |
+----------------------+---------------------------------+---------------------+
| is_folderish         | Verdadero si es un objeto       | isFolderish         |
|                      | "folderish"                     |                     |
+----------------------+---------------------------------+---------------------+
| is_structural_folder | Verdadero si es una carpeta     | isStructuralFolder  |
|                      | estructural                     |                     |
+----------------------+---------------------------------+---------------------+
| is_default_page      | Verdadero si es la página por   |                     |
|                      | defecto en una carpeta          |                     |
+----------------------+---------------------------------+---------------------+
| is_portal_root       | Verdadero si este es el root    |                     |
|                      | del portal o la página por      |                     |
|                      | defecto en el root del portal   |                     |
+----------------------+---------------------------------+---------------------+
| is_editable          | Verdadero si el objeto actual   | is_editable         |
|                      | es editable                     |                     |
+----------------------+---------------------------------+---------------------+
| is_locked            | Verdadero si el objeto actual   | isLocked            |
|                      | está bloqueado                  |                     |
+----------------------+---------------------------------+---------------------+
| actions              | Las acciones de filtrado en el  |                     |
| (Plone 4)            | contexto. Puede restringir las  |                     |
|                      | acciones a una sola categoría.  |                     |
+----------------------+---------------------------------+---------------------+
| portlet_assignable   | Si el contexto es capaz de      |                     |
| (Plone 4)            | tener  portlets localmente      |                     |
|                      | asignados.                      |                     |
+----------------------+---------------------------------+---------------------+


Herramientas
~~~~~~~~~~~~

view @@plone_tools


+----------------------+-----------------------------------+---------------------+
| Método               |  Lo que se obtiene                | global define       |
+======================+===================================+=====================+
| actions              | La herramienta de portal para     | atool               |
|                      | acciones                          |                     |
+----------------------+-----------------------------------+---------------------+
| catalog              | La herramienta portal_catalog     |                     |
+----------------------+-----------------------------------+---------------------+
| membership           | La herramienta portal_membership  | mtool               |
+----------------------+-----------------------------------+---------------------+
| properties           | La herramienta portal_properties  |                     |
+----------------------+-----------------------------------+---------------------+
| syndication          | La herramienta portal_syndication | syntool             |
+----------------------+-----------------------------------+---------------------+
| types                | La herramienta portal_types       |                     |
+----------------------+-----------------------------------+---------------------+
| url                  | La herramienta portal_url         | utool               |
+----------------------+-----------------------------------+---------------------+
| workflow             | La herramienta portal_workflow    | wtool               |
+----------------------+-----------------------------------+---------------------+
| types                | La herramienta portal_types       |                     |
+----------------------+-----------------------------------+---------------------+


6.5. Utilizando las herramientas jQuery y jQuery
================================================

Plone incluye las bibliotecas JavaScript para las herramientas jQuery y
jQuery sacadas de paquete, las cuales puede utilizar en sus propios scripts
inmediatamente.

`jQuery`_ es una popular librería JavaScript que simplifica traversal de
documento HTML, manejo de eventos, animación, y interacciones. `Herramientas jQuery`_ 
es una colección de componentes de interfaz de usuarios que incluye
revestimientos (overlays), pestañas, acordeones y tooltips (o descripciones
emergentes).

jQuery se ha incluido desde Plone 3.1. jQuery Tools (Herramientas jQuery) se
agregá con Plone 4.0.


Usando jQuery
~~~~~~~~~~~~~

jQuery tiene una excelente documentación disponible en
`http://api.jquery.com`_. Tenga en cuenta, sin embargo, que nunca es
aconsejable depender de la disponibilidad del alias "$", para la función
jQuery ya que otras bibliotecas pueden redefinirlo.

Así que en vez:

.. code-block:: javascript

    $(document).ready(function(){
       $("a").click(function(event){
         alert("Thanks for visiting!");
       });
     });

debe incorporar código jQuery que use el alias "$" en un empaquetador como:

.. code-block:: javascript

    **(function($) {

       $(document).ready(function(){
       $("a").click(function(event){
         alert("Thanks for visiting!");

       });
     });
    })(jQuery);**
    
Usando jQuery Tools
~~~~~~~~~~~~~~~~~~~

jQuery Tools es un plugin de jQuery, y Plone 4 incluye las pestañas, tooltip,
desplazamiento, revestimiento (overlay), y toolset. El resto de los plugins
jQuery tools kit se hacen disponibles permitiendo el recurso de registro de
JavaScript de Plone plone.app.jquerytools.plugins.js

La integración con jQuery tools es proporcionado a través del paquete
`plone.app.jquerytools`_, que incluye una serie de ayudantes de
revestimientos para necesidades comunes de overlay de AJAX. Este kit is usado
para proporcionar muchas de las formularios "revestidos" de Plone. Vea la
página `plone.app.jquerytools`_ pypi para documentación y ejemplos.


.. _Zope book: http://www.plope.com/Books/2_7Edition/SearchingZCatalog.stx
.. _The Definitive Guide to Plone: http://docs.neuroinf.de/PloneBook/ch11.rst#searching-and-categorizing-content
.. _Plantillas y el lenguaje de plantillas: http://plone.org/documentation/manual/theme-reference/page/buildingblocks/skin/templates
.. _http://plone.org/kb/manual/archetypes-developer-manual/fields/fields-reference: http://plone.org/kb/manual/archetypes-developer-manual/fields/fields-reference
.. _http://plone.org/documentation/kb/richdocument/pil: http://plone.org/kb/tutorial/richdocument/pil
.. _Skin: http://plone.org/documentation/manual/theme-reference/page/buildingblocks/skin
.. _Skin o Componentes: http://plone.org/documentation/manual/theme-reference/page/buildingblocks/components/skinorcomponents
.. _siguiente sección: http://plone.org/documentation/manual/theme-reference/page/css/resource-registries
.. _TALES: http://docs.zope.org/zope2/zope2book/source/AppendixC.html#tales-overview
.. _global template variables (variables globales de plantilla): http://plone.org/documentation/manual/theme-reference/buildingblocks/skin/templates/global-template-variables
.. _dentro de ellas.: http://plone.org/documentation/how-to/cmf-expressions
.. _http://msdn.microsoft.com/en-us/library/ms537512.aspx: http://msdn.microsoft.com/en-us/library/ms537512.aspx
.. _Lea más acerca de las configuraciones de medios de CSS en w3.org: http://www.w3.org/TR/CSS21/media.html
.. _http://developer.mozilla.org/en/docs/Properly_Using_CSS_and_JavaScript_in_XHTML_Documents: http://developer.mozilla.org/en/docs/Properly_Using_CSS_and_JavaScript_in_XHTML_Documents
.. _ http://dean.edwards.name/packer/usage/: http://dean.edwards.name/packer/usage/
.. _Sección - Utilizando otra información sobre su sitio: http://plone.org/documentation/manual/theme-reference/page/otherinfo
.. _el modo de depuración: http://plone.org/documentation/kb/how-to-make-your-css-changes-take-effect-instantly
.. _Guía de actualización: http://plone.org/documentation/manual/upgrade-guide/version/upgrading-plone-3-x-to-4.0/updating-add-on-products-for-plone-4.0/no-more-global-definitions-in-templates
.. _jQuery: http://jquery.com/
.. _Herramientas jQuery: http://flowplayer.org/tools/index.html
.. _http://api.jquery.com: http://api.jquery.com/
.. _plone.app.jquerytools: http://pypi.python.org/pypi/plone.app.jquerytools/
