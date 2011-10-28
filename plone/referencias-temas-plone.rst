.. -*- coding: utf-8 -*-

=============================
Referencias de Temas en Plone
=============================

.. contents :: :local:

En esta referencia de Temas en Plone es la traducción al Español del `Plone Theme Reference`_ el cual explica los diversos enfoques de realizar temas y pieles en Plone, además de no ser una guía paso a paso simplemente es una referencias sobre estilos de trabajo.

1. Introducción
===============

Objetivos, prerrequisitos, visión general del manual y una definición rápida
de lo que es un tema de Plone.


1.1. Objetivos y Prerrequisitos
-------------------------------

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


1.2. ¿Qué es un tema Plone?
---------------------------

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
con Plone 4, pues la ` guía de actualización`_ tiene más información y
orientación.


1.3. Resumen
------------

Esta es una vista rápida de lo temas de este manual.

.. image:: images/image_mini.png
  :alt: Mapa conceptual del Manual de referencia

Mapa conceptual de este manual, haga clic para agrandar

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



2. Comienzo rápido
==================

El inicio, y algunas técnicas para que se familiarice con las cosas básicas


2.1. Resumen
------------

Una vez que usted tenga su nuevo y deslumbrante sitio de Plone, lo primero
que recomendamos es que se mueva un poco por las personalizaciones de web -
cambiando los colores de fuente y reemplazando el logotipo de Plone con uno
suyo.

Usted probablemente tenga muchas más ambiciones que estas para el diseño de
su sitio, pero editando el CSS (hojas de estilo en cascada) y reemplazando el
logotipo; son buenas maneras de comenzar a aprender las técnicas para temas.


Prerrequisitos
..............

Hemos asumido que usted está familiarizado con HTML y CSS - sin embargo las
personalizaciones básicas descritas aquí no necesitan de un conocimiento
profundo de ellas. Ayudará si usted como, administrador, ha tenido la
oportunidad de conocer la sección Configuración del sitio de Plone.


Descripción
...........

En primer lugar afile sus lápices 
  Hay una serie de herramientas que facilitarán bastante el proceso de tematización,
  `estas herramientas las describiremos aquí`_. Para ver sus personalizaciones 
  tiene que asegurarse que está ejecutando su sitio en `modo depuración/desarrollo`_.  

Ahora trate algunas personalizaciones de CCS
  Lo acompañaremos en el `proceso de sustituir el estilo del título de la página`_, 
  por medio de la personalización y edición del estilo de hoja ploneCustom.css 
  Todo esto se hace en línea a través-de-la-web vía la Interfaz de Administración 
  de Zope.

Por último remplace el logotipo
  Revisaremos y desplegaremos las técnicas de personalización y edición CCS 
  `reemplazando la imagen del logotipo de Plone`_ con su propio logotipo.

--


2.2. Afilando sus lápices
-------------------------

Breve recorrido de las herramientas que usted encontrará útiles


2.2.1. Herramientas de la UI (Interfaz de Usuario) de Firefox/mozilla
.....................................................................

Firefox y mozilla tienen un conjunto de extensiones que realmente le pueden
ayudar en el trabajo de desarrollo en la Interfaz de Usuario. Un conjunto
básico es listado aquí.

La vieja y confiable opción de "ver código fuente" era antes el camino de
depurar html de mala apariencia. Ahora hay extensiones de mozilla/firefox que
resultan en un desarrollo html mucho más productivo. Un conjunto básico es
listado aquí para que se ponga al día.

Desarrollador Web
  El `desarrollador web`_ agrega una barra de herramientas a su firefox con casi todo lo que quiera hacer o saber. Información de CSS, validación, cambio de tamaño para probar otras resoluciones de pantalla, conversión de POSTs a GETs. **Algo esencial**.

Aardvark
  Cuando se habilita `Aardvark`_ para una página, y pasa el cursor por un elemento se muestra información de clase/identificación Por ejemplo al presionar la tecla ``v`` se mostrará el código fuente del elemento donde está posado el cursor. Comience el demo de su sitio y experimente con las funciones de teclas. Es una herramienta elegante y ligera.

ColorZilla
  `ColorZilla`_ es sorprendentemente útil. Hace lo que el nombre sugiere: provee un selector de color que muestra el código hexadecimal del píxel por donde pase el cursor en la barra de estado. Aún hay más: se muestra el tamaño de caja del elemento actual de caja; mostrando el elemento, clase e identificación del elemento actual, y distancia entre dos puntos. Todo en la barra de estado.

FireBug
  `FireBug`_ muestra constantemente el número de errores que encuentre en su página. Provechoso durante el desarrollo de encontrar clases CSS mal escritas o sentencias defectuosas de javascript. También incluye una revisión de CSS y código fuente, pero Aardvark tiende a ser un poco mejor para eso.

X-ray
  La `extensión x-ray de firefox`_ es bastante beneficiosa para entender el diseño del sitio Plone. Muestra las etiquetas, las identificaciones y clases en línea, concibiendole una sorprendente y buena idea de lo que est? pasando tras bambalinas.

View formatted source
  `View formatted source`_ le da una buena vista del código fuente de la página. Más importante es que cuando pasa sobre una etiqueta desplegable, le muestra la CSS que se usa para esa etiqueta. Y con múltiples archivos CSS (¿alguien con Plone?) le muestra el orden en que estos son usados (y sobrescritos).

View source with
  `View source with`_ le permite hacer clic derecho sobre cualquier área de texto o vista de código fuente y seleccionar un programa para editarlo/verlo. Parecido a ExternalEditor, pero sobre **cualquier** Área de texto. No es 100% orientada a desarrolladores, pero igualmente útil para cambios pequeños y evaluación de archivos CSS en la carpeta de skin por defecto. 

Otros tipos de gadgets (herramientas) útiles son los **bookmarklets** (marcadores).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dos fuentes de estos son http://squarefree.com y http://slayeroffice.com. Vea
para ejemplos:

Bookmarklets para desarrollo Web
  Los `Web development bookmarklets`_ proveen el mismo tipo de funcionalidad que la barra de herramientas Web para desarrolladores. El `JavaScript Shell`_ y el `JavaScript Development Environment`_ merecen ser mencionados.

Mouse-over DOM (Modelo de Objetos del Documento) Inspector
  El `Mouseover DOM Inspector`_ , o abreviado MODI , es un favelet (también conocido como bookmarklet) que le permite ver y manipular el DOM de una página web simplemente posicionándose con el cursor sobre todo el documento.

Javascript Object Tree Favelet
  El `Javascript Object Tree Favelet`_ sobrepondrá su documento actual con un elemento DIV que contiene una lista contraída de todos los tipos de objetos javascript actualmente referenciados por la página, desde funciones a cadenas de caracteres y booleanos y todo aquello que este en el medio.

Favelet Suite
  Esto es un `favelet que combina la mayoría de [slayeroffice] favelets de desarrollo`_ . Cuando se invoca, un elemento DIV aparecerá en la esquina superior izquierda del navegador Web con una lista de todos los favalets que se han mencionado. Simplemente haga clic en el enlace para invocar el favalet.


2.2.2. ¿Cómo hacer para que los cambios de CCS surtan efecto inmediatamente?
............................................................................

Asegurarse que los cambios hechos de CCS puedan verse instantáneamente. Este
es el problema más común que se le presenta a las personas nuevas en Plone,
que están tratando con el asunto de temas.


Activación del modo de desarrollo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Antes de comenzar cualquier personalización CSS debería cambiarse a modo
depuración/desarrollo. Esto garantizará que el almacenamiento en caché y la
compresión de CSS están desactivadas. Esto le asegura que pueda ver los
cambios en tiempo real, después de recargar o actualizar su navegador Web.

Esta es la manera en que se activa el modo depuración/desarrollo:

1.  Entre a su sitio Plone como el usuario "admin":

2.  agregue "/manage" al URL para accesar a la ZMI (Interfaz de
    Administración de Zope)
3.  Navegue a **ZMI > portal_css**

En Plone 3:

1.  haga clic en la casilla de verificación para modo
    depuración/desarrollo
2.  haga clic en el botón Guardar

En Plone 4:

1.  asegúrese que la casilla de verificación para el modo desarrollo está
    confirmada; si usted inició la instancia de Zope en modo desarrollo, pues
    esta estará automáticamente confirmada.

2.  haga clic en el botón Guardar

----

Cuando haya finalizado con las modificaciones de CSS debería desactivar el
modo depuración/desarrollo, ya que este afecta el rendimiento de su sitio
Plone.

----

2.3. Cambiar los colores de fuente
----------------------------------

¿Cómo cambiar los colores de fuente?: un enfoque a través-de-la-web.

Aquí se presentarán algunas técnicas sencillas para la personalización del
CSS de Plone a través-de-la-web.

-   ¿Cómo encontrar los estilos que usted quiere cambiar?
-   ¿Cómo en sustituir estos estilos mediante el uso del estilo de hoja 
    ploneCustom.css?

En este caso cambiaremos los títulos de las paginas de color negro a color
turquesa.


Antes de comenzar
.................

Para mayor comodidad, los temas de Plone a menudo se comprimen en un conjunto
de hojas de estilo separadas, pero para velocidad y eficiencia en modo de
producción, Plone posee un mecanismo (portal_css) para crear los paquetes en
uno o dos archivos.

Usted necesitará desactivar esto al momento de hacer cambios o personalizar
la CSS. Así que asegúrese completamente que ha seguido las instrucciones de
cómo poner su sitio en `modo desarrollo/depuración`_.


Encontrando los estilos que quiere cambiar
------------------------------------------

-   Si todavía no tiene una página en su sitio Plone, agregue una,
    guárdela e inspecciónela en modo vista.
-   Use `Firebug, o alguna herramienta similar,`_ para localizar el
    nombre de la clase del título de la página; en este caso es
    h1.documentFirstHeading.


Localizando la hoja de estilo ploneCustom.css
---------------------------------------------

Como algo natural, la hoja de estilo que se carga de último en cada página
Plone es ploneCustom.css. Usted puede ver esto si inspecciona la etiqueta de
encabezado HTML de su página usando Firebug. Si escarba un poco más,
probablemente encontrará que esta hoja de estilo está completamente vacía.
Según las reglas de precedencia de la Cascada CSS, cualquier estilo
especificado en esta hoja sustituir? esos estilos en la hoja precedente.
Entonces aquí tiene una "hoja en blanco" para sus propias personalizaciones.

El truco ahora es encontrar el archivo, para que está disponible para su
respectiva edición.

-   Para hacer la vida más sencilla, quizás quiera abrir una segunda
    pestaña o ventana de su navegador Web; luego puede retornar rápidamente a
    la primera pestaña para observar sus cambios.
-   Vaya a la Configuración del sitio > Interfaz de Administración de
    Zope y haga clic en portal_skins
-   Use la opción de Buscar en las pestañas de la parte superior para
    encontrar ploneCustom.css:

-   Escriba *ploneCustom.css* en la caja "with ids:" y haga clic en
    buscar
-   Puede que obtenga más de un resultado, pero no es importante la que
    elija, sin embargo la mejor manera es escoger aquella opción que está
    marcada con un asterisco rojo.


Editando y Personalizando ploneCustom.css
-----------------------------------------

Cuando hace clic en ploneCustom.css se dar? cuenta que no puede editarlo. El
próximo paso es poner ploneCustom.css en un lugar donde la edición sea
posible. Usted verá una opción de Personalizar justo arriba del ?rea gris de
texto, haga clic en el botón de Personalización y verá que el estilo de hoja
se ha copiado automáticamente a portal_skins/custom.

Ahora ya es libre de editar el archivo a su gusto. Para cambiar el color de
los títulos de nuestra página, agregue: ::

    h1.documentFirstHeading {
      color: #0AAE95;
    }


y guarde.

Si usted instalá Plone 4 con el tema Sunburst, el archivo ploneCustom.css
trae una serie de estilos pre-empaquetados comentados con los que puede
experimentar si desea. Usted puede sustituir los estilos de diseños para un
ancho fijo y modificar los colores de los enlaces.


Revocar sus cambios
-------------------

Usted cuenta con un par de opciones para revertir a la CSS original:

-   comente sus estilos en el ploneCustom.css; se aplica la sintaxis
    habitual de CSS para comentar
-   elimine (o si quiere mantener un registro de lo que hizo, entonces
    renombre) su versión de ploneCustom.css que encontrará aquí:

-   Configuración de sitio > Interfaz de Administración de Zope >
    portal_skins > custom
-   puede escoger entre las opciones de eliminar o renombrar: trate de
    renombrar ploneCustom.css.old
-   luego puede volver al comienzo del proceso para localizar y
    personalizar ploneCustom.css


Más información
-----------------

De hecho aquí ha encontrado dos tipos de personalización.

1.  El primero es un método estándar mediante el uso del orden de
    precedencia, la Cascada, para sobrescribir estilos CSS tal y como llegan
    al navegador Web.
2.  El segundo es un método específico de Plone/Zope para cambios en las
    mismas hojas de estilo mediante la colocación de estas en la carpeta
    predeterminada de portal_skins. Este método también pude ser usado con
    platillas y otros recursos, y es explicado con más `profundidad en la
    sección de capas Skin`_ en este manual.

Técnicas más avanzadas que incluyen la incorporación de sus propias hojas de
estilo dentro de un producto de tema, son descritas posteriormente en este
manual.

Puede descubrir más acerca de cómo el CSS Registry (Registro CSS)
(portal_css) empaqueta los hojas de estilo para montarlos a la página en la
sección de `Plantillas y Componentes para página`_ de este manual.


2.4. Cambiar el logotipo
=========================

¿Cómo substituir el logotipo estándar de Plone con su propio logotipo?; un
enfoque a través-de-la-web.


Los fundamentos
---------------

En Plone 3 y 4 el logotipo es simplemente una imagen que contiene un enlace a
la página de inicio (solamente hay una pequeña diferencia entre versiones, y
es que en Plone 3 se llama logo.jpg y en Plone 4 logo.png).

::<a id="portal-logo" href="http://[your site]" accesskey="1">

        <img width="252" height="57" title="Plone" alt=""
        src="http://[your site]/logo.jpg"/>

    </a>

Si le parece bien este enfoque entonces no tendrá que cambiar el HTML ya que
todos los atributos en este fragmento se generan automáticamente. Siga las
instrucciones en la Sección 1: Cambiando la Imagen y su Título.

Si quiere hacer algún cambio pequeño en los estilos vaya a la Sección 2:
Cambiando el estilo de portal_logo.


Si prefiere montar su logotipo con un estilo diferente y necesita rescribir
el HTML, pues puede hacer esto a través de la personalización de la plantilla
del logotipo; siga las instrucciones en la Sección 3: Cambiando el HTML.


1. Cambiando la Imagen y su Título

-----------------------------------

La imagen del Logotipo: logo.jpg (Plone 3) logo.png (Plone 4). Se encuentra
en la carpeta plone_images en portal_skins. La manera más rápida de remplazar
esta imagen es simplemente subiendo su propia imagen y dandole el mismo
nombre:

-   Vaya a la ZMI (Interfaz de Administración de Zope) (Configuración del sitio > ZMI)
-   Luego a portal_skins > plone_images
-   Haga clic en logo.jpg (Plone 3) o logo.png (Plone 4) y después clic
    en el botón de Personalizar.
-   Ahora remplace la imagen haciendo clic en el botón de buscar y así
    escoger su propia imagen en su sistema de archivos
-   Edite el campo del título (esto asegurará que el atributo del título
    cambie en el HTML)
-   Guarde los cambios y actualice su navegador para observar los
    modificaciones en su sitio.


Enfoque alternativo (sólo Plone 3)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El nombre (ID: identificación) del logotipo está especificado en
base_properties (propiedades_básicas); una lista de valores útiles que en
Plone 3 se seleccionan y se usan en las hojas de estilo del tema de Plone por
defecto. Esto le da la posibilidad de subir su propria imagen de logotipo,
otorgarle cualquier nombre, y luego personalizar la base_properties con ese
nombre.

-   Vaya a la ZMI (Interfaz de Administración de Zope) (Configuración del
    sitio > ZMI)
-   Asegúrese de haber cambiado su CSS Registry (Registro CSS) a modo
    depuración (portal_css)
-   Vaya a portal_skins > custom y escoja Image en la lista desplegable a
    la derecha
-   Escoja la imagen que quiera y le da una Identificación y un Título,
    ej.: ::
        ID (Identificación) = MyLogo.jpg
        Title (Título) = My Logo
-   Vaya a portal_skins > plone_styles, haga clic base_properties y luego
    clic en el botón de Personalizar

-   En este momento tendrá una versión personalizada de base_properties
    en la carpeta predeterminada de portal_skins la cual puede cambiar si
    desea. Encuentre el campo logoName y reemplace el valor *logo.jpg* con la
    ID que le haya dado a su imagen (asegúrese de haber introducido a su ID
    una terminación .jpg o .gif, y recuerde que toma en cuenta la mayúsculas
    y minúsculas) por ejemplo:
::logoName = MyLogo.jpg
-   Guarde sus cambios y recargue o actualice su navegador Web

En Plone 4 base_properties sigue existiendo pero tiene un uso bastante
limitado.

**Note** que cuando usted se devuelva a su base_properties personalizado en
portal_skins > custom, se verá como una carpeta vacía. Haga clic en la
pestaña de propiedades para retornar a la lista de propiedades.


2. Cambiando el estilo de portal_logo
-------------------------------------

No hay ningunos estilos definidos para *#portal-logo*, pero hay algunos para
*#portal-logo img* en basic.css. Investigue esto con Firebug, la extensión de
Firefox. El enfoque más simple es sustituir estos con su propios estilos en
ploneCustom.css.

-   Vaya a la ZMI (Interfaz de Administración de Zope) (Configuración del
    sitio > ZMI)
-   Como siempre asegúrese de estar en modo de depuración/desarrollo
    activado en el CSS Registry (Registro CSS) (portal_css)
-   Haga clic en portal_skins > plone_styles > ploneCustom.css y luego en
    el botón de Personalizar.
-   Ahora tendrá una versión editable de ploneCustom.css en la carpeta
    predeterminada de portal_skins
-   Agregue su propios estilos aquí, y haga clic en guardar, y recargue o
    actualice su navegador Web para salvar los cambios



3. Cambiando el HTML
--------------------

El HTML para el logotipo es generado mediante logo.pt; una plantilla de
página parte del viewlet denominado plone.logo. Para personalizar esto a
través de la web, necesitará usar portal_view_customizations.

-   Vaya a portal_view_customizations en la ZMI (Interfaz de
    Administración de Zope) (Configuración del sitio > ZMI)

-   Haga clic en plone.logo en el botón de Personalizar

-   Ahora tendrá una plantilla que puede rescribir. Hemos resaltado los
    detalles importantes en la sección de teoría que está más adelante,
    mostrándole algunos ejemplos para que comience.
-   Guarde sus cambios y actualice o recargue su navegador Web para
    verlos

**Nota**: si en algún momento quiere retornar y hacer más cambios, verá que
plone.logo está resaltado en la lista portal_view_customizations, haga clic
en él para editarlo. Si quiere quitar completamente sus personalizaciones use
las pestaña de contenido de portal_view_customizations, marque la casilla al
lado de su plantilla y haga clic en Eliminar.


La Teoría
~~~~~~~~~~

Aquí esta la plantilla logo.pt. Est? escrita en lenguaje de plantillas que
usa Plone - TAL (o ZPT). Es saludable aprender esto (y no toma mucho tiempo
en aprenderse) pero nos explicaremos a través de este ejemplo:

::<a metal:define-macro="portal_logo"
       id="portal-logo"
       accesskey="1"
       **tal:attributes="href view/navigation_root_url"**
       i18n:domain="plone">
        <img src="logo.jpg" alt=""
             **tal:replace="structure view/logo_tag"** />
    </a>

Primero tenemos la etiqueta del enlace:

Usted puede hacer caso omiso de *metal:define-macro="portal_logo" * esto
simplemente est? conteniendo o envolviendo el código en algo que pueda ser
re-usado nuevamente si es necesario.

El detalle importante es *tal:attributes="href view/navigation_root_url"*,
este el código que proporciona su sitio URL al atributo href.

Aquí hay una variable mágica, *view/navigation_root_url, * que paciera haber
surgido de la nada. De hecho, *vista* es una colección de propiedades
computados por el viewlet plone.logo viewlet and seamlessly passed to the
logo.pt template. Aquí están las propiedades disponibles:

navigation_root_urlProporciona la URL de su sitio (podría ser potencialmente
diferente si usted ha configurado un root de navegación distinta)
logo_tagbusca el nombre de la imagen del logotipo en base_properties,
encuentra la imagen, determina sus dimensiones y título y convierte todo esto
en una etiqueta de imagen HTML con los atributos apropiados. Revise
nuevamente el enfoque alternativo en la Sección 1 de este Cómo hacer para más
información en relación a base_properties.
portal_titleBusca y proporciona el título de su sitio

Ahora mire la etiqueta de imagen en la plantilla.

La clave aquí es *tal:replace="structure view/logo_tag"*. Esto significa que
la plantilla no cargará la etiqueta de imagen escrita aquí, sino que
**reemplazará todo** con la generada del viewlet plone.logo. Si usted no
quiere que esto pase, pues debería borrar esta linea.

Nota: *estructura* significa tratar el valor como HTML en lugar de una cadena
de texto.


Ejemplo 1: Un título de texto corriente

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Aquí tiene una versión personalizada de la plantilla, usando
*view/portal_title* en vez de *view/logo_tag*, para darle un encabezado de
texto en su lugar (si ha usado Plone 2, esto le puede parecer familiar)

::<h1 metal:define-macro="portal_logo"
       id="portal-logo">
       <a accesskey="1"
       tal:attributes="href view/navigation_root_url"
       i18n:domain="plone" **tal:content="view/portal_title**">
        </a>
    </h1>

Por supuesto que querrá proporcionar sus estilos propios, regrese a la
Sección 2 de este Cómo hacer para información de cómo definir estos en
ploneCustom.css. Puede ajustar este ejemplo para utilizar una técnica de
sustitución de imagen accesible en la CSS.


Ejemplo 2: Proporcionando su propia etiqueta de imagen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No tiene que utilizar logo_tag si no lo desea:

::<a metal:define-macro="portal_logo"
       id="portal-logo"
       accesskey="1"
       tal:attributes="href view/navigation_root_url"
       i18n:domain="plone">
        **<img src="[My logo ID]" alt="[My Logo]"

             width="[My Width]" height="[My Height]"

             tal:attributes="title view/portal_title" />**
    </a>

Obviamente necesitará subir su propio logotipo en la carpeta predeterminada
en portal_skins, revise las instrucciones en la Sección 1 de este Cómo hacer:


Más información
-----------------

-   En la sección Logotipo de la documentación de Plone hay más
    descripciones de Como hacer relacionados a métodos de personalización más
    avanzados.
-   Una mayor orientación sobre TAL y ZPT se puede encontrar en el
    tutorial de ZPT.

-   Si desea transferir los cambios al sistema de archivos en su propio
    producto de tema, a continuación, en las secciones siguientes de este
    manual de referencia, mostraremos un resumen de los archivos y plantillas
    que necesitará (`Sección del viewlet del Logotipo`_).




3. Enfoques
===========

Hay diferentes maneras de abordar temas de Plone. Aquí est? la información
para ayudarle a tomar una decisión sobre su enfoque; ya sea para basar su
tema en estructuras existentes, o para trabajar a través de la web o en el
sistema de archivos, si todavía necesita este manual para ejecutar estas
acciones.


3.1. ¿Empezar desde cero o basarse en Plone Default?
=====================================================

Es perfectamente posible crear su propio tema Plone desde cero, pero es
probable que no quiera hacer esto.


?Basarse en Plone Default?
---------------------------

En particular, las características avanzadas de la interfaz de edición de
Plone están empaquetadas como parte del tema por defecto: Plone Default, y es
probable que desee mantenerlos.

La buena noticia es que puede **basar** su propio tema en Plone Default y
entrelazar sus pedacitos de plantillas, estilos, scripts y componentes, con
los que ya existen. Hay tres maneras de hacerlo:

-   con el bloque Skin para construcción **personalice **los detalles de
    Plone Default (hay una manera elegante de hacer esto, la cual deja el
    tema Plone Default completamente intacto)

-   con el bloque Components para construcción **construya el suyo
    propio**, pero también puede **reusar** partes de componentes de Plone
    Default en el proceso
-   con la Configuración, simplemente ** agregue nuevas ** pautas


Hay otras buenas noticias: los elementos de un tema Plone se dividen en
partes muy pequeñas. Cada uno puede tratarse de manera independiente con
respecto a los demás, por lo que puede enfocarse tan sólo en las partes que
desea cambiar. El costo de toda esta flexibilidad es que a veces es difácil
localizar exactamente que parte desea, y las cosas podrían comenzar a parecer
complicadas. Este manual puede ayudarle con eso.

Puede cambiar bastante la apariencia sólo con sobrescribir los estilos CSS
existentes, o reescribiendo algunas de las hojas de estilo existentes. Sin
embargo, si usted quiere empezar a mover elementos de la página o rescribir
algo del XHTML, entonces usted necesita profundizar en las plantillas,
componentes y configuración con más detalle.

Al final de todo puede que surja con un tema basado en Plone Default (basado
estructuralmente, más no visualmente). Esto probablemente incluirá

-   su propia hoja de estilo, o los rescritos de algunas partes de la CSS
    de Plone
-   un reordenamiento de los elementos de la página

-   algunos rescritos de algunos elementos de la página

-   unos elementos "nuevos" de la página




3.2. ?A través de la Web o en el Sistema de archivos?
=======================================================

¿Cómo decidir si se debe construir su tema a través de la web o en el sistema
de archivos?

Tarde o temprano se enfrentar? con una decisión. Plone es lo suficientemente
flexible para que regularmente haya más una manera de hacer esto, y la
interrogante por lo general no es *cómo* hacerlo, sino a través de *cuál
camino*.

Se puede personalizar Plone Default a través de la web muy fácilmente,
especialmente el skin y los bloques de configuración para construcción. En
secciones posteriores de este manual le se?alaremos las dirección de los
lugares relevantes en la Interfaz de Administración de Zope para hacer esto.
Sin embargo, si desea mover estas personalizaciones a un nuevo sitio,
encargarse de personalizaciones bastante extensas, o construir un tema
completamente nuevo, pues entonces es recomendable mover su trabajo al
sistema de archivos.

En este caso necesitará crear un modulo instalable (también conocido como
producto de tema o huevo) Esta puede ser una perspectiva atemorizante, pero
se cuenta con herramientas para simplificar el proceso. Mediante un paquete
listo para usarse en el que se colocan todos los elementos de sus bloques
para construcción de temas. Explicaremos estas herramientas en las siguientes
páginas.

Si apenas est? comenzando, es una buena idea familiarizarse con los bloques
para construcción y las técnicas para trabajar a través de la web. No hay
ninguna dificultad en mover después lo que ha hecho al sistema de archivo.
Una vez que comience a reestructurar o mover componentes de un lado a otro
descubrir? que el sistema de archivos es una forma más cómoda para trabajar.


A través de la Web
-------------------

ProsContras
Rápido y sencilloDificultad para replicar o mover de un sitio a otro
Resultados inmediatamente visiblesPersonalizaciones de gran escala pueden
complicarse

Algunas personalizaciones no son posibles (ej.: no puede mover viewlets entre
administradores de viewlets)

En el Sistema de archivos
-------------------------

ProsContras
Portútil y reutilizableCurva de aprendizaje más abrupta cuando comience por
primera vez
Completa flexibilidad, puede escribir sus propios viewlets y portletsNecesita
acceso al sistema de archivos
Agrupa sus propios cambios dentro de sus propio tema / skinA menudo
necesitará reiniciar para ver los cambios


3.3. Direcciones futuras
========================

Este manual de referencia describe el enfoque actual de temas en Plone. Pero
de igual manera puede estar al tanto de que hay otros caminos en el
horizonte, quizás mucho más simples.

La tematización de Plone se est? complicando un poco. Así que la comunidad
Plone, a su manera inimitable y llena de energía, est? explorando diferentes
soluciones para el asunto de temas.

Las cosas se mueven rápidamente Al momento de diseñar, algunas de las
soluciones presentadas a continuación quizás ya no están lo suficientemente
desarrolladas para ser usadas muy seriamente, particularmente si usted est?
empezando. No obstante, debería investigarlas para ver cómo est?n
progresando:


Temas listos
------------

Un proyecto veloz y en curso para generar temas que se incluirán con el Plone
de caja, y aportes mediante lluvias de ideas para mejorar las historia de
temas en Plone:

-   `http://www.openplans.org/projects/ootb-plone-themes/summary`_


Deliverance
-----------

Deliverance es un programa ligero que aplica un tema a contenido de acuerdo a
un conjunto de reglas.

-   ` http://www.openplans.org/projects/deliverance/summary `_
-   ` http://blog.repoze.org/setting-up-deliverance-screencast-20071025.html `_






4. Herramientas
===============

Lleg? el momento de afilar sus lapices. Herramientas de autor, poniendo su
sitio Plone en modo de depuración, cómo crear un producto de tema (para
trabajar en el sistema de archivos).


4.1. Herramientas de autor
==========================

Si est? trabajando con el sistema de archivos, puede usar cualquier editor de
texto para escribir las plantillas, archivos de configuración (xml, zcml) y
las pequeñas cantidades de códigos en Python que necesitará.

Usted puede encontrar los siguiente útil:


Soporte Zope/Plone TextMate
---------------------------

-   `http://plone.org/products/textmate-support/`_

-   `http://dev.plone.org/collective/browser/textmate-support`_


Tendrá que revisar esto en el collective svn; instrucciones de cómo hacer
esto pueden encontrarse en http://svn.plone.org. Además hay una versión para
Windows de Textmate (`http://www.e-texteditor.com/`_).


Revisando la sintaxis de plantillas
-----------------------------------

Una ruta rápida y sucia para encontrar que hay de malo con una plantilla que
haya escrito usted mismo, es personalizarla a través de la Interfaz de
Administración de Zope. Sin embargo usted también puede configurar su propia
revisión, para correrla antes de que instale una plantilla en su sitio:

-   `http://docs.neuroinf.de/PloneBook/ch6.rst#conducting-syntax-checks`_

esto es un poco complejo si no se siente cómodo con Python, pero vale la pena
el esfuerzo a largo plazo.


Editores de código Python
--------------------------

Algo un poco más avanzado que el Bloc de notas le dar? el resaltado de código
para Python. Encontrará una lista completa aquí

-   `http://wiki.python.org/moin/PythonEditors`_.


Entorno de Desarrollo Integrado
-------------------------------

Si le apetece usar un IDE (Del inglés Integrated Development Environments),
tiene un montón de opciones, aunque estas están directamente orientadas al
desarrollo de Python más que a la escritura de plantillas para
personalización:

-   ` http://plone.org/documentation/how-to/developing-plone-with-eclipse-ide `_
-   ` http://plone.org/documentation/tutorial/debugging-plone-products-with-pida `_

Otros IDE incluyen Wing (`http://www.wingware.com/`_), BoaConstructor y
Komodo (`http://www.activestate.com/Products/komodo_ide/index.mhtml`_).




4.2. Modo de depuración
========================

Es inevitable no hacer las cosas bien la primera vez, por lo que necesita
asegurarse de que su sitio est? funcionando en modo de depuración.


Modo de depuración CSS
-----------------------

Plone empaqueta todos su archivos CSS dentro de uno o dos archivos para
eficiencia mediante el uso de un registro de recurso (para más información de
cómo funciona revise `CSS and JavaScript to Page section`_). Es mucho más
fácil ver lo que est? haciendo, si usted desactiva esta función cuando est?
dise?ando. Puede hacer lo mismo para JavaScript.

-   Vaya a la Configuración del sitio > Interfaz de Administración de
    Zope > portal_css o portal_javascripts
-   Marque la casilla de verificación para depuración


Modo de depuración Zope
------------------------

Si est? creando su propio producto de tema, se dar? cuenta que es útil correr
Zope en modo de depuración. Esto se configura en el archivo zope.conf el cual
puede encontrar en /etc en su instancia Zope. simplemente quite el # de esta
linea:

::#debug-mode = on

si est? utilizando buildout, puede configurarlo en buildout.cfg:

::[instance]
    debug-mode = on

Igualmente deber? reiniciar de tanto en tanto, aunque los cambios en la Skin
de su tema hechos sobre el sistema de archivo se actualizar?n inmediatamente.


?No puede ver sus cambios?
---------------------------

Cambios a....A través de la WebEn el Sistema de archivos
ComponentesDebe verlos inmediatamenteReinicie Zope
SkinsDebe verlos inmediatamenteEjecute Zope en modo de depuración
Hojas de estilo y JavaScriptCambie portal_css y portal_javascripts a
depuraciónCambie portal_css y portal_javascripts a depuración
ConfiguraciónDebe verlos inmediatamenteReinstale el producto con el quick
installer (instalador rápido)

Mensajes de error
-----------------

Plone trae un modulo de reporte de errores - PloneErrorReporting. Cuando
usted crea un sitio Plone, esta característica estar? lista para instalarse

-   Configuración del sitio > Agregar/Quitar Productos

Asegúrese de desinstalarla antes de ponga el sitio en modo de producción.


Evite reiniciar todo el tiempo

------------------------------

Si usted est? haciendo un trabajo extenso componentes del sistema, pronto se
cansar? de reiniciar Zope. `plone.reload`_ le ahorrar? tiempo. Agreguelo a su
configuración de buildout como cualquier otro huevo, vuelva a ejecutar
buildout y verá que puede recargar su código a través de su navegador.


4.3. Sobre el Sistema de archivos: Creando un producto de Tema
==============================================================

Si usted desea trabajar sobre el sistema de archivos, aquí est? la magia que
necesita para sostenerse sobre un cimiento de archivos y códigos


4.3.1. Resumen
==============

Si usted desea trabajar sobre el sistema de archivos, aquí est? la magia que
necesita para sostenerse sobre un cimiento de archivos y códigos

Esta sección lo guiar? a través del proceso requerido para crear su propio
tema en el sistema de archivos y la instalación de este en su propio sitio
Plone.

Las buena noticia es que usted mismo no tiene que escribir grandes cantidades
de código para crear el marco de su tema en el sistema de archivos, usted
puede usar un generador (Paster from ZopeSkel) para que haga el trabajo por
usted. Este le dar? un directorio que contiene un conjunto previamente
preparado de directorios y archivos,que puede aumentar o rescribir con sus
propias personalizaciones.

-   En la `Práctica 1: Cómo crear un producto de Tema de Plone 3 en el
    Sistema de archivos`_, usted usar? el generador de código para construir
    su cimiento. Esta práctica también le ayudar? con los archivos
    disponibles y sus respectivas funciones.

-   En la `Práctica 2: Cómo instalar su tema de Plone 3 usando
    buildout`_, usted har? que este producto est? disponible para su sitio
    Plone con respecto a su instalación y uso.







4.3.2. Práctica 1: Cómo crear un producto de Tema de Plone 3 en el Sistema de archivos
======================================================================================


4.3.2.1. Realice un jumpstart a su tema de desarrollo usando Paster
===================================================================

La manera más rápida y eficiente de comenzar no es creando las carpetas de su
tema y asociando los archivos hechos desde cero, sino tomando ventaja del
generador de un producto el cual le crear? el marco automáticamente para el
producto de tema, basado en las respuestas que proporcione a unas preguntas
interactivas.


Usando Paster a través de la Web

=================================

Nuevos usuarios se pueden sentir más cómodos usando una herramienta a través
de la web, que le permita generar un producto de tema. Una herramienta como
se encuentra en `http://paster.joelburton.com/`_. Es posible que desee hacer
referencia a parte de la información a continuación, para obtener más
detalles sobre lo que est? sucediendo a medida que responde estas preguntas.


Usando Paster en su computadora local

-------------------------------------

Usuarios que se sienten más cómodos usando la línea de comandos, tienen la
tendencia a usar una herramienta llamada ZopeSkel las plantillas Paster que
contiene. ZopeSkel es una colección de plantillas PasteScript las cuales
pueden usarse para generar rápidamente Zope y Plone como buildouts, productos
de arquetipos, y lo que más nos interesa, temas de Plone.


Ubique o Instale Paster

~~~~~~~~~~~~~~~~~~~~~~~

Para determinar si usted tiene Paster y ZopeSkel instalado, en la línea de
comandos pruebe con:

:: paster create --list-templates

o para verificar si Paster o ZopeSkel han sido instalados en el Python que
vino con su instalación Plone (de la versión 3.2 en adelante)

::[path to your buildout]/python-[version]/paster create --list-templates


Si "plone3_theme" no est? en la lista de plantillas disponibles, tendrá
entonces que `instalar Paster y/o ZopeSkel`_, como lo explica Daniel Nouri.


Cree su producto de Tema
~~~~~~~~~~~~~~~~~~~~~~~~

Si tiene Paster y ZopeSkel instalados, navegue al directorio donde le
gustaría crear su producto (nosotros recomendamos [your
buildout]/[zinstance|zeocluster/src]) y ejecute de la línea de comandos:

::$ paster create -t plone3_theme plonetheme.mytheme

o si tiene Paster en su instalación Plone:

::$ [path to your buildout]/python-[version]/paster create -t plone3_theme
plonetheme.mytheme


Esto iniciar? una serie de preguntas por el script de Paster. Las
predeterminadas son verdaderamente apropiadas para su primer tema, así en la
mayoría de los casos simplemente presione enter. este es un ejemplo del
resultado de una sesión interactiva.

::Selected and implied templates:
      ZopeSkel#basic_namespace  A project with a namespace package
      ZopeSkel#plone            A Plone project
      ZopeSkel#plone3_theme     A Theme for Plone 3.0

    Variables:
      egg:      plonetheme.mytheme
      package:  plonethememytheme
      project:  plonetheme.mytheme
    Enter namespace_package (Namespace package (like plonetheme)) ['plonetheme']:
    Enter package (The package contained namespace package (like example)) ['example']:mytheme
    Enter skinname (The skin selection to be added to 'portal_skins' (like 'My Theme')) ['']:My Theme
    Enter skinbase (Name of the skin selection from which the new one will be copied) ['Plone Default']:
    Enter empty_styles (Override default public stylesheets with empty ones?) [True]: False
    Enter include_doc (Include in-line documentation in generated code?) [False]:True
    Enter zope2product (Are you creating a Zope 2 Product?) [True]:
    Enter version (Version) ['1.0']:
    Enter description (One-line description of the package) ['An
    installable theme for Plone 3.0']:
    Enter long_description (Multi-line description (in reST)) ['']:
    Enter author (Author name) ['Plone Collective']:
    Enter author_email (Author email) ['product-
    developers@lists.plone.org']:
    Enter keywords (Space-separated keywords/tags) ['web zope plone theme']:
    Enter url (URL of homepage) ['http://svn.plone.org/svn/collective/']:
    Enter license_name (License name) ['GPL']:
    Enter zip_safe (True/False: if the package can be distributed as a .zip file) [False]:


Usted no puede utilizar la tecla de "borrar" para corregir un error de
escritura durante la sesión interactiva. Si comente un error entonces
presione ctrl-c para detener el script y empiece nuevamente.


Opciones de Paster
------------------

Algunas de estas preguntas requieren una explicación más detallada:

Enter namespace_packageEs una buena practica si usa el namespace (espacio de
nombres) "temaplone" para su tema. Obviamente puede usar otros espacio de
nombres, ("productos" puede ser otro), si tiene una razón valida, sino, use
"temaplone".Enter packageEl "package" (paquete) es simplemente el nombre en
minúsculas de su producto de tema, sin espacio o subguiones. Enter skinnameEl
"skinname" (nombreskin) es el nombre legible (alfabeto latino) para el nombre
de su tema. Es adecuado usar espacios y mayúsculasEnter skinbaseEn la mayoría
de los casos debería dejar esto como 'Plone Default'.
Enter empty_stylesResponder "True" (Verdad) tendrá como resultado que las
stylesheets (hojas de estilo) vacías se a?adan a su producto, lo que
sustituir? los archivos por defecto: base.css, public.css, y portlets.css que
est?n incluidos en cualquier sitio Plone que use el skin "Plone Default".
"False" (Falso) no agregar? ninguna stylesheet vacía. Para propósitos de esta
practica le recomendamos introducir "False"
Enter include_docResponder "True" causar? que la documentación en línea se
agregue a los archivos creados por ZopeSkel. Vale la pena hacer esto al menos
una vez, como parte de la documentación es bastante útil.Enter
zope2productResponder "True" har? que el paquete se pueda utilizar como un
huevo, listandose en la ZMI, carpetas de skin se registrar?n como capas con
la herramienta de Skins ("portal_skins"), y el perfil de Generic Setup
(configuración gen?rica) para el producto se puede cargar a través de la
herramienta de Instalación ("portal_setup"). Estudiaremos esto más adelante,
por ahora basta con decir que aquí siempre responder? "true" cuando quiera
generar un tema de Plone.Enter zip_safeQu?dese con el valor por defecto aquí.
`Creando nuevos huevos y paquetes rápidamente con Paster`_Cómo utilizar el
comando Paster para crear nuevos paquetes con las apropiadas setuptools
(herramientas de configuración) y diseños filesystem (archivos de sistema)
huevo-compatible e manera rápida y fácil.


4.3.2.2. Huevos Python, Instalación Gen?rica y Zope 3
=======================================================

Notas informativas sobre los cambios entre Plone 2.5 y Plone 3.

Productos, en el lenguaje de Plone, son an?logos a los módulos o extensiones
para otras aplicaciones. En el paso de Plone 2.5 a Plone 3, varios cambios
importantes se hicieron para la forma en que Plone manipula productos. En
primer lugar, algunos productos comenzaron a ser empaquetados ??como huevos
de Python, lo que los hizo más fáciles de administrar, distribuir e instalar.
En segundo lugar, los productos comenzaron a utilizar GenericSetup
(Instalación gen?rica) como medio para la instalación. Y en tercer lugar, los
productos incorporan cada vez más tecnolog?as Zope 3 (Z3) tales como vistas
del explorador.


Huevos Python
~~~~~~~~~~~~~

Un huevo python es simplemente un conjunto de archivos y directorios los
cuales constituyen un paquete de python. Estos huevos simplemente pueden
comprimirse, en tal caso aparecen como un sólo archivo *.egg, o pueden
descomprimirse. Huevos poseen un concepto y función similar a archivos JAR de
Java.

Los huevos son instalados a través de los marcos setuptools, un proyecto
paralelo de Python Enterprise Application Kit (Peak: Kit de Aplicación de
Empresa de Python) que provee administración y distribución para paquete (y
dependencia).

Si est? usando un control de versiones, querrá agregar *.egg-info y *.pyc a
los patrones ignorados en su instalación, para que los metadatos del huevo y
archivos python compilados no sean añadidos a su repositorio.

`Guía rápida para los huevos Python`_Un buen resumen de huevos y setuptools
por la gente de PEAK.`Hatch Python Eggs (Huevos Python) con SetupTools`_David
Metz revisa el marco de setuptools.


GenericSetup
~~~~~~~~~~~~

GenericSetup (GS) es una herramienta para la configuración de administración
del sitio en Plone usando archivos xml. GS permite exportar las
personalizaciones de un sitio Plone e importarlos a otro. Y hasta cierto
punto, la GS sustituye al QuickInstaller Portal (portal de instalación
rápida) (QI) posterior a Plone 2.5 en las que GS se puede utilizar para
instalar los productos. En productos que dependen de la GS, encontramos
archivos de configuración XML. En productos que utilizan versiones
anteriores, importante QI para la instalación, nos encontramos en comparación
con métodos de instalación escritos en python.

Tenga en cuenta que GenericSetup actualmente no le permite deshacer el perfil
aplicado durante la instalación. Puede desinstalar su tema usando el
Quickinstaller, no obstante, asumiendo que un método para desinstalar est?
presente.

Ya que nuestro producto de tema base utiliza GenericSetup para instalarse a
s? mismo, en brece estaremos configurando archivos xml requeridos por la GS.

`Comprensión y uso de GenericSetup en Plone`_Aunque ya est? un poco
desactualizada, el tutorial de Rob Miller para GS sigue siendo un recurso
útil para la formación en GS.`Mejoras de GenericSetup`_Más información de Rob
Miller sobre GS.`Aproveche AHORA el uso de GenericSetup y Tecnolog?as
Z3`_?impresione a su colegas utilizando GenericSetup y vistas Zope 3
eficientemente y con m?nimo esfuerzo! En este tutorial se muestra cómo
agregar un nueva vista, cómo usarla, cómo agregar un nuevo tipo de contenido
y cómo conectar y relacionar todo.
Tecnolog?a Zope 3
~~~~~~~~~~~~~~~~~~

A pesar de cualquier confusión con cualquier versión número-inducida,
recuerde que Plone 3 funciona con Zope 2. Zope 3 es una versión
dramáticamente cambiada de Zope 2, y algunas funcionalidades de Zope 3 se han
trabajado (Backport) para que funcionen con Zope 2. Para un completa
explicación de las tecnolog?as Zope 3 involucradas, consulte este tutorial:

`Personalización para desarrolladores`_Un breve recorrido de las
personalizaciones de Plone 3 por Martin Aspeli.


4.3.2.3. Anatomía de un producto de Tema en Plone
==================================================

Estructura del directorio y explicación de la funcionalidad de todos estos
archivos.



Asumiendo que usted haya creado su producto de tema con éxito, usted debería
tener una estructura de directorios que se ve más o menos así:

::    plonetheme.mytheme
        docs
             HISTORY.txt
             INSTALL.txt
             LICENSE.GPL
             LICENSE.txt
        MANIFEST.in
        plonetheme
             __init__.py
             mytheme
                 __init__.py
                 browser
                      __init__.py
                      configure.zcml
                      images
                           README.txt
                      interfaces.py
                      stylesheets
                           main.css
                           README.txt
                      viewlet.pt
                      viewlets.py
                 configure.zcml
                 profiles
                      default
                          cssregistry.xml
                          import_steps.xml
                          jsregistry.xml
                          metadata.xml
                          plonetheme.mytheme_various.txt
                          skins.xml
                          viewlets.xml
                 profiles.zcml
                 setuphandlers.py
                 skins
                      plonetheme_mytheme_custom_images
                           CONTENT.txt
                      plonetheme_mytheme_custom_templates
                           CONTENT.txt
                      plonetheme_mytheme_styles
                          base.css.dtml
                          base_properties.props
                          CONTENT.txt
                          portlets.css.dtml
                          public.css.dtml
                 skins.zcml
                 tests.py
                 version.txt
        plonetheme.mytheme-configure.zcml
        plonetheme.mytheme.egg-info
             dependency_links.txt
             entry_points.txt
             namespace_packages.txt
             not-zip-safe
             paster_plugins.txt
             PKG-INFO
             requires.txt
             SOURCES.txt
             top_level.txt
        README.txt
        setup.cfg
        setup.py
        zopeskel.txt


En este punto las cosas pueden parecer un poco complicadas pero no se
preocupe. Miremos con más detenimiento los archivos principales y directorios
de acuerdo a sus respectivas funciones.


Documentación
~~~~~~~~~~~~~~

docs/El directorio docs contiene instrucciones para instalación
(INSTALL.txt),, archivos de licencia, y el desarrollo del ingreso
(HISTORY.txt). README.txtEl archivo de texto de nivel-superior contiene la
descripción en una-línea del producto que ingres? durante la sesión
interactiva con ZopeSkel. Otros archivos README se encuentran contenidos por
todo el producto.
Paquete Python
~~~~~~~~~~~~~~

plonetheme/Este es un paquete espacio de nombres, que sirve para agrupar
otros paquetes.mytheme/Este es nombre real de su tema, habitualmente el
nombre del cliente o proyecto en el cual est? trabajando.
tests.pyLa evaluación de Python para nuestro paquete va aquí. Normalmente,
los temas no tienen mucho código Python, por lo que no tienen que hacer en el
proceso de evaluación.version.txtLa versión de nuestro producto. De igual
manera esta información se puede encontrar en /profiles/default/metadata.xml.
Huevo Python
~~~~~~~~~~~~

plonetheme.mytheme.egg-info/Los metadatos del huevo se almacenan
aquísetup.cfgEste archivo de configuración contiene información que se
utiliza para crear archivos de información de huevo.setup.pySi quisi?ramos
que setuptools maneje la instalación del paquete y las dependencias, se
podría instalar a través de "python setup.py install" (pero por el momento,
no lo haremos).
GenericSetup
~~~~~~~~~~~~

profiles.zcmlRegistro de perfiles GenericSetup apropiados.profiles/"Default"
es el perfil de configuración actual (solamente un perfil es automáticamente
creado, pero otros pueden ser añadidos) Dentro de nuestro perfil de
configuración tenemos archivos XML los cuales le comunican a GS cómo
configurar archivos CSS (cssregistry.xml), archivos Javascript
(jsregistry.xml), capas skin (skins.xml), y viewlets (viewlets.xml).
Metadata.xml rastrea el número de versión del producto y otros metadatos,
import_steps.xml _____ y la presencia de plonetheme.mytheme-various.txt le
transmite a GS para que busque setuphandlers.py por métodos adicionales.
Zope 3
~~~~~~

plonetheme.mytheme-configure.zcmlEste es el slug ZCML (Lenguaje de Marcado de
Configuración Zope) el cual deber? estar localizado en el etc/package-
includes si nuestro tema es instalado como un paquete Python (en nuestro caso
no lo será).configure.zcml
skins.zcmlRegistrar capas skin (imágenes, estilos, plantillas) como vistas de
directorios de filesystem (archivosdesistema)browser/
Stylesheets (hojas de estilo), Plantillas y más
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Una vez que tenga el producto de tema posicionado, el próximo paso es
modificar las piezas que Plone le otorga, específicamente plantillas,
stylesheets, y viewlets.

Templates/Las plantillas de Plone, específicamente la main_template que
controla el diseño del sitio Plone, puede ser tomada del directorio
parts/plone/CMFPlone/skins/plone_templates. La mayoría de las plantillas que
est?n contenidas aquí en 2,5 se han trasladado a huevos y son controladas por
viewlets. Para modificar una plantilla en este directorio, c?pielo a su
producto de tema, dentro la carpeta skins/templates y haga sus modificaciones
all?.
Stylesheets/La stylesheets por defecto de Plone se pueden encontrar en su
directorio buildout/parts/plone/CMFPlone/skins/plone_styles. Generalmente es
recomendable crear stylesheet específicas para su producto de tema, ej.
"mytheme.css" (donde "mytheme" es el nombre del produco de su tema), para
luego tomar cualquier estilo relevante de las stylesheets de CMFPlone y
personalizarlas en su propio producto, en vez de sustituir completamente las
stylesheets de CMFPlone. La excepción aquí puede ser IEFixes.css, la cual
posiblemente estar? de acuerdo en mantener intacta como un sólo archivo, ya
que expl?citamente se le llama del main_template.
Viewlets/Es una gran simplificación afirmar que con mayor frecuencia usted
estar? sustituyendo viewlets de huevos comúnmente denominados
plone.app.layout, plone.app.portlets y plone.app.content. Esos viewlets,
pueden encontrarse en su buildout/eggs/ en paquetes llamados
"plone.app.layout[xx]," "plone.app.portlets[xx]," y "plone.app.content[xx],"
donde [xx] es el número de versión. Cuando esos viewlets y sus respectivos
códigos son modificados pertenecen en el directorio de su producto de tema
browser/. Para más información de cómo trabajar con viewlets, `lea esta
tutorial`_.


Si modifica plantillas de páginas, no necesitará reiniciar Zope para que los
cambios surtan efecto. Sin embargo, cambios a Python, XML o ZCML, si
requieren reiniciar.

`Personalización para desarrolladores`_Un breve recorrido de las
personalizaciones de Plone 3 por Martin Aspeli.


4.3.3. Práctica 2: Cómo instalar su tema de Plone 3 usando Buildout
=====================================================================


4.3.3.1. Instalando su producto de Tema de base-huevo
=====================================================

En esta sección, examinaremos como instalar temas de base-huevo usando
buildout. En relación a Plone 3.1.2, todos los instaladores Plone crean un
buildout que contiene su instancia Plone. Al instalar o desarrollar temas,
buildout es muy recomendable.

 Para instalar el producto de tema creado en la práctica 1:

-   En primer lugar, si todavía no est? ah?, copie su producto de tema a
    [your buildout]/[zinstance|zeocluster]/src (en el caso de que este
    directorio no exista, puede crearlo usted mismo)
-   Luego, usando un editor de texto, edite su buildout.cfg (lo
    encontrará en [your buildout]/[zinstance|zeocluster]) y agregue la
    siguiente información dentro del buildout, y secciones de ZCML. . El
    archivo buildout.cfg real será mucho más largo que los fragmentos de
    código a continuación:

::[buildout]
     ...
     develop =
        src/plonetheme.mytheme

    [instance]
     eggs =
     ...
     plonetheme.mytheme

    zcml =
     ...
     plonetheme.mytheme

La última línea le indica al buildout que genere un fragmento de ZCML (slug)
que le dice a Zope que reconozca su producto de tema. Los puntos [...]
indican que usted puede tener líneas adicionales de código ZCML aquí.

-   Despu?s de actualizar la configuración, detenga su sitio y ejecute el
    comando ''bin/buildout'', el cual actualizar? su buildout.
-   Luego, reinicie su sitio y vaya a la página para "Configuración del
    sitio" en la interfaz de Plone y haga clic en el enlace "Add-on Products"
    (Agregar productos). El ?rea de "Configuración del sitio" también se le
    conoce como plone_control_panel, ya que esta es la URL utilizada para
    acceder a "Configuración del sitio".
-   Elija el producto (Mi tema 1.0) seleccionando la casilla que aparece
    junto a ella y haga clic en el botón 'Instalar'.

Nota: Puede que tenga que vaciar la caché del navegador Web para que surtan
los efectos de la instalación del producto.


Desinstalando un producto de Tema

---------------------------------

La deinstalación se puede hacer en la "Configuración del sitio" / en la
página "Add/Remove Products" (Agregar/remover productos) , pero sólo si usted
utiliz? esta misma pantalla ('Add/Remove Products' screen) para la
instalación. No todos los temas se desinstalan correctamente, pero la
reinstalación del tema Plone Default generalmente soluciona cualquier
problema.


4.3.3.2. Formación: productos de Temas hechos por Terceros.
============================================================

En esta sección, revisaremos cómo instalar un tema de Plone que haya
descargado de Plone.org/products, PyPi, etc. También vamos a mostrar cómo se
puede distinguir entre un producto estilo-viejo de 2.5 de uno nuevo base-
huevo.

Hay dos tipos de productos de temas: nuevos **productos base-huevo** , y
viejos productos de tema que se encuentran en el**"magical Products
namespace" ("espacio de nombres m?gico de productos")** . El tipo de producto
el tema con cual est? trabajando determina los pasos que debe seguir para
instalar el tema. Ahora veamos cómo distinguir la diferencia entre ambos.


?El producto es base-huevo o est? en el namespace de Productos?

-----------------------------------------------------------------

Primero tenemos que entender el significado de base-huevo. Si el tema, cuando
se descomprime, es nombrado "plonetheme.loquesea", o si genera un tema nuevo
usando la receta `Paster`_ y responde "yes" a la pregunta "is this a Zope2
product" (?Es este un producto Zope2?), pues su producto es base-huevo. O
incluso una manera más sencilla es saber si su carpeta root contiene
setup.py, si est? el archivo entonces es un huevo. En un t?pico producto de
tema base-huevo, setup.py lucir? más o menos así. en donde el texto resaltado
es el nombre del huevo.

::from setuptools import setup, find_packages

    version = '1.1'
    **

    setup(name='webcouturier.icompany.theme',

    **
    [...]**

    **

Si el producto parece como si hubiera sido creado mediante DIYPloneStyle 3.x
(ahora desactualizado), este est? almacenado en namespace. También puede
constatar que est? trabajando con un tema en Products namespace si no hay
setup.py en la carpeta root.


Instalando su producto base-huevo
---------------------------------

Recomendamos usar buildout para instalar un producto base-huevo. Puede
decidir si quiere descargar el paquete usted mismo o dejar que buildout lo
haga por usted. En caso de la primera opción, siga las instrucciones en la
sección previa. Si desea dejar el tema de la descarga al buildout, la
configuración de este es más simple:



[configuration here]


Dependencias

~~~~~~~~~~~~

Si otro paquete depende del huevo de tema o tiene su ZCML directamente, no es
necesario especificar nada en la configuración del buildout, ya que lo
detectar? automáticamente. Esto se considera un tema más avanzado.
Igualmente, si el tema de huevo depende de otro producto, el buildout se
encargará de esto también.


Instalando un producto si se encuentra en los namespace de Productos 2.x

------------------------------------------------------------------------

Siempre que el producto de tema sea un tema más viejo de 3.x y que se
encuentra en el namespace de los Productos, todo lo que tiene que hacer es
localizar el producto de tema en el directorio del buildout "products/" y
reiniciar su instancia Zope. No hay necesidad de volver a ejecutar el
buildout, porque no hemos cambiado ningún código ZCML.

Entonces, después de que su Zope se ha reiniciado, vaya a la página de
"Configuración del sitio" en la interfaz de Plone y haga clic en el enlace
"Añadir/Eliminar productos". El ?rea de "Configuración del sitio" también se
le conoce como plone_control_panel, ya que esta es la URL utilizada para
acceder a "Configuración del sitio".

Escoja el producto seleccionando la casilla que aparece junto a ella y haga
clic en el botón de instalar.

Temas más viejos en el namespace de Productos pueden aparecer dos veces en el
portal_quickinstaller, pero esto es un bug (error) que ha sido arreglado en
una versión más reciente de ZopeSkel. Usted puede ignorar el bug o
solucionarlo mediante la eliminación de esta línea de su archivo de producto
de tema configure.zcml para luego reiniciar su instancia Zope.

::<five:registerPackage package="." initialize=".initialize" />


Nota: Puede que tenga que vaciar la caché del navegador Web para que surtan
los efectos de la instalación del producto.


5. Bloques para construcción
=============================

Skin, Componentes, Configuración. Los tres bloques para construcción
principales de un tema; interconectados, pero cada con un tipo distinto de
comportamiento.


5.1. Resumen
============

Revisión general de los bloques para construcción y la forma en que se unen
para crear un tema.

En realidad, hay tres elementos principales en un tema. El siguiente diagrama
le muestra cómo estas ranuras se comportan en conjunto:

.. image:: images/image_large.png
  :alt: diagrama de bloques para construcción usados para crear un tema



Skin
----

-   Est? relacionado a la construcción general de una página y a la
    entrega de contenido
-   contiene plantillas de páginas, macros y scripts de Python, y es
    también el lugar para poner las hojas de estilo y JavaScript
-   para ayudarle a entender estos le apuntaremos en la dirección de
    tutoriales en el lenguaje TAL de plantillas y le presentaremos las capas
    de skin y el orden de precedencia
-   para encontrar elementos skin, busque en

    -   portal_skins en la Interfaz de Administración de Zope
    -   el directorio de skins en el producto de un sistema de archivos


Componentes
-----------

-   los parte de Componentes lidia (en su mayoría) con la decoración de
    la página, los elementos de página que poseen un nivel de consistencia de
    una página a otra, junto con elementos de página que presentan una
    actividad de procesamiento, tales como el árbol de navegación y los
    canales RSS
-   despliega una mezcla de clases Python y plantillas de página para
    crear viewlets, portlets y las vistas del explorador Web
-   para ayudarle a entender estas, le daremos un breve recorrido de cómo
    están conectadas entre sí con el ZCML, y le daremos la más corta de las
    introducciones a las partes de clases Python de las cuales realmente
    necesita saber
-   para encontrar las piezas que calzan para construir un componente,
    busque en

    -   portal_view_customizations in the Zope Management Interface
    -   the browser directory in a file system product


Configuración
--------------

-   la parte de Configuración lidia con determinar el orden de algunos
    elementos de páginas (o elementos individuales) en la página y con la
    estructuración automática de algunas configuraciones, que usted en caso
    contrario tendráa que hacer manualmente a través de la interfaz de la
    Configuración de sitio.
-   para ayudarle a comprender la configuración, le se?alaremos en la
    dirección de herramientas principales para la configuración manual, darle
    una vista general de la herramienta Generic Setup (instalación gen?rica)
    y el XML que se usa para la configuración automática
-   las herramientas de configuración se encuentran en varios lugares del
    sitio, pero los archivos necesarios para ejecutar una configuración de
    forma automática se encuentran en el directorio de perfiles de un
    producto del sistema de archivos


5.2. Skin
=======================================================

Plantillas, hojas de estilo, archivos Javascript, el modo de personalizarlos,
dónde encontrarlos.


5.2.1. Plantillas y el lenguaje de plantillas
=============================================

Plantillas y el lenguaje de plantillas


5.2.1.1. Plantillas y el lenguaje de plantillas
===============================================

Los elementos principales de un skin son las plantillas de página, imágenes,
scripts de Python, archivos CSS, y archivos JavaScript.


Plantillas de página (Zope)
----------------------------

Las plantillas de página (archivos .pt o ZPT) son una parte esencial de un
tema Plone y probablemente es el aspecto más fácil de dominar en Plone. Est?n
escritos en un lenguaje elegante de plantillas base-XML llamado TAL, a veces
hacen uso de macros (METAL), y en ocasiones incorporan expresiones Python
(c?lculos pequeños de una línea) o scripts de Python.

Hay varias introducciones excelentes para ZPT, y no se necesita mucho tiempo
para aprender TAL. Pruebe estas:

-   `Zope Page Templates tutorial on plone.org (Tutorial de Plantillas de
    página Zope en plone.org)`_
-   `ZPT Reference on Zope.org (Referencia de ZPT en Zope.org)`_

TAL es el único idioma que realmente recomendamos para que aprenda
correctamente. Para el resto puede escoger su camino o familiarizarse a
medida que avanza.

-   `Zope Page Template Tutorial on plone.org - Advanced Usage (Tutorial
    de Plantillas de página Zope en plone.org; uso avanzado)`_

Una página Web Plone se realiza mediante la agregación de plantillas, en
lugar de una sola, y hay un par de aspectos de las Plantillas de página Zope
que tendrá que tener en cuenta.


1. Ranura (Slot)
~~~~~~~~~~~~~~~~

Una ranura es una sección de una plantilla predefinida. Esta puede dejarse
vacía, o darle un contenido por defecto, pero est? disponible para ser
llenada en el momento. Un ranura est? definida en una plantilla con un código
como este:

::<metal:bodytext metal:define-slot="main" tal:content="nothing">
        .....
    </metal:bodytext>

Y llenada a través de otra plantilla como esta:

::<metal:main fill-slot="main">
     <h1 class="documentFirstHeading">
        ......
     </h1>
    </metal:main>

El tutorial ZPT en plone.org le guía a través de esto con más detalle, y la
sección `Plantillas y componentes para página`_ de este manual le muestra un
ejemplo.


2. Plantillas de vista de contenidos (_view)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

> Nota: el término "vista" también tiene una aplicación más técnica, por lo
que en el contexto de los Componentes (descrito posteriormente en este
manual) va a significar algo diferente.

Desde la perspectiva del usuario, contribuyente, o la del visitante, una
vista es la forma en que un elemento de contenido es presentado en la página.
Hay una `útil introducción`_ a este tema en el manual de usuario de Plone.

la plantillas que se utilizan para representar un elemento de contenido para
una vista poseen _view anexadas a sus nombres (ej., document_view.pt) y
pueden tener un título como "Standard View" (Vista estándar) Estas plantillas
en realidad so un conjunto de información a punto de encajar en ranuras.


Scripts
-------

Se trata de pequeñas funciones independientes para los momentos en que
necesita unas pocas líneas de código para realizar el c?lculo. En el sistema
de archivos poseen una extensión .py; Los encontrará en la Interfaz de
Administración de Zope como Script (Python).

He aquí un fragmento de la plantilla event_view (la vista de contenido para
el tipo de contenido evento), la cual utiliza un script de Python para dar
formato al campo de tiempo de acuerdo con el formato predeterminado para el
sitio. Si busca en CMFPlone/skins/plone_scripts, encontrará el
toLocalizedTime.py; sólo unas pocas líneas de código.

::<span metal:define-slot="inside"
                class="explain"
                tal:attributes="title python:here.end()"
tal:content="python:*here.toLocalizedTime*(here.end(),
                             long_format=1)">End
                             Date Time</span>





5.2.1.2. Comenzando
===================

Las Plantillas de página son una herramienta de generación de páginas Web. En
esta parte, revisaremos los fundamentos y mostraremos cómo utilizarlos en su
sitio Web para crear páginas Web din?micas fácilmente.

El objetivo de las Plantillas de página es flujo de trabajo natural. un
dise?ador usar? un editor HTML WYSIWYG (del ingl?s What You See Is What You
Get que se traduce como "Lo que ves es lo que obtienes") para crear una
plantilla, luego un programador lo editar? para que forme parte de una
aplicación. Si es requerido, el dise?ador puede cargar la plantilla *de
nuevo* dentro de su editor y realizar más cambios en su estructura y
apariencia. A través medidas razonables para preservar los cambios realizados
por el programador, ?l no va a alterar la aplicación.

Las plantillas de páginas apuntan a este objetivo mediante la adopción de
tres principios:

1.  Jugar agradablemente con herramientas de edición.

2.  Lo que ve es muy similar a lo que obtiene.

3.  Mantiene del código de plantillas, excepto por la lógica estructural.

Una Plantilla de página es como un modelo de páginas que se generar?. En
particular es una página valida HTML/XHTML. Puesto que HTML es altamente
estructurado, y los editores WYSIWYG cuidadosamente preservan esta
estructura, hay l?mites estrictos en la forma en que el programador puede
cambiar una página y seguir respetando el primer principio

A pesar de que las Plantillas de página son adecuadas para programadores y
dise?adores que necesitan trabajar juntos para crear páginas web din?micas
construyendo la base para la mayoría de páginas Plone, usted igualmente
debería aprender al menos un poco sobre esto si es necesario personalizar el
aspecto de Plone o el diseño . Además, puede ser más sencillo de usarlas y
entenderlas que la alternativa DTML (Lenguaje de Marcado de Documento de
Plantilla). .


Pero, ?Por qu? otro Lenguaje de plantilla?
--------------------------------------------

Hay una gama de sistemas de plantillas en el mercado, algunas de ellas
populares como ASP, JSP, y PHP. Desde el principio, Zope siempre ha integrado
un lenguaje de plantilla llamado DTML. ?Por qu? inventar otro?

En primer lugar ninguno de estos sistemas de archivos están dirigidos a
dise?adores de HTML. Una vez que una página se ha convertido en una
plantilla, no es HTML v?lido, por lo que es difácil trabajarla fuera de la
aplicación. Cada uno de ellos viola el primer o segundo principio de
Plantillas de página de Zope en cierto grado u otro. Los programadores no
deberían "secuestrar" el trabajo de los dise?adores y convertir el HTML en
software. XMCL, parte del proyecto Enhydra, comparte nuestro objetivo, pero
requiere que el programador escriba cantidades considerables de código de
soporte Java para cada plantilla.

En segundo lugar, todos estos sistemas sufren con respecto a la separación
entre presentación, lógica y contenido (datos). Sus violaciones del tercer
principio disminuyen la escalabilidad de la administración de contenidos y
los esfuerzos de desarrollo de sitios Web que utilizan estos sistemas.


Aplicando los principios
------------------------

Las Plantillas de página usan **Template Attribute Language (TAL) (Lenguaje
de Atributo de Plantillas)**. TAL consiste en atributos especiales de
etiquetas, por ejemplo, el título de una página din?mica puede lucir como
este:

::      <title tal:content="context/title">Page Title</title>

El atributo ``tal:content`` es una sentencia TAL. Debido a que tiene un
namespace XML (la parte ``tal:``) la mayoría de herramientas de edición no se
quejar?n por no entenderlo, y no lo eliminar?n. No cambiar? la estructura o
apariencia de la plantilla cuando se carga en el editor WYSIWYG o en un
navegador Web. El nombre ``content`` (contenido) indica que definir? el
contenido de la etiqueta ``title`` (título), y el valor "context/title" es
una expresión que provee el texto a insertar en la etiqueta

Para el dise?ador HTML que usa una herramienta WYSIWYG, esto es HTML
perfectamente v?lido, y se muestra en el editor de la manera en que un título
debería verse. El dise?ador que no preocupa por los detalles de aplicación de
TAL, sólo ve una * maqueta * de la plantilla din?mica, con valores ficticios
como "Page Title" (Título de página) para el título del documento.

Cuando esta plantilla se guarda en Zope y es vista por un usuario, Zope
convierte este contenido est?tico en contenido din?mico y reemplaza "Page
Title", con lo que sea que "context/title" resuelva. En este caso,
"context/title" se resuelve en el título del objeto para el cual se aplica la
plantilla. Esta sustitución se realiza de forma din?mica, cuando la plantilla
se ve.

Este ejemplo demuestra también el segundo principio. Cuando usted ve la
plantilla en un editor, el texto del título actuar? como un marcador de
posición para el texto del título din?mico, la plantilla proporciona un
ejemplo de cómo los documentos generados se verán.

Hay comandos de plantilla para la sustitución de etiquetas completas, su
contenido, o sólo algunos de sus atributos. Usted puede repetir una etiqueta
varias veces u omitirla por completo. Puede unir partes de varias plantillas,
y especificar el tratamiento de errores simples. Todas estas funciones son
usadas para generar estructuras de documentos, usted **no puede** crear
subrutinas o clases, escribir bucles o pruebas multi-modo, o fácilmente
expresar algoritmos complejos. Para estas tareas, utilice Python.

El lenguaje de plantillas deliberadamente no es tan poderoso y objetivo-
general como podría ser. Est? destinado a ser utilizado dentro de un marco
(como Zope) en el que otros objetos manejan la lógica de negocio y aquellas
tareas no relacionadas con el diseño de la página.

Por ejemplo, el lenguaje de plantillas seráa ventajoso para renderizar una
página de factura, al generar una fila para cada elemento, e insertar la
descripción, cantidad, precio, y otros para el texto de cada fila. No se pude
utilizar para crear el registro de la factura en una base de datos o para
interactuar con un centro de procesamiento de tarjetas de cr?dito.


Creando una Plantilla de página
--------------------------------

Si usted dise?a páginas, probablemente use FTP o WebDAV en vez de la Interfaz
de Administración de Plone (ZMI) para crear y editar Plantillas de páginas, o
desarrolla plantillas en el filesystem para su posterior instalación. Si
usted no es el due?o del sitio Zope, pregunte a su administrador Zope por
instrucciones, pero para los pequeños ejemplos mostrados en este artículo, es
mucho más sencillo usar la ZMI. Para más información sobre el uso de FTP o
WebDAV con Zope, vea ` The Zope Book (el Libro de Zope)`_ o el `artículo
WebDAV`_ de Jeffrey Shell.

También puede usar `Emacs`_, `cadaver`_, o algún otro cliente, pero si usted
es un programador o administrador de Zope, lo más seguro es que use la ZMI de
igual manera, al menos ocasionalmente. Revise el Libro de Zope para
instrucciones sobre la configuración de este para que trabaje con varios
clientes.

Use su navegador Web para entrar en la Interfaz de Administración de Zope
como lo haría normalmente con Zope. Escoja una carpeta (root est? bien) y
seleccione "Page Template" (Plantilla de página) de la lista desplegable.
Escriba "simple_page" en el campo de ``Id`` del formulario para agregar,
luego pulse el botón "Agregar y Editar".

Ahora debería ver la página principal de edición para la nueva Plantilla de
página. El título est? en blanco, el tipo-contenido es ``text/html``, y el
texto de la plantilla por defecto est? en el ?rea de edición.

Ahora crear? una página din?mica muy simple. Escriba las palabras "Simple
Page" (página simple) en el campo de ``Título``. Luego edite el cuerpo de
texto de la plantilla para que luzca como este:

::      This is <b tal:replace="template/title">the Title</b>.

Ahora presione el botón de guardar cambios, y la página de edición debería
mostrar un mensaje confirmando que los cambios han sido guardados. Si un
mensaje de error aparece en la parte de arriba del ?rea de código, o algún
texto que comienza con ``<-- Page Template Diagnostics (diagn?stico de
plantilla de página)`` se ha añadido a la plantilla, entonces revise que
escribi? el ejemplo correctamente y gu?rdelo nuevamente. No necesita borrar
el comentario de error, ya que una vez que este haya sido corregido
desaparecer?.

Haga clic en la pestaña ``Test`` (Prueba). debería ver una página casi
completamente vacía con "This is a simple Page" (Esto es una página simple)
en la parte superior.

Respalde, y haga clic en el enlace "Browse HTML source" (Examinar fuente
HTML) bajo el campo de tipo-contenido. Esto le mostrar? la fuente *no
renderizada o procesada* de la plantilla. debería ver "This is (Esto es)
**the Title (el título)**." retorne nuevamente, para que así este listo para
editar más a?n el ejemplo.


Expresiones simples
-------------------

El texto "template/title" (plantilla/título) en su simple Plantilla de página
es una *expresión de ruta*. Este el tipo más común de expresiones definidas
por la Sintaxis de Expresiones TAL (TALES). Manda a buscar la propiedad del
``título`` de la plantilla. Aquí hay otras expresiones comunes de ruta:

-   request/URL: La URL de la solicitud actual de Web.

-   user/getUserName: el nombre de usuario autenticado para el inicio de
    sesión.

-   container/objectIds: una lista de Ids (Identificaciones) de los
    objetos que están en la misma Carpeta de las plantillas.

Cada ruta comienza con una nombre variable. Si la variable contiene el valor
que usted quiere, detengase all?. Caso contrario, agregue una barra (``/``) y
el nombre de un sub-objeto o propiedad. Es posible que tenga que pasar a
través de varios sub-objetos para llegar al valor que usted est? buscando.

Hay una construcción pequeña en un conjunto de variables tales como ``request
(solicitud)`` y ``user (usuario)``, que serán listados y descritos
posteriormente, y también aprendi? a cómo definir sus propias variables.


Insertando texto
----------------

En su plantilla "simple_page", utiliz? la sentencia ``tal:replace`` en una
etiqueta en negrita. Cuando la prob?, esta remplaz? la etiqueta completa por
el título de la plantilla. Por otra parte cuando examin? el código, vio el
texto de la plantilla en negrita. Nosotros hemos utilizado una etiqueta en
negrita para resaltar la diferencia.

Con el fin de colocar el texto din?mico dentro de otro texto, se suele usar
``tal:replace`` en una etiqueta ``span (lapso)``. Agregue las líneas
siguientes a su ejemplo:

::      <br>
          The URL is <span tal:replace="request/URL">URL</span>.

La etiqueta ``span`` es estructural, no visual, así que esta luce como "The
URL is URL." (La URL es URL), cuando vea el código en un editor o navegador.
Cuando vea la versión renderizada, esta puede lucir a algo como esto:

::      <br>
          The URL is http://localhost:8080/simple_page.

Recuerde que tiene que tener cuidado cuando este editando y no destruir el
``span`` o ingresar etiquetas de formato tales como ``b`` o ``fuente`` dentro
de este, ya que también serán remplazadas.

Si quiere insertar texto en una etiqueta sin modificarla como tal,
use``tal:content``. Para definir el título de su página de prueba al título
de propiedad de la plantilla, agregue las líneas siguientes encima del otro
texto:

::      <head>
            <title tal:content="template/title">The Title</title>
          </head>

Si usted abre la pestaña Test en una nueva ventana, el título que tendrá la
ventana será "a Simple Page" (una página simple).


Repitiendo estructuras
----------------------

Ahora agregar? contexto a su página, en la forma de una lista de objetos
almacenados en la misma carpeta. Crear? una tabla que una fila numerada para
cada objeto, y columnas para el ID, meta-type, y título. Agregue estas líneas
a la parte inferior de su plantilla:

::      <table border="1" width="100%">
            <tr>
              <th>#</th><th>Id</th><th>Meta-
              Type</th><th>Title</th>
            </tr>
            <tr tal:repeat="item container/objectValues">
              <td tal:content="repeat/item/number">#</td>
              <td tal:content="item/id">Id</td>
              <td tal:content="item/meta_type">Meta-Type</td>
              <td tal:content="item/title">Title</td>
            </tr>
          </table>

La sentencia ``tal:repeat`` en la fila de tabla se traduce en "repita esta
fila para cada elemento en mi lista contenedora de valores de objetos".
Repetir la sentencia coloca los objetos de la lista dentro de la variable del
``elemento`` uno a la vez, y hace una copia de la fila usando esa variable.
El valor de "item/id" en cada fila es la ID del objeto para esa fila.

Puede usar cualquier nombre que le parezca para la variable del item
(elemento), siempre y cuando comience con una letra y contenga sólo letras,
números, y subguiones (``_``). Esta sólo existe en la etiqueta <tr> tag; si
la trata de usar por encima o por debajo de esa etiqueta obtendrá un error.

También puede usar el nombre de la variable ``tal:repeat`` para obtener
información sobre la repetición actual. Coloc?ndola después de la variable
incorporada ``repetida`` en una ruta, puede acceder a la cuenta de repetición
comenzando a partir de cero (``index``), de uno (``number``), de "A"
(``Letter``), y de otras maneras. De esta manera la expresión
``repeat/item/number`` será ``1`` en la primera fila, ``2`` en la segunda
fila, y así sucesivamente.

Ya que un bucle ``tal:repeat`` puede colocarse dentro de otro, más de uno
puede estar activo al mismo tiempo. Por esta razón debe escribir
``repeat/item/number`` en vez de ``repeat/number``. Usted debe especificar el
bucle por el que est? interesado incluyendo el nombre de este.


Elementos condicionales
-----------------------

Vea la plantilla, y se dar? cuenta de que la tabla es muy sobria. Vamos a
mejorarla dandole sombra a ciertas filas. Copia de la segunda fila de la
tabla, luego edite el código para que se vea así:

::      <table border="1" width="100%">
            <tr>
              <th>#</th><th>Id</th><th>Meta-
              Type</th><th>Title</th>
            </tr>
            <tbody tal:repeat="item container/objectValues">
              <tr bgcolor="#EEEEEE"
              tal:condition="repeat/item/even">
                <td tal:content="repeat/item/number">#</td>
                <td tal:content="item/id">Id</td>
                <td tal:content="item/meta_type">Meta-
                Type</td>
                <td tal:content="item/title">Title</td>
              </tr>
              <tr tal:condition="repeat/item/odd">
                <td tal:content="repeat/item/number">#</td>
                <td tal:content="item/id">Id</td>
                <td tal:content="item/meta_type">Meta-
                Type</td>
                <td tal:content="item/title">Title</td>
              </tr>
            </tbody>
          </table>

La ``tal:repeat`` no ha cambiado, simplemente la ha movido a la nueva
etiqueta ``tbody``. Esta es una etiqueta HTML estándar destinada a agrupar
las filas del cuerpo de una tabla, que es la manera en que las est?
utilizando. Hay dos filas en el cuerpo con columnas id?nticas, y una tiene un
fondo gris.

Si ve el código de la plantilla, verá dos filas. Si usted no hubiera agregado
la sentencia ``tal:condition`` a la filas, la plantilla generar?a ambas filas
para cada elemento, que es algo que usted no quiere. La sentencia
``tal:condition`` en la primera fila asegura que sólo sea agregada en
repeticiones de indexación-par, mientras que la segunda condición sólo le
permite aparecer en repeticiones de indexación-impar.

Una sentencia ``tal:condition`` no hace nada si su expresión tiene un valor
verdadero, pero elimina la etiqueta de declaración en su totalidad,
incluyendo su contenido, si el valor es falso. Las propiedades ``par`` e
``impar`` de ``repeat/item`` son cero o uno. El número cero, una cadena en
blanco, una lista vacía, y la variable integrada ``nothing (nada)`` son todos
valores falsos. Casi cualquier otro valor es verdadero, otros números a parte
del cero, y cadenas con cualquier cosa dentro de ellas (?incluso espacios!).


Definiendo variables
--------------------

Nota: de Plone 4 en adelante, use *container/values* en lugar de
*container/objectValues* de abajo..


La plantilla mostrar? siempre al menos una fila, ya que la propia plantilla
es uno de los objetos listados. En otras circunstancias, puede existir la
posibilidad de que quiera que la tabla este vacía. Supongamos que usted
quiere en este caso, omitir toda la tabla. Esto lo puede hacer agregando
``tal:condition`` a la tabla:

::      <table border="1" width="100%"
                 tal:condition="container/objectValues">

Ahora cuando no haya objetos, ninguna parte de la tabla será incluida en el
diseño. Sin embargo cuando haya objetos, la expresión
"container/objectValues" será evaluada dos veces, lo cual es un poco
ineficiente. Además, si usted quiere cambiar la expresión, tendráa que
cambiarla en ambos lugares.

Para evitar estos problemas, puede definir una variable para que contenga la
lista y luego usarla en ambos casos: ``tal:condition`` y ``tal:repeat``.
Cambie las primeras líneas para que se vean así:

::      <table border="1" width="100%"
                 tal:define="items container/objectValues"
                 tal:condition="items">
            <tr>
              <th>#</th><th>Id</th><th>Meta-
              Type</th><th>Title</th>
            </tr>
            <tbody tal:repeat="item items">

La sentencia ``tal:define`` crea la variable ``items``, y la puede usar en
cualquier parte de la etiqueta de la tabla. Note también cómo puede tener dos
atributos TAL en la misma etiqueta ``table``. De hecho puede tener tantas
como quiera, en este caso, son evaluadas en orden La primera asigna la
variable ``items`` y la segunda usa ``items`` en una condición para ver si es
falsa (en este caso, una secuencia vacía) o verdadera.

Ahora supongamos que en lugar de simplemente no mostrar la tabla cuando no
hay elementos, usted desea mostrar un mensaje. Para hacer esto, introduzca lo
siguiente encima de la tabla:

::      <h4 tal:condition="not:container/objectValues">There
          Are No Items (No hay elementos)</h4>

La variable ``items`` no la puede usar todavía, ya que no est? definida. Si
usted mueve la definición a la etiqueta ``h4``, no la puede usar más en la
etiqueta ``table``, porque se convierte en una variable *local* de la
etiqueta ``h4``. Puede situar la definición en una etiqueta que encierre a
ambas ``h4`` y ``table``, pero hay una solución más simple. Al colocar la
palabra clave ``global`` delante del nombre de la variable, hace que la
definición dure desde la etiqueta ``h4`` hasta el fondo de la plantilla:

::      <h4 tal:define="global items container/objectValues"
              tal:condition="not:items">There Are No Items</h4>
          <table border="1" width="100%"
              tal:condition="items">

El ``not:`` en la primera ``tal:condition`` es un tipo prefijo de expresión
que puede ser ubicado delante de cualquier expresión. Si la expresión es
verdadera, ``not:`` es falso y viceversa.


Cambiando atributos
-------------------

La mayoría, sino todos, de objetos listados por su plantilla tiene una
propiedad ``icono``, que contiene la ruta al icono para ese tipo de objeto.
Con el fin de mostrar este icono en la columna meta-type, tendrá que insertar
esta ruta dentro del atributo ``src`` de una etiqueta ``img``, mediante la
edición de la columna meta-type en ambas filas para que se vean así:

::      <td>
              <img src="/misc_/OFSP/Folder_icon.gif"
                   tal:attributes="src item/icon">
              <span tal:replace="item/meta_type">Meta-
              Type</span>
          </td>

La sentencia ``tal:attributes`` remplaza el atributo ``src`` de la imagen con
el valor de ``item/icon``. El valor de ``src`` en la plantilla act?a como un
marcador de posición, de modo que la imagen no est? da?ada, y sea del tamaño
correcto.

Ya que el atributo ``tal:content`` hubiera remplazado los contenidos
completos de la celda, incluyendo las imágenes con le texto meta-type, este
tiene que ser eliminado. En su lugar, se inserta el meta-type en línea de la
misma manera como la dirección URL en la parte superior de la página.

Based on the `Zope Book`_, ? `Zope Corporation`_


5.2.1.3. Macros y ranuras
=========================


Macros
------

Hasta ahora, ha visto cómo las Plantillas de página se pueden utilizar para
añadir comportamientos din?micos a las páginas Web individuales. Otra
característica de las Plantillas de página es la posibilidad de reutilizar
elementos de apariencia a través de muchas páginas.

Por ejemplo, con las Plantillas de página, puede tener un sitio que tenga un
aspecto estándar. Y no importa el "contenido" de una página, igual tendrá un
encabezado estándar, barra lateral, pie de página, y/u otros elementos de
página. Este es un requisito muy común para los sitios web, y así es
exactamente como funciona Plone.

Puede reutilizar los elementos de presentación a través de las páginas con
**macros** . Los Macros definen la sección de una pagina que puede ser
reutilizada en otras páginas. Un macro puede ser una página completa, o sólo
una parte de ella como el encabezado o pi? de página. Despu?s de que define
uno o más macros en una Plantilla de página, puede usarlos en otras
Plantillas de páginas.


Usando macros
~~~~~~~~~~~~~

Puede definir macros con atributos de etiqueta similares a las sentencias
TAL. Atributos de etiquetas macro son también denominados sentencias **Macro
Expansion Tag Attribute Language (METAL) o en espa?ol Lenguaje de Expansión
Macro para Atributos de Plantillas**. Aquí hay un ejemplo de definición
macro:

::<p metal:define-macro="copyright">
      Copyright 2008, <em>Foo, Bar, and Associates</em> Inc.
    </p>

Esta sentencia metal:define-macro define un macro llamado "copyright". El
macro consiste del elemento p (incluye todos los elementos contenidos que
terminan con una etiqueta de cierre p).

Los macros definidos en una Plantilla de página son almacenados en el
atributo *macros* de la plantilla. Puede usar los macros de otra Plantilla,
refiri?ndose a ellos a través del atributo *macros* de una Plantilla de
página en la cual están definidos. Por ejemplo supongamos que el macro
*copyright* est? en una Plantilla de página llamada "master_page". Aquí est?
como usar el macro *copyright* desde otra Plantilla de página:

::<hr />
    <b metal:use-macro="container/master_page/macros/copyright">
      Macro goes here
    </b>


En esta Plantilla de página el elemento b será completamente remplazado por
el macro cuando Zope renderice la página.

::<hr />
    <p>
      Copyright 2008, <em>Foo, Bar, and Associates</em> Inc.
    </p>

Si usted cambia el macro (por ejemplo si cambia el titular de los derechos de
autor), todas las Plantillas de página que usen este macro automáticamente
reflejaran el cambio.

Note cómo el macro es identificado por una expresión de ruta utilizando la
sentencia metal:use-macro. La sentencia metal:use-macro remplaza el elemento
de sentencia con el macro nombrado.


Detalles macro
~~~~~~~~~~~~~~

Las sentencias metal:define-macro y metal:use-macro son bastante sencillas.
No obstante hay algunas sutilezas en sus usos, que vale la pena mencionar.

El nombre de un macro debe ser único dentro de la Plantilla de página en la
que se define. Puede definir más de un macro en una plantilla, pero todos
necesitan nombres distintos.

También hay que se?alar que a pesar del atributo define-macro, el macro sigue
siendo una sección regular de la plantilla; así que cuando llama a la
plantilla completa, la sección macro es renderizada con el diseño de la
página igual que cualquier otra sección de la misma. Cuando usa el atributo
define-macro simplemente est? **agregando** una especie de "ancla" a esa
sección, por lo que se puede llamarse desde otra parte, pero no va a cambiar
nada respecto al comportamiento de la misma sección en la propia plantilla.

Normalmente usted hace referencia a un macro en una sentencia metal:use-macro
con una expresión de ruta. Sin embargo, puede utilizar cualquier tipo de
expresión que desee, siempre y cuando devuelva un macro. Por ejemplo:

::<p metal:use-macro="python:context.getMacro()">
      Replaced with a dynamically determined macro,
      which is located by the getMacro script.
    </p>

En este caso la expresión de ruta devuelve un macro definido din?micamente
por el script getMacro. El uso de expresiones Python para localizar macros le
permite variar de forma din?mica cual macro su plantilla utiliza.

Puede usar la variable por defecto con la sentencia metal:use-macro:

::<p metal:use-macro="default">
      This content remains - no macro is used
    </p>

El resultado es el mismo que al usar default con tal:content y tal:replace.
El contenido "default" en la etiqueta no cambia cuando sea renderizado. Esto
puede ser útil si usted necesita condicionalmente utilizar un macro o caer en
el contenido por defecto si este no existe.

Si trata de utilizar la variable nothing con metal:use-macro obtendrá un
error ya que nothing no es un macro. Si usted quiere utilizar nothing para
que condicionalmente incluya un macro, debería entonces encerrar la sentencia
metal:use-macro con una sentencia tal:condition.

Zope maneja macros primero al renderizar sus plantillas. Luego Zope eval?a
las expresiones TAL. Por ejemplo, considere este macro:

::<p metal:define-macro="title"
       tal:content="template/title">
      template's title
    </p>

Cuando se utiliza este macro se insertar? el título de la plantilla en la
cual el macro es utilizado, y no el título de la plantilla en la que se
define el macro. En otras palabras, cuando se utiliza un macro, es como
copiar el texto de un macro dentro de la plantilla y luego renderizar su
plantilla.


Usando ranuras (slots)
----------------------

Las macros son mucho más útiles si se pueden anular partes de ellos al
momento de utilizarlos. Puede hacer esto definiendo **slots (ranuras)** en el
macro que puede llenar cuando use la plantilla. Por ejemplo, considere un
macro de barra lateral:

::<div metal:define-macro="sidebar">
      Links
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/products">Products</a></li>
        <li><a href="/support">Support</a></li>
        <li><a href="/contact">Contact Us</a></li>
      </ul>
    </div>

Este macro est? bien, pero supongamos que le gustar?a incluir información
adicional en la barra lateral sobre algunas páginas. Una manera de lograr
esto es con ranuras:

::<div metal:define-macro="sidebar">
      Links
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/products">Products</a></li>
        <li><a href="/support">Support</a></li>
        <li><a href="/contact">Contact Us</a></li>
      </ul>
      <span metal:define-slot="additional_info"></span>
    </div>

Cuando use este macro puede elegir ocupar la ranura de este modo:

::<p metal:use-macro="container/master_page/macros/sidebar">
      <b metal:fill-slot="additional_info">
        Make sure to check out our <a href="/specials">specials</a>.
      </b>
    </p>

Cuando renderice esta plantilla la barra lateral incluirá información
adicional que usted haya proporcionado en la ranura:

::<div>
      Links
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/products">Products</a></li>
        <li><a href="/support">Support</a></li>
        <li><a href="/contact">Contact Us</a></li>
      </ul>
      <b>
        Make sure to check out our <a href="/specials">specials</a>.
      </b>
    </div>

Note cómo el elemento span que define la ranura es remplazado con el elemento
b para que llene la ranura.


Personalizando presentación por defecto
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Un uso común de la ranura es proporcionar presentación por defecto la cual
puede personalizar. En el ejemplo de ranura de la última sección, la
definición de ranura era simplemente un elemento span vacío. Sin embargo,
usted puede proporcionar presentación por defecto en una definición de
ranura. Por ejemplo, considere este macro revisado de barra lateral:

::<div metal:define-macro="sidebar">
      <div metal:define-slot="links">
      Links
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/products">Products</a></li>
        <li><a href="/support">Support</a></li>
        <li><a href="/contact">Contact Us</a></li>
      </ul>
      </div>
      <span metal:define-slot="additional_info"></span>
    </div>

Ahora la barra lateral es completamente personalizable. Puede llena los
enlaces de la ranura para red?finir los enlaces de la barra lateral. Sin
embargo, si decide no ocupar el puesto de enlaces obtendrá entonces los
v?nculos predeterminados que aparecen dentro de la definición de la ranura.

Usted puede incluso tomar esta técnica más a fondo mediante la definición de
ranuras dentro de ranuras. Esto le permite sustituir presentación por defecto
con un buen grado de precisión. Aquí hay un macro de barra lateral que define
ranuras dentro de ranuras:

::<div metal:define-macro="sidebar">
      <div metal:define-slot="links">
      Links
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/products">Products</a></li>
        <li><a href="/support">Support</a></li>
        <li><a href="/contact">Contact Us</a></li>
        <span metal:define-slot="additional_links"></span>
      </ul>
      </div>
      <span metal:define-slot="additional_info"></span>
    </div>

Si usted desea personalizar los enlaces de la barra lateral puede llenar las
ranuras de *enlaces* para sustituir los enlaces completamente, o puede llenar
la ranura *additional_links* para insertar algunos enlaces adicionales
después de los enlaces predeterminados. Usted puede modificar ranuras tanto
como quiera.


Combinando METAL y TAL
----------------------

Usted puede usar ambas sentencias METAL y TAL en los mismos elementos. Por
ejemplo:

::<ul metal:define-macro="links"
        tal:repeat="link context/getLinks">
      <li>
        <a href="link_url"
           tal:attributes="href link/url"
           tal:content="link/name">link name</a>
      </li>
    </ul>

En este caso, getLinks es un script (imaginario) que reúne una lista de
objetos de enlace, posiblemente usando un consulta de Cat?logo.

Ya que las sentencias METAL son evaluadas primero que las sentencias TAL, no
hay conflictos. Este ejemplo es interesante también porque personaliza un
macro sin usar ranuras. El macro llama el script getLinks para determinar los
enlaces. De esta manera puede personalizar los enlaces de su sitio
r?definiendo el script getLinks sobre distintas locaciones dentro de su
sitio.

No siempre es fácil descubrir la mejor manera de personalizar el aspecto de
distintas partes de su sitio. En general, usted debe utilizar las ranuras
para sustituir elementos de presentación, y se debe utilizar scripts para
proporcionar contenido din?mico. En el caso del ejemplo de enlaces, es
discutible si los enlaces son contenido o presentación. Probablemente los
scripts proporcionan una solución más flexible, especialmente si su sitio
incluye objetos de contenido.


Macros de página completa
--------------------------

En lugar de utilizar macros para partes de presentación compartida entre las
páginas, puede utilizar macros para definir páginas completas. Las ranuras
hacen esto posible. Aquí hay un macro que define la página completa:

::<html metal:define-macro="page">
      <head>
        <title tal:content="context/title">The title</title>
      </head>

      <body>
        <h1 metal:define-slot="headline"
            tal:content="context/title">title</h1>

        <p metal:define-slot="body">
          This is the body.
        </p>

        <span metal:define-slot="footer">
          <p>Copyright 2008 Fluffy Enterprises</p>
        </span>

      </body>
    </html>

Este macro define una página con tres ranuras: *headline (encabezado)*, *body
(cuerpo)*, y *footer (pi? de página)*. Note como la ranura *headline* incluye
una sentencia TAL para determinar din?micamente el contenido del encabezado.

Luego usted puede usar este macro en plantillas para diferentes tipos de
contenidos, o distintas partes de su sitio. Aquí hay un ejemplo de cómo un
elemento de noticia puede usar este macro:

::<html metal:use-macro="container/master_page/macros/page">

      <h1 metal:fill-slot="headline">
        Press Release:
        <span tal:replace="context/getHeadline">Headline</span>
      </h1>

      <p metal:fill-slot="body"
         tal:content="context/getBody">
        News item body goes here
      </p>

    </html>

Esta plantilla r?define la ranura *headline* para que incluya las palabras
"Press Release" (Notas de prensa) y ejecuta el método getHeadline en el
objeto actual. También r?define la ranura *body* para que ejecute el método
getBody en el objeto actual.

Lo mejor de este enfoque es que ahora puede cambiar el macro de la *página* y
la plantilla de notas de prensa será automáticamente actualizada. Por ejemplo
usted puede poner el cuerpo de la página en una tabla y agregar una barra
lateral a la izquierda y la plantilla de notas de prensa automáticamente
usar? estos elementos nuevos de presentación.

Based on the `Zope Book`_, ? `Zope Corporation`_


5.2.1.4. Uso avanzado
=====================

En esta parte vamos a ver algunas de las características más avanzadas del
Lenguaje de Atributo de Plantilla, incluyendo un an?lisis más profundo a la
Sintaxis de Expresiones TAL ().


Mezclando y combinando sentencias
---------------------------------

Como ha podido ver en el ejemplo de la plantilla, usted puede situar más de
una sentencia TAL en la misma etiqueta. Sin embargo, hay tres limitaciones
que debería conocer:

1.  Solamente uno de cada tipo de sentencia puede ser usada en una sola
    etiqueta. Ya que HTML no le permite m?ltiples atributos con el mismo
    nombre, usted no puede tener dos ``tal:define`` en la misma etiqueta.

2.  Ninguno de los dos ``tal:content`` y ``tal:replace`` pueden ser
    usados en la misma etiqueta, por la razón de que sus funciones hacen
    conflicto.

3.  El orden en el que usted escribe atributos TAL en una etiqueta no
    afecta el orden en que se ejecutan. No importa cómo las ordene, las
    sentencias TAL en una etiqueta siempre se ejecutaran de la siguiente
    manera : ``define (definir)``, ``condition (condición)``, ``repeat
    (repetir)``, ``content (contenido)`` / ``replace (remplazar)``,
    ``attributes (atributos)``.

Para superar estas limitaciones, se puede añadir otra etiqueta y dividir las
sentencias entre las etiquetas. Si no hay ningún tipo obvio de etiqueta que
encaje, use ``span`` o ``div``.

Por ejemplo, si quiere definir una variable para cada repetición de un
párrafo, usted no puede situar ``tal:define`` en la misma etiqueta que
``tal:repeat``, ya que la definición pasar? antes que todas las repeticiones.
En cambio, podría escribir una de las siguientes:

::      <div tal:repeat="ph phrases">
            <p tal:define="n repeat/ph/number">
            Phrase number <span tal:replace="n">1</span> is
            <b tal:content="ph">Phrase</b>.</p>
          </div>

          <p tal:repeat="ph phrases">
            <span tal:define="n repeat/ph/number">
            Phrase number <span tal:replace="n">1</span> is
            <b tal:content="ph">Phrase</b>".</span>
          </p>

Nota: la definición de "n" en realidad no es muy útil en este ejemplo porque
podríamos haber utilizado directamente "repeat/ph/number" en el atributo de
sustituir el cual sólo ocurre una vez,pero sirve para nuestro propósito.


Sentencias con partes m?ltiples
--------------------------------

Si usted necesita definir m?ltiples atributos en una etiqueta, no puede
hacerlo mediante la colocación de m?ltiples sentencias ``tal:attributes`` en
la etiqueta, y dividi?ndolas de manera inservible por las etiquetas.

Ambas sentencias ``tal:attributes`` y ``tal:define``pueden tener partes
m?ltiples en una sola sentencia. Para separar partes se utiliza el punto y
coma (``;``), así que cualquier expresión que contenga punto en coma en estas
sentencias debe repetirse dos veces (``;;``). Aquí hay un ejemplo de
configuración de ambos atributos ``src`` y ``alt`` de una imagen:

::      <img src="default.jpg"
               tal:attributes="src item/icon; alt item/id">

Aquí hay una mezcla de definiciones de variables:

::      <span tal:define="global logo context/logo.gif; ids
context/objectIds">

**Nota:** de Plone 4 en adelante usted puede utilizar *context/items* en
lugar de *context/objectIds*.


Expresiones de cadena
---------------------

Expresiones de cadenas le permiten fácilmente mezclar expresiones de ruta con
texto. Todo el texto después del ``string:`` l?der se toma y se busca para
expresiones de ruta. Cada expresión de ruta de precederse por un s?mbolo de
dolar (``$``). Si tiene más de una parte, o debe ser separado del texto que
le sigue, debe estar rodeado por llaves (``{}``). Ya que el texto est? dentro
de un valor de atributo, sólo puede incluir una cita doble usando la sintaxis
de entidad ``&quot;``. Debido a que los s?mbolos de dolar son usados para
se?alar expresiones de ruta, un s?mbolo de dolar literal debe repetirse dos
veces (``$$``). Por ejemplo:

::      <span tal:replace="string:Just text."/>
          <span tal:replace="string:?? $year, by Me."/>
          <span tal:replace="string:Three ${vegetable}s, please."/>
          <span tal:replace="string:Your name is
          ${user/getUserName}!"/>
          <span tal:replace="string:She answered
          &quot;$answer&quot;."/>
          <span tal:replace="string:This product costs $price
          $$."/>
Expresiones de ruta nocall
--------------------------

Una expresión de ruta ordinaria trata de renderizar el objeto que manda a
llamar. Esto significa que si el objeto es una función, script, método, o
algún otro tipo de elemento ejecutable, la expresión evaluar? el resultado de
llamar al objeto. Usualmente esto es lo que se quiere, pero no siempre es el
caso. Por ejemplo, si usted quiere poner un documento DTML dentro de una
variable para que así pueda referirse a sus propiedades, no puede usar
entonces una expresión normal de ruta ya que renderizar? el documento dentro
de una cadena.

Si introduce un prefijo de expresión ``nocall:`` delante de una ruta,
previene la renderización y simplemente le da el objeto. Por ejemplo:

::      <span tal:define="doc nocall:context/aDoc"
                tal:content="string:${doc/id}: ${doc/title}">
          Id: Title</span>

Este tipo de expresión también es útil cuando quiere definir una variable que
mantenga una función o una clase de un módulo, para su uso en una expresión
Python.


Otras variables integradas
--------------------------

Ya usted ha visto algunos ejemplos de variables integradas ``template``,
``user``, ``repeat``, y ``request``. Aquí est? una lista más completa de las
otras variables integradas y sus usos:

nothing Un valor falso similar a una cadena en blanco que puede usar en
``tal:replace`` o ``tal:content`` para eliminar una etiqueta o sus
contenidos. Si usted define un atributo a ``nothing``, el atributo se quita
de la etiqueta (o no se inserta), a diferencia de una cadena en blanco.
Equivalente a ``None`` en Python.default Un valor especial que no cambia nada
cuando se usa en ``tal:replace``, ``tal:content``, o ``tal:attributes``. Deja
el texto de la plantilla en su lugar.options Los argumentos *palabras clave*
, en el caso de haber, que fueron pasados a la plantilla.attrs Un diccionario
de atributos de la etiqueta actual en la plantilla. Las claves son los
nombres de los atributos y los valores son los valores originales de los
atributos de la plantilla.root El objeto Zope ra?z. Utilice esta opción para
obtener los objetos Zope desde una ubicación fija, sin importar dónde est? o
se haya llamado la plantilla.context El objeto en el que se llama la
plantilla. Regularmente esto es lo mismo que *container*, pero puede ser
diferente si est? usando adquisición. Utilice esta opción para obtener los
objetos Zope que usted espera encontrar en diferentes lugares dependiendo de
cómo se llama la plantilla.here Un sobrenombre (viejo) para
*context*.container El contenedor (generalmente una carpeta) donde la
plantilla se mantiene. Utilice esta opción para obtener los objetos Zope
desde ubicaciones relativas a contenedores permanentes de plantillas.request
Contiene la información completa sobre la solicitud actual HTTP que ZOPE est?
procesando. Vea `esta página en zope.org wiki`_ para más información sobre el
objeto de la solicitud.modules La colección de módulos Python disponibles
para plantillas. Vea la sección sobre la escritura de expresiones Python.view
(vista)*Solamente* para plantillas llamadas de una vista de estilo Zope 3,
esta variable se refiere a la clase de vista asociada. Esto entonces puede
contener funciones y variables preparadas expresamente para la salida de la
plantilla
Rutas alternas
--------------

La ruta ``template/title`` se garantiza que existe cada vez que una plantilla
es usada, sin embargo esta puede ser una cadena en blanco. Algunas rutas tal
como ``request/form/x``, puede que no existan durante algunas renderizaciones
de la plantilla. Normalmente esto causa un error cuando la ruta es evaluada.

Cuando una ruta no existe, a menudo tiene una ruta de retorno o valor que le
gustar?a usar en su lugar. Por ejemplo si ``request/form/x`` no existe, quiz?
quiera usar en su lugar ``context/x``. Puede hacer esto listando las rutas en
orden de preferencia, separados por caracteres plecas (``|``):

::      <h4 tal:content="request/form/x | context/x">Header</h4>

Dos variables que son bastante útiles como la última ruta en un lista de
alternativas son ``nothing`` y ``default``. Use ``nothing`` para poner en
blanco el objetivo si ninguna de las rutas es encontrada o ``default`` para
dejar el texto de ejemplo en su lugar.

También puede probar la existencia de una ruta directamente con el prefijo de
ruta ``exists:`` . Una ruta de expresión con el prefijo ``exists:`` delante
de ella será verdadera si la ruta existe, y falsa si no existe. Estos dos
ejemplos mostrar?n un mensaje de error sólo si esta pasa la solicitud:

::      <h4 tal:define="err request/form/errmsg | nothing"
              tal:condition="err" tal:content="err">Error!</h4>

          <h4 tal:condition="exists:request/form/errmsg"
              tal:content="request/form/errmsg">Error!</h4>
Elementos dummy
---------------

Usted puede incluir elementos de página que son visibles en la plantilla pero
son lo están en texto generado mediante el uso de la variable integrada
``nothing``, como esta:

::      <tr tal:replace="nothing">
            <td>10213</td><td>Example Item</td><td>$15.34</td>
          </tr>

Esto puede ser útil para rellenar las partes de la página que se ocupan más
por la página generada que por la plantilla. Por ejemplo, una tabla que
usualmente tiene diez filas sólo tendrá una en la plantilla, agregando nueve
filas dummy, el resultado de la plantilla lucir? mas parecida al resultado
final.


Insertando estructuras
----------------------

Normalmente las sentencias ``tal:replace`` y ``tal:content`` citan el texto
que insertan, convirtiendo ``<`` a ``&lt;`` por ejemplo. Si usted quiere
insertar el texto no citado, necesita preceder la expresión con la palabra
clave ``structure``. Dada una variable ``copyright`` con un valor de cadena
de "?? 2008 By <b>Me</b>", las siguientes dos líneas:

::      <span tal:replace="copyright">Copyright 2008</span>
          <span tal:replace="structure copyright">Copyright
          2008</span>

...generar?n "?? 2001 By <b>Me</b>" y "?? 2001 By **Me**" respectivamente.

Esta característica es especialmente útil cuando se est? insertando un
fragmento de código HTML que es almacenado en una propiedad o generado por
otro objeto Zope. Por ejemplo, es posible que tenga elementos de noticias que
contienen simple código de marcado HTML tales como texto en negrita y cursiva
cuando se renderizan, y desea conservarlos cuando los inserte dentro de una
?rea de "Noticias más importantes" de la página. En este caso, podría
escribir:

::      <p tal:repeat="article topnewsitems"
             tal:content="structure article">A News Article</p>
Expresiones básicas Python
---------------------------

Una expresión Python comienza con ``python:``, seguida por una expresión
escrita en el lenguaje Python. Python es un lenguaje de programación sencillo
y expresivo. Si nunca se hab?a encontrado con en ?l antes, debería leer una
de las excelentes tutoriales o introducciones disponibles en el sitio oficial
`http://www.python.org`_.

Una expresión de Plantilla de página Python puede contener cualquier cosa que
el lenguaje Python considere una expresión. Puede usar sentencias tales como
``if`` y ``while``,y las restricciones de seguridad de Zope son aplicadas.


Comparaciones
:::::::::::::

Un lugar donde las expresiones Python son prácticamente necesarias es en la
sentencia ``tal:condition``. Por lo general, se quiere comparar dos cadenas o
números, y no hay otra manera de hacer eso. Puede usar operadores de
comparación ``<`` (less than), ``>`` (greater than), ``==`` (equal to), y
``!=`` (not equal to). También puede usar operadores booleanos ``and``,
``not``, y ``or``. Por ejemplo:

::        <p tal:repeat="widget widgets">
              <span tal:condition="python:widget.type ==
              'gear'">
              Gear #<span
              tal:replace="repeat/widget/number">1</span>:
              <span tal:replace="widget/name">Name</span>
              </span>
            </p>

Algunas veces usted desea escoger distintos valores dentro de una sola
sentencia sobre la base de una o más condiciones. Eso lo puede hacer con la
función ``test``, como esta::

::        You <span tal:define="name user/getUserName"
                  tal:replace="python:test(name=='Anonymous
                  User', 'need to log in', default)">
                  are logged in as
                  <span tal:replace="name">Name</span>
                </span>

            <tr tal:define="oddrow repeat/item/odd"
                tal:attributes="class python:test(oddrow,
                'oddclass', 'evenclass')">
Usando otros tipos de expresiones
:::::::::::::::::::::::::::::::::

Usted puede usar otros tipos de expresiones dentro de una expresión Python.
Cada tipo tiene una función correspondiente con el mismo nombre, incluyendo
``path()``, ``string()``, ``exists()``, y ``nocall()``. Esto le permite
escribir expresiones tales como:

::        "python:path('context/%s/thing' % foldername)"
            "python:path(string('context/$foldername/thing'))"
            "python:path('request/form/x') or default"

La última línea del ejemplo tiene un significado ligeramente diferente que la
expresión de ruta "request/form/x | default", ya que usar? el texto por
defecto si "request/form/x" no existe *o* si este es falso.


Llegar a los objetos de Zope
----------------------------

Gran cantidad del poder de Zope involucra enlazar objetos especializados. Sus
Plantillas de páginas pueden usar Scripts, SQL Methods, Catalogs, y objetos
predeterminados de contenidos. Con el fin de utilizarlos, hay que saber cómo
acceder a ellos.

Las propiedades de objetos son generalmente atributos, así que puede obtener
el título de una plantilla con la expresión "template.title". La mayoría de
objetos Zope aceptan adquisición, lo que les permite obtener atributos de
objetos "padres". Esto significa que la expresión Python
"context.Control_Panel" adquirir? el Objeto de Panel de control de la carpeta
root. Los métodos de objetos son atributos, como en "context.objectIds" y
"request.set". Los objetos contenidos en una carpeta se pueden acceder como
atributos de la carpeta, pero ya que suelen tener identificaciones que no son
identificadores Python v?lidos, no puede utilizar la notación normal. Por
ejemplo en lugar de escribir "context.penguin.gif" debe escribir
"getattr(context, 'penguin.gif')".

Algunos objetos tales como ``request``, ``modules``, y acceso de elementos de
soporte para carpetas Zope. Algunos ejemplos de esto son:

::      request['URL'], modules['math'], and context['thing']

Cuando se utiliza el acceso de elemento en una carpeta, este no trata de
adquirir el nombre, por lo que sólo tendrá éxito si en realidad hay un objeto
con ese ID contenidos en la carpeta.

Las expresiones de ruta le permiten ignorar los detalles de cómo llegar de un
objeto a otro. Zope trata el acceso a atributos, luego el acceso a elementos.
Puede escribir "context/images/penguin.gif" en vez de
"python:getattr(context.images, 'penguin.gif')", y "request/form/x" en lugar
de "python:request.form['x']".

El intercambio es que las expresiones de ruta no le permiten especificar esos
detalles. Por ejemplo. si usted tiene una variable de formulario "get", debe
escribir "python:request.form['get']", ya que "request/form/get" evaluar? al
*método* "get" del diccionario del formulario.


Usando scripts
--------------

Los objetos scripts a menudo son usados para encapsular lógicas de negocios y
manipulación compleja de datos. En el momento que usted se encuentre
escribiendo una gran cantidad de sentencias TAL con expresiones complicadas
dentro de ellas, debería considerar si un script haría el trabajo mejor.

Cada script tiene una lista de par?metros que espera recibir cuando se le
llama. Si esta lista est? vacía, entonces puede usar el script usando una
expresión de ruta. De otra forma, necesitará usar una expresión Python como
esta:

::      "python:context.myscript(1, 2)"
          "python:context.myscript('arg', foo=request.form['x'])"

Si desea devolver más de un solo bit de datos desde un script a una plantilla
de página, es una buena idea devolverlo en un diccionario. De esta manera, se
puede definir una variable para contener todos los datos, y el uso de
expresiones de ruta para hacer referencia a cada bit. Por ejemplo suponga que
tenemos un script ``getPerson`` el cual llama un diccionario como
``{'nombre':'Fred', 'edad':25}``:

::      <span tal:define="person context/getPerson"
                tal:replace="string:${person/name} is
                ${person/age}">
          Name is 30</span> years old.
Llamando a DTML
---------------

DTML es otro lenguaje de plantillas disponible para Zope, en la actualidad
mayormente remplazado por ZPT, pero sigue estando en uso. Puede leer más
acerca de esto en `the relevant chapter of the Zope Book`_.

A diferencia de Scripts, Métodos DTML no tienen ninguna lista explicita de
par?metros. En cambio, esperan que sea pasado un cliente, un mapeo, y
argumentos de palabras claves. Se utilizan para construir un espacio de
nombres.

Cuando ZPublisher de Zope publica objetos DTML, pasa el contexto del objeto
como el cliente, y el REQUEST como el mapeo. Cuando un objeto DTML llama a
otro, pasa su propio espacio de nombres como el mapeo, y sin cliente.

Si usted utiliza una expresión de ruta para renderizar un objeto DTML, este
pasar? un espacio de nombres con ``request``, ``context``, y las variables de
plantilla que ya están con ?l. Esto significa que el objeto DTML será capaz
de utilizar los mismos nombres como si hubieran sido publicados en el mismo
contexto que la plantilla, junto con los nombres de las variables definidas
en la plantilla.


Módulos Python
---------------

El lenguaje Python viene con un gran número de módulos, que proporcionan una
amplia variedad de capacidades para los programas Python. Cada módulo es un
conjunto de funciones, datos y las clases Python relacionadas con un solo
propósito, tales como c?lculos matem?ticos o expresiones regulares.

Varios módulos, como "math" y "string", están disponibles en las expresiones
Python por defecto. Por ejemplo puede obtener el valor de *pi* desde módulo
math escribiendo "python:math.pi". Sin embargo para acceder desde una
expresión de ruta, necesita usar la variables de ``modules``. En este caso
usar?a "modules/math/pi". Por favor consulte el libro Zope o a una guía de
referencia DTML para obtener más información sobre estos módulos.

El módulo "string" est? escondido en expresiones Python por la función de
expresión "string", así que tiene que entrar a través de la variable
``modules``. Usted puede hacer esto directamente con una expresión que lo
use, o definir una variable global para ?l, de esta manera:

::      tal:define="global mstring modules/string"
          tal:replace="python:mstring.join(slist, ':')"

Los módulos se pueden agrupar en paquetes, que son simplemente una forma de
organizar y nombrar los módulos relacionados. Por ejemplo, los scripts de
Zope de base-Python son proporcionados por una colección de módulos en el
sub-paquete "PythonScripts" del paquete de Zope "Products". En particular el
módulo "standard" dentro de este paquete proporciona un número de funciones
para formato útiles que son estándares en la etiqueta DTML "Var". El nombre
completo de este módulo es "Products.PythonScripts.standard", así que puede
obtener acceso a ?l usando cualquiera de la siguientes sentencias:

::      tal:define="pps modules/Products.PythonScripts.standard"
          tal:define="pps
          python:modules['Products.PythonScripts.standard']"

La mayoría de los módulos Python no se pueden acceder desde Plantillas de
página, DTML, o scripts a menos que agregue a ellos las declaraciones de
seguridad de Zope. Pero esta información est? fuera del alcance de este
documento; la puede revisar en `Zope Security Guide (Guía de Seguridad de
Zope)`_.


Atributos especiales HTML

-------------------------

Los atributos HTML booleanos checked*,* selected, *nowrap*, *compact*,
*ismap*, *declare*, *noshade*, *disabled*, *readonly*, *multiple*, *selected*
y *noresize* son tratados de manera diferente por tal:attributes. El valor es
verdadero o falso (como es definido por tal:condition). El atributo se define
para attr="attr" en caso verdadero y omitido en el caso contrario. Si el
valor es default, se considera entonces como verdadero si el atributo ya
existe, y falso si no existe. Por ejemplo cada una de las siguientes líneas:

::<input type="checkbox" checked tal:attributes="checked default">
    <input type="checkbox" tal:attributes="checked string:yes">
    <input type="checkbox" tal:attributes="checked python:42">

se renderizar? como:

::<input type="checkbox" checked="checked">

mientras que cada uno de estos:

::<input type="checkbox" tal:attributes="checked default">
    <input type="checkbox" tal:attributes="checked string:">
    <input type="checkbox" tal:attributes="checked nothing">

se renderizar? como:

::<input type="checkbox">

This article contains information and examples from the `Zope Book`_, ??
`Zope Developers Community.
`_


5.2.1.5. Variables globales de plantillas
=========================================

Plone define algunas variables globales útiles para usarlas en sus plantillas

Cuando este escribiendo plantillas para Plone, se dar? cuenta de un conjunto
de variables que usa más seguido, como la URL del portal o el miembro
actualmente autenticado.

Para su conveniencia, Plone define algunas variables globales de plantillas
que son tra?das a main_template vía global_defines. Algunas de los más útiles
son:

portal El objeto del portalportal_url El URL del portalmemberEl usuario
actual (``None`` si el usuario es an?nimo)checkPermission Una función para
revisar si el usuario actual tiene cierto permiso para el contexto actual
``checkPermission('View portal content "(Ver contenido del portal)",
contexto)``.isAnonVerdadero si el usuario actual no ha iniciado
sesión.is_editable Verdadero si el usuario actual tiene permisos de edición
en el contexto.
default_language El idioma por defecto del portalhere_url El URL del objeto
actual..

Para ver la lista completa de estas variables revise `the docstring for
``globalize()`` in the interface
``Products.CMFPlone.browser.interfaces.IPlone```_.


5.2.1.6. Personalizando plantillas AT
=====================================

En este tutorial se describen los pasos para producir una vista totalmente
personalizada de objetos de Arquetipos. Esto es aplicable para afinar
pequeños detalles de comportamiento por defecto AT así como la destrucción y
reconstrucción de la vista a partir de cero. (Aportado por Floyd May)


5.2.1.6.1. Introducción
========================

Objetivos, prerrequisitos y herramientas

Si usted piensa que la manera en que Archetypes (Arquetipos) automáticamente
genera HTML para ver su objeto no sea lo suficientemente bonita, pues ?ha
venido al lugar correcto! Voy a ense?arle cómo adornar esas mon?tonas y
aburridas vistas y hacer que ?*brillen*!


Objetivos: ¿Qué voy a aprender?
---------------------------------

-   Cómo Arquetipos genera vistas para los objetos de contenido
-   Que tanto control me da Arquetipos
-   Cómo cambiar el diseño HTML para un campo en particular mediante la
    creación de una plantilla widget por defecto.
-   Cómo usar el marco de plantillas de Arquetipos para realizar cambios
    pequeños a la vista AT generada por defecto
-   Cómo personalizar el diseño HTML para la vista completa de un objeto
    de Arquetipo usando los macros de ``title``,``body``,``folderlisting``, y
    ``footer``


Prerrequisitos: ¿Qué necesito saber?
--------------------------------------

-   Como leer y escribir código Python
-   Cómo leer y escribir en ZPT (páginas de Plantillas Zope)
-   Cómo crear productos base-Arquetipos (ArchGenXML es aceptable)


Herramientas: ¿Qué necesito tener instalado?
----------------------------------------------

-   Plone 2.0 o 2.1
-   Arquetipos (incluidos por defecto en Plone 2.1)
-   `The ATViewTutorial product`_ - este producto cuentas con ejemplos de
    los conceptos de esta tutorial.


5.2.1.6.2. ¿Qué lo hace funcionar?
====================================

Esta página describe cómo Arquetipos usa diferentes plantillas para generar
HTML, y como se puede aplicar la personalización a plantillas de base-AT.

Arquetipo posee un sistema bastante inteligente para generar páginas HTML
para objetos de base-AT. El mismo conjunto de plantillas genera **todas** las
?reas de contenido para **todos** los objetos de base-AT. Esto le compra el
siguiente beneficio, provechoso para la consistencia del sitio:

-   Todas las páginas lucen iguales.

Sin embargo también tienen el siguiente inconveniente:

-   Todas las páginas lucen iguales.

Diferentes tipos de contenido necesitan mostrarse de diferente manera.
Averig?emos cómo Arquetipos hace las cosas, para que podamos descubrir cómo
hacer que los tipos de contenido ?*brillen*!


La plantilla ``base_view``
---------

La plantilla ``base_view`` (se encuentra en el skin de arquetipos) se encarga
de seleccionar el macro apropiado desde la plantillas apropiadas, y usa esos
macros para mostrar el contenido. Si observa este parte del código de
'base_view':

::        <tal:block define="portal_type
python:here.getPortalTypeName().lower().replace(' ', '_');
                               view_template
                               python:'%s_view' % portal_type;
                               view_macros
                               python:path('here/%s/macros|nothing' %
                               view_template);
                               macro
                               view_macros/css | nothing"
                       condition="macro">


Puede ver que define la variable ``view_template`` como el Nombre de portal
cambiado a minúsculas y subguiones (_) en vez de espacios, seguido de
``_view``. Por ejemplo la plantilla MyType's view se llamar?a
``mytype_view``.

Ahora antes de continuar le debo advertir que no edite ``base_view``. En
serio, no lo haga.`[1]`_

En serio NO personalice ``base_view``. Si cree que necesita personalizar
primero ``base_view``, pues...no lo haga. Siga leyendo este tutorial. Si
después de leer esta tutorial, esta seguro que necesita personalizar
``base_view``, **?NO!** lo haga. Escriba un ejemplo claro y conciso indicando
por qué después de leer esta tutorial, cree que debería personalizar
``base_view``, y env?ela la lista de correos de ``archetypes-users``. Si
usted necesita *realmente* personalizar ``base_view``, pues habrá encontrado
un defecto en Arquetipos, y las personas en la lista le confirmar?n que ese
es su caso particular. Así que repita después de m?: "No personalizar
``base_view``." ?Bien!

Ahora, hay que tener en cuenta seis macros importantes. Estos seis macros le
dan el poder para insertar código de plantilla que es personalizado por su
clase. Estos macros son:

``js`` Un macro para insertar javascript dentro de la etiqueta ``<head>`` de
la página HTML generada. ``css`` Un macro para insertar CSS y código de
estilo dentro de la etiqueta ``<head>`` de la página ``header`` El macro que
define la parte superior del ?rea de contenido. Por defecto este macro tiene
un etiqueta ``<h1>`` que contiene el título, enlaces para imprimir, enviar
correo, etc. en la parte derecha. ``body`` Este macro define el ?rea de
"body" (cuerpo) del contenido Aquí es donde se muestran los campos y sus
valores. ``folderlisting`` Este macro muestra una lista del contenido hijo
para un objeto. No lo confunda con ``folder_contents``, esto es lo que la
pestaña ``vista`` muestra para objetos folderish. Objetos folderish usan
ambos macros ``body`` y ``folderlisting``. ``footer`` Aquí es donde AT pone
la línea de fondo.

.. image:: images/at-folderish-screenshot.jpg
  :alt: Esta imagen muestra las ?reas generadas por el header, el
    cuerpo y macros folderlisting


Como puede ver el macro ``header`` genera dentro del contorno marcado en rojo
como "header" (encabezado), el macro ``body`` genera el contenido justo abajo
de este, y el macro ``folderlisting`` genera la lista de objetos dentro del
objeto folderish.

La plantilla ``base_view`` extrae automáticamente el macro apropiado de vista
por defecto (``mytype_view``, de nuestro ejemplo ad-hoc anterior), o de la
próxima plantilla que exploraremos: ``base``.


La plantilla ``base``
----

La plantilla ``base`` contiene cuatro de los seis macros buscados por
``base_view``:

-   ``header``
-   ``body``
-   ``folderlisting``
-   ``footer``

La única razón por la que he mencionado ``base`` es para que sepa de donde
proviene el comportamiento AT por defecto. Esto es importante si usted sólo
desea cambiar un poco de la vista de un tipo. Regularmente es útil copiar el
macro desde ``base`` a su plantilla de vista por defecto o predeterminada, y
luego empezar a ajustar y personalizar.


Widgets
-------

Un Widget es lo que usa Arquetipos para mostrar campos. Estos poseen dos
partes:

La clase widget Esta clase define el comportamiento y datos para el widget.
En la mayoría de casos, nunca tendrá que crear un clase derivada-"Widget" por
defecto. Vea Archetypes/Widget.py para ejemplos. La plantilla widget: Esta es
una ZPT que proporciona tres macros: ``view (vista)``, ``edit (editar)``, y
``search (buscar)``. Estos macros presentan el campo: Algunos de los macros
dependen de ciertas variables que hayan sido definidas en la plantilla de
llamado, así que preste atención. A menudo sólo tendrá que proporcionar una
plantilla widget por defecto, y no una clase widget por defecto.

Hay todo tipo de widgets en el mercado que hacen todo tipo de cosas. El
`Archetypes Quick Reference Manual (Manual rápido de referencia para
Arquetipos)`_ cubre los detalles para distintos widgets en Arquetipos.

[1] A menos que est? apurado o nervioso.


5.2.1.6.3. Personalizando widgets
=================================

Esta página le muestra cómo personalizar widgets, y da algunos ejemplos de
qu? tipo de ingeniosos trucos se pueden hacer con la personalización de
widgets.

Como ya hemos dicho, los widgets son lo que Arquetipos utiliza para mostrar
los campos individuales. Las plantillas integradas en Arquetipos,
``base_view``,``base``, y ``widgets/field`` usan cada campo y widget de campo
asociado (especificado en el esquema) para determinar cual plantilla de
widget usar. No obstante, puede sustituir un plantilla de widget, como
mostraremos más abajo. Además, puede crear una clase completamente nueva de
widget, que tendrá los datos y las operaciones específicas para la
presentación de tipos datos por defecto. Lea la siguiente sección para
determinar que tanto hackeo de widget tiene que hacer.


Cómo determinar si usted necesita crear una clase de widget personalizada.
---------------------------------------------------------------------------

Si no puede encontrar un widget en Archetypes (Arquetipos) o en productos de
disponibilidad fácil hechos por terceros que hagan lo que usted necesite, use
el siguiente grupo de preguntas para determinar si puede simplemente
personalizar una **plantilla** versus crear una nueva **clase de widget**. Si
responde "no" a las siguientes preguntas, una plantilla personalizada es todo
lo que necesita:

-   ?La pantalla de su campo requiere funciones auxiliares para hacer
    conversiones o formato que seráan difáciles o incómodas en TALES?
-   ?Posee usted m?ltiples clases de base-AT donde algunos campos en esas
    clases comparten las siguientes característicasí

    -   Los mismos tipos de datos.
    -   Necesidades similares para la presentación
    -   Uno o más atributos que son clase-específico que se aplican a la
    presentación (es decir, el lugar más adecuado para situar estos atributos
    est? en la definición de esquema)

-   ?Sus tipos de datos personalizados necesitan super-específicas
    organizaciones (para que los datos puedan presentarse en un formato
    estándar) al momento de editar o buscar, los cuales no puede obtener de
    ninguna clase estándar de widget AT?
-   Necesita sustituir o cambiar la manera que Arquetipos maneja el
    procesamiento del formulario ``editar`` de un campo en específico?

Si usted contest? "s?" a la mayoría de las preguntas, entonces puede que
tenga que crear una clase widget. Si le parece que las preguntas no est?n
claras, eche un vistazo a `RichDocument tutorial`_ . Si usted tiene un caso
lo suficientemente específico (como RichDocument) en el que *necesita* clases
de widget personalizadas, probablemente pueda hacerlo por el simple hecho de
*saber* que los necesita. `[1]`_


Personalizando plantillas widget
--------------------------------

La creación de plantillas widget personalizadas no es difácil, así que no
tenga miedo. Asumo que si est? leyendo esta sección ya debe haber determinado
que usted no necesita una clase de widget personalizada, y simplemente
necesita retocar un poco cómo se hacen las cosas por defecto.

En primer lugar, usted debe entender que control tiene al personalizar una
plantilla widget en sí misma. Usted est? controlando la presentación de los
*datos* del widget, pero no su *label (r?tulo)*. Para un StringField llamado
``myfield``, la presentación por defecto seráa algo como:

**myfield:** some value (algún valor)

Lo único que podemos controlar es la presentación de lo que viene después de
"**myfield:**", que simplemente son los datos contenidos dentro del campo
mismo (hablaremos de cómo personalizar los r?tulos posteriormente) Sin
embargo, si personalizamos la plantilla, ?podemos insertar *todo tipo* de
ingenioso HTML all? dentro! Asi que veamos la plantilla StringWidget',
'widget/string':

Es bastante sencilla Como puede ver, hay tres macros importantes en una
plantilla widget:

-   ``view (vista)``
-   ``edit (editar)``
-   ``search (buscar)``

No se preocupe por los macros ``edit`` y ``search``; recuerde que estamos
personalizando *view (vista)*. Empecemos por crear una nueva plantilla
llamada ``my_string_widget`` `[2]`_. Comience de esta manera:

Observe cómo se utiliza la misma llamada de "pase-a través" macro en el macro
``edit`` que la plantilla ``string`` originalmente utiliza en el macro de ``
b?squeda ``. Es importante recordar el siguiente concepto: **las plantillas
widget necesitan tener definidos los tres macros:** ``view``, ``edit``, y
``search``. También note cómo no existe un código de visualización para el
r?tulo, como es de costumbre en otras partes. Si se est? preguntando de dónde
viene la variable ``accessor``, pues es parte del código de visualización del
widget. La clase widget define las siguiente variables locales que son
accesibles dentro de las plantillas widget:

``accessor``El método accessor para el campo. Ll?melo para recuperar el valor
del campo.``fieldName``El nombre del campo.``widget``El objeto de widget para
el campo.``field``La instancia de la clase misma del campo``mode``será
``view`` o ``edit``, basado en la acción que se haya tomado. Para nuestros
fines debería ser siempre ``view``.

Ahora vamos a modificar la manera en que StringField se muestra. Para
brevedad, solo mostrar? el macro ``view``:

Luego deberíamos decirle a nuestro esquema de tipo que apunte a la nueva
plantilla

::    StringField('myfield',
            widget=StringWidget(
                label='Myfield',
                label_msgid='ATViewTutorial_label_myfield',
description_msgid='ATViewTutorial_help_myfield',
                i18n_domain='ATViewTutorial',
                macro='my_string_widget',
            )
        ),


Asegúrese de reiniciar Zope y reinstalar usando ``portal_quickinstaller``.
Ahora cuando renderizamos StringField, se verá como este:

.. image:: images/image_preview_004.jpeg
  :alt: Widget personalizado


Así es amigos, es *así de sencillo*.

[1]  Una vez más, esto probablemente sólo se aplica a cierto nerviosismo.

[2] Note que aquí estoy rompiendo la convención AT. Usted no tiene que hacer
eso, pero yo encuentro más conveniente y inteligible añadir ``_widget`` a los
nombres de mi plantillas widget.




5.2.1.6.4. Control total: La plantilla de Vista
===============================================

Esta página describe cómo se puede controlar cada parte del diseño HTML en el
?rea de contenido mediante la creación de una plantilla de vista
personalizada.

Bueno, usted ya ha hackeado un poco las plantillas widget, y est?n
disfrutando de la gloria de su poder reción descubierto, sin embargo, todavía
usted no est? satisfecho. ?Quiere controlarlo **todo**! Bueno ?*yo tengo* la
información que *usted* necesita!


Arquetipos y tipos-específicos de plantillas de Vistas
-------------------------------------------------------

Arquetipos automáticamente reconoce las plantillas con nombre específicos, y
usa el código dentro de esas plantillas para mostrar su objeto base-AT. Toda
la magia ocurre dentro de la plantilla ``base_view``. Para crear una
plantilla de vista personalizada, convierta el nombre su tipo a minúscula (el
nombre que est? listado en ``portal_types``, o lo que se arroja desde
``myObject.portal_type``). Ahora remplace los espacios con subguiones ( _ ).
Y finalmente agregue ``_view`` al final del nombre, y ya *casi* tiene una
plantilla de vista personalizada.

Revise más abajo para ejemplos de nombres de tipos a sus respectivas
plantillas de vista.

Nombre de tipo

Nombre de la plantilla de Vista

My Type

``my_type_view``

SomeTypeV2

``sometypev2_view``

Ahora para remediar la parte "casi" de la oración anterior, defina uno o más
de los siguientes macros en su plantilla:

-   ``header``
-   ``body``
-   ``folderlisting``
-   ``footer``

?Eureka! Ya tiene una plantilla de vista personalizada. Para ver cómo
funciona esto, cree una simple plantilla (por supuesto nombrada
apropiadamente) que contenga el siguiente código:

::          Foo

              Foo

              Foo

              Foo

Y como magia debería ver renderizado en ?rea de contenido:

.. image:: images/image_preview_002.jpeg
  :alt: The Infamous "Foo" View



?Pero aguarde! ¿Dónde están todos mis campos?
-------------------------------------------------

Así que ahora quiere sus datos devuelta. Usted dijo que quería total control,
y ahora no quiere total control. Pero el punto de esta tutorial no es el
control, es el *brillo*. Así que exploremos como mezclar y combinar las
plantillas existentes AT con sus códigos personalizados para hacer una
plantilla brillante que presente lo que *usted* quiera.

En primer lugar, mantenga presente la plantilla "Foo" anterior. Es bastante
útil cuando no est? seguro de cual de los cuatro macros est? generando una
porción del ?rea de contenido. Simplemente comente uno o más de los macros, y
verá que macro genera cual porción.

Ahora ?recuerda cuando hice referencia sobre el uso de la plantilla ``base``
como un punto de partida para la creación de plantillas personalizadasí
Bueno, eso es lo que haremos. Empecemos por personalizar el pi? de página. El
macro ``footer`` en la siguiente plantilla es copiado directamente desde
"base":

::



    Get the byline - contains details about author and modification date.




Ahora agreguemos algo debajo de la byline (línea de fondo), alguna
información importante que se aplique a cada instancia de su tipo
personalizado:

::



    Get the byline - contains details about author and modification date.




    Important information that applies to every instance of my custom
    type.




Note que todo lo que tuvimos que hacer fue copiar el macro desde ``base`` , y
añadir la etiqueta `` <p>`` con algún texto contenido en ?l. Note por
ejemplo, que podríamos haber usado ``tal:content="here/getCustomFooterData"``
en la etiqueta ``</p> <p>`` si hubi?ramos definido un método
``getCustomFooterData()`` en nuestra clase.

Apliquemos este concepto al macro ``body``, y juegue un poco con los campos
que se muestran. Primero empecemos por copiar el ``body (cuerpo)`` desde
``base`` en nuestra plantilla.

Ahora vamos a cambiar algunas cosas añadiendo un poco de código en la macro.
Primero note que ``tal:repeat`` est? repitiendo sobre todos los campos que no
son metadatos. Por lo tanto, si quiere hacer algo para cada campo, col?quelo
dentro de este macro. Usted podría (posiblemente) reorganizar el macro para
que el bucle ``tal:repeat`` est? dentro de otro bloque de contención, y ponga
el código TAL antes y después de la presentación de los campos, o haga uso de
las variables para ``repetir`` ``first`` y ``last`` para lograr la misma
cosa. hagamos dos cosas para personalizar nuestro macro ``body``:

-   Encierre todos los capos con ``</p> <div>`` que tienen un clase CSS
    personalizada, ``my-custom-at-body``
-   Encierre cada campo con `` <div>`` que tiene una clase CSS
    personalizada, ``my-custom-at-field``



Estos cambios, como estoy seguro que usted ha descubierto, no van a hacer
mucha diferencia (en el caso de alguna) en el aspecto de la página
renderizada sin escribir algún código CSS. Ahora introducimos el macro
``css``:

::<link href="#" type="text/css" rel="stylesheet" />
    <div class="my-custom-at-body">
    <div class="my-custom-at-field">&nbsp;</div>
    </div>

Podemos definir una stylesheet CSS llamada ``my_custom_css.css`` que contenga
nuestro código CSS

::    .my-custom-at-body {
            border: thin dashed;
            background-color: #cccccc;
            padding-top: 1em;
        }

        .my-custom-at-field {
            background-color: #ffffff;
        }

Arquetipos inserta el macro ``css`` dentro de la etiqueta de la página
renderizada, creando nuestro código CSS personalizado, archivos enlazados, e
incluye disponibles en la página. Nuestro resultado final seráa algo como
esto:

.. image:: images/image_preview_003.jpeg
  :alt: Macro de cuerpo personalizado


Si hemos creado plantillas widget personalizadas, estas también serán
aplicadas a las páginas renderizadas.


Personalizando r?tulos
-----------------------

Todavía hay un elemento de control que nos falta: a?n no se puede sustituir
la presencia de un r?tulo de campo. Al personalizar la visualización del
r?tulo, podemos insertar imágenes, enlaces, etc. dentro de la página en lugar
de el r?tulo por defecto.

El macro incluido en nuestra plantilla de vista personalizada a continuación
har? la magia por nosotros:

::<link href="#" type="text/css" rel="stylesheet" />
    <div class="my-custom-at-body">
    <div class="my-custom-at-field">&nbsp;</div>
    </div>
    <label>Now presenting... Field1!</label>

Note que solo he sustituido el r?tulo por defecto para los campos llamados
"myfield". El macro ``label (r?tulo)l`` en ``widgets/field`` es donde el
comportamiento predeterminado se puede encontrar. El resultado final luce
como este:

.. image:: images/image_preview.jpeg
  :alt: R?tulo personalizado


No olvide tampoco que tiene el poder de omitir ``head (encabezado)``,``body
(cuerpo)``,``folderlisting (listado de carpetas)``, y ``footer (pi? de
página)`` simplemente escribiendo en macros sin-acción dentro de su plantilla
de vista. Además, se puede llegar a su objeto y recuperar los valores de
campo sin necesidad de utilizar el marco de widget.


5.2.1.6.5. Conclusión
======================

Algunas notas finales sobre la personalización de las plantillas de vista en
Arquetipos

Ahora ya debería saber toda la información siguiente:

-   Cómo identificar cuales partes de una plantilla de vista en
    Arquetipos son generadas por los macros de ``header (encabezado)``,``body
    (cuerpo)``,``folderlisting (listado de carpetas)``, y ``footer (pi? de
    página)</c3
-   Cómo crear una plantilla de vista personalizada que sustituya uno o
    más de los macros ``header ``,``body``,``folderlisting``, y ``footer``
-   Cómo crear una plantilla de widget personalizada que funcione en el
    marco Arquetipos
-   Cómo crear una plantilla ``body`` personalizada que use el widget de
    Arquetipos para renderizar plantillas.
-   Cómo inyectar código CSS y enlaces a los archivos CSS personalizados
    en su plantilla de vista


Algunas notas finales
---------------------

Quiero presentar algunos detalles de cómo aplicar todas estas herramientas.
un tipo sabio en algún momento dijo algo como, "Para el hombre cuya
herramienta es un martillo, cada problema entonces tiende a lucir como un
clavo". Su éxito con Arquetipos realmente depende de la selección de la
herramienta adecuada para el problema especifico. Por lo tanto, utilice el
siguiente esquema del diseño básico de página AT como guía para determinar lo
que debe ser personalizado:

-   macro ``header``

    -   Título (o Identificación si el título no est? presente)
    -   Acciones sobre el documento (Ejemplo: imprimir, enviar a, etc)

-   macro ``body``

    -   Lista de campos

        -   R?tulo del campo (del macro ``label (r?tulo)`` en la
        plantilla de vista, si alguno existe)
        -   Valor del campo (del macro de la plantilla widget ``view
        (vista)``)

-   macro ``folderlisting``

    -   Lista de enlaces para cada sub-objeto

-   macro ``footer``

    -   línea de fondo

Así que basado en cuales partes de este diseño estándar que necesita para
personalizar, utilice el macro adecuado. Mantenga la infame plantilla "Foo"
presente en caso de que necesite depurar Vea la siguiente página para una
referencia sobre personalización de plantillas de vista en Arquetipos.


5.2.1.6.6. Referencias
======================

Una referencia para personalizar plantillas de vista en Arquetipos


Plantillas de vista
-------------------

Las plantillas son nombradas de acuerdo con la clase ``portal_type``. Para
crear el nombre de una plantilla, siga estos pasos:

1.  Cambie ``portal_type`` a minúsculas.
2.  Remplace todos los espacios con subguiones (``_``).
3.  Anexe ``_view`` al final del nombre

Arquetipos localizar? automáticamente las plantillas con nombres creados de
acuerdo a los pasos anteriores, y har? uso de las macros definidos dentro de
la plantilla. Plantillas de vista puede definir uno o más de las siguientes
macros:

``css`` Un macro para insertar código CSS de tipo-específico, incluyendo
etiquetas de ``<link>`` apuntando a archivos CSS personalizados. No hay
ningún macro por defecto dentro de los Arquetipos, este utiliza los actuales
estilos CSS en Plone para renderizar objetos de base-AT. ``header`` Este
macro, por defecto, genera la etiqueta ``<h1>`` conteniendo el título del
objeto y las acciones sobre el documento (imprimir, RSS, etc.) ``body`` El
lugar donde los campos y los valores se muestran por defecto. Cuando se
renderiza campos usando el mecanismo widget existente, asegúrese de definir
con ``tal:define`` la variable de ``field`` como el campo actual; las
plantillas widget dependen de que esta variable se configure.
``folderlisting`` Este es el listado de carpetas cuando se esta viendo la
etiqueta de ``vista`` de un objeto folderish. Esta **no** es lo misma que la
vista de ``contenido``. ``footer`` Por defecto, aquí es donde Arquetipos
coloca la línea de fondo. ``label`` Esta plantilla genera r?tulos de campo.

Para cualquiera de estos macros que no este definido en la plantilla de vista
personalizada. Arquetipos usar? el comportamiento por defecto en este lugar,
tomado de ``base`` o ``widgets/field``.


Plantillas widget
-----------------

Use las plantillas widget personalizadas nombrándolas en el esquema; inserte
un par?metro ``macro`` dentro del constructor widget en el esquema, y defina
los valores para el nombre de la plantilla. Por ejemplo
``macro="my_widget_template"``. Las plantillas widget tienen que tener los
siguientes tres macros:

-   ``view (vista)``
-   ``edit (editar)``
-   ``search (buscar)``

Plantillas widget tienen las siguientes variables locales disponibles dentro
de las expresiones TALES:

``accessor`` El método accessor para el estado actual. El código ``<p
tal:content="accessor" />`` causar? que el valor del campo se escriba dentro
de la etiqueta ``<p>``. ``fieldName`` El nombre del campo. ``widget`` El
objeto de widget para el campo. ``mode`` Siempre será ``view`` para ver las
plantillas, pero también puede ser útil para revisar errores.


5.2.1.7. Cómo personalizar las vista o edición sobre los elementos de
    contenidos en Arquetipos
=============================================================================
===================

Explica una forma de personalizar la vista o editar plantillas sin tener que
cambiar la acción de un objeto.


Razones/Casos de uso

--------------------

Usualmente me gusta modificar lo menos posible para que más de las plantillas
de mi página sean tal como las plantillas por defecto de Plone. Descubr? que
esto me ayuda cuando me mudo a nuevas versiones y también hace que la
creación del uso para estilos CSS sea más fácil.

Otro caso de uso es que si quiero generar un formulario utilizando el esquema
pero lo necesito para hacer diferente las cosas en función de que botón se
presiona, se puede lograr esto con la colocación de botones nombrados en el
formulario en combinación con el uso de portal_formcontroller para sustituir
lo que pasa en un env?o. Ejemplo: para importar datos desde CSV en un esquema
independiente tengo un botón form.button.Import y en este esquema sólo
muestro este botón y el botón de cancelar, (en vez de guardar, siguiente,
anterior, etc.) y luego personalizo la acción (y validación)
portal_formcontroller para que content_edit (el script que guarda) vaya al
script que hace la importación antes del volver a la acción de vista.


Arquetipos base_view y base_edit
--------------------------------

Ambas plantillas tienen varias macros que se consiguen a través de otras
plantillas de páginas. Que están configuradas de tal manera que buscar?n una
plantilla llamada con el tipo de contenido para estos macros y luego
predeterminar a las macros de arquetipos gen?ricos. Es decir, digamos que
tiene un tipo de contenido llamado "Newsletter", base_view busca por una
plantilla llamada "newsletter_view", si la encuentra y esta contiene los
macros correctos usar? esos en lugar de los predeterminados "view_macros"
(Encontrados en la carpeta de skin "portal_skins/archetypes").

A continuación se muestra un ejemplo del esqueleto de una plantilla de vista
personalizada que muestra las diferentes cosas que se pueden personalizar.
See base.pt

::<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en"

          lang="en"

          metal:use-macro="here/main_template/macros/master"

          i18n:domain="plone">

    <body>



    <metal:main fill-slot="main">

            <!-- header, H1 with title in it -->

            <metal:header define-macro="header">



            </metal:header>



            <!-- body macro where all the fields are -->

            <metal:body define-macro="body">



            </metal:body>



            <!-- folderlisting that shows sub-objects if there
            are any -->

            <metal:folderlisting define-macro="folderlisting">





            </metal:folderlisting>



            <!-- footer, by line created date etc. -->

            <metal:footer define-macro="footer">



            </metal:footer>



    </metal:main>

    </body>

    </html>



Abajo hay un esqueleto de una plantilla de edición personalizada:

::<html xmlns="http://www.w3.org/1999/xhtml"

          xml:lang="en"

          lang="en"

          xmlns:tal="http://xml.zope.org/namespaces/tal"

          xmlns:metal="http://xml.zope.org/namespaces/metal"

          xmlns:i18n="http://xml.zope.org/namespaces/i18n"

          i18n:domain="plone">



      <metal:head define-macro="topslot">

      </metal:head>



      <metal:head define-macro="javascript_head">

      </metal:head>



      <body>

            <!-- header, h1 of Edit <Type>, schemata links and
            webdav lock message -->

            <metal:header define-macro="header">



            </metal:header>



            <!-- typedesription, typeDescription from the content
            type -->

            <metal:typedescription define-
            macro="typedescription">



            </metal:typedescription>



            <!-- body, editform , fields, buttons, the default
            macro

                 contains a number of slots which usually
                 provide enough

                 ways to customise so often I use that macro
                 and just

                 fill the slots

            -->

            <metal:body define-macro="body">

                <metal:default_body use-
                macro="here/edit_macros/macros/body">

                  <!-- inside the fieldset but above all
                  the fields -->

                  <metal:block fill-slot="extra_top">

                  </metal:block>



                  <!-- listing of the fields, usually I
                  won't customise this

                  <metal:block fill-slot="widgets">

                  </metal:block>

                  -->



                  <!-- below the fields above the
                  formControls (hidden fields for refernce stuff is above
                  buttons) -->

                  <metal:block fill-slot="extra_bottom">

                  </metal:block>



                  <!-- within the formControls these are
                  the default previous, next, save, cancel buttons -->

                  <metal:block fill-slot="buttons">

                  </metal:block>



                  <!-- within the formControls a slot for
                  extra buttons -->

                  <metal:block fill-slot="extra_buttons">

                  </metal:block>



                </metal:default_body>

            </metal:body>





            <!-- footer, by line created date etc. -->

            <metal:footer define-macro="footer">



            </metal:footer>



      </body>



    </html>





Vea las plantillas dentro de Products.Archetypes:skins/archetypes para
ejemplos sobre cómo hace Arquetipos para trabajar por defecto, obtenga las
listas de campos, trabaje la traducción, maneje el procesamiento de
formularios y más. Usándolas como base y personalización de sólo los detalles
necesarios pueden hacer el trabajo mucho más fácil que empezar de cero.


¿Cómo se hace?

----------------

Digamos que su tipo de contenido es "**Newsletter**"


Pasos para la vista

~~~~~~~~~~~~~~~~~~~

1.  Cree un plantilla de página (ya sea en el sistema de archivos o por
    la ZMI) llamado "newsletter_view"
2.  Utilice el esqueleto y comente los macros que desea conservar de la
    misma manera. Estos son los que desea usar de la plantilla view_macros
    (en portal_skins/archetypes)

3.  Ponga su código en los macros/ranuras relevantes.
4.  Pruebe y usted ha finalizado.


Pasos para la edición
~~~~~~~~~~~~~~~~~~~~~~

1.  Cree una plantilla de página llamada "newsletter_edit"
2.  Use el esqueleto y luego comente los macros para los que desea
    utilizar la opción predeterminada. (from edit_macros).
3.  Ponga su código en los macros/ranuras relevantes.
4.  Pruebe y usted ha finalizado.


5.2.2. ¿Dónde encontrar lo que usted necesita?
================================================

En que lugar est? almacenada el skin en Plone y en su propio producto de
tema.


A través de la Web
-------------------

Puede personalizar todas las plantillas de página, skins y CSS muy fácilmente
a través de la web.

-   Configuración de sitio > Interfaz de Administración de Zope >
    portal_skins

Localice el elemento que desee cambiar, haga clic en el botón de personalizar
y una copia será movida a la capa de personalización.

También puede agregar nuevas plantillas de páginas, scripts de Python y
archivos (para CSS y JavaScript) a la capa de personalización mediante el uso
de lista desplegable en la ZMI. En la mayoría de los casos, sin embargo, le
resultar? más fácil encontrar una plantilla en la cual desea basar la nueva
plantilla, personalizarla y luego cambiarle el nombre a través de la ZMI.

No se olvide que si est? cazando algo, en pestaña de Buscar en la ZMI puede
ser muy útil.


Skin de Plone por defecto en el sistema de archivos.
----------------------------------------------------

Todas las plantillas de página, hojas de estilo, scripts y JavaScript para el
skin por defecto de Plone se pueden encontrar en el producto CMFPlone:

[your products directory]/CMFPlone/skins verá que hay una serie de
directorios correspondientes a las capas de skin específicas. La mayoría de
esto debería ser auto-explicativo, pero vale la pena recordar que únicamente
las plantillas gen?ricas están almacenadas en plone_templates. Si desea
localizar una vista específica de contenido (e.j., document_view) entonces
tendrá que buscar en plone_content.

Dentro de su propio producto de tema
------------------------------------

.. image:: images/your_theme_egg_skin_cutdown.gif
  :alt: The skins folder in your theme product
/skins/[su espacio de nombre de tema].[su espacio de tema]_custom_templates |
custom_images | styles Estos directorios formar?n las capas de skins. Sus
plantillas, imágenes y hojas de estilo pueden ir aquí. Si usted pidi? por
esto, la plantilla de pegado plone3_theme proveer? una hoja de estilo en
blanco para sustituir los por defecto de Plone. /skins.zcml Cuando la
instancia de Zope arranca, esto convierte sus directorios en las capas de
skin. 

.. image:: images/your_theme_egg_skin_cutdown1.gif
  :alt: Subsidiary files used for installing and setting up the Skin
/profiles/default/skins.xml | cssregistry.xml | jsregistry.xml Cuando su tema
est? instalado en el sitio Plone, este configura la jerarqu?a de las capas de
skin, y registra sus hojas de estilo y JavaScript con los registros




5.2.3. Hojas de estilo
======================

Hojas de estilo


5.2.3.1. La hoja de estilo personalizada y las propiedades de base
==================================================================

Usted puede hacer mucho con sólo reemplazar los estilos existentes de Plone.
Hay stylesheet (hojas de estilo) disponibles sólo para este propósito.

Usted encontrará una stylesheet vacía llamada ploneCustom.css en

-   [your products directory]/CMFPlone/skins/plone_styles or
-   Configuración de sitio > Interfaz de Administración de Zope >
    portal_skins > plone_styles

Este stylesheet est? siempre cargado de último en una página, y por lo tanto
puede utilizarse para sustituir cualquier otro estilo. Hay un excelente y
completa tutorial sobre esto aquí:

-   `http://plone.org/documentation/tutorial/working-with-css`_




DTML (Document Template Markup Language - Lenguaje de Marcado de Documento de
Plantilla)
-----------------------------------------------------------------------------
------------

verá que ploneCustom.css tiene una extensión .dtml, y la CSS que est? en el
interior est? empaquetada

::/* <dtml-with base_properties> */
     .......
    /* </dtml-with> */

DTML es otro lenguaje de plantillas de Zope, que en este caso se ha
implementado de manera que ciertas variables puedan ser recogidas a partir de
una hoja de propiedades (base_properties.props), por ejemplo:

::#portal-column-one {
        vertical-align: top;
        *width: <dtml-var columnOneWidth missing="16em">;

    *    border-collapse: collapse;
        padding: 0;
    }


Nosotros no recomendamos el uso de esta técnica, ya que es probable que
desaparezca, pero es bueno saber que est? all?. Algunas veces puede quedar
atrapado si est? personalizando ploneCustom.css y accidentalmente elimina la
parte superior o inferior de la sentencia "dtml-with" o se le olvida agregar
la extensión .dtml.


5.2.3.2. CSS
==========================================================

Familiariz?ndose con las hojas de estilo de Plone


5.2.3.2.1. Conceptos básicos de CSS
====================================

instrucciones para encontrar y modificar base_properties de Plone y CSS.


Prop?sito, prerrequisitos y audiencia

--------------------------------------

Esta tutorial describe el uso de CSS (Cascading Style Sheets - Hojas de
Estilo en Cascada) en Plone 3.x y est? pretendido para personalizadores de
sitio que están familiarizados con CSS y poseen privilegios administrativos
en un sitio Plone. Este enfoque est? estrictamente hecho para crear
modificaciones a-través-de-la-Web a stylesheets (hojas de estilo).

Ning?n conocimiento previo de Python, Plone o Zope es requerido y los
ejemplos guiar?n a aquellos nuevos en Plone a través de cada paso requerido
para hacer modificaciones CSS en Plone. Si usted ha montado un sitio Plone
pero igual es nuevo en Plone, esta tutorial es para usted. Si es un dise?ador
Web que necesita trabajar como parte de un equipo de Plone, esta tutorial le
puede ayudar a clarificar como la CSS es usada en Plone.


Usando las herramientas adecuadas
---------------------------------

Por mucho, la herramienta instrospector CSS más popular de sitios web es
`Firebug`_ de Mozilla. No importa el nivel de su experiencia, Firebug es la
última herramienta de depuración CSS y todos los personalizadores deberían
utilizarla.

La idea básica es que usted puede recorrer el HTML que enmarca sus páginas de
Plone, y ver la CSS que es aplicada al HTML. Usted puede incluso cambiar la
configuración de CSS en el momento para experimentar con el diseño de su
sitio. Para obtener ayuda sobre el uso de Firebug, `haga clic aquí`_ .


Introducción
-------------

El uso extenso de CSS en Plone le da a los personalizadores una gran cantidad
de control sobre la apariencia de un sitio Plone. La manera más rápida de
obtener una idea de esto es mirar en un sitio Plone con los estilos
deshabilitados en su explorador. En Firefox puede deshabilitar los estilos en
"Ver>Estilo de la página>sin estilo", (pruebe esto ahora). Claramente CSS es
bastante usada, y la hace bastante provechosa para la separación de forma y
contenido.

Dise?o personalizado de un sitio Plone se puede realizar mediante una de las
siguientes maneras:

1.  modificando 'base_properties'
2.  substituyendo el estilo existente agregando información para
    estilizar a ploneCustom.css
3.  añadir, borrar o reordenar stylesheets

Esta tutorial describir? las técnicas 1 y 2.

Note que las personalizaciones serias de la interfaz de Plone se hacen mejor
`creando productos personalizados`_. Estos le permiten encapsular todos los
cambios de estilos y plantillas en un solo sitio, guardarlos y re-aplicarlos
en otro sitio. Las instrucciones que se explican aquí son para
personalizaciones "rápidas y robustas" en un sitio individual.


Navegando la ZMI

----------------

Las siguientes carpetas en la ZMI (Zope Management Interface - Interfaz de
Administración de Zope) le permite controlar que stylesheets son usadas y sus
respectivos contenidos:

ZMI > portal_CSS
Controla el registro y ordenamiento de stylesheets dentro de Plone.  ZMI >
portal_skins > custom Ubicación para versiones locales personalizadas de los
stylesheets encontrados en **ZMI > portal_skins > plone_styles**.ZMI >
portal_skins > plone_styles
Ubicación por defecto de base_properties y stylesheets.
Personalizaciones simples

-------------------------


Activación del modo de desarrollo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Antes de comenzar cualquier personalización CSS debería activar el modo
debug-/development. Esto le garantizará que el almacenamiento en caché y la
compresión de CSS est? desactivada.

Esta es la manera en que se activa el modo depuración/desarrollo:

1.  Acceda a su sitio Plone con el usuario "admin" o con su cuenta de
    administrador.

2.  agregue "/manage" al URL para accesar a la ZMI (Interfaz de
    Administración de Zope)
3.  Navegue a **ZMI > portal_css**
4.  haga clic en la casilla de verificación para modo
    depuración/desarrollo
5.  haga clic en el botón Guardar

Cuando haya finalizado con las modificaciones de CSS debería desactivar el
modo depuración/desarrollo, ya que este afecta el rendimiento de su sitio
Plone.


Modificando base_properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Plone proporciona un grupo de base_properties que controlan ciertas cosas del
color, fuente, logotipo y m?rgenes por defecto de Plone. Estas propiedades le
permiten modificar la apariencia básica de un sitio sin trabajar directamente
con los archivos CSS de Plone y proporciona la manera más simple de hacer
personalizaciones básicas. Los nombres de propiedades individuales son
razonablemente auto-explicativos (linkColor, borderStyle, *etc.*) y aceptar
valores estándar de estilo CSS.

Así es como modifica base_properties:

1.  active el modo de desarrollo
2.  Navegue a la **ZMI > portal_skins > plone_styles > base_properties**
3.  haga clic en el botón de personalizar
4.  modifique propiedades individuales usando los valores de estilo CSS
5.  haga clic en el botón de guardar (al final de la página)

La sección 3 de esta tutorial proporciona una descripción más detallada de
cada una de las propiedades de base.


Modificando la CSS
~~~~~~~~~~~~~~~~~~

El siguiente paso más all? de las modificaciones de base_property es la
substitución de la CSS de Plone con su propia CSS personalizada. Plone
proporciona la stylesheet ploneCustom.css para las personalizaciones de
sitio. La parte difácil para las personas nuevas en Plone es averiguar los
selectores CSS que son usados dentro de Plone.

Para mucha gente, el Firebug o las extensiones de Firefox para desarrollo Web
proporcionan la manera más fácil de inspeccionar los estilos asociados con
los elementos HTML en una página web. Cualquiera de estas proporciona una
forma fácil de acceso a los selectores CSS e información de estilo requerida
para la creación de stylesheets personalizadas.

Note que los archivos .css en ZMI > portal_skins > plone_styles son realmente
plantillas dtml, lo que significa que pueden utilizar base_properties para
hacer cambios globales vía variables.  Esto quiere decir que pueden contener
referencias a base_properties junto con CSS estándar, como en el siguiente
ejemplo de public.css:

::h1, h2 {

        border-bottom: **&dtml-borderWidth;** **&dtml-borderStyle;**
        **&dtml-globalBorderColor;**;

        font-weight: normal;

    }d

Aquí est? cómo agregar personalizaciones CSS a su sitio Plone:

1.  active el modo de desarrollo
2.  Navegue a **ZMI > portal_skins > plone_styles > ploneCustom.css**

3.  haga clic en el botón de personalizar
4.  agregue CSS

5.  haga clic en el botón de guardar (al final de la página)


Las secciones 4 y 5 de este tutorial describen las stylesheets (hojas de
estilo) de Plone y los selectores CSS asociados con los distintos elementos
de la interfaz de Plone.


Restableciendo los estilos por defecto
--------------------------------------

Cuando al principio comienza a jugar con base_properties y stylesheets usted
querrá la libertad de hacer muchos cambios, pero sabiendo que igual puede
regresar fácilmente a las configuraciones por defecto. Plone hace que esto
sea fácil, siempre manteniendo las versiones de base_properties y stylesheets
personalizadas en una carpeta separada. Cuando Plone reúne las stylesheets de
CSS, este busca primero por versiones personalizadas y usa estas cuando las
encuentra. Por otra parte si no las encuentra utiliza entonces las versiones
por defecto. Para restablecer las configuraciones por defecto sólo necesita
eliminar las versiones personalizadas.

Esta es la manera como restablece los estilos por defecto en su sitio Plone.

1.  active el modo de desarrollo
2.  navegue a **ZMI > portal_skins > custom**

3.  revise **base_properties** y/o **ploneCustom.css** (o cualquier cosa
    que haya modificado)

4.  haga clic en el botón de eliminar.



5.2.3.2.2. Ejemplos de personalización CSS
===========================================

Ejemplos de personalización de Plone 3.0.x a través de base_properties y CSS.

Los siguientes ejemplos son proporcionados para darle un impulso en hacer
cambios a su sitio. No se pretende que sean ejemplos completos. En cada caso
tomaremos un sitio Web existente para usarlo como nuestro objetivo y hacer
algunos cambios que imiten el estilo del objetivo. Terminar el estilo lo
dejaremos como ejercicio para el estudiante.


Ejemplo 1: estilo *"Austin Neon"*

-------------

Una de las maneras más fáciles de ver el control de base_properties es crear
un estilo "oscuro" para su sitio. Como ejemplo de donde es apropiado este
estilo usaremos `Austin Neon`_ como nuestro sitio.  Como siempre, la
extensión Firebug para Firefox es invaluable para inspeccionar el estilo de
nuestro objetivo. Si usted todavía no la ha hecho, por favor instale y entre
en confianza con Firebug antes de tratar de descubrir cómo el objetivo es
estilizado.


Configuración inicial de base_properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El primer paso será modificar base_properties de nuestro sitio Plone como se
describe en la sección 1. La siguiente captura muestra la base_properties que
se acerca a representar los colores que se encuentran en nuestro objetivo.
Vaya y realice estos cambios a su base_properties ahora.

.. image:: images/neon_base_properties.png
  :alt: neon_base_properties



Dar más estilo con CSS
~~~~~~~~~~~~~~~~~~~~~~~

TODO (marcador de código)


Example 2: estilo *'New York Times'*

----------------

?alguien desea hacer alguna contribución?


5.2.3.2.3. base_properties
========================================================================

Descripción de todas las base_properties en Plone 3.0.x

La siguiente lista de base_properties son usadas para dar estilizar a través
de Plone. Estas pueden editarse mediante la ZMI en**
**

**ZMI > portal_skins > plone_styles > base_properties**


Plone 3.0.x base_properties
---------------------------

logoNamenombre del archivo del logotipo del portal fontFamilyfamilia de
fuente usada para todo el texto que no es encabezado fontBaseSizeel tamaño de
la fuente base de donde todo es calculado fontColorel color de fuente
principal fontSmallSizeusado para varios elementos como botones y texto
discreto discreetColorcolor de fuente para el texto discreto
backgroundColorcolor de fondo linkColorcolor utilizado en los enlaces
normales linkActiveColorcolor que se utiliza en enlaces activos
linkVisitedColorcolor que se utiliza en los enlaces ya visitados
borderWidthancho de la mayoría de los m?rgenes en Plone borderStyleestilo de
las líneas de borde, normalmente s?lido borderStyleAnnotationsestilo de las
líneas de m?rgenes de los comentarios, etc globalBorderColorcolor del borde
utilizadas en las pestañas principales, portlets, etc
globalBackgroundColorcolor de fondo para las pestañas seleccionadas, títulos
de portlets, etc. globalFontColorcolor de la fuente en las pestañas y en los
encabezados de portlets headingFontFamilyfamilia de fuente para los
encabezados h1/h2/h3/h4/h5/h6 contentViewBorderColorcolor de las pestañas de
vista de contenidos contentViewBackgroundColorcolor del fondo de las pestañas
de vista de contenidos contentViewFontColorcolor de la fuente usada en las
pestañas de vista de contenidos inputFontColorcolor de fuente usado para los
elementos de entrada  textTransformtransformación de texto a minúsculas en
portlets, pestañas, etc evenRowBackgroundColorcolor de fondo de las filas
impares en los listados oddRowBackgroundColorcolor de fondo de las filas
impares en los listados notifyBorderColorcolor del borde de los elementos de
notificación tal como el mensaje de estado, el enfoque del calendario
notifyBackgroundColorcolor de fondo de los elementos de notificación como el
mensaje de estado, el enfoque del calendario lpBackgroundColorcolor de fondo
de la información en ventanas emergente (en la actualidad no se utiliza)


5.2.3.2.4. Stylesheets CSS por defecto
======================================

Descripción de los stylesheets CSS por defecto en Plone 3.0.x.

Las stylesheets por defecto están descritas más abajo junto con las listas de
los selectores CSS definidos en cada una.  Las stylesheets son presentadas en
el mismo orden en que están definidas en **ZMI > portal_css** para que el
estilo definido en las stylesheets de más abajo sustituyan el estilo definido
en las de más arriba.


member.css
----------

Estilos para estados de flujo de trabajo de usuarios que hayan iniciado
sesión.

::.state-private { ... }
    .state-visible { ... }
    .state-published { ... }
    .state-pending { ... }
    .state-expired { ... }
    .syndicated { ... }
RTL.css
-------

Estilos de izquierda a derecha para el idioma árabe y hebreo


base.css
--------

Estilos para elementos base (etiquetas HTML)

::body { ... }
    table { ... }
    a { ... }
    img { ... }
    p { ... }
    p img { ... }
    hr { ... }
    h1, h2, h3, h4, h5, h6 { ... }
    h1 a{ ... }
    h1 { ... }
    h2 { ... }
    h3 { ... }
    h4 { ... }
    h5 { ... }
    h6 { ... }
    ul { ... }
    ol { ... }
    li { ... }
    dt { ... }
    dd { ... }
    abbr, acronym, .explain { ... }
    abbr .explain { ... }
    q { ... }
    blockquote { ... }
    code, tt { ... }
    pre { ... }
    ins { ... }
    del { ... }

public.css
----------

Gran cantidad de elementos destinados al público.

::/* Accessibility elements, applied by JS */
    body.largeText { ... }
    body.smallText { ... }

    /* Padding for the columns */
    #portal-column-one .visualPadding { ... }
    #portal-column-two .visualPadding { ... }

    /* Content area */
    h1, h2 { ... }
    body.kssActive h2.inlineEditable:hover, body.kssActive
    h1.inlineEditable:hover { ... }
    h3, h4, h5, h6 { ... }

    .documentFirstHeading { ... }
    .documentContent { ... }
    .documentContent ul { ... }
    .documentContent ol { ... }

    /* Links with differently colored link underlines - only for content
    */
    .documentContent p a { ... }
    .documentContent p a:visited { ... }
    .documentContent p a:active { ... }
    #content a:target { ... }
    .documentContent li a { ... }
    .documentContent li a:visited { ... }
    .documentContent li a:active { ... }
    .documentContent dd a { ... }
    .documentContent dd a:visited { ... }
    .documentContent dd a:active { ... }
    /* End links */

    #visual-portal-wrapper { ... }

    /* Logo properties */
    #portal-logo img { ... }

    /* The skin switcher at the top, only shows up if you have multiple
    skins available */
    #portal-skinswitcher { ... }
    #portal-skinswitcher a { ... }
    #portal-top { ... }

    /* Site-wide action menu - font size, contact, index, sitemap etc */
    #portal-siteactions { ... }
    #portal-siteactions li { ... }
    #portal-siteactions li a { ... }
    #portal-siteactions li.selected a { ... }
    #portal-siteactions li a:hover { ... }

    /* Searchbox style and positioning */
    #portal-searchbox { ... }
    #portal-advanced-search { ... }
    #portal-advanced-search a { ... }

    /* Search results elements */
    dl.searchResults dt { ... }
    form.searchPage { ... }
    input.searchPage { ... }
    form.searchPage input.searchButton { ... }

    /* LiveSearch styles */
    .LSRes { ... }
    #LSHighlight, .LSHighlight { ... }
    .LSRow { ... }
    .LSRow a { ... }
    .LSDescr { ... }
    .LSResult { ... }
    .LSShadow { ... }
    .livesearchContainer { ... }
    * html .livesearchContainer { ... }
    #livesearchLegend { ... }
    * html #livesearchLegend { ... }

    /* Workaround for Internet Explorer's broken z-index implementation
    */
    .LSIEFix { ... }
    .LSBox { ... }
    #LSNothingFound { ... }
    .LSBox label { ... }

    /* The global section tabs. */
    #portal-globalnav { ... }
    #portal-globalnav li { ... }
    #portal-globalnav li a { ... }
    #portal-globalnav li.selected a { ... }
    #portal-globalnav li a:hover { ... }
    /* Bar with personalized menu (user preferences, favorites etc) */
    #portal-personaltools { ... }
    #portal-personaltools .portalUser { ... }
    /* Used on all descriptions relevant to those not logged in */
    #portal-personaltools .portalNotLoggedIn { ... }
    #portal-personaltools li { ... }
    #portal-personaltools li a { ... }
    #portal-personaltools .visualIconPadding { ... }
    .visualCaseSensitive { ... }
    #portal-languageselector { ... }
    #portal-languageselector li { ... }
    /* The path bar, including breadcrumbs and add to favorites */
    #portal-breadcrumbs { ... }
    #portal-breadcrumbs a { ... }
    .breadcrumbSeparator { ... }
    .addFavorite { ... }
    .documentEditable { ... }
    #content-news h1 { ... }

    /* Only h5/h6 headlines in the content area should have the discreet
    color */
    #content h5, #content h6 { ... }
    .newsItem { ... }
    .newsImage { ... }
    .newsImageContainer { ... }
    .newsContent { ... }
    .newsContent ul, .newsContent li { ... }
    .newsAbout { ... }
    .newsAbout li { ... }
    .newsFooter { ... }
    .newsFooter li { ... }
    .documentActions { ... }
    .documentActions ul { ... }
    .documentActions li { ... }
    .documentActions a { ... }

    /* Status messages */
    dl.portalMessage { ... }
    dl.portalMessage a { ... }
    dl.portalMessage dt { ... }
    dl.portalMessage dd { ... }
    dl.warning dt { ... }
    dl.error dt { ... }
    dl.warning dd { ... }
    dl.error dd { ... }

    /* The summary text describing the document */
    .documentDescription { ... }
    .documentByLine { ... }
    dl.searchResults span.documentByLine { ... }
    #category ul { ... }
    #category ul li { ... }
    .discussion { ... }
    .even { ... }
    .odd { ... }
    .visualHighlight { ... }
    .discreet { ... }
    .pullquote { ... }
    .callout { ... }
    .notify, .documentEditable * .notify { ... }
    .card { ... }
    .card a { ... }
    .portrait { ... }
    .portraitPhoto { ... }

    /* The table used for listings - horizontal and vertical variants */
    table.listing, .stx table { ... }
    table.listing th, .stx table th { ... }
    table.listing .top { ... }
    table.listing .listingCheckbox { ... }
    table.listing td, .stx table td { ... }
    table.listing a { ... }
    table.listing a:hover { ... }
    table.listing img { ... }
    table.listing td a label, .stx table td a label { ... }

    /* Vertical addition class */
    table.vertical { ... }
    table.vertical th { ... }
    table.vertical td { ... }

    /* grid addition class */
    table.grid td { ... }

    /* plain table class with light gray borders */
    table.plain, table.plain td, table.plain th { ... }

    /* Batch selector */
    .listingBar { ... }
    .listingBar span.previous, .listingPrevious { ... }
    .listingBar span.next, .listingNext { ... }
    .listingBar img { ... }
    .listingBar a { ... }
    .tileItem { ... }
    .tileHeadline { ... }
    .tileHeadline a { ... }
    .tileBody { ... }
    .tileImage { ... }
    .eventDetails { ... }

    /* Useful deviations from regular style on elements */

    /* List classes without markers */
    ul.visualNoMarker, ol.visualNoMarker { ... }
    ul.discreet { ... }
    textarea.proportional { ... }
    .productCredits { ... }
    #portal-footer { ... }
    #portal-footer p { ... }
    #portal-footer a { ... }
    #portal-footer a:visited { ... }
    #portal-footer a:hover { ... }
    #portal-colophon { ... }
    #portal-colophon ul { ... }
    #portal-colophon ul li { ... }
    #portal-colophon ul li a { ... }

    .feedButton { ... }
    .poweredBy { ... }

    /* Sitemap styles */
    #portal-sitemap { ... }
    #portal-sitemap a { ... }
    #portal-sitemap a:hover { ... }
    #portal-sitemap .navTreeLevel1 { ... }
    #portal-sitemap .navTreeLevel2 { ... }

    /* Album view classes */
    .photoAlbumEntry { ... }
    .photoAlbumEntry img { ... }
    .photoAlbumEntryWrapper { ... }
    .photoAlbumEntry a { ... }
    .photoAlbumFolder { ... }
    .photoAlbumEntryTitle { ... }

    /* Link types */
    a.link-parent { ... }
    #content .link-category { ... }
    #content .link-user { ... }
    #content .link-comment { ... }
    #content .link-anchor { ... }
    #content .link-presentation { ... }
    #content .link-wiki-add { ... }

    /* Handling external/internal links, we first set the icon on all
    links, then
    remove it from the ones that are local - for both http and https */
    #content a[href ^="http:"], #content a.link-external { ... }
    #content a[href ^="https:"], #content a.link-https { ... }
    #content a[href ^="&dtml-portal_url;"] { ... }

    /* Protocol-specific links */
    #content a[href ^="mailto:"], #content a.link-mailto { ... }
    #content a[href ^="news:"], #content a.link-news { ... }
    #content a[href ^="ftp:"], #content a.link-ftp { ... }
    #content a[href ^="irc:"], #content a.link-irc { ... }
    #content a[href ^="callto:"], #content a.link-callto { ... }
    #content a[href ^="webcal:"], #content a.link-webcal { ... }
    #content a[href ^="feed:"], #content a.link-feed { ... }

    #content .link-plain { ... }

    /* For ghosted elements */
    .visualGhosted { ... }

    /* Fullscreen */
    body.fullscreen #portal-logo, body.fullscreen #portal-siteactions {
    ... }
    body.fullscreen #portal-globalnav { ... }
    body.fullscreen #portal-searchbox { ... }

    /* Kupu image alignment classes */
    .image-left { ... }
    .image-inline { ... }
    .image-right { ... }
    dd.image-caption { ... }
    dl.captioned { ... }

    /* Dashboard */
    #dashboard-info-message { ... }
    #dashboard { ... }
    #dashboard-portlets1,
    #dashboard-portlets2,
    #dashboard-portlets3 { ... }
    #dashboard-portlets4 { ... }
    #dashboard-portlets1 a,
    #dashboard-portlets2 a,
    #dashboard-portlets3 a,
    #dashboard-portlets4 a { ... }
    #dashboard-portlets1 dl.portlet,
    #dashboard-portlets2 dl.portlet,
    #dashboard-portlets3 dl.portlet,
    #dashboard-portlets4 dl.portlet { ... }
    div.managedPortlet.portlet { ... }
    #dashboard select { ... }
    .portletAssignments { ... }
    #dashboard-portlets1 div.managedPortlet a,
    #dashboard-portlets2 div.managedPortlet a,
    #dashboard-portlets3 div.managedPortlet a,
    #dashboard-portlets4 div.managedPortlet a { ... }
    #dashboard-portlets1 div.managedPortlet span a,
    #dashboard-portlets2 div.managedPortlet span a,
    #dashboard-portlets3 div.managedPortlet span a,
    #dashboard-portlets4 div.managedPortlet span a{ ... }
    #dashboard-actions { ... }
    #dashboard-actions ul { ... }
    #dashboard-actions ul li { ... }
    #dashboard-actions ul li.portalUser { ... }

    /* manage portlets */
    .section div { ... }

columns.css
-----------

Estilos para columnas de tabla-basada también conocido como "slot izquierdo",
"slot derecho", etc.

::#portal-columns { ... }
    #portal-column-one { ... }
    #portal-column-content { ... }
    #portal-column-two { ... }
    body.fullscreen #portal-column-one, body.fullscreen #portal-column-
    two { ... }
    body.fullscreen #portal-column-content { ... }
authoring.css
-------------

Estilos asociados con elementos de creación visible para los proveedores de
contenido.

::/* Editable border */
    .contentViews { ... }
    .contentViews li { ... }
    .contentViews li a { ... }
    .contentViews .selected a { ... }
    .contentViews li a:hover { ... }
    .configlet .contentViews { ... }

    /* begin ECMAScript Content Action Menus */
    .contentActions { ... }
    .contentActions ul, .contentActions li { ... }
    .contentActions li { ... }
    .contentActions a { ... }
    .contentActions span.subMenuTitle { ... }
    .contentActions a span.subMenuTitle { ... }
    .actionMenu { ... }
    .actionMenu .actionMenuHeader { ... }
    .actionMenu.activated .actionMenuHeader { ... }
    .actionMenu .actionMenuHeader a { ... }
    .arrowDownAlternative { ... }
    .actionMenu .actionMenuContent { ... }
    .actionMenu.activated .actionMenuContent { ... }
    .actionMenu.activated .actionMenuContent { ... }
    .actionMenu.deactivated .actionMenuContent { ... }
    .actionMenu .actionMenuContent ul { ... }
    .actionMenu .actionMenuContent li { ... }
    .actionMenu .actionMenuContent li a { ... }
    .actionMenu .actionMenuContent .selected { ... }
    .actionMenu .actionMenuContent li a:hover { ... }
    .actionMenu .actionMenuContent .actionSeparator a { ... }
    #templateMenu li a { ... }
    /* end ECMAScript Content Action Menus */

    ul.configlets { ... }
    ul.configlets li { ... }
    ul.configlets li a { ... }
    ul.configlets li a:visited { ... }
    ul.configlets li a:active { ... }
    ul.configlets li label { ... }
    ul.configletDetails { ... }
    ul.configletDetails li { ... }
    ul.configletDetails li a { ... }
    ul.configletDetails li label { ... }

    /* Additional STX workaround classes */
    .stx table p { ... }
    .stx table { ... }
    .stx table td { ... }

    .reviewHistory { ... }
    .comment { ... }
    .comment h1, .comment h2, .comment h3, .comment h4, .comment h5,
    .comment h6 { ... }
    .comment h3 a { ... }
    .commentBody { ... }
    .spacer { ... }

    /* Collapsible elements */
    dl.collapsible { ... }
    dl.collapsible dt.collapsibleHeader { ... }
    dl.collapsible dd.collapsibleContent { ... }

    /* for IE the following isn't needed, that's why the css2 selector is
    used */
    dl.collapsible dd.collapsibleContent > dl { ... }
    dl.expandedInlineCollapsible dt.collapsibleHeader,
    dl.expandedBlockCollapsible dt.collapsibleHeader { ... }
    dl.collapsedBlockCollapsible { ... }
    dl.collapsedBlockCollapsible dt.collapsibleHeader { ... }
    dl.collapsedInlineCollapsible dd.collapsibleContent,
    dl.collapsedBlockCollapsible dd.collapsibleContent { ... }
    dl.collapsedInlineCollapsible { ... }
    dl.collapsedInlineCollapsible dt.collapsibleHeader { ... }

    .configlet .documentEditable { ... }
    .documentEditable .documentContent { ... }
    .label { ... }
    .optionsToggle { ... }

    #portal-column-content fieldset > * input:focus, #portal-column-
    content fieldset > * textarea:focus { ... }

    .highlightedSearchTerm { ... }
    dl.searchResults .highlightedSearchTerm { ... }
    .noInheritedRoles { ... }
    .currentItem { ... }
    tr.dragging td { ... }
    .draggingHook { ... }
    .notDraggable { ... }

    .managePortletsLink { ... }
    ul.formTabs { ... }
    li.formTab { ... }
    li.formTab a { ... }
    li.formTab a { ... }
    li.firstFormTab a { ... }
    li.lastFormTab a { ... }
    li.formTab a.selected { ... }
    li.formTab a:hover { ... }
    li.formTab a.notify { ... }
    li.formTab a.required span { ... }
    li.formTab a.notify:hover { ... }
    .formPanel { ... }
    .formPanel.hidden { ... }
    div.formControls input.hidden { ... }

portlets.css
------------

Estilos asociados con componentes de portlets individuales

::/* Main portlet elements */
    .portlet { ... }
    .portlet a { ... }
    .portlet a.tile { ... }

    .portletItem a:visited, .portletFooter a:visited { ... }
    .portletHeader { ... }
    .portletHeader a { ... }
    .portletItem { ... }
    .portletItem ol { ... }
    .portletItemDetails { ... }
    .portletFooter { ... }

    /* Elements that enable layout with rounded corners */
    .portletTopLeft { ... }
    .portletTopRight { ... }
    .portletBottomLeft { ... }
    .portletBottomRight { ... }

    /* Calendar elements - used in the calendar rendering */
    .dayPopup { ... }
    .date { ... }
    .portletCalendar { ... }
    .portletCalendar dt { ... }
    .portletCalendar dd { ... }
    .portletCalendar a { ... }
    .portletCalendar a:hover { ... }
    .ploneCalendar { ... }
    .ploneCalendar td { ... }
    .ploneCalendar .weekdays th { ... }
    .ploneCalendar .event { ... }
    .ploneCalendar .todayevent { ... }
    .ploneCalendar .todaynoevent { ... }

    .managePortletsLink { ... }
    div.portlets-manager div.section { ... }
    div.managedPortlet { ... }
    .managedPortlet .portletHeader { ... }
    .managedPortlet a { ... }
    .managedPortletActions { ... }
    .managedPortletActions a { ... }
    .managedPortletActions a.up,
    .managedPortletActions a.down { ... }
    .managedPortletActions a.delete { ... }

    /* Table of Contents styling - essentially a portlet with smaller
    fonts and aligned right + limited in width */
    .toc { ... }

controlpanel.css
-----------------

Estilos asociados con el panel de control de Plone

::.inlineDisplay { ... }

    table.controlpanel-listing { ... }
    table.controlpanel-listing td, table.controlpanel-listing th { ... }
    table.controlpanel-listing dl { ... }
    table.controlpanel-listing dd { ... }
    table.controlpanel-listing dl dt a .trigger{ ... }
    table .controlpanel-listing td { ... }
    table.controlpanel-listing td.checker{ ... }
    table.controlpanel-listing th.smallcolumn { ... }

    .chooser-right { ... }

    .rule-element { ... }
    .rule-element dl { ... }
    .rule-element dl dd { ... }
    .rule-updown, .rule-operations { ... }

print.css
---------

Estilos de impresión para exploradores con capacidad CSS2. Gran parte de esta
stylesheets (hoja de estilo) tiene que ver con esconder componentes
considerados inapropiados para documentos impresos.


deprecated.css
--------------

Estilos para elementos desacreditados o en desuso que desaparecer?n de Plone
en versiones futuras.


navtree.css
-----------

Estilos asociados con el árbol de navegación.

::.portletNavigationTree { ... }
    .navTree { ... }
    .navTree li { ... }
    .navTreeItem { ... }
    .navTreeItem a, dd.portletItem .navTreeItem a { ... }
    .navTreeItem a:hover, dd.portletItem .navTreeItem a:hover { ... }
    .navTreeCurrentItem { ... }
    li.navTreeCurrentItem { ... }
    li.navTreeCurrentItem a, li.navTreeCurrentItem a:hover { ... }

    .navTreeLevel0 { ... }
    .navTreeLevel1 { ... }
    .navTreeLevel2 { ... }
    .navTreeLevel3 { ... }
    .navTreeLevel4 { ... }
    .navTreeLevel5 { ... }


invisibles.css
--------------

Estilos para los elementos invisibles y de accesibilidad.

::/* List classes without markers */
    ul.visualNoMarker, ol.visualNoMarker { ... }
    .visualOverflow { ... }
    .visualOverflow pre, .visualOverflow table, .visualOverflow img { ...
    }

    /* Accessibility and visual enhancement elements */
    .hiddenStructure { ... }
    .contentViews .hiddenStructure, .contentActions .hiddenStructure {
    ... }
    .hiddenLabel { ... }

    /* Helper element to work with CSS floats */
    .visualClear { ... }

    /* Hiding helper elements for old browsers */
    .netscape4 { ... }

forms.css
---------

Estilos asociados con formularios.

::textarea { ... }
    input { ... }

    input[type=checkbox] { ... }

    #searchGadget { ... }

    button { ... }
    select { ... }
    form { ... }
    fieldset { ... }
    legend { ... }
    label { ... }
    optgroup { ... }
    option { ... }
    optgroup > option { ... }

    dl.enableFormTabbing dd { ... }

    #login-form { ... }
    #login-form .field { ... }
    #login-form input { ... }
    #login-form input.context { ... }

    #forgotten-password { ... }

    .standalone, .documentEditable * .standalone { ... }
    .context, .formControls .actionButtons .button, .documentEditable *
    .context { ... }
    .destructive, .documentEditable * .destructive { ... }
    input.searchButton { ... }
    .searchSection { ... }
    .searchSection label:hover { ... }

    /* The edit form elements */
    .field { ... }
    .field .field { ... }
    .fieldRequired { ... }
    .fieldUploadFile { ... }
    .fieldTextFormat { ... }
    .formHelp { ... }
    .formHelp:hover { ... }
    div.error { ... }
    .error .fieldRequired { ... }

    /* Styles to make the editing widgets look more like their view
    counterparts */
    #archetypes-fieldname-title input, input#form\.title { ... }
    #archetypes-fieldname-description textarea,
    textarea#form\.description { ... }
    input.inputLabelActive { ... }

    textarea#form\.description { ... }

    tr.selected { ... }

    .kupu-save-message { ... }

ploneKss.css
------------

No es accesible a través de ZMI > portal_skins > plone_styles.


ploneCustom.css
---------------

Aquí es donde sus estilos modificados localmente deben ir. Por defecto,
ningún estilo se define en esta stylesheet.


kupustyles.css
--------------

No es accesible a través de ZMI > portal_skins > plone_styles.


kupuplone.css
-------------

No es accesible a través de ZMI > portal_skins > plone_styles.


kupudrawerstyles.css
--------------------

No es accesible a través de ZMI > portal_skins > plone_styles.


5.2.4. Capas del skin
=====================

Skin layers


5.2.4.1. Capas del skin
=======================

Plantillas, scripts, imágenes, CSS y archivos JavaScript se organizan con las
capas del skin

> Nota: en el contexto de componentes, "capa" tiene un significado
ligeramente distinto.

A la piel se compone de una serie de capas del skin. En el sistema de
archivos, cada capa es un directorio. En la Interfaz de Administración de
Zope (ZMI), cada capa aparece en portal_skins como una carpeta separada (con
plantillas de páginas, hojas de estilos o scripts de Python).

.. image:: images/portal_skins_zmi_snip.html


Estas tienen dos usos.

-   En primer lugar mantienen las cosas organizadas. Si echa un vistazo a
    la skin de Plone por defecto (una parte mostrada en la captura de
    portal_skins de más arriba), usted verá que han separado plantillas,
    scripts, estilos e imágenes dentro de distintas capas del skin.

-   Más importante es que tienen un orden de precedencia. Esto significa
    que un elemento denominado main_template en la capa superior será
    encontrado y utilizado antes que un elemento denominado main_template en
    la capa inferior. Vamos a entrar en esto con más detalle en la página
    siguiente.

Para crear una capa del skin a través de la web, basta con agregar una nueva
carpeta. En el sistema de archivos, agregue un directorio a su directorio del
skin. También tendrá que agregar una pequeña cantidad de configuración para
asegurarse de que su directorio es encontrado y registrado como una capa skin
en la instalación.

Primero en [your theme package]/skins.zcml

::<cmf:registerDirectory
           name="[Your Skin Directory Name]"/>


Luego en [your theme package]/profiles/default/skins.xml

::<object name="[Your Skin Directory Name]"
        meta_type="Filesystem Directory View"
        directory="[your namespace].[your theme name]:skins/[Your
        Skin Directory Name]"/>

y

::<skin-path name="[your skin name]" based-on="Plone Default">
      <layer name="[Your Skin Directory Name]"
         insert-after="custom"/>
     </skin-path>





5.2.4.2. Personalización a través del Orden de precedencia
============================================================

Cómo las capas del skin funcionan y cómo estas pueden ser usadas en la
personalización.

Si usted ha trabajado con Plone 2, estar? entonces familiarizado con este
tipo de personalización. Como hemos mencionado anteriormente, el orden de
capas en una skin determina cuales plantillas de página, archivos CSS y
scripts de Python se procesen primero.

Para inspeccionar el orden de precedencia:

-   Configuración de sitio > Interfaz de Administración de Zope >
    portal_skins
-   haga clic en la pestaña Propiedades

Usted debería ver las capas del skin por defecto de Plone que all? se listan.
Capas como "plone_templates" provienen del tema principal de Plone, pero
también habrá capas que proveen plantillas desde productos adicionales
específicos (por ejemplo, el editor visual kupu).

.. image:: images/order_of_precedence.html
  :alt: captura de las capas skins en la ZMI

Cuando se le pidi? para procesar una plantilla específica, Plone trabajar?
desde arriba hacia abajo de la lista, buscando en cada capa a su vez para
recuperar la plantilla.

En la parte superior hay una capa personalizada; cualquier plantilla colocada
aquí se encontrará y se utilizar? de primero. Por lo tanto, para crear su
propia versión de una plantilla de Plone o archivo CSS, dele el mismo nombre
que la versión de Plone pero p?ngalo en la capa personalizada.

Este es el enfoque más simple, pero el hecho de garantizar que la versión
est? en un capa superior en el orden de precedencia en un skin que el tema
principal de Plone será suficiente para asegurar que Plone lo encuentre
primero e ignore la versión original.

Esta técnica se puede utilizar de dos maneras:

utilizando la carpeta personalizada a través de la Interfaz de Administración
de Zope, usted puede agregar sus propias versiones de plantillas, hojas de
estilo, etc en la carpeta personalizada. Esto siempre se produce en la parte
superior, por lo que puede estar seguro que sus versiones se encontrarán
primero. agregando sus propias capas skin en su propio producto de tema en el
sistema de archivos, cree una o dos capas skin, y asegúrese que en la
instalación estas capas están puestas justo debajo de la carpeta
personalizada en el orden o precedencia. Hay más información sobre cómo hacer
esto en la siguiente sección.

Probablemente la descripción más completa de skins, capas y orden de
precedencia puede encontrarse en las primeras dos secciones del `Capitulo 7
de la guía definitiva para Plone`_ (note que la mayoría de este libro hace
referencia a Plone 2, pero estas secciones siguen siendo relevantes para
Plone 3).


5.2.4.3. Creando y nombrando su propio Skin
===========================================

¿Cómo se crea realmente un skin?


A través de la ZMI
-------------------

-   Vaya a la Configuración del sitio > Interfaz de Administración de
    Zope > portal_skins
-   haga clic en la pestaña Propiedades

-   Elija agregar nuevo y otórguele a su skin un nombre
-   Ahora puede escribir en una lista las capas que desea utilizar y en
    el orden que desee usarlas
-   Finalmente, en la parte inferior de la página, configure su nuevo
    skin por defecto



En el Sistema de archivos
-------------------------

Si usted utiliza la plantilla paster plone3_theme, el código lo
proporcionar?, cuando el producto de tema est? instalado, lo cual registrar?
los directorios del skin como capas skins y las reunir? en una skin nueva.

La plantilla paster le da la opción de basar su skin en el Plone Default.
Esto es, cuando instala el tema en su sitio, las capas skins de Plone serán
añadidas a las suyas, pero por debajo de las suyas en el orden de
precedencia. Esta es una buena idea, para luego reusar detalles de Plone
Default sin duplicarlos, y sustituir aquellos que no quiera.

Los pasos clave son:

1.  Registre los directorios de su skin como Filesystem Directory Views
    "Vistas de directorios del sistema de archivos", para que se puedan
    convertir en capas skin. Esto ocurre en dos sitios:[your theme
    package]/skins.zcml and [your theme package]/profiles/default/skins.xml
::<cmf:registerDirectory
               name="[Your Skin Directory Name]"/>
         ::<object name="[Your Skin Directory Name]"
            meta_type="Filesystem Directory View"
            directory="[your namespace].[your theme
            name]:skins/[Your Skin Directory Name]"/>
2.  Agregue y organice sus capas skins dentro de una sola skin [your
    theme package]/profiles/default/skins.xml
::<skin-path name="[your skin name" based-on="Plone Default">
          <layer name="[Your Skin Directory Name]"
             insert-after="custom"/>
         </skin-path>
3.  Defina su skin como la skin por defecto [your theme
    package]/profiles/default/skins.xml empaquetando este nodo alrededor de
    los nodos de los dos ejemplos anteriores.
::<object name="portal_skins" allow_any="False" cookie_persistence="False"
           default_skin="[your skin name]">
            .........
        </object>



 Acerca del nombre del Skin
--------------------------

El nombre de su skin es requerido en algunos sitios en su producto de tema.
Vale la pena conocer dónde y por qué, para referencia, las ocurrencias
figuran en esta lista.

Dónde

Atributos/Directivas utilizados/as

Uso

profiles/default/skins.xml

<skin_path name="[your skin name]"

Usado para nombrar el conjunto de capas skin

profiles/default/skins.xml

<object name="portal_skins"

default_skin="[your skin name]">

Usado para definir su grupo de capas skin como el skin por defecto.

browser/configure.zcml

<interface ???

name="[your skin name]"

/>

Usado para nombrar la interfaz específica de tema (vea la sección de
`Componentes`_)

profiles/default/viewlets.xml

<order manager="plone.portalfooter" skinname="[your skin name]"

>

Usado para especificar el tema cuando ordena los viewlets en el administrador
de estos.

(Vea la sección de `Componentes`_)


5.3. Componentes
================

La decoración de la página, viewlets, portlets, y sus respectivos
administradores. Cómo hacer el suyo propio y cómo encontrar las cosas que
necesita.


5.3.1. Estructurando componentes y ZCML
=======================================

Información sobre componentes y cómo están conectados entre sí.

.. image:: images/component.gif
  :alt: diagrama de un componente

Componentes son herramientas potentes y flexibles de Plone 3, pero un poco
más abstracto que las plantillas de página o scripts de Python. Como el
diagrama arriba intenta mostrar, estos son normalmente combinaciones de
clases Python y plantillas de páginas conectadas entre sí en el Lenguaje de
Marcado de Configuración Zope (ZCML) y con un nombre dado.

Hay dos cosas importantes para recordar acerca de los componentes

Los componentes son combinados de clases, plantillas, interfaces, permisos,
etc. Para hacer un seguimiento de componentes usted necesita buscar en primer
lugar en los archivos. ZCML, localizar sus nombres, y esto le llevar? a las
clases y plantillas que contribuyen a ellos. Los Componentes llegan a
existencia cuando la instancia de Zope es iniciada A condición de que Zope
haya le?do el archivo .zcml, un componente estar? disponible para su uso. No
es posible sobrescribir los componentes existentes, es mejor que cree la suya
propia, reusando algunas de las partes.

Partes de un Componente
-----------------------

Un componente llega a existir a través de una "directiva" ZCML (hay un
ejemplo de una de estas más adelante). La directiva tendrá un serie de
"atributos" los cuales apuntar?n a las diferentes piezas que intervienen en
su creación. Estas piezas tienen cuatro funciones principales.

1.  **Identificar** el componente (en el caso de un viewlet habitualmente
    se hace con un atributo de "nombre"
2.  **Computar **la información que el componente debe mostrar (esto
    habitualmente se hace con una clase Python apuntada con un atributo de
    "clase"). Por ejemplo, en el caso del árbol de navegación, esta seráa la
    elaboración de cual parte del árbol se debe mostrar para cada página.

3.  **Mostrar** la información que la clase del componente ha computado
    (esto habitualmente se hace con una plantilla de página).
4.  **Restringir** la presentación del componente. En el caso de un
    Viewlet, esto podría ser la restricción para mostrarlo sólo a ciertos
    usuarios registrados (mediante el atributo de "permiso") o la restricción
    para mostrarlo sólo con ciertos tipos de contenidos (mediante el atributo
    "for").


Hay más sobre esto en la sección de `partes de componentes`_


Lenguaje de Marcado de Configuración Zope (ZCML)
-------------------------------------------------

El `Five Tutorial on WorldCookery.com`_ lo guiar? a través del ZCML, y hay
suficientes ejemplos en los tutoriales en el sitio de documentación de Plone.

Aquí est? una directiva de muestra ZCML evocando el viewlet de presentación
(que simplemente ofrece un enlace a una versión de presentación de una
página):

::<configure    xmlns="http://namespaces.zope.org/zope"
        xmlns:browser="http://namespaces.zope.org/browser">
        <browser:viewlet
             name="plone.presentation"
             for="Products.ATContentTypes.interface.IATDocument"
manager="plone.app.layout.viewlets.interfaces.IAboveContentBody"
             class=".presentation.PresentationViewlet"
             permission="zope2.View"
        />
    </configure>

Hay tres cosas que destacar:

-   Al igual que cualquier tipo de XML, ZCML utiliza namespaces (espacios
    de nombre o espaciosnombre); atento de estos si usted est? escribiendo su
    propio archivo ZCML. Para componentes de tema, mayormente usar? el
    namespace del explorador.
-   Los atributos ZCML generalmente se refieren más a la interfaces que
    de los tipos de contenido. clases o componentes (vea los atributos *for*
    y *manager* en el ejemplo anterior). Encontrará más información sobre las
    interfaces en una `sección más adelante`_ .
-   Mira el atributo de clase y verá que comienza con un punto inicial.
    Esto significa que puede encontrarlo en el mismo directorio que el
    archivo ZCML como tal. Si no se encuentra dentro del mismo directorio
    entonces tendrá que dar el nombre completo.

Puede obtener información detallada sobre las directivas ZCML en la sección
de Referencia de ZCML de la API (Interfaz de programación de aplicaciones)
para Zope 3 - `http://apidoc.zope.org/++apidoc++/`_. Si usted quiere ser muy
disciplinado y ordenado, consulte la ZCMLStyleGuide
`http://wiki.zope.org/zope3/ZCMLStyleGuide`_ .




5.3.2. Viewlets, portlets y otros componentes
=============================================

Tipos de componentes.


Viewlet
=======

Esta es una nueva característica de Plone 3 y se utiliza para proporcionar
los aspectos de la decoración de la página; los elementos de la página que
por lo general no cambian en las ?reas del sitio. Estos son organizados por
otro tipo de contenido; un Administrador de Viewlet.

Para más información puede revisar:

-   Sección `Anatomía de un Viewlet`_ en este manual de referencia
-   `http://plone.org/documentation/tutorial/customizing-main-template-viewlets `_
-   `http://plone.org/documentation/tutorial/customization-for-developers/viewlets/`_


Portlet
-------

Los Portlets en Plone son cajas de información, usualmente en la columnas de
izquierda o derecha de una página, que contienen contenido agregado o
información adicional, que puede ser directamente relevante o no al elemento
de contenido que se est? mostrando. Tras bambalinas est?s se sol?an construir
de plantillas de páginas ordinarias, pero ahora en Plone 3, estos son
conectados en conjunto como componentes y manejadas por otro componente: un
Administrador de Portlet.

Para más información echa un vistazo a:

-   The `Anatomy of a Portlet`_ section of this manual
-   `http://plone.org/documentation/how-to/override-the-portlets-in-
    plone-3.0/`_
-   `http://plone.org/documentation/tutorial/customization-for-developers
    /portlet-renderers/`_ (for a much more technical explanation)
-   `http://plone.org/documentation/how-to/adding-portlet-managers`_


Vista (Vista del explorador)
----------------------------

Ya hemos dado una definición del término "vista" en la `sección de skin`_
anterior. Sin embargo, tras bambalinas, en el contexto de componentes, Vista
tiene un significado más técnico. Se refiere a un componente el cual es
regularmente creado de una clase Python o una plantilla o incluso ambas, en
pocas palabras, procesa los datos desde un elemento de contenido antes de que
llegue a la página. Hay una `explicación técnica`_ en el Manual de Desarrollo
de Plone.

A veces verá que es referida como BrowserView (Vista de Explorador) o
<browser:page> y en plantillas usted verá el nombre de vista del navegador
precedido por @@. Nos fijamos en las vistas del explorador una vez más en la
sección de `armar una página`_ .

> Note que el término explorador y namespace del explorador son usados para
demarcar componentes de presentación; esto es, esas partes de códigos que se
usan para crear elementos las cuales encontrarán el camino al navegador Web
en algún momento.


Recurso (Recurso de Explorador) y ResourceDirectory (Directorio de Recurso)
---------------------------------------------------------------------------

Aunque hemos indicado que el skin y las capas son el hogar habitual de
plantillas de páginas, imágenes y hojas de estilo, también es posible
convertirlas en componentes mediante su registro en ZCML. En este caso las
verá referidas así ++resource++[nombre del recurso]. Lo mismo se puede hacer
para un directorio que contiene las plantillas y hojas de estilo.

En este momento puedo escuchar que est? diciendo "Genial" y "¿cual debería
usar, componentes o skins?", vaya a la sección `Skin o Componentes?`_ para
una discusión de los pros y contras. Al momento de escritura sugerimos la
opción más sencilla que es mantener sus plantillas, imágenes y hojas de
estilo en su skin. Estamos mencionando los recursos del explorador para que
sepa que son en el caso de encontr?rselos.


5.3.3. Personalizando o creando nuevos
======================================

Usted puede personalizar a través de la Web, pero en el sistema de archivos
la manera para personalizar o crear componentes para su tema es conectar
nuevos.


A través de la Web
-------------------

Al igual que para skins y capas, es posible personalizar las plantillas
usadas por componentes a través de Interfaz de Administración de Zope.

-   Configuración de sitio > Interfaz de Administración de Zope >
    portal_view_customizations

Usted necesitará saber el nombre de su componente (por ejemplo
plone.presentation). La sección `Elementos`_ de este manual le ayudar? en el
caso de que el nombre no sea obvio. Solo puede rescribir las plantillas, lo
cual puede ser limitante.


En el Sistema de archivos
-------------------------

Usted puede lograr mucho más si est? construyendo su propio tema en el
sistema de archivos, y en este caso el enfoque es ligeramente diferente.

En vez de rescribir un componente (como puede hacer para el skin), es mucho
más fácil crear su propia versión. Esto involucra un poco de reestructuración
o nueva estructuración en su propio archivo .zcml, pero realmente es más
sencillo de lo que parece.

He aquí un ejemplo de la viewlet de presentación, ya que es utilizado por
Plone:

::<browser:viewlet
          name="plone.presentation"
          for="Products.ATContentTypes.interface.IATDocument"
manager="plone.app.layout.viewlets.interfaces.IAboveContentBody"
          class=".presentation.PresentationViewlet"
          permission="zope2.View"
          />

Imagine para sus propósitos, que necesita usar una nueva clase para obtener
este viewlet como usted quiere. En su propio archivo configure.zcml, dele un
nuevo nombre y conéctelo a su propia clase.

::<browser:viewlet
     *     name="[your namespace].[your presentation viewlet]"

         * for="Products.ATContentTypes.interface.IATDocument"
manager="plone.app.layout.viewlets.interfaces.IAboveContentBody"
          *class=".[your viewlet module].[your viewlet class]"

    *      permission="zope2.View"
          />

-   Recuerde que el punto delante del namespace de su clase indica que
    puede ser encontrada en el mismo directorio que el archivo de
    configure.zcml.
-   Si no est? seguro en donde se encuentra el archivo configure.zcml,
    consulte la página `¿Dónde encontrar lo que usted necesita?`_ de esta
    sección.



5.3.4. Partes de componentes
============================

Más información sobre algunas de las piezas que sirven para constituir los
componentes.


5.3.4.1. Interfaces y por qué son importantes
==============================================

Interfaces son un tema un poco tecnol?gico y algo que una persona que no sea
desarrolladora preferir?a evitar. No obstante, son una parte importante de
las conexiones (estructuras) de un componente, así que vale la pena saber un
poco que son y que hacen.


Interfaces como marcadores
--------------------------

Atributos ZCML a menudo se refieren a las interfaces en lugar de clases, por
ejemplo, el siguiente ejemplo conecta el viewlet de presentación de los tipos
de contenido que tienen la interfaz IATDocument.

::<browser:viewlet
          name="plone.presentation"
          *for="Products.ATContentTypes.interface.IATDocument"*
manager="plone.app.layout.viewlets.interfaces.IAboveContentBody"
          class=".presentation.PresentationViewlet"
          permission="zope2.View"
          />

En efecto esto se traduce en que el viewlet de presentación est? disponible
para cualquier tipo de contenido que sea un ATDocument o se comporta como un
ATDocument. Por lo tanto, en este caso, la interfaz es un marcador.

Lo conveniente de esto es que un tipo de contenido puede tener una o más
interfaces. y varios tipos de contenido pueden compartir las misma interfaz.
Si usted desarrolla un nuevo tipo de contenido y lo marca con una interfaz
IATDocumen, usted puede usar este viewlet de presentación dentro de ?l: sin
extra conexiones (estructuración) requerida.


Componentes e Interfaces
------------------------

Los componentes se pueden marcar con una interfaz, el término técnico es
"proporcionar". Tenga en cuenta que en el ejemplo de viewlet de presentación,
el administrador de viewlet es referido por su interfaz, y no por su nombre:

:: manager="plone.app.layout.viewlets.interfaces.IAboveContentBody"

Para localizar el componente, busque en el archivo configure.zcml en el mismo
directorio que las interfaces. Por ejemplo en
plone/app/layout/viewlets/configure.zcml verá que la interfaz ha sido
conectada con una clase Python para crear un componente de administrador de
viewlet:

::      <browser:viewletManager
            name="plone.abovecontentbody"
            provides=".interfaces.IAboveContentBody"
            permission="zope2.View"
class="plone.app.viewletmanager.manager.OrderedViewletManager"
            />
¿Cómo detectar una interfaz?
------------------------------

Generalmente es bastante fácil detectar una referencia a una interfaz. Por
convención sus nombres tendrán el prefijo "I" y estar?n alojados en una
interfaz o namespace de la interfaz. Si usted investiga interfaces.py o
interface.py en cualquier huevo o producto, no encontrará mucha cantidad de
código, pero a menudo encontrará información útil. Efectivamente es
documentación sobre lo que un componente que est? proporcionando (es decir
marcado por) esa interfaz debería hacer. Por ejemplo:

::class IAboveContentBody(IViewletManager):
        """A viewlet manager that sits above the content body in view
        templates    """

Si ha utilizado la plantilla de paster plone3_theme, usted encontrará que
tiene un archivo interfaces.py ya hecho, en donde puede agregar sus propias
interfaces en el caso de que sea necesario crearlas.


5.3.4.2. Clases de Python
=========================

Habr? notado que las clases de Python a menudo son parte de las conexiones
entre componentes, y entender? que realmente no puede evitar tener un poco de
conocimiento acerca de ellas, especialmente si quiere crear sus propios
viewlets.

Tener que lidiar con algo tan avanzado como las clases Python puede ser
desalentador para el aquel no-desarrollador. La buena noticia es que el uso
de clases Python será más un asunto de copiar y cambiar pequeñas partes de
código que escribir desde cero.


¿Qué es una clase?
--------------------

Lo mejor es pensar en una clase como una pieza discreta de código que
contiene una colección de métodos ("acciones" de algún tipo) y atributos
("variables" que pueden contener un valor).

En el caso de componentes, el objetivo principal de una clase es computar las
partes de información que un componente necesita mostrar. La clase del
viewlet de logotipo es un buen ejemplo. Puede encontrarlo en:

-   [ubicación de su huevo]/plone/app/layout/viewlets/common.py - busque
    por LogoViewlet

Despu?s de un poco de trabajo preparatorio, la clase LogoViewlet primero
averigua el nombre de la imagen que se va a utilizar para el logotipo (y se
define en la hoja de propiedades base_properties):

::logoName = portal.restrictedTraverse('base_properties').logoName


Luego resuelve las estad?sticas vitales, tamaño, alt text (texto alternativo)
etc y lo convierte en una etiqueta de anclaje HTML:

::self.logo_tag = portal.restrictedTraverse(logoName).tag()


Finalmente, en el caso de que sea necesario, busca el título del sitio:

::self.portal_title = self.portal_state.portal_title()

En la plantilla de página asociada con este viewlet puede hacerse con esta
información (self.logo_tag, self.portal_title) usando la variable "view":

::<img src="logo.jpg" alt=""
             tal:replace="structure view/logo_tag" />
?Tengo que usar clases?
------------------------

Los viewlets tienden a estar conectados con una clase Python que apunta a una
plantilla. Así que, aunque es posible que sólo desea crear una nueva
plantilla, usted descubrir? que tiene que escribir una clase para que apunte
a su nueva plantilla. La sección `Elementos`_ de este manual debería ayudarlo
d?ndole un fragmento de código para que cada elemento copie y pegue dentro de
su propio producto.

Aquí hay un ejemplo: La plantilla de logotipo estándar en realidad no hace
uso de view/portal_title. Así que si usted quería incorporar esto de alguna
manera en su logotipo, entonces usted tendráa que escribir su propia
plantilla y también su propia clase:

::from plone.app.layout.viewlets.common import LogoViewlet
    from Products.Five.browser.pagetemplatefile import
    ViewPageTemplateFile

    class [your class name](LogoViewlet):
        render = ViewPageTemplateFile('[nombre de su plantilla]')

-   Primero traiga ("import" ("importar")) todas las partes y detalles
    mediante los cuales construir? su clase por...... import......

-   A continuación, defina su clase. Lo importante aquí es que se base en
    una clase pre-existente, de modo que usted no tenga que empezar de cero.
    Ponga el nombre de la clase pre-existente entre par?ntesis después del
    nombre de su clase (asegúrese de que lo haya importado primero). ?No
    olvide los dos puntos!
-   Finalmente, reescriba cualquiera de los métodos y atributos que
    necesite. Aquí hemos reescrito el método *render* para mostrar nuestra
    propia plantilla.

Nota: el sangrado es muy importante en el código Python, la convención es
usar cuatro espacios (en lugar de un espacio tabulador). Si est? teniendo
problemas, revise la sangr?a primero.

-   `http://wiki.python.org/moin/HowToEditPythonCode`_

Si se siente valiente o quiere saber más, una introducción clara se puede
encontrar aquí:`
`_

-   `Dive Into Python - Defining Classes `_





5.3.4.3. Permiso
================

El atributo de permiso se puede usar para restringir la visibilidad de un
componente.

Cuando un usuario inicia sesión en un sitio, se le dar? cierto rol
("administrador", "editor", etc.) Este rol, efectivamente, es un conjunto de
permisos, que otorgan derechos particulares sobre ciertos aspectos del sitio.

Para saber más sobre permisos consulte el tutorial para el entendimiento de
permisos y seguridad:

-   `http://plone.org/documentation/tutorial/understanding-permissions/`_

En el caso de componentes, el atributo de permiso permite al sitio decidir si
un usuario tiene un derecho (permiso) para ver o interactuar con un
componente. La mayoría de viewlets tiene los permisos Zope2.View o
Zope2.Public, los cuales se asignan a todo el mundo, incluso usuarios
an?nimos. Sin embargo observe el viewlet Lock info (información de bloqueo)

::<browser:viewlet
            name="plone.lockinfo"
            manager=".interfaces.IAboveContent"
            class="plone.locking.browser.info.LockInfoViewlet"
            permission="cmf.ModifyPortalContent"
            for="plone.locking.interfaces.ITTWLockable"
            />


Al usar cmf.ModifyPortalContent, este viewlet est? restringido, es decir, se
limita a sólo aquellos usuarios que tienen derecho de editar contenido
(aquellos que no lo posean no estar?an interesados si un elemento est?
bloqueado o no).

La lista de permisos disponibles est? enterrada profundamente en el producto
FIVE, el cual viene con la instalación de Zope, revise en permissions.zcml
para la lista más actualizada.



zope2.Public

público, cualquiera puede acceder

zope2.Private

Privado, sólo accesible desde código de confianza

zope2.AccessContentsInformation

Acceder a información de contenido

zope2.ChangeImagesFiles

Cambiar Im?genes y Archivos

zope2.ChangeConfig

Cambiar configuración

zope2.ChangePermissions

Cambiar permisos

zope2.CopyOrMove

Copiar o Mover

zope2.DefinePermissions

Definir permisos

zope2.DeleteObjects

Eliminar objetos

zope2.FTPAccess

Acceso FTP

zope2.ImportExport

Importar/Exportar objectos

zope2.ManageProperties

Administrar propiedades

zope2.ManageUsers

Administrar usuarios

zope2.Undo

Deshacer cambios

zope2.View

Vista

zope2.ViewHistory

Ver historial

zope2.ViewManagementScreens

Ver pantallas de administración

zope2.WebDAVLock

WebDAV Lock items (elementos de bloqueo WebDAV)

zope2.WebDAVUnlock

Elementos desbloqueados WebDAV

zope2.WebDAVAccess

Acceso WebDAV

cmf.ListFolderContents

Listar contenido de carpetas

cmf.ListUndoableChanges

Listar cambios infactibles

cmf.AccessInactivePortalContent

Acceso a contenido inactivo del portal

cmf.ManagePortal

Administrar portal

cmf.ModifyPortalContent

Modificar contenido del portal

cmf.ManageProperties

Administrar propiedades

cmf.ListPortalMembers

Listar miembros del portal

cmf.AddPortalFolders

Agregar carpetas de portal

cmf.AddPortalContent

Agregar contenido de portal

cmf.AddPortalMember

Agregar miembro de portal

cmf.SetOwnPassword

Definir su propia contrase?a

cmf.SetOwnProperties

Definir sus propiedades

cmf.MailForgottonPassword

Env?o por correo de contrase?as olvidadas

cmf.RequestReview

Solicitar revisión

cmf.ReviewPortalContent

Revisión de contenido de portal

cmf.AccessFuturePortalContent

Acceso a contenido futuro de portal




5.3.5. Creando componentes específicos de tema
===============================================

Quiz? usted quiere hacer componentes que sólo están disponibles para su tema
particular. Para hacer esto necesitará una interfaz.

En la medida que los componentes entren en existencia en el momento que Zope
inicie y lea los archivos .zcml, estar?n disponibles para cada sitio Plone
que usted tenga en la su instancia Zope. Tal vez usted no quiere que esto
pase..


Una interfaz de tema
--------------------

Usted puede especificar que sus componentes están disponibles sólo para su
tema con una interfaz de marcador y un atributo de capa en ZCML. Aquí hay una
versión re-conectada (reestructurada) del viewlet de presentación:

::<browser:viewlet
          *name="[your namespace].[your presentation viewlet]"

         * for="Products.ATContentTypes.interface.IATDocument"
manager="plone.app.layout.viewlets.interfaces.IAboveContentBody"
          *class=".[your viewlet module].[your viewlet class]"

          layer=".interfaces.IThemeSpecific"*
          permission="zope2.View"
          />

Nota: no confunda el atributo de capa con una capa de skin. Aquí, capa se
refiere al tema completo y no a una sola parte de ?l.

Hay dos métodos para crear una interfaz de tema:


Usando plone.theme
~~~~~~~~~~~~~~~~~~

En Plone 3.0, plone.theme es usado:

-   Una interfaz de marcador es definida en [su paquete de
    tema]/browser/interfaces.py:

::from plone.theme.interfaces import IDefaultPloneLayer

    class IThemeSpecific(IDefaultPloneLayer):
        """Marker interface that defines a Zope 3 browser layer.
        """

-   y esto es registrado en ZCML en [su paquete de
    tema]/browser/configure.zcml

::<interface
            interface=".interfaces.IThemeSpecific"
type="zope.publisher.interfaces.browser.IBrowserSkinType"
            name="[your skin name]"
            />

Nota: [el nombre de skin] surge aquí; revise de nuevo la sección de skins si
se est? preguntando que es esto.


Usando plone.browserlayer
~~~~~~~~~~~~~~~~~~~~~~~~~

En Plone 3.1, plone.browserlayer est? disponible para usted.

-   Cree su interfaz (por ejemplo en [su paquete de
    tema]/browser/interfaces.py)

::from zope.interface import Interface
        class IThemeSpecific(Interface):
            """A layer specific to my product        """

-   Registre esto en la configuración (en [su paquete de
    tema]/profiles/default/browserlayer.xml):

::<layers>
     <layer name="[your skin name]"
       interface="[your namespace].[your theme
       name].browser.interfaces.IThemeSpecific"
     />
    </layers>

Si usted genera su producto de sistema de archivo o huevo utilizando la
plantilla paster plone3_theme, pues lo básico estar? hecho para usted (usando
el método plone.theme), simplemente tendrá que localizar la interfaz para
encontrar su respectivo nombre. Busque en

-   [su paquete de tema]/browser/interfaces.py or configure.zcml

Y debería encontrara el nombre IThemeSpecific. Cuando se refiera a ella, use
esta ruta

::layer=".interfaces.IThemeSpecific"


5.3.6. Skin o Componentes?
==========================

Habr? notado que usted puede convertir cualquier plantilla, archivo css, o
cualquier directorio que contenga estos en un componente. Así que ?por qué
molestarse con el bloque para construcción de skin?

El producto creado por la plantilla de paster plone3_theme hace lo siguiente:

-   **sustituye y sobrescribe** en las plantillas estándar de Plone
    Default y archivos CSS van en la sección**Skin**; el directorio de skins.
-   **nuevas** hojas de estilos e imágenes van en la sección de
    **Componentes**: el directorio del explorador.

Este manual sugiere poner todas sus plantillas, hojas de estilo e imágenes en
la sección de Skin, y dejar sólo las plantillas de viewlets y portlets en los
componentes. Hay varias razones para esto

-   es más fácil hacer esto cuando usted apenas est? comenzando
-   sigue el camino por el cual Plone Default es construido
-   hace que sea rápido y fácil ajustar su tema sobre la marcha después
    de que se haya instalado. En ese punto, usted puede realizar más
    personalizaciones del skin a través de la Interfaz de Administración de
    Zope.


Al momento de estar escribiendo esto hay una `gran discusión`_ tratando de
resolver esta pregunta.



Si usted quiere quitar los recursos del explorador fuera del producto creado
por la plantilla paster plone3_theme

-   remove the images and stylesheets directories in the [your theme
    package]/browser
-   elimine las entradas <browser:resourceDirectory /> en [su paquete de
    tema]/browser/configure.zcml
-   elimine la entrada de la stylesheet de registro para main.css en [su
    paquete de tema]/profiles/default/cssregistry.xml
-   si ya ha instalado el producto es posible que tenga que consultar el
    registro de CSS en la interfaz de Administración de Zope (portal_css) y
    elimine la entrada main.css all? también





5.3.7. ¿Dónde encontrar lo que usted necesita?
================================================

En dónde colocar los componentes de su propio producto y la manera de
rastrearlos en la interfaz de Administración de Zope, y en el sistema de
archivos.


A través de la Web
-------------------

Las plantillas para la mayoría de componentes pueden ser personalizadas a
través de la web:

-   Configuración de sitio > Interfaz de Administración de Zope >
    portal_view_customizations

La sección `Elementos`_ le puede ayudar a identificar el componente que usted
necesita.


Componentes de Plone Default en el sistema de archivos
------------------------------------------------------

Si usted est? planeando conectar sus propios componentes, puede que sea
necesario localizar los archivos relevantes de componentes existentes para
copiarlos. Esto puede tener cierto grado de dificultad, Estos est?n
empaquetados en un número de huevos distintos, por lo que necesita primero
localizar dónde se almacenan los huevos, y luego averiguar cuál de estos
contiene los elementos de componentes que necesita.

-   Para averiguar dónde se encuentran sus huevos, vea la sección `¿Dónde
    est? qu??`_ de este manual
-   La sección `Elementos`_ de este manual le ayudar? a encontrar el
    huevo que contiene ese componente que usted necesita.


Dentro de su propio producto de tema
------------------------------------

.. image:: images/your_theme_egg_components_cutdown.gif
  :alt: La carpeta del explorador en producto de tema
/browser/viewlet.py | viewlet.pt Un ejemplo de un componente viewlet
/browser/interfaces.py Esto se usa para crear la interfaz de su tema
/profiles/default/viewlets.xml Utilice este archivo para ordenar sus viewlets
dentro de los administradores de viewlets /browser/configure..zcml Utilice
este archivo para conectar los componentes /browser/templates | styles Estos
directorios pueden usarse para plantillas, estilos, e imágenes. Usted tendrá
que registrar estos como directorios para recursos en configure.zcml


5.4. Configuración
===================

¿Cómo escribir un archivo de configuración y dónde ponerlo?


5.4.1. Perfiles
===============

Configuración y los perfiles

La configuración se refiere al comportamiento predeterminado de un sitio (por
ejemplo, si usted permite que las personas se registren en su sitio, o cómo
se muestran las fechas). Es probable que quiera que algo de este
comportamiento sea incorporado en su tema.

También hay cierta coincidencia entre los componentes, skins, y
configuración. Por ejemplo, el orden de las capas del skin y el orden en que
aparecen los viewlets dentro de un administrador de viewlet se consideran
aspectos para la configuración.


Perfil
------

Un perfil es un conjunto de archivos de configuración. Cada archivo est?
escrito en un XML bastante simple y hace referencia a un grupo en particular
de componentes o elementos de página. Hay dos tipos diferentes de perfiles:
perfiles de base y perfiles de extensión. Para fines de temas el único que
usted necesitará es el perfil de extensión (es decir, un perfil que extiende
la configuración de un sitio existente).

Un perfil aparece cuando se conecta mediante ZCML. Aquí est? la versión
creada por la plantilla de paster plone3_theme:

::<genericsetup:registerProfile
     name="default"
     title="[your skin name]"
     directory="profiles/default"
     description='Extension profile for the "[your skin name]" Plone
     theme.'
     provides="Products.GenericSetup.interfaces.EXTENSION"
    />

verá que apunta a un directorio para la ubicación de los archivos XML e
indica que se trata de un perfil de extensión mediante el uso de una
interfaz.


5.4.2. Configuración gen?rica XML (Generic Setup XML)
=======================================================

El lenguaje utilizado para definir los perfiles.

El XML utilizado para los archivos de perfil es sencillo. No hay ningún DTD
disponible, pero hay una cantidad de ejemplos para reusarlos o adaptarlos
para sus propósitos. Si todo esto parece demasiado, la buena noticia es que
puede conseguir que Generic Setup escriba los archivos por usted exportando
la configuración de un sitio existente. Hay más información sobre cómo hacer
esto en la página de herramienta Generic Setup.

El nodo root de un perfil XML es por lo general un objeto:

::<object name="portal_javascripts" meta_type="JavaScripts Registry">
         .......
    </object>

pertenece a una herramienta de sitio en particular (en este caso el registro
JavaScripts). Sub-nodos representan sub-objetos y atributos XML corresponden
a los atributos de esas clases.

::<javascript cacheable="True" compression="none" cookable="True"
                enabled="True" expression="" id="jquery.js"
                inline="False"/>

Así que en este caso, el sub-nodo representa una entrada en el registro
JavaScripts y sus casillas de verificación.

.. image:: images/portal_js_snippet.gif
  :alt: screenshot of the javascripts registry in the ZMI


En el caso muy improbable de que sea necesario que averig?e por sí mismo que
atributos usar, tendrá que investigar la API (o las interfaces y clases) de
la herramienta en cuestión. Use `http://api.plone.org`_ o revise el código
fuente.


5.4.3. Herramienta Generic Setup (instalación gen?rica)
=========================================================

Esta herramienta se utiliza para aplicar perfiles a su sitio.

La puede encontrar aquí

-   Configuración de sitio > Interfaz de Administración de Zope >
    portal_setup

Puede ejecutar la herramienta manualmente, pero para efectos de temas, si ha
creado un producto usando la plantilla de paster plone3_theme, Generic Setup
será activada automáticamente cuando instale su tema en su sitio.

Encontrará información más extensa acerca de la herramienta Generic Setup en
este tutorial:

-   `Understanding and Using Generic Setup on plone.org`_

Sin embargo, hay dos datos útiles que valen la pena conocerlos.


No Deshacer
-----------

Aunque se puede desinstalar su tema usando portal_quickinstaller, en la
actualidad, no puede deshacer los perfiles que Generic Setup aplic? durante
la instalación. En la mayor parte esto no es un problema, pero puede ser
confuso. Por ejemplo si est? experimentando con el orden de sus viewlets y ha
probado varias versiones de viewlets.xml en instalaciones sucesivas. En este
caso, la exportación de un perfil (explicado más adelante) le puede ayudar a
dar sentido a lo que ha hecho.


Exportando de perfiles
----------------------

Puede exportar la configuración actual de su sitio como un conjunto de
archivos XML. Esto puede ser útil si no est? muy seguro de lo que ha hecho,
si est? buscando un perfil para basar su propia configuración, o si
simplemente desea que la herramienta Generic Setup escriba una configuración
para usted.

-   Configuración de sitio > Interfaz de Administración de Zope >
    portal_setup
-   Haga clic en la pestaña de exportación
-   Seleccione los steps que desea exportar

-   Haga clic en el botón para exportar los steps seleccionados
-   Se le dar? un archivo zip con los archivos XML correspondientes


No siempre es obvio cuál step necesita exportar para obtener la exacta
configuración que desea, es posible que tenga que experimentar.


5.4.4. ¿Dónde encontrar lo que usted necesita?
================================================

Cómo funciona la configuración a través de la web y cómo localizar los
archivos en el sistema de archivos.


A través de la Web
-------------------

Hay una serie de rutas diferentes para configurar su sitio a través de la
web. La sección`Elementos`_ de este manual debe proporcionarle algunos
consejos sobre dónde buscar para configurar ciertos elementos de página. En
general

-   Configuración de sitio le lleva a configlets para las configuraciones
    del sitio.

-   Configuración de sitio > ZMI le guiar? a la hoja de estilo y registro
    JavaScript (portal_css y portal_javascripts)
-   Añadiendo /@@viewlet_manager a la URL le permitir? ordenar viewlets.


Configuración de Plone Default en el sistema de archivos
---------------------------------------------------------

Usted encontrará mayoría de los archivos de configuración que usted necesita
en:

-   [su locación de productos]/CMFPlone/profiles/default

Sin embargo, tenga en cuenta que algunos archivos de configuración pueden
estar ubicados en productos de terceros. Por ejemplo, si desea añadir algunos
estilos al editor visual Kupu, como parte de su tema, entonces necesitará
kupu.xml el cual encontrará en [su locación de
producto]/kupu/plone/profiles/default.

Hay una alternativa para cazar en el sistema de archivos, y esta es utilizar
la herramienta Generic Setup para exportar el perfil.


Dentro de su propio producto de tema
------------------------------------

.. image:: images/your_theme_egg_config_cutdown.gif
  :alt: El directorio de configuración de su producto tema
/profiles/default/ Este directorio contiene el XML para Generic Setup La
plantilla paster plone3_theme le proporcionar? algunos archivos ya hechos;
para definir sus capas de skin, registrar sus hojas de estilo y JavaScript, y
ordenar los viewlets. /profiles/default/import_steps.xml es un archivo
esencial para instalación, no debería tener que cambiar esto,
/profiles/default/cssregistry.xml | jssregistry.xml registrar? cualquier hoja
de estilo y JavaScript en su skin. Tendrá que editar estos por usted mismo si
tiene cualquier archivo css o Javascript que agregar.
/profiles/default/skins.xml Colocar? sus capas de skin en el orden correcto
de precedencia. No necesitará cambiar esto a menos que lo haya re-nombrado,
eliminado, o agregado directorios en los skins.
/profiles/default/viewlets.xml determinar? en que orden los viewlets aparecen
en el administrador de viewlet Necesitar? editar esto usted mismo si quiere
agregar sus propios viewlets. /profiles.zcml Cuando la instancia de Zope
inicia, este archivo hace que el perfil est? disponible para el uso de
Generic Setup.


6. Armando una página
======================

¿Cómo todas estas partes y piezas van de la mano para hacer una página web?
Y, más importante a?n, ¿cómo se obtiene el contenido sobre la página?


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
contenido que est? visualizando. Aquí hay un fragmento de la plantilla RSS,
llamando el campo de descripción de una elemento de colección de contenido:

::<description>
        <metal:block define-slot="description">
           <tal:block content="*context/Description*">
              Default rss description goes here
           </tal:block>
        </metal:block>
    </description>

-   *context *se refiere al elemento actual de contenido
-   *Description * es el accessor (acceso) del campo de descripción


Accessors
~~~~~~~~~

Un accessor es simplemente el método por el cual los datos en un campo son
extra?dos. En la mayoría de los casos el nombre de un accessor es el nombre
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

::<p class="documentDescription">
     <metal:field use-macro="python:here.widget('description',
     mode='view')">
         .....
    </metal:field>
    </p>
Obteniendo contenido del cat?logo
----------------------------------

Cada elemento de contenido est? catalogado en la creación y edición. Algunos
de sus campos están indexados para b?squeda rápida y clasificación, mientras
que los valores de los demás se almacenan en lo que se llama el "cerebro" o
"metadatos" para rápido acceso.

páginas reuniendo un conjunto de tipos de contenido; una carpeta o colección
listando. A menudo reciben su contenido de una consulta de cat?logo y
cerebro, en vez de despertar cada elemento de contenido. Normalmente
encontrará una variable definida en alguna parte que contiene los resultados
de una consulta de cat?logo:

::folderContents here.queryCatalog(contentFilter);

Luego la plantilla har? bucles a través de los resultados y los valores de
llamada desde el cerebro/metadatos:

::item_url item/getURL;
    item_id item/getId;

Estos se parecen mucho a los accessors normales, de hecho, son los nombres de
campos en el cerebro/metadatos del cat?logo. Esto puede tornarse confuso, si
usted trata de acceder a un campo que no est? en el cerebro/metadatos
obtendrá un error.

Usted puede ver qu? campos están disponibles para usted a través de

-   Configuración de sitio > Interfaz de Administración de Zope >
    portal_catalog > metadata tab

Si quiere entender más del catalogo, hay una visión general útil en el `Zope
book`_, un recorrido más específico de Plone en `The Definitive Guide to
Plone`_ (Este libro es sólo para Plone 2, pero la sección de cat?logo sigue
siendo relevante para Plone 3).


Obteniendo contenido vía Python (usando un componente de vista)
----------------------------------------------------------------

Usualmente es más eficiente usar una vista para procesar los datos desde un
elemento de contenido (o un grupo de elementos de contenido) y luego situarlo
dentro de la plantilla de página. En este caso, por view (vista) queremos
decir un componente específico definido en ZCML.

Aquí hay un fragmento que llama una vista para renderizar el sitemap (mapa
del sitio):

::<ul id="portal-sitemap"
        class="navTreeLevel0 visualNoMarker"
        tal:define="view *context/@@sitemap_view;*">
         <tal:sitemap replace="structure view/*createSiteMap*" />
    </ul>

-   *context/@@sitemap_view* es asignado a un variable llamada
    (amablemente) "view"
-   *createSiteMap* es un método de @@sitemap_view
-   @@ indica que esto es un componente de vista

Aquí est? la estructuración o conexi?n en ZCML que crea @@sitemap_view:

::<browser:page
         for="*"
    (there???s no restriction on where I can be used)
         name="sitemap_view"
    (this is my name)
         class=".sitemap.SitemapView"
    (this is where you can find the code to deliver my content)
         permission="zope.Public"
    (you can see me if you have the Public permission)
         allowed_interface=".interfaces.ISitemapView"
    />

En resumen

-   El contenido es procesado por una clase Python
-   ZCML conecta esta clase en un componente
-   la plantilla llama este componente






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
su visualización. Como hemos visto en la sección `Plantillas y el lenguaje de
plantillas`_, estas usualmente tienen _view agregado a sus nombres. Usted
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

.. image:: images/maintemplate.html


Si no se siente seguro acerca de las ranuras, entonces vuelva a revisar
`Plantillas y el lenguaje de plantillas`_.

Alrededor del la ranura (slot) principal, los componentes; viewlets y
portlets entran en juego, suministrando los elementos de decoración para el
contenido. La plantilla principal simplemente trae estos a través de los
administradores de viewlets y portlets.

Los viewlets son tan flexibles que incluso pueden ser tra?dos a la vista de
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

::metal:use-macro="here/main_template/macros/master"

El código que se usa desde document_view es en realidad el pedacito entre
estas etiquetas:

::<metal:main fill-slot="main"> ?????? </metal:main>

Esto se sit?a en un slot en el the main_template:

::<metal:bodytext metal:define-slot="main"
                    tal:content="nothing">
    ...
    </metal:bodytext>

2. Si regresamos al fill-slot (slot-para llenar) en el document_view
    podr? ver algunas etiquetas que llaman campos relevantes desde el tipo de
    contenido, como este:

::<metal:field
           use-macro="python:here.widget('title', mode='view')">
    </metal:field>

También verá algunas etiquetas como llamar a los administradores viewlet que,
a su vez, convocar? grupos de viewlets:

::<div tal:replace="structure provider:plone.abovecontentbody" />

Estos le permiten colocar piezas extra de decoración de página alrededor del
contenido específico desde los campos (ejemplo, el enlace de modo de
presentación).


Acerca de la plantilla principal (main template)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Regrese a main_template y verá llamadas similares a otros
    administradores viewlet manejando grupos de viewlets para más decoración
    de página:

::<div tal:replace="structure provider:plone.portaltop" />

2. Y las llamadas a los administradores para traer los portlets definidos
    para esa página en particular:

::<tal:block replace="structure provider:plone.leftcolumn" />

3. verá también un numero de slots adicionales (define-slot), los cuales
    pueden ser llenados (fill-slot) desde la plantilla de vista de contenido.
    Aquí hay una que puede utilizar para añadir un poco de css:

::<metal:styleslot define-slot="style_slot" />

Regrese a su plantilla de vista de contenido y simplemente agregue un fill-
slot adicional (fuera de los fill-slot principales):

::<metal:mystyleslot fill-slot="style_slot">
     .....
    </metal:mystyleslot>

Revisaremos otras maneras de proporcionar estilos con más detalle en la
siguiente sección.


6.2.2. ¿Cómo mostrar el contenido completo en las vistas de carpetasí
=======================================================================

Esta parte sólo tiene sentido para las carpetas, carpeta inteligente, u otros
puntos de vista similares con un número bastante reducido de elementos.
Muestra cómo presentar una vista completa de los contenidos en los listados
mediante el uso de macros ya definidos para los tipos de contenido. El mismo
método puede ser utilizado para definir viewlets para los productos de diseño
como compositepack.

Yo estaba buscando un producto de diseño para la portada de un sitio en el
que estoy trabajando, y los productos existentes no satisfac?an mis
necesidades, ya que sólo mostraban vistas de resumen de contenido en lugar de
la vista completa. En vez de escribir viewlets para diferentes tipos de
contenido desde cero, utilic? los macros de vista existentes de los tipos de
contenido de la siguiente manera, en una nueva vista de carpeta que llam?
folder_full_view (esto es sólo un fragmento de código):

::        <tal:listing condition="folderContents">

                    <div tal:repeat="item
                    folderContents">
                    <tal:block tal:define="here
                    item/getObject;
         actions nothing;
         view here/defaultView;
         object_title
                                           item/pretty_title_or_id"
                               tal:on-
                               error="nothing">
                       <div metal:use-
                       macro="here/?view/macros/main"/>

                    </tal:block>
                    </div>

            </tal:listing>

El establecimiento de acciones a "nothing" (nada) es para que los iconos de
acción no se muestren en cada elemento de contenido. El on-error="nothing"
puede que no aparezca con usted. Yo lo tengo porque permit? que el cat?logo
devolviera resultados para los cuales no hay permiso de Vista.

De igual manera para el producto CompositePack, yo defin? un viewlet.

::<div class="viewlet default_view">
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



Use estas ideas bajo su propio riesgo. Hasta ahora a m? me han funcionado.


6.2.3. ¿Cómo cambiar el tamaño de imágenes usando PiL en Plantillas de página?
==============================================================================

Una breve descripción de cómo cambiar el tamaño de imágenes (image field)
desde un campo de imagen utilizando la biblioteca de imágenes de Python en
sus Plantillas de página mediante el uso de TAL.

PROBLEMA:

Tengo un tipo personalizado con un ImageField. Estoy personalizando un
listado de carpeta de estos tipos y yo quería una vista miniatura de cada
imagen en el listado de carpetas. Esto es muy sencillo usando PiL (Python
Imaging Library - librería para imágenes en Python), si sabe qu? hacer.
También se me present? el problema de trabajar con el cerebro y no con el
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

::<tal:foldercontents define="contentFilter
contentFilter|request/contentFilter|nothing;

contentsMethod
                                python:test(here.portal_type=='Topic',
                                here.queryCatalog, here.getFolderContents);

folderContents folderContents|python:contents
                                Method(contentFilter);">



        <tal:entry tal:repeat="item folderContents">

        <tal:block tal:define="item_url item/getURL|item/absolute_url;">

Como puede ver, mientras que se itera sobre "item" (elemento) usted est?
accediendo a las cosas del cerebro de una manera cerebro, como "item/getURL".
Pero se dar? cuenta de que no se puede hacer "item/my_image" porque no est?
en el cerebro. ¿Qué hacer? podría aclamar. Bueno puede despertar los objetos,
obtener el campo de imagen, y luego llamar el cambio de tamaño de imagen de
una manera "pythonica", pero esto es un impacto en el rendimiento, ya que
pone Python en su TAL, cosa que debería evitar.

En lugar de esto usted va a ser astuto. Ya tiene "item_url" y sabe el nombre
de su campo de imagen (my-image) así que coloque estas juntas y llegar? justo
a la imagen. Pruebe esto en su navegador:

http://full/url/to/your/object/my-image

y ?debería ver su imagen! Al traducir esto en TAL, seráa de la siguiente
manera:

::<img src="#" tal:attributes="src string:${item_url}/my-image" />

Ahora añadir la parte de modificar el tamaño de la imagen, y aquí es donde me
equivoqu?. Mucha de la documentación sobre PiL de Plone asume que usted est?
trabajando con un objeto ATImage, pero no es así. Est? trabajando con un
ATImageField. ATImageField sólo define UN solo tamaño de escala de la imagen
por defecto:

::sizes = {'thumb': (80,80)}

 Donde ATImage define un montón:

::sizes = {'large'   : (768, 768),

               'preview' : (400, 400),

               'mini'    : (200, 200),

               'thumb'   : (128, 128),

               'tile'    :  (64, 64),

               'icon'    :  (32, 32),

               'listing' :  (16, 16),

              },

Para empeorar el asunto, note que los tamaños definidos para el mismo tamaño
clave son diferentes. ?Perro malo, no hay galleta! De cualquier forma, lo que
esto significa es que para acceder al tamaño que quiere, tiene que definirlo
en su esquema por adelantado, de esta manera:

::    ImageField(

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
(schema) personalizado, est? listo para usarlo en su Plantilla de página.
?Recuerda la manera en que accedimos a esto antes?

::<img src="#" tal:attributes="src string:${item_url}/my-image" />

Para acceder a los tamaños definidos en su esquema, simplemente agregue el
nombre al final de su imagen, precedida por un gui?n.

::<img src="#" tal:attributes="src string:${item_url}/my-image_mini" />

Es así de simple, y debería ser así. No debería tener que acceder y por
consiguiente ?despertar sus objetos!. Hay también otras maneras de obtener
PiL, pero considero que esta es la manera más fácil y sin arrojar ningún
error bizarro como "Unauthorized" o "TypeError:a float is required"

?Disfrute!
~Spanky

TAMBI?N VEA:

`http://plone.org/documentation/manual/archetypes-developer-manual/fields
/fields-
reference`_`http://plone.org/documentation/tutorial/richdocument/pil`_


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
adicional. Usted notar? que hay bastantes hojas de estilo y archivos
JavaScript disponibles (y no todos son siempre requeridos). Por lo tanto una
herramienta de registro se?ala y escoge como es requerido y asocia sólo
aquellos que necesitan para velocidad y eficiencia.

Hay un tutorial detallado sobre cómo utilizar estos registros en el `
siguiente sección `_ .

incluyendo el uso de condiciones para especificar que sólo desea un recurso
en particular cargado en un contexto particular (por ejemplo, con la vista de
documento).


Registrando hojas de estilo y JavaScript
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   A través de la web puede agregar o eliminar hojas de estilo y
    JavaScript yendo a la interfaz de Administración de Zope > portal_css o
    portal_JavaScripts.
-   En el sistema de archivos, el registro de hojas de estilo y
    JavaScript es parte de la configuración. Por lo que tendrá que buscar en
    profiles/default/jssregistry.xml and cssregistry.xml.


DTML (Document Template Markup Language - Lenguaje de Marcado de Documento de
Plantilla)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~

Algunos de los archivos por defecto en la hojas de estilo de Plone poseen una
extensión .dtml, y la CSS que est? adentro est? empaquetada.

::/* <dtml-with base_properties> */
     .......
    /* </dtml-with> */

DTML es otro lenguaje de plantillas de Zope, que en este caso se ha
implementado de manera que ciertas variables puedan ser recogidas a partir de
una hoja de propiedades (base_properties.props), por ejemplo:

::#portal-column-one {
        vertical-align: top;
        *width: <dtml-var columnOneWidth missing="16em">;

    *    border-collapse: collapse;
        padding: 0;
    }


Nosotros no recomendamos el uso de esta técnica, ya que es probable que
desaparezca, pero es bueno saber que est? all?. A veces puede quedarse
atrapado al estar personalizando una hoja de estilo existente y
accidentalmente borra la parte superior o inferior de la sentencia "dtml-
with".


6.3.2. Utilizando los Registros de recursos para controlar CSS y
    JavaScript
===========================================================================

Plone tiene dos herramientas claras para la gestión de hojas de estilo en
cascada y JavaScript en una forma práctica. Este tutorial explica algunos
porqu?s y cómo e incluso tiene un m?nimo ejemplo pr?ctico de cómo funciona.


6.3.2.1. ?Por qu? tenemos estos registros?
============================================

?Por qu? los registros de recursos fueron escritos, qu? hacen, y por qué son
útiles?

Los ResourceRegistries brotan fuera (como la mayoría de características en
Plone) de frustraciones con el estado del mundo ante su existencia: si desea
agregar una hoja de estilo CSS o una librería JavaScript a su sitio Plone,
más all? de usar Custom.css-file, usted tendráa que sustituir las plantillas
de encabezado. Esto era doloso desde el punto de vista de mantenimiento, y
tampoco permit?a que ocurriera más de una vez. No hab?a manera de que
Productos suministraran sus propios archivos css sin grandes conflictos en el
caso de que más de un producto intentara hacer lo mismo. Tener varias hojas
de estilo y archivos JavaScript para hacer las cosas más manejables en el
sistema de archivos fue doloroso también.

Con la existencia de ResourceRegistries también hemos sido capaces de dividir
CSS de Plone y JavaScript en partes más manejables que pueden ser activadas o
desactivadas con el clic de un botón. No hubi?ramos podido hacer esto en
versiones anteriores de Plone ya que la división de las hojas de estilo
hubiera aumentado el número de peticiones separadas HTTP necesarias para
mostrar una página de manera incre?ble.


Los registros de recursos deberían:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

~~~~~~~~~~~~~~~~~~~~~~~~~

Los registros de recursos actualmente consisten en dos herramientas Plone que
est?n en la ZMI en el root de su sitio Plone. Ellos han sido parte del
paquete/instaladores de Plone desde Plone 2.1. (Se pueden usar con Plone
2.0.x también. Hay un archivo especial readme en el producto para
instrucciones de instalación para Plone 2.0.x)


¿Cómo funcionan los registros?

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cada registro tiene una lista ordenada de los recursos, archivos CSS o
JavaScript, y cada uno con su propio conjunto de atributos. Las entradas de
los registros serán conectadas automáticamente en páginas Plone en las
plantillas estándar cuando el navegador solicite una página. Los registros se
han configurado para que tengan defaults bastante sensibles; así que para
casi todos los casos de uso (probablemente el 90%+) no es más que la cuestión
de añadir la identificación del recurso que desea utilizar.

NOTA: Para experimentación, por ejemplo, al leer este documento, asegúrese de
marcar la casilla de verificación "modo de depuración/desarrollo" en la parte
superior del panel de configuración. (Lea más acerca del por qué en la parte
2.)




6.3.2.2. Condiciones, la fusión, almacenamiento en caché y depuración
========================================================================

otros detalles sobre cómo ResourceRegistries funciona


Condiciones
-----------

Cuando un agente de usuario (es decir, un navegador) hace una solicitud de
página, todos los recursos registrados en el registro son evaluados en contra
de su campo de condición. Si la condición es verdadera, el recurso es servido
en el navegador. Si la condición se eval?a como falsa, el recurso no se
sirve.

Esto le da la capacidad de servir condicionalmente diferentes hojas de estilo
o scripts basados ??en lógica como si el usuario est? conectado o no, si
usted est? en la sección "Recursos Humanos" de su intranet o si el tipo de
contenido es un elemento de noticias.

Las Condiciones tienen que ser expresiones `TALES`_. Y puede usar `global
template variables (variables globales de plantilla)`_ dentro de ellas.``_


Fusionando
----------

Cada vez que haga clic en el botón de guardar en un registro, un nuevo
conjunto de archivos CSS o JavaScript se crean. El registro tratar? de reunir
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
como sus nombres. Por lo que encontrará entradas como ``<link
rel=\"stylesheet\" href=\"plone2341.css\" />`` en su código HTML. Puede
examinar cómo los recursos se fusionan si hace clic en la segunda pestaña en
el registro, "composición". Se le presentar? una lista de archivos "m?gicos",
como 'plone2341.css, y en su interior los recursos de componentes que se usan
para su respectiva construcción. Puede hacer clic en cada entrada para
inspeccionar lo que se verá cuando sea servido.


La UI (interfaz de usuario) de composición-CSS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. image:: images/image_preview.html
  :alt: La UI de composición de css-registry (registro-css)


Cada recurso combinado tendrá un pequeño fragmento en el código identificando
su origen para que pueda hacerse con el código no modificado en el caso de
necesitarlo.

El asunto de comentario generalmente luce así.

::/* ----- base.css ----- */
    @media screen {
    /* http://yourhost/plone/portal_css/base.css?original=1 */
    /* */




El almacenamiento en caché y HTTP
----------------------------------

Los recursos fusionados de forma automática se sirven con encabezados-HTTP
optimizados para que est?n en la memoria caché por largo tiempo. Dado que el
número auto-generado se cambia cada vez que guarde las configuraciones del
registro, el explorador solicitar? los nuevos "archivos" y no utilizar? los
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
de desactivar el modo de depuración cuando su Plone est? en línea.


6.3.2.3. Par?metros de recursos
================================

Los par?metros para una entrada de registro en el registro CSS (y
JavaScript).

Cada entrada en los registros de CSS y JavaScript tiene algunos par?metros
que pueden ser ajustados.

idLa id de la hoja de estilo o JavaScript que será utilizada. De Plone 3.3 en
adelante, puede especificar un recurso alojado externamente mediante la
introducción de la URL completa aquí.
expressionUna expresión `TALES`_ a ser evaluada para comprobar si la hoja de
estilo o JavaScript debe ser incluida en la producción o no. Puede usar
`global template variables (variables globales de plantilla)`_ aquí.
conditionalcomment (disponible de Plone 3.3 en adelante)
Una pequeña cadena para ser incluida en un comentario condicional alrededor
del recurso. Por ejemplo, si escribe simplemente "IE" en el campo se
traducir? en un comentario condicional de:
::<!--[if IE]>...<![endif]--Este comportamiento est? actualmente habilitado
para los registros de CSS y JavaScript. El registro KSS es el único registro
que no tiene soporte completo para comentarios condicionales. Para más
información vea: ` http://msdn.microsoft.com/en-
us/library/ms537512.aspx`_mediaLos medios (media) para los cuales la hoja de
estilo se debería aplicar, normalmente vacía o "all" (todos). otros posibles
valores son "screen" (pantalla), "print" (impresión) etc. `Lea más acerca de
las configuraciones de medios de CSS en w3.org`_ relRelación de enlace.
defaults to 'stylesheet', y casi siempre debería permanecer de esa manera.
Para la designación de las hojas de estilo alternativas. Esto se utiliza para
alternar entre las fuentes grandes, medianas y pequeñas, en Plone por
defecto. No cambie esto a menos que sepa realmente lo que est?
haciendo.titleel título de una hoja de estilo alternativa.renderingCómo la
hoja de estilo es enlazada desde la página html. Esta es una configuración
avanzada. Deje su valor por defecto "import" a menos que conozca los efectos
que tienen las diferentes formas de renderizar y vincular hojas de
estiloimportEl predeterminado. normal importación csslinkfunciona mejor con
navegadores antiguos y es necesario para alternar hojas de
estiloinlinerenderizar la stylesheet en línea en lugar de vincularla de forma
externa. ?No se debería utilizar en absoluto! no es posible crear sitios que
la validen si lo hace.
Para más información: `http://developer.mozilla.org/en/docs/Properly_Using_CS
S_and_JavaScript_in_XHTML_Documents`_ compressionSi y en qu? medida el
recurso debería ser comprimidononeel contenido original no se
modificar?safeel contenido se comprime de una manera que debe ser seguro para
cualquier método de solución alternativa para errores en el explorador. El
código condicional para Internet Explorer se mantiene desde
ResourceRegistries 1.2.3 y 1.3.1.
fullel contenido se comprime con algunas reglas adicionales. Para css todos
los comentarios y la mayoría de saltos de línea se eliminan, esto puede
romper hacks de navegador especiales, así que utilice con cuidado. Para
JavaScript esto codifica variables con prefijos especiales de acuerdo a las
reglas descritas aquí (caracteres especiales):
` http://dean.edwards.name/packer/usage/`_ El código fuente tiene que estar
escrito de acuerdo a esas reglas, de lo contrario, es más que probable que se
rompa.
safe-encode- sólo disponible para JavaScript
- 'full-encode' - sólo disponible para JavaScript. Además codifica palabras
clave. Esto en gran medida comprime el JavaScript, pero necesita ser
decodificado en el proceso en el navegador en cada carga. Dependiendo del
tamaño de los scripts esto podría conducir a timeouts en Firefox. ?Use con
especial cuidado!applyPrefix - sólo disponible para CSS.
- Si su stylesheet usa URL relativas en una sentencia ``url()``, por ejemplo
para hacer referencia a otro stylesheet o imagen, puede experimentar
problemas cuando utiliza el registro en modo-no-depuración, ya que
*portal_css* altera la URL que se ve en el explorador. Si es así, configure
esta opción a *True (Verdadero)* o marque la opción de "Replace relative
paths in url() statements with absolute paths? (?reemplazar rutas relativas
en sentencias url () con rutas absolutasí" en la pantalla de administración
*portal_css* para remplazar cualquier ruta alternativa dentro de una
sentencia ``url()`` con una ruta absoluta (con el prefijo de la ruta de root
del sitio Plone) durante la etapa de fusión de recursos. Esto no modifica la
stylesheet original. Puede tener un ligero impacto en el rendimiento, pero no
debería ser un problema si los recursos se almacenan en caché de manera
apropiada. No tiene ningún efecto en modo de depuración.




6.3.2.4. Práctico: Agregar una hoja de estilo al registro a través de la Web
============================================================================

Operaciones básicas de los registros CSS y Javascript. Y un ejemplo
verdaderamente m?nimo de cómo usarlos en la vida real. Como un simple ejemplo
de la funcionalidad más básica, vamos a agregar y registrar una m?nima
stylesheet que agregue al fondo de su Plone un horripilante color rojo.

Para utilizar uno de los registros, usted tiene que

1.  Contar con un recurso (por ejemplo un Archivo) en su Skin con un poco
    de CSS o JavaScript en ?l (lo que podría, por ejemplo, estar en la
    carpeta personalizada de portal_skins).

2.  Realizar una entrada en el registro correspondiente (por ejemplo
    portal_css) con la id del recurso.


Hacer una hoja de estilo
------------------------

-   Vaya a la Configuración del sitio > Interfaz de Administración de
    Zope y navegue a *portal_skins/custom*
-   Desde el menú de agregar elementos, seleccione Archivos
-   Dele a su nuevo archivo una id de "*css-demo.css*"
-   Pegue el siguiente contenido dentro del archivo:
::body{ background-color : red }
-   ...y gu?rdelo


Agr?guela al Registro CSS

--------------------------

Los registros son dos herramientas que están sólo en la Interfaz de
Administración de Zope (ZMI); estas no tiene ninguna interfaz en la interfaz
de usuario Plone como tal. Sin embargo, usted las puede encontrar fácilmente
cuando navega por la ZMI de su sitio Plone. Busque por *portal_css* y
*portal_javascript*

-   Vaya a la Configuración del sitio > Interfaz de Administración de
    Zope y haga clic en portal_css. Una vez seleccionado, el Registro CSS
    (aquel que utilizamos para este ejemplo. El de JavaScript es exactamente
    igual) presentar? una interfaz mostrando todo los recursos registrados
    (en el caso del Registro CSS, los recursos son archivos CSS).

-   Asegúrese de marcar la casilla de verificación para modo de
    depuración. Esto asegurará que usted vea los cambios inmediatamente.

-   Despl?cese hasta la parte inferior del formulario, donde hay un
    formulario para agregar una hoja de estilo

-   En el campo de id introduzca "*css-demo.css*" (Deje los demás valores
    por defecto como están por ahora)

-   ?Eureka! . Vea su sitio Plone y fácilmente se dar? cuenta de su (la
    verdad es bastante horripilante) ?brillante color rojo de fondo!


La explicación técnica
------------------------

Cada entrada en los registros tiene un identificador que hace referencia a un
recurso que se puede encontrar en el contexto actual de adquisición de Plone.
Técnicamente podría ser una herramienta o una utilidad o cualquier cosa que
tenga un nombre y este disponible, pero más frecuente es que sea un objeto de
Archivo (por CSS y JS est?tico) o un Método DTML (para reemplazo de variable
din?mica). Los registros de recursos no hacen ninguna diferencia en cuanto a
qu? es el objeto, siempre y cuando se pueda encontrar y llamar, renderizar o
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
debería haber creado esto para usted, pero si no están all?, cr?elos usted
mismo.

Una entrada para una hoja de estilo en el directorio de skins de su producto
de tema, se verá así:

::<?xml version="1.0"?>
    <object name="portal_css" meta_type="Stylesheets Registry">
     <stylesheet title="" cacheable="True" compression="safe"
     cookable="True"
        enabled="1" expression="" id="mytheme.css" media="screen"
        rel="stylesheet" rendering="import"/>
    </object>

Tenga en cuenta que los par?metros son los mismos que por la forma a-través-
de-la-Web. Usted sólo tendrá que dar el ID de la hoja de estilo, Plone, la
encontrará, ya que es parte del skin.

Una entrada para una hoja de estilo en el directorio del explorador de su
producto de tema se verá así:

::<?xml version="1.0"?>
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
importar el step CSS. Reinstalar el producto de tema también funcionar?,
aunque hay que tener cuidado para evitar enfrentamientos de GenericSetup. Es
más seguro importar el step individual si su tema se ha instalado
previamente.


De la versión Plone 3.3 en adelante
------------------------------------

De Plone 3.3 en adelante también le puede decir al Registro CSS poner
comentarios condicionales alrededor del stylesheet:

::<stylesheet title="" cacheable="False" compression="none" cookable="False"
     rel="stylesheet" expression="" id="IEFixes.css" media="all"
     enabled="1"
     rendering="import" **conditionalcomment="IE"** />

También puede especificar un recurso externo:

::<javascript cacheable="False" compression="none" cookable="False"
     enabled="True" expression=""
     **id="http://ajax.googleapis.com/ajax/libs/jquery/1.2.6/jquery.min.js"**
     inline="False" insert-before="jquery-integration.js" />

 Si est? usando SSL y especificando un recurso externo, puede verse en la
 necesidad de especificar el protocolo http y una entrada ssl en el registro.
 Usted puede utilizar el par?metro de expresión para decidir cuál será
 utilizado:

::<javascript cacheable="False" compression="none" cookable="False"
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

Algunos ejemplos de limitación para Hojas de Estilo por el par?metro de
condición, que le ayudar?n a empezar.

En estos ejemplos hemos dado la condición como aparecer?a en
profiles/default/jsregistry.xml and cssregistry.xml. Si usted est? trabajando
a través de la web, el texto dentro de las comillas "...." simplemente se
puede situar en la casilla de condición para la CSS relevante o el archivo
JavaScript en portal_css portal_javascripts.


Tipo de contenido
-----------------

Si su CSS, o JavaScript, sólo es relevante para un determinado tipo de
contenido:

::expression = "python:object.meta_type == 'ATFolder'"

Vista
-----

Usted puede revisar una vista de navegador específica para una propiedad (en
este ejemplo es de Products.Maps):

::<javascript
        cacheable="True"
        ...
        expression="object/@@maps_googlemaps_enabled_view/enabled
  | nothing" />

Así es como se busca una de las vistas globales (vea la `Sección: Utilizando
otra información sobre su sitio`_ para más información sobre estas vistas).
En este ejemplo se ofrece la Hoja de estilo Plone RTL:

::<stylesheet
        ...
        expression="python:portal.restrictedTraverse
('@@plone_portal_state').is_rtl()"
        id="RTL.css"
        .../>
Rol
---

Lo siguiente comprobar? si el visitante ha iniciado sesión o no; en este caso
entrega el estándar member.css si el visitante no es an?nimo:

::<stylesheet
        ...
        expression="not: portal/portal_membership/isAnonymousUser"
        id="member.css"
        .../>

En este ejemplo se hace lo mismo, pero utiliza la vista plone_portal_state

::expression="python: not here.restrictedTraverse
('@@plone_portal_state').anonymous()"
Sección y/o lugar en el sitio
------------------------------

Tenga en cuenta que el cuerpo de la etiqueta de cada página tiene una sección
y clase de plantilla CSS. Así que puede que no tenga que usar los registros
de recursos en absoluto.

Sin embargo, si desea cambiar los estilos para una carpeta que no est? en el
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

::expression="python: here.getSectionInTree(object,1)=='news'"
     ::## Script (Python) "getSectionInTree"
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
=========================================================

Este documento explica cómo agregar y definir nuevos estilos de clase
personalizado para su uso en Kupu.

 Prerrequisitos: conocimiento CSS

1. Vaya a la Configuración de sitio en su sitio Plone.

2. Seleccione el icono de configuración del producto adicional para el
    editor visual Kupu, como se ve a continuación:

.. image:: images/image_preview_003.png
  :alt: Site-setup kupu




3. Vaya a la caja de estilos de párrafo.

.. image:: images/image_preview_011.png
  :alt: Kupu paragraph styles


4. Agregue su nuevo estilo de párrafo en la caja. Format is title|tag or
    title|tag|className, one per line. Por ejemplo:

::Smalltext|p|smalltext

5. Abra su ZMI.

6. Asegúrese de que su sitio est? en `el modo de depuración`_ la primera
    vez que se hacen cambios. Esto le permitir? ver los cambios de inmediato.

7. Vaya a
    *http://yoursite/portal_skins/plone_styles/ploneCustom.css/manage_main*.

8. Haga clic en el botón de personalización.

9. Ingrese su nuevo estilo de párrafo, donde dice "add your custom stuff
    here" (agregue sus elementos personalizados aquí)

::.smalltext {font-size: 70%;}

Nota: desplazarse por la página para revisar elementos disponibles. Vea
*base_properties* para definiciones de estos elementos

.. image:: images/copy_of_customcss.html





6.4. Utilizando otra información sobre su sitio en una página
===============================================================

Cómo obtener información sobre el estado de su sitio y otras variables
globales.

En algún momento u otro se dar? que necesita utilizar el título de su sitio
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

-   [locación de su huevo]/plone/app/layout/globals OR

-   [locación de su
    huevo]/plone.app.layout-[version]/plone/app/layout/globals


Puede encontrar una descripción de cada método en interfaces.py en ese
directorio, pero los métodos principales se describen a continuación Este
extracto de main_template en el núcleo de plantillas de Plone Default en
Plone 4, muestra cómo estas vistas, o sus métodos individuales, están a
disposición de cada página:

::<html xmlns="http://www.w3.org/1999/xhtml"
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

::        <p tal:define="**is_editable
context/@@plone_context_state/is_editable**"
               tal:condition="python: not len_text and
               is_editable"
               i18n:translate="no_body_text"
               class="discreet">
                This item does not have any body text, click
                the edit tab to change it.
            </p>



--


2.  Global Define (en desuso)

--------------------------

El segundo enfoque ha estado en uso por un tiempo largo, pero se est?
remplazando gradualmente (ya que es más lento) en Plone 3 y ha sido casi
eliminado en Plone 4. Este es el uso de un conjunto de variables que est?n
disponibles para cada página.

En Plone 3:

Estas son llamadas main_template:

::<metal:block use-macro="here/global_defines/macros/defines" />

Si quiere investigarlas más a fondo, las encontrará en

-   [your products directory]/CMFPlone/browser/ploneview.py.

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

-----------------------------


Acerca del sitio
~~~~~~~~~~~~~~~~

View @@plone_portal_state

MétodoLo que se obtieneglobal define
portalPortal Objectportal
portal_titleEl título de su sitioportal_title
portal_urlLa dirección URL de su sitioportal_url
navigation_root_pathRuta del root de navegación

navigation_root_urlLa dirección URL del root de navegaciónnavigation_root_url
default_languageEl idioma por defecto del sitio

languageEl idioma actual

localeLa localización actual

is_rtlSi el sitio se est? viendo en un lenguaje RTLisRTL
memberEl actual miembro autenticadomember
anonymousSi el visitante actual es an?nimo
isAnon
friendly_typesObtener una lista de tipos que se pueden implementar por un
usuario


Sobre el contexto actual
~~~~~~~~~~~~~~~~~~~~~~~~

View @@plone_context_state

Método

Lo que se obtiene

global define

current_page_url

La dirección URL de la página actual

current_page_url

current_base_url

La dirección URL real de la página actual






canonical_object

El objeto actual en s?






canonical_object_url

La dirección URL del objeto actual






view_url

La URL utilizada para visualizar el objeto






view_template_id

La id de la plantilla de vista






is_view_template

Verdadero si el URL actual se refiere a la vista estándar






object_url

La dirección URL del objeto actual






object_title

El título "embellecido" del objeto actual






workflow_state

El estado de flujo de trabajo del objeto actual

wf_state

parent

El "padre" directo del objeto actual






folder

La carpeta actual






is_folderish

Verdadero si es un objeto "folderish"

isFolderish

is_structural_folder

Verdadero si es una carpeta estructural

isStructuralFolder

is_default_page

Verdadero si es la página por defecto en una carpeta






is_portal_root

Verdadero si este es el root del portal o la página por defecto en el root
del portal






is_editable

Verdadero si el objeto actual es editable

is_editable

is_locked

Verdadero si el objeto actual est? bloqueado

isLocked

 actions
(Plone 4)
Las acciones de filtrado en el contexto. Puede restringir las acciones a una
sola categor?a.
 portlet_assignable
(Plone 4)
 Si el contexto es capaz de tener portlets localmente asignados.

Herramientas
~~~~~~~~~~~~

view @@plone_tools

Método

Lo que se obtiene

global define

actions

La herramienta de portal para acciones

atool

catalog

La herramienta portal_catalog






membership

La herramienta portal_membership

mtool

properties

La herramienta portal_properties






syndication

La herramienta portal_syndication

syntool

types

La herramienta portal_types






url

La herramienta portal_url

utool

workflow

La herramienta portal_workflow

wtool




6.5. Utilizando las herramientas jQuery y jQuery
================================================

Plone incluye las bibliotecas JavaScript para las herramientas jQuery y
jQuery sacadas de paquete, las cuales puede utilizar en sus propios scripts
inmediatamente.

`jQuery`_ es una popular librería JavaScript que simplifica traversal de
documento HTML, manejo de eventos, animación, y interacciones. ` Herramientas
jQuery `_ es una colección de componentes de interfaz de usuarios que incluye
revestimientos (overlays), pestañas, acordeones y tooltips (o descripciones
emergentes).

jQuery se ha incluido desde Plone 3.1. jQuery Tools (Herramientas jQuery) se
agreg? con Plone 4.0.


Usando jQuery

~~~~~~~~~~~~~

jQuery tiene una excelente documentación disponible en
`http://api.jquery.com`_. Tenga en cuenta, sin embargo, que nunca es
aconsejable depender de la disponibilidad del alias "$", para la función
jQuery ya que otras bibliotecas pueden redefinirlo.

Así que en vez:

::$(document).ready(function(){
       $("a").click(function(event){
         alert("Thanks for visiting!");
       });
     });

debe incorporar código jQuery que use el alias "$" en un empaquetador como:

::**(function($) {

    ** $(document).ready(function(){
       $("a").click(function(event){
         alert("Thanks for visiting!");**

       });**
     });
    **})(jQuery);

    **
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
`página plone.app.jquerytools pypi`_ para documentación y ejemplos.


7. Elementos de página
=======================

Una referencia para viewlets, portlets, administradores de viewlets, y
columnas de portlets que componen una página. Hay una breve referencia para
cada tipo de componente, con enlaces y recordatorios sobre la forma de
manejarlos, un ?ndice visual de los elementos de página, más fragmentos de
código para hacer su vida más fácil.


7.1. Viewlet
==========================================================

Qu? se hace para crear un viewlet, además hojas de trucos sobre cómo mover,
eliminar o modificar, y enlaces a tutoriales útiles.


7.1.1. Anatomía de un Viewlet
==============================

Las partes que construyen un componente viewlet.


Directiva en ZCML
-----------------

<browser:viewlet />


Atributos en ZCML
-----------------

name ejemplo [su namespace].[nombre de su viewlet] manager una interfaz de
administrador layer una interfaz de marcador para su tema en particular class
una clase de Python. Esta clase requiere un atributo "render" (renderizar),
sobre el cual, en la mayoría de los casos, apunta a una plantilla. No es
necesario especificar la plantilla en el ZCML, sin embargo, en versiones de
Plone 3.1.3 en adelante, se puede sustituir esta plantilla usando el atributo
de plantilla más abajo
template En la versión de Plone 3.1.2 o anteriores, sólo se puede usar esta
opción si no est? utilizando una clase, en la versión de Plone 3.1.3 o
posteriores, puede utilizar esto para sustituir la plantilla que ha definido
en la clase que usted ha especificado anteriormente
permission en la mayoría de los casos será Zope.Public for especificar una
interfaz marcando a un grupo de tipos de contenido, si lo desea. El viewlet
luego se limitar? a aquellos tipos de contenido (por ejemplo, vea el `Viewlet
de presentación`_ en la sección de Elementos) view (vista) especifique una
interfaz que marca una vista del navegador específica, si lo desea. El
viewlet se limitar? a elementos con esa vista específica (por ejemplo
investigar el código fuente del viewlet de acciones de contenido; usted
encontrará las instrucciones sobre la ubicación de este código en la página
`Acciones de contenido`_ de la sección de Elementos)


7.1.2. Mover, quitar u ocultar un viewlet
=========================================

Mover, quitar u ocultar un viewlet


7.1.2.1. Información general y hoja de trucos
==============================================

Una hoja de trucos de que tiene que hacer para mover viewlets en su diseño de
página, como también quitarlos u ocultarlos de su página.

Encontrará información detallada y un tutorial sobre cómo mover viewlets
aquí:

-   ` http://plone.org/documentation/tutorial/customizing-main-template-
    viewlets/reordering-and-hiding-viewlets`_


Hoja breve de trucos para lo básico
------------------------------------


A través de la Web
~~~~~~~~~~~~~~~~~~~

-   Agregue @@manage-viewlets al URL de su sitio.
-   Si solo quiere mover viewlets que solo aparezcan en una página,
    asegúrese de agregar @@manage-viewlets al URL de esa página.
-   Usted encontrará que puede mover, ocultar o eliminar viewlets
    mediante este método, pero no puede moverlos de un adminitrador de
    viewlet a otro.


En su propio producto
~~~~~~~~~~~~~~~~~~~~~

Mover o desplazar viewlets es parte de la configuración de su sitio:

-   Agregue o edite [su paquete de tema]/profiles/default/viewlets.xml

Encontrará información general sobre la configuración del sitio en la sección
`Configuración`_ de este manual. Vale la pena leer esto antes de iniciar
aquí, ya que la configuración de viewlets y administradores de viewlets puede
ser un poco complicado. aquí se mostrar?

-   cómo puede poner a la herramienta Generic Setup para que escriba la
    configuración por usted
-   por qué las cosas no están funcionando como usted esperaba

`GloWorm`_ es una herramienta útil aquí también. Esta le ayudar? a mover los
viewlets a través de la interfaz de usuario de Plone e inspeccionar la
configuración resultante.


Eliminar un viewlet de un administrador de viewlet
::::::::::::::::::::::::::::::::::::::::::::::::::

No se puede hacer más que ocultar su viewlet en el administrador de viewlet

::<object>
        <hidden manager="[Viewlet Manager Name]" skinname="[your skin
        name]">
            <viewlet name="[Viewlet Name]" />
        </hidden>
    </object>

Tenga en cuenta que usted puede hacer este proceso a través de la web y luego
poner a la herramienta Generic Setup para que escriba la configuración por
usted para transferir dentro de su propio paquete de tema.


Moviendo un viewlet dentro de un administrador de viewlet
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::<object>**
        <order manager="[Viewlet Manager Name]" skinname="[your skin
        name]">
    *Specify all the viewlets you want to see in this viewlet

    in the order you want them with this directive:*
            <viewlet name="[Viewlet Name]">
        </order>
    </object>

Tenga en cuenta que usted puede hacer este proceso a través de la web y luego
poner a la herramienta Generic Setup para que escriba la configuración por
usted para transferir dentro de su propio paquete de tema.


Moviendo un viewlet de un administrador viewlet a otro
::::::::::::::::::::::::::::::::::::::::::::::::::::::

Si est? basando su tema sobre el tema Plone Default, pues encontrará que la
reasignación de un viewlet de Plone Default es un proceso que involucra dos
pasos

-   esconderlo en su administrador de viewlet actual
-   agregarlo y darle una posición en un administrador diferente de
    viewlet

::<object>
    *Hide it from the current viewlet manager*
        <hidden manager="[current Viewlet Manager Name]"
        skinname="[your skin name]">
            <viewlet name="[Viewlet Name]" />
        </hidden>
    *Add it to a different viewlet manager*
        <order manager="[a different Viewlet Manager]"
        skinname="[your skin name]"
               based-on="Plone Default">
            <viewlet name="[Viewlet Name]"
                     insert-before="[Name of Viewlet
                     Below]" />
        </order>
    *OR Add it to your own viewlet manager*
        <order manager="[Your Viewlet Manager]" skinname="[your skin
        name]">
            <viewlet name="[Viewlet Name]"/>
        </order>
    </object>



-   También puede usar "insert-after='[Name of Viewlet Above]'"' o
    utilizar un asterisco para colocar el viewlet en la parte superior o
    inferior del administrador (e.g 'insert-after'=*).
-   based-on="Plone Default" significa que va a tomar la orden de Plone
    Default y luego aplicar los ajustes insert-after y insert-before que
    usted ha especificado.



7.1.3. Sustituyendo (anulando) o creando un nuevo viewlet
=========================================================

Sustituyendo (anulando) o creando un nuevo viewlet


7.1.3.1. Información general y hoja de trucos
==============================================

Una hoja breve de trucos sobre cómo personalizar o crear un nuevo viewlet.

Usted puede personalizar una plantilla de viewlet a través de la web, pero no
puede alterar la base de la clase Python.

En el sistema de archivos, en lugar de personalizar, el proceso es conectar
un nuevo viewlet, o re-conectar un viewlet existente.

Encontrará un tutorial detallado sobre la creación de un viewlet en `este
artículo`_ .


Breve hoja de trucos

--------------------


A través de la Web
~~~~~~~~~~~~~~~~~~~

-   Use Configuración de sitio > Interfaces de Configuración de Zope >
    portal_view_customizations para personalizar la plantilla de un viewlet
    existente de Plone Default.
-   No se puede crear un nuevo viewlet a través de la web.


En su propio producto
~~~~~~~~~~~~~~~~~~~~~

Usted tendrá que saber el nombre de:

1. La interfaz de administrador de viewlet Revise esto en la sección
    Elementos de este manual 2. La interfaz específica de su tema Esto es
    opcional, pero le asegura que su viewlet sólo est? disponible para su
    tema. Si utiliza la plantilla de paster plone3_theme, el nombre
    probablemente será IThemeSpecific.

Usted tendrá que crear los siguientes (debe ser capaz de localizar los
originales para copiar revisando la sección Elementos o mediante el uso de
`GloWorm`_):

3. directiva viewlet de navegación Esto ir? en [su paquete de
    tema]/browser/configure.zcml 4. archivo de configuración [su paquete de
    tema]/profiles/default/viewlets.xml5. página de la plantilla[su paquete
    de tema]/browser/[your template name].pt
6. Clase PythonEsto es opcional (pero vea la nota de abajo para la
    versión de Plone 3.1.2 o anteriores)
coloque esto en [su paquete de tema]/browser/[your module].py
Muestra de directiva de configuration.zcml
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Re-conectando un viewlet de Plone Default para utilizar su propia plantilla
(tenga en cuenta el atributo de capa es muy importante aquí)

::<browser:viewlet
     name="plone.[viewlet name]"
     manager="[viewlet manager interface]"
     class="plone.app.layout.viewlets.common.[viewlet class name]"
     template="templates/[your template name]"
     layer="[your theme specific interface]"
     permission="zope2.View"
     />


Conectando un nuevo viewlet pero prestando una clase de viewlet de Plone
Default

::<browser:viewlet
     name=[your namespace].[your viewlet name]"
     manager="[viewlet manager interface]"
     class="plone.app.layout.viewlets.common.[viewlet class name]"
     template="templates/[your template name]"
     layer="[your theme specific interface]"
     permission="zope2.View"
     />


Conectando con un viewlet nuevo con su propia clase o su propia plantilla

::<browser:viewlet
     name=[your namespace].[your viewlet name]"
     manager="[viewlet manager interface]"
     class=".[your module].[your class name]"
     (or: template="templates/[your template name]")
     layer="[your theme specific interface]"
     permission="zope2.View"
     />

Notas de la versión de Plone 3.1.2 o anteriores:
-------------------------------------------------


Ejemplo de clase Python
~~~~~~~~~~~~~~~~~~~~~~~

En la versión de Plone 3.1.2 o anteriores, usted tendrá que usar esto para
sustituir un viewlet de Plone Default, incluso si usted sólo desea cambiar la
plantilla de página.

::from [element namespace] import [element class name]
    from Products.Five.browser.pagetemplatefile import
    ViewPageTemplateFileclass

    [your class name]([element class name]):
        render = ViewPageTemplateFile("[your template name]")


~~


7.2. Portlet
==========================================================

Una hoja de trucos de los detalles que componen un portlet, además
información sobre cómo mover, ocultar o sustituir (anular) un portlet.


7.2.1. Anatomía de un portlet
==============================

Las partes que construyen un renderizador de portlet (que es la parte de un
portlet que usted desea personalizar).

La personalización de un portlet es similar a la que sustitución de un
viewlet, pero más directa. Hay una directiva específica ZCML para la
personalización.


Directiva en ZCML
-----------------

<plone:portletRenderer />


Atributos en ZCML
-----------------

layer una interfaz de marcador para su tema en particular portlet la interfaz
del portlet que desea personalizar template ubicación de la plantilla que
desea sustituir class su clase personalizada (use esta opción si no
especifica una plantilla) para la renderización del portlet


7.2.2. Mover, quitar u ocultar un portlet
=========================================

Algunos consejos para mover u ocultar los portlets.

Sea que los portlets aparezcan o no en su sitio es altamente personalizable a
través de la web, usted puede utilizar el enlace para el administrador de
portlets en la mayoría de contextos. Para más información:

-   `http://plone.org/documentation/tutorial/where-is-what/portlets-1/`_

Se asume que usted no quiere *arreglar* portlets en una página (de lo
contrario, probablemente seráan viewlets). Sin embargo, si desea establecer
una asignación inicial de portlets en la instalación de su producto de tema,
use

-   [su paquete de tema]/profiles/default/portlets.xml.

He aquí un extracto de portlets.xml de Plone Default, configurando el inicio
de sesión y portlet de navegación para la columna de la izquierda, y los
portlets de rese?as y noticias para la columna de la derecha.

::<?xml version="1.0"?>
    <portlets
        xmlns:i18n="http://xml.zope.org/namespaces/i18n"
        i18n:domain="plone">


     <!-- Assign the standard portlets -->

     <assignment
         manager="plone.leftcolumn"
         category="context"
         key="/"
         type="portlets.Navigation"
         name="navigation"
         />

     <assignment
         manager="plone.leftcolumn"
         category="context"
         key="/"
         type="portlets.Login"
         name="login"
         />

      <assignment
         manager="plone.rightcolumn"
         category="context"
         key="/"
         type="portlets.Review"
         name="review"
         />

     <assignment
         manager="plone.rightcolumn"
         category="context"
         key="/"
         type="portlets.News"
         name="news"
         />


    </portlets>

 Los atributos para la directiva de asignación son descritos en detalle
 aquí: `http://plone.org/products/plone/roadmap/203/ `_ . En pocas palabras:

manager y typeLos nombres de estos se pueden consultar en
plone.app.portlets.portlets.configure.zcml (para el tipo de portlet) o en el
archivo profiles/default/portlets.xml de Plone Default. category Este puede
ser uno de los cuatro valores de "context" (contexto), "content_type" (tipo
de contenido), "group" (grupo) o "user" (usuario) - dependiendo de donde
desea asignar los portlets.key Esto depender? del valor dado en la categor?a
anterior. En el caso de "context", la ubicación en el sitio es indicada (los
ejemplos anteriores especifican el root del sitio).

Si desea configurar el portlet con más detalle, se puede nidificar directivas
de propiedad dentro de la directiva de asignación. Aquí est? un detalle para
asegurar que el portlet de navegación aparezca en el root del sitio:

::<assignment name="navigation" category="context" key="/"
        manager="plone.leftcolumn" type="portlets.Navigation">
         <property name="topLevel">0</property>
     </assignment>


7.2.3. Sustituyendo de un portlet
=================================

Una hoja breve de trucos sobre cómo sustituir o personalizar un portlet


A través de la Web
~~~~~~~~~~~~~~~~~~~

-   Use Configuración de sitio > Interfaces de Configuración de Zope >
    portal_view_customizations para personalizar la plantilla de un portlet
    existente de Plone Default.


En su propio producto
~~~~~~~~~~~~~~~~~~~~~

Hay un tutorial detallado disponible aquí:

-   `http://plone.org/documentation/how-to/override-the-portlets-in-
    plone-3.0/`_

También puede consultar los detalles del portlet que desee reemplazar en la
sección Elementos de este manual.


Breve hoja de trucos

~~~~~~~~~~~~~~~~~~~~

Usted tendrá que saber el nombre de

La interfaz específica de su tema Esto es opcional pero le asegura que su
portlet sólo est? disponible para su tema. Si utiliza la plantilla de paster
plone3_theme, el nombre probablemente será IThemeSpecific.

Usted tendrá que crear los siguientes (debe ser capaz de localizar los
originales para copiar revisando la sección de Elementos):

directiva del renderizador de portlet de plone [su paquete de
tema]/browser/configure.zcml página de la plantilla [su paquete de
tema]/browser/[your template name].pt Clase Python * [su paquete de
tema]/browser/[your module name].py

* En la mayoría de los casos no será necesario una clase Python


Muestra de directiva de configuration.zcml
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::<configure
        xmlns:plone="http://namespaces.plone.org/plone">
        <include package="plone.app.portlets"  />
        <plone:portletRenderer
           portlet="[element interface]"
           template="[your template name].pt"
          (or class=".[your module].[your class name]")
          layer="[your theme specific interface]"
         />
    </configure>

Ejemplo de clase Python para la sustitución de portlet de navegación
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Si desea personalizar el portlet de navegación, es posible que deba
suministrar la clase, así como también la plantilla. Dos plantillas est?n
involucradas: la primera es usual plantilla de visualización, y la segunda se
encarga de la recursión a través del árbol de navegación. Si usted necesita
hacer su propia versión de la segunda, entonces tendrá que asignarla al
método recursivo en la clase.

::from plone.app.portlets.portlets.navigation import Renderer
    from Products.Five.browser.pagetemplatefile import
    ViewPageTemplateFile

    class [your class name](Renderer):
        _template = ViewPageTemplateFile([your template name].pt)
        recurse = ViewPageTemplateFile([your recurse template name])


7.2.4. Sustituir los portlets de Plone 3.0
==========================================

La personalización de portlets es una tarea regular, trabajando con el tema
de Plone. En este tutorial averiguaremos cómo hacer esto en Plone 3.0 con su
nuevo mecanismo para la administración de portlets (aportado por Denys
Mishunov)


Prop?sito
~~~~~~~~~~

Era bastante fácil personalizar uno de los portlets estándar en tiempos de
las versiones anteriores de Plone 3.0. Tan sólo ten?a que copiar una
plantilla de página para el portlet adecuado para su producto de tema y hacer
lo que quiera, cambiando el XHTML. También podía crear un portlet nuevo con
la misma facilidad; simplemente creando una plantilla para el nuevo portlet y
registrando este portlet con las Propiedades de su sitio.

En Plone 3.0 los portlets se convirtieron en algo más complejo. Pero no tema.
Al mismo tiempo se volvieron ?más poderosos! La ventaja se hace evidente
ahora, ?no? ;) Estos se sirven desde paquetes Python separados y realmente
tienen posibilidades de administración flexibles. Por lo tanto, vale la pena
probar este nuevo mecanismo para darse cuenta de lo poderoso que es.


Prerrequisitos
~~~~~~~~~~~~~~

Lo primero que hay que destacar; esto no se trata de personalización a través
de la web. Si usted necesita un truco rápido y no muy estilizado, eche un
vistazo a la herramienta portal_view_customizations. Este tutorial asume que
usted desea que sus cambios se repitan, de modo que usted pueda obtener los
mismos cambios en cualquier otro sitio donde se instale su producto.

Otra cosa que podría tener en cuenta vale la pena mencionar: usted no
necesita esta técnica en **ningún** caso que quiera personalizar un portlet
en Plone 3.0. Si usted ha apenas personalizado portlets utilizados en
versiones anteriores de Plone o si desea seguir utilizando los portlets de la
manera "a-la-era-anterior-a-3.0" (que no recomiendo en absoluto) puede que
tenga que revisar ClassicPortlet incluido con Plone 3.0. Este lidia con las
plantillas de página regulares de la misma manera en que ha trabajado con
portlets antes de la 3.0.

Y el último antes de seguir adelante. Si quiere personalizar cualquier de los
portlets estándar eliminandole toda la lógica de fondo (creando un portlet
est?tico), no lo haga Lo que queremos decir es que **no** haga esto. Gente
con experiencia pens? en usted. Mejor instale plone.portlet.static y juegue
con ?l, creando los portlets est?ticos cuando los necesite.

Así que para todos aquellos que todavía siguen con nosotros...finalmente
seguimos adelante.

Suponemos que ha creado el tema de Plone 3 **MyTheme** ya sea con los
generadores DIYPloneStyle o ZopeSkel. Aquí no cubrimos las explicaciones de
todos los aspectos de la creación de un tema para Plone 3.0. Para obtener más
información acerca de las ideas centrales en la elaboración de un tema,
administración de viewlets en Plone 3.0 y muchos más, revise un excelente
tutorial por David Convent, ` Personalización de viewlets en main_template `_
.

El concepto clave en el trabajo con portlets en Plone 3.0 es el uso de la
capa de skin de Zope 3, la misma que tenemos cuando se reemplaza un viewlet.
Asumimos que usted tiene al menos el siguiente conjunto m?nimo de archivos en
la carpeta **MyTheme/browser**:

::- browser/
        - __init__.py
        - configure.zcml
        - interfaces.py


Generalmente el proceso de sustitución de portlets es así:

-   elija el portlet que desea reemplazar;
-   registre una capa de skin si todavía no tiene una en
    **interfaces.py**;
-   agregue la directiva especial <plone:portletRenderer/> a
    **MyTheme/browser/configure.zcml**;
-   defina el atributo de **portlet** para la directiva
    <plone:portletRenderer />. Este es un tipo de portlet para proveedor de
    datos utilizado para esta sustitución. Esto puede ser una clase o una
    interfaz. Por ejemplo
    plone.app.portlets.portlets.navigation.INewsPortlet;
-   defina una nuevo atributo **template** para la directiva
    <plone:portletRenderer />. Cuando agregue esto el renderizador
    predeterminado será usado para el portlet que est? sustituyendo, pero con
    su plantilla;
-   en caso de que necesite personalizar el comportamiento por defecto
    para el portlet, debe utilizar el atributo **class** en vez de una simple
    plantilla. Esta nueva clase estar? actuando como el renderizador para el
    portlet en lugar de la opción predeterminada;
-   defina el atributo **layer** para la directiva <plone:portletRenderer
    /> con la capa de navegador **MyTheme**. El atributo **layer** del
    atributo portletRenderer asocia un particular IPortletRenderer con una
    particular capa de navegador (capa **MyTheme** en nuestro caso). Cuando
    nuestra capa est? en en acción (es decir, MyTheme est? instalado) el
    nuevo renderizador será utilizado en lugar de la opción predeterminada:
-   agregue una nueva plantilla a **MyTheme/browser** que implementar? el
    renderizador;
-   reinicie Zope y disfrute.


Paso a paso
~~~~~~~~~~~


1. Elija el portlet
:::::::::::::::::::

Primero que nada debemos decidir qu? portlet deseamos personalizar. Vamos a
elegir el portlet de Noticias. Si echara un vistazo portlet estándar de
noticias, podr? ver esas imágenes news_icon en frente de los títulos. Vamos a
deshacernos de ellas en el XHTML sólo para ejemplificar.

Los portlets por defecto de Plone se declaran en el paquete
**plone.app.portlets.portlets**. Los portlets de núcleo en Plone 3.0 se
pueden encontrar en
**$INSTANCE_HOME/lib/python/plone/app/portlets/portlets/**. Aunque se pueden
ubicar en otro lugar en $PYTHONPATH. Dependiendo de la instalación de Zope
(win32 o UNIX como sistema operativo, instalación desde el código fuente, por
el instalador, huevos u otros...), puede que tenga que utilizar las
herramientas de b?squeda disponibles en su sistema operativo para localizar
el paquete.

El paquete**plone.app.portlets.portlets** contiene módulos de Python,
plantillas de página y el archivo de configuración de ZCML: **configure.zcm
**. Este archivo contiene un conjunto de directivas <plone:portlet /> que
definen portlets estándar de esta manera

::<plone:portlet
        name="portlets.News"
        interface=".news.INewsPortlet"
        assignment=".news.Assignment"
        renderer=".news.Renderer"
        addview=".news.AddForm"
        editview=".news.EditForm"
        />


Los atributos en el código anterior se explican por si mismo. Pero si no
est?n claros para usted o desea saber más acerca de los atributos adicionales
para <plone:portlet />, eche un vistazo a la interfaz **IPortletDirective**
en el módulo **metadirectives** dentro del paquete plone.app.portlets.


2. Registre una capa de skin si todavía no tiene una
:::::::::::::::::::::::::::::::::::::::::::::::::::::

Podemos registrar un reemplazo para un portlet sólo para un tema (una
selección de skin), gracias al paquete **plone.theme**. Gracias a
**plone.theme**, podemos establecer una capa de skin de Zope 3 que
corresponda con un skin particular en portal_skins (un tema).

Agregue el siguiente código a **MyTheme/browser/interfaces.py** si todavía no
la tiene:

::from plone.theme.interfaces import IDefaultPloneLayer

    class IThemeSpecific(IDefaultPloneLayer):
        """Marker interface that defines a Zope 3 skin layer bound to
        a Skin
           Selection in portal_skins.
        """



3. A?ada la directiva a configure.zcml con los atributos adecuados
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Junto con la directiva <plone:portlet />, el paquete plone.app.portlets
define otro; <plone:portletRenderer />. El último se utiliza para sustituir
los portlets, definidos en su sitio. Tiene unos pocos atributos posibles que
se pueden encontrar en el módulo **metadirectives** dentro del paquete
plone.app.portlets. No vamos a listar todos aquí, así que simplemente pase 5
minutos y eche un vistazo a esos atributos, para que pueda comprender el
siguiente código ...

... 5 minutos después...

Bien, volvamos al trabajo. Para sustituir el portlet estándar de noticias
para el producto MyTheme debemos agregar la directiva <plone:portletRenderer
/> a **MyTheme/browser/configure.zcml**. Revisemos cómo debería verse esto
(asegúrese de tener el namespace
xmlns:plone="http://namespaces.plone.org/plone" definido en su nodo superior
**<configure>**):

::<include package="plone.app.portlets" />

    <interface
       interface=".interfaces.IThemeSpecific"
       type="zope.publisher.interfaces.browser.IBrowserSkinType"
       name="My Theme"
       />

    <plone:portletRenderer
       portlet="plone.app.portlets.portlets.news.INewsPortlet"
       template="mytheme_news.pt"
       layer=".interfaces.IThemeSpecific"
       />


Primero incluya el paquete plone.app.portlets para asegurar que los portlets
por defecto están activados antes de sustituir cualquier cosa.

Luego creamos una interfaz de capa de navegador para **MyTheme**, definida en
**MyTheme/browser/interfaces.py** disponible. Si ha personalizado cualquier
viewlet ya debería tener esto en **configure.zcml** así que no hay necesidad
de añadirlo dos veces en el mismo tema.

A continuación, vamos a resolver cuáles son los atributos que usamos aquí:

-   **portlet**: defina el portlet que vamos a sustituir. En nuestro
    caso, definimos la ruta con puntos completa a la interfaz INewsPortlet,
    implementada por el portlet de noticias;
-   **template**: el nombre de una plantilla que implementa el
    renderizador. El renderizador por defecto para este portlet de noticias
    será usado, pero con la plantilla "mytheme_news.pt en vez de la
    predeterminada.
-   **layer**: nuestra capa de navegador para la cual el renderizador es
    utilizado.
-   un atributo más que puede ser necesario recordar aquí es **class**.
    Usted tendrá que utilizarlo en caso de que quiera cambiar el
    comportamiento por defecto del portlet. Este atributo definir? la clase
    que se utilizar? como un renderizador para este portlet en lugar de la
    opción predeterminada.

Es todo con **configure.zcml**. Sigamos.


4. Agregue una nueva plantilla para renderizador del portlet
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

En el apartado anterior hemos definido mytheme_news.pt como un valor para el
atributo **template**. Pero no tenemos esa plantilla en el sistema de
archivos. Vamos a añadirla a ** MyTheme / browser / ** . Simplemente copie la
plantilla **news.pt** para el portlet de noticias desde
**plone.app.portlets.portlets** a **MyTheme/browser/** y renombrelo para
mytheme_news.pt. Abra esta plantilla en su editor favorito y vamos a jugar
con ella un poco.

Como debe recordar tiene que deshacerse de los iconos estándar news_icon.gif
que obtenemos para los elementos de noticias por defecto. Encuentre la
siguiente línea en la plantilla:

::<img tal:replace="structure item_icon/html_tag" />


y comentela de modo que no hagamos pasos irrecuperables y podamos deshacer
nuestros cambios más tarde. Así, tenemos:

::<!-- <img tal:replace="structure item_icon/html_tag" /> -->



?Eso es todo amigos!
:::::::::::::::::::::

Por lo tanto, eso es todo. Reinicie su Zope y vea su portlet de elementos de
noticia; ?no hay imágenes! ?Bien! ?Excelente! Bueno en realidad no tanto ya
que la imágenes pueden ser útiles para portales de comunidades :)


¿Qué sigue?
:::::::::::::

Este ejemplo es muy simple y de seguro no es realmente muy útil. Pero
definitivamente ahora puede hacer personalizaciones mucho mejores. Cuando se
utiliza el atributo **class** en la directiva <plone:portletRenderer/> usted
puede crear portlets que realmente se diferencien de los predeterminados. Y
es all? donde se encuentra la belleza de los portlets en Plone 3.0; no tendrá
que poner una carga de Python a sus plantillas de página como ten?a que hacer
antes. Todas las cosas de Python estar?n exactamente donde tienen que estar;
en clases Python. Y la plantilla sólo obtendrá los resultados de diferentes
métodos de Python dentro de esa clase.

?Disfrute!


7.3. Administrador de viewlet
=============================

Cómo mover u ocultar los administradores de viewlet y cómo crear uno nuevo.


7.3.1. Anatomía de un administrador de viewlet
================================================

Las partes que construyen un administrador de viewlet.


Directiva en ZCML
-----------------

<browser:viewletManager />


Atributos en ZCML
-----------------

name ejemplo [su namespace].[nombre del administrador de su viewlet] provides
una interfaz de marcador que define lo que este gerente hace layer una
interfaz de marcador para su tema en particular class esto será
plone.app.viewletmanager.manager.OrderedViewletManager permission en la
mayoría de los casos será Zope.Public for especificar una interfaz marcando a
un grupo de tipos de contenido, si lo desea. El administrador de viewlet se
limitar? a esos tipos de contenido view (vista) especificar una interfaz que
marca una vista, si lo desea. El administrador de viewlet se limitar? a los
artículos con esas de vista.


7.3.2. Mover, quitar u ocultar un administrador de viewlet
==========================================================

Algunos consejos de cómo mover u ocultar administradores de viewlet.

Los administradores de viewlets son llamados por plantillas de página.
Moverlos o eliminarlos es simplemente un asunto de personalización de
plantilla. La mayoría son llamados por main_template, pero es posible que
tenga que buscar dentro de las vistas específicas de contenido para algunos
de ellos.


Breve hoja de trucos

--------------------


A través de la Web
~~~~~~~~~~~~~~~~~~~

-   Configuración de sitio > Interfaz de Administración de Zope >
    portal_skins > plone_templates o plone_content
-   haga clic en el botón de personalizar, y busque por
::<div tal:replace="structure provider:[viewlet manager name]" />
-   (Use la clave de Elementos para identificar exactamente qu?
    administrador le interesa)


En su propio producto
~~~~~~~~~~~~~~~~~~~~~

-   Ponga su propia versión de main_template o de vistas de contenido en

[su paquete de tema]/skins.


7.3.3. Creando un nuevo administrador de viewlet
================================================

Una breve hoja de trucos para crear un nuevo administrador de viewlet.


A través de la Web
~~~~~~~~~~~~~~~~~~~

No se puede crear un nuevo administrador de viewlet a través de la web. Para
sustituir el orden en que aparecen los viewlets en un administrador de
viewlet, siga las instrucciones para viewlets.


En su propio producto
~~~~~~~~~~~~~~~~~~~~~

Si usted est? basando su nuevo administrador de viewlet en un administrador
de Viewlet de Plone Default, busque los detalles en la sección de Elementos
de este manual.

Usted tendrá que saber el nombre de

La interfaz específica de su tema Esto es opcional, pero le asegura que su
viewlet sólo est? disponible para su tema. Si utiliza la plantilla de paster
plone3_theme, el nombre probablemente será IThemeSpecific.

Usted tendrá que crear los siguientes (debe ser capaz de localizar los
originales para copiar revisando la sección de Elementos):

browser viewletManager directive [su paquete de tema]/browser/configure.zcml
Su interfaz de administrador de viewlet [su paquete de
tema]/browser/interfaces.py directivas del archivo de configuración [su
paquete de tema]/profiles/default/viewlets.xml
Muestra de la interfaz
~~~~~~~~~~~~~~~~~~~~~~

::from zope.viewlet.interfaces import IViewletManager

    class [your viewlet manager interface](IViewletManager):
        """ [A description of your viewlet manager goes here]  """
Muestra de la directiva configure.zcml
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::<browser:viewletManager
     name=[your namespace].[your element name]"
     provides=".interfaces.[your viewlet manager interface]"
     class="plone.app.viewletmanager.manager.OrderedViewletManager"
     layer="[your theme interface]"
     permission="zope2.View"
     />


7.4. Administrador de portlet
=============================

Consejos para mover u ocultar administradores de portlets. Hoja de trucos
para la creación de un nuevo administrador de portlet.


7.4.1. Mover o quitar un administrador de portlet
=================================================

Consejos sobre cómo mover o quitar los administradores de portlets.

Los administradores de portlets son llamados por main_template. Moverlos o
eliminarlos es simplemente un asunto de personalización de plantilla.


A través de la Web
~~~~~~~~~~~~~~~~~~~

-   Configuración de sitio > Interfaz de Administración de Zope >
    portal_skins > plone_templates > main_template
-   Personalice esto, y busque por
::<div tal:replace="structure provider:[portlet manager name]" />
-   (Use la clave de Elementos para identificar exactamente qu?
    administrador le interesa)


En su propio producto
~~~~~~~~~~~~~~~~~~~~~

-   Coloque su propia versión de main_template en

[su producto de tema]/skins.


7.4.2. Ocultando un administrador de portlet
============================================

Existen varios métodos para ocultar un administrador de portlet.

Un administrador de portlet no se mostrar? si no hay portlets para mostrar
asignados a ?l o si los portlets asignados no tienen datos.

En el caso de las columnas de portlets, si el administrador de portlet est?
vacío, entonces también es útil desaparecer los elementos de bloque
circundantes también, para que no obtenga un amplio margen en blanco en su
página. Por esta razón, las columnas que contienen los administradores de
portlets en el main_template están empaquetados con slots (ranuras). Ocultar
los administradores de portlets es, por lo tanto, un asunto de la
manipulación de estas ranuras. Existen varias técnicas:

Definiendo una ranura vacía Utilice lo siguiente en una plantilla de vista de
contenido para asegurarse de que la columna de la derecha se retire:

-   ``<metal:column_one fill-slot="column_one_slot" />``

Usando las variables globales sl y sr Estas se establecen como condiciones en
las ranuras; ellas comprueban los respectivos administradores de portlet de
contenido y, si están vacíos, dan como resultado un false (falso). Usted
puede sustituir estas en la plantilla misma. Usando la opción show_portlets
show_portlets=false se puede pasar como una opción a una plantilla para
establecer sl y sr a falso Para ver esto en acción, eche un vistazo a

-   CMFPlone/skins/plone_templates/standard_error_message.py y
-   CMFPlone/browser/ploneview.py





7.4.3. Creando un nuevo administrador de portlet
=================================================

Cómo crear un nuevo administrador de portlet.

Un ejemplo pr?ctico de la creación de un nuevo administrador de portlet puede
encontrarla aquí

-   ` http://plone.org/documentation/how-to/adding-portlet-managers `_

He aquí una lista rápida de lo que tiene que hacer.


Breve hoja de trucos
--------------------


A través de la Web
~~~~~~~~~~~~~~~~~~~

No se puede crear un nuevo administrador de portlet a través de la web.


En su propio producto
~~~~~~~~~~~~~~~~~~~~~

Usted tendrá que proporcionar el nombre de

La interfaz específica de su tema Esto es opcional pero le asegura que su
administrador de portlet est? disponible sólo para su tema. Si utiliza la
plantilla de paster plone3_theme, el nombre probablemente será
IThemeSpecific.

Usted tendrá que crear los siguientes (debe ser capaz de localizar los
originales para copiar revisando la sección de Elementos):

Interface Esto ir? en [su paquete de tema]/browser/interfaces.py. Le puede
dar cualquier nombre que desee, pero por convención, debe ser precedido por
"I". directiva de configuración [su paquete de
tema]/profiles/default/portlets.xml browser:page directive (para la vista del
administrador) [su paquete de tema]/browser/configure.zcml plantilla de
página (para la vista del administrador) [su paquete de tema]/browser/[su
plantilla].pt
Muestra de la interfaz
~~~~~~~~~~~~~~~~~~~~~~

::from plone.portlets.interfaces import IPortletManager

    class [your portlet manager interface](IPortletManager):
     """A description goes here    """
Muestra de portlets.xml
~~~~~~~~~~~~~~~~~~~~~~~

::<?xml version="1.0"?>
    <portlets>
     <portletmanager
        name="[your namespace].[your portlet manager]"
        type="[your namespace].[your theme
        name].browser.interfaces.[your portlet manager interface]"
     />
    </portlets>
Muestra de directiva configure.zcml (para la vista del administrador)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::<browser:page
     for="plone.portlets.interfaces.ILocalPortletAssignable"
     class="plone.app.portlets.browser.manage.ManageContextualPortlets"
     name="[your view name]"
     template="[your template name].pt"
     permission="plone.app.portlets.ManagePortlets"
    />


7.4.4. Práctico
================

Práctico


7.4.4.1. Agregando administradores de portlets
==============================================

Usted necesita portlets en otro lugar en su Plone. En este ejemplo colocamos
portlets contextuales sobre el contenido (aportado por Jens Klein)

> Esto se trata de agregar ADMINISTRADORES de portlets, pista: **
PortletManager! = Portlet. ** Un PortletManager es una especie de contenedor
para los portlets, tal como es el ViewletManager para viewlets. Bueno,
después de reducir el mom?ntum de malentedimiento, comencemos:


Prerrequisitos
--------------

Supongo que est? familiarizado con las configuraciones base GenericSetup de
Plone 3. Revise los tutoriales *DIYPloneStyle* y otros relacionados si no es
así.

Usted necesita instalar Plone 3 y un producto NEWTHEME (nuevo tema) para su
propio skin (basado en DIYPloneStyle funciona bien).


Estrategia
----------

En mi ejemplo, yo no quiero personalizar la plantilla principal. Por lo tanto
la idea es agregar un viewlet a
*plone.app.layout.viewlets.interfaces.IContentViews* viewletmanager. Así que
los pasos que hay que hacer son

1.  A?ada un viewlet al viewlet-manager
2.  A?ada un portlet-manager

3.  A?ada una vista de administrador para el portlet-manager.


Paso uno: Añadir un Viewlet
----------------------------

en Products.NEWTHEME agregue un archivo *abovecontentportlets.pt* que
contenga:::<tal:block replace="structure provider:my.abovecontentportlets" />

Aquí llamamos al administrador de portlet, y lo creamos en el paso dos.
Pero primero registremos nuestro nuevo viewlet para el viewletmanager.
Edite su Products/NEWTHEME/configure.zcml y agregue:

::<browser:viewlet
        name="my.abovecontentportlets"
        manager="plone.app.layout.viewlets.interfaces.IContentViews"
        template="abovecontentportlets.pt"
        permission="zope2.View"
    />

Paso dos: Agregar un administrador de portlet

---------------------------------------------

Crear una interfaz de marcado para el administrador y agregue o edite
*Products/NEWTHEME/interfaces.py*

::from plone.portlets.interfaces import IPortletManager

    class IMyAboveContent(IPortletManager):
        """we need our own portlet manager above the content area.
        """


Agregue (o edite) su *Products/NEWTHEME/profiles/default/portlets.xml* y
registre un administrador de portlet:

::<?xml version="1.0"?>
    <portlets>
     <portletmanager
       name="my.abovecontentportlets"
       type="Products.NEWTHEME.interfaces.IMyAboveContent"
     />
    </portlets>


Eso es todo lo que necesita si no quiere administrar los portlets a través de
la web. Oh! ?si quiere? Pues entonces necesita un tercer paso:


Paso tres: Añadir una vista de administrador para el administrador de portlet
-----------------------------------------------------------------------------
-

La vista para administración es renderizada para los slots (ranuras) de la
izquierda y derecha en plantilla principal (main-template) Sin embargo
utilizamos un viewlet y tenemos aquí una vista diferente. así que tenemos que
llamar expl?citamente a nuestra vista y llamar a nuestro administrador dentro
de su contexto.



Tenemos que registrar una nueva vista de navegador para ver nuestra plantilla
de página llamando directamente a nuestro administrador. Nuevamente agregue
algunas líneas a su *configure.zcml*:::<browser:page
        for="plone.portlets.interfaces.ILocalPortletAssignable"
class="plone.app.portlets.browser.manage.ManageContextualPortlets"
        name="manage-myabove"
        template="templates/managemyabove.pt"
        permission="plone.app.portlets.ManagePortlets"
    />Y finalmente, necesitamos la plantilla, así que agregue un archivo
    *managemyabove.pt* y edite:



::<html xmlns="http://www.w3.org/1999/xhtml"
          xmlns:metal="http://xml.zope.org/namespaces/metal"
          xmlns:tal="http://xml.zope.org/namespaces/tal"
          xmlns:i18n="http://xml.zope.org/namespaces/i18n"
          metal:use-macro="context/main_template/macros/master"
          i18n:domain="plone">
    <head>
        <div metal:fill-slot="javascript_head_slot" tal:omit-tag="">
            <link type="text/css" rel="kinetic-stylesheet"
                tal:attributes="href
                string:${context/absolute_url}/++resource++manage-
                portlets.kss"/>
        </div>
    </head>
    <body>
    <div metal:fill-slot="main">
      <h1 class="documentFirstHeading">Manage My Portlets</h1>
      <span tal:replace="structure provider:my.abovecontentportlets" />
    </div>
    </body>
    </html>
    Eso es todo. Despu?s de reiniciar su Zope puede llamar
    *http://DOMAIN.TLD/plone/path/to/some/context/@@manage-myabove*

y asignar portlets sobre su contenido.




7.5. Indice de elementos de página, Plone Default (Plone por defecto) y
    Classic Theme (tema cl?sico)
=============================================================================
=========================

Un ?ndice visual de los elementos de la página principal.

Por el momento, este ?ndice le ofrece solamente viewlets, pero la intención
es ampliarlo para incluir portlets y los respectivos administradores.

Una alternativa al uso de este ?ndice es la instalación de `GloWorm`_ en su
instancia de Plone. Este es un inspector visual que le dar? información sobre
diversos aspectos del tema Plone Default directamente a través de su
explorador, y facilitarle realizar personalizaciones de viewlet a través de
la Web.

ClaveTítuloHTMLNombre del
Tipo
de Administrador

Enlaces para salto<p class="hiddenStructure"> ??? </p>`plone.skip_links`_
plone.portalheader
`viewlet`_

Título de Cabecera HTML<title> ...</title>`plone.htmlhead.title`_
plone.htmlhead
`viewlet`_

Enlaces anterior/siguiente<link title="Go to previous item" ???
/>`plone.nextprevious.links`_
plone.htmlhead.links
`viewlet`_

Enlace Favicon<link rel="shortcut icon" ??? />`plone.links.favicon`_
plone.htmlhead.links
`viewlet`_

Enlace de b?squeda<link rel="search" ??? />`plone.links.search`_
plone.htmlhead.links
`viewlet`_

Enlace de autor<link rel="author" ??? />`plone.links.author`_
plone.htmlhead.links
`viewlet`_

Enlace de navegación<link title="Front Page" ???> and <link title="Site Map"
..>`plone.links.navigation`_
plone.htmlhead.links
`viewlet`_

Analytics(Fragmento de código definido por el administrador del
sitio)`plone.analytics`_
plone.portalfooter
`viewlet`_

Encabezado<div id="portal-header"> ??? </div>`plone.header`_
plone.portaltop
`viewlet`_

Selector de idiomas<ul id="portal-languageselector"> ???
</ul>`plone.app.i18n.locales.languageselector`_
Portal Top
`viewlet`_

.. image:: images/image_thumb_009.png
  :alt: plone.site_actions

Acciones del sitio<ul id="portal-siteactions">...</ul>`plone.site_actions`_
plone.portalheader
`viewlet`_

.. image:: images/image_thumb_011.png
  :alt: plone.searchbox

Cuadro de b?squeda<div id="portal-searchbox">???</div>`plone.searchbox`_
plone.portalheader
`viewlet`_

.. image:: images/image_thumb.png
  :alt: plone.logo

Logotipo<a id="portal-logo" ...>... </a>`plone.logo`_
plone.portalheader
`viewlet`_

.. image:: images/image_thumb_005.png
  :alt: plone.global_sections

Secciones globales<h5 class="hiddenStructure">Sections</h5> <ul id="portal-
globalnav"> ??? </ul>`plone.global_sections`_
plone.portalheader
`viewlet`_

.. image:: images/image_thumb_006.png
  :alt: plone.personal_bar

Barra personal<div id="portal-personaltools-wrapper">
???</div>`plone.personal_bar`_
plone.portaltop
`viewlet`_

Barra de ruta (hilo de Ariadna del portal)<div id="portal-
breadcrumbs">...</div>`plone.path_bar`_
plone.portaltop
`viewlet`_

Vistas de contenido<ul class="contentViews"> ??? </ul>`plone.contentviews`_
plone.contentviews
`viewlet`_

Acciones de contenido
`plone.contentactions`_
plone.contentviews
`viewlet`_

.. image:: images/image_thumb_016.png
  :alt: plone.tableofcontents

Tabla de contenidos<dl id="document-toc" class="portlet toc" style="display:
none"> ??? </dl>`plone.tableofcontents`_
plone.abovecontentbody
`viewlet`_

.. image:: images/image_thumb_004.png
  :alt: plone.presentation

Presentación<p id="link-presentation">...</p>`plone.presentation`_
plone.abovecontentbody
`viewlet`_

Palabras clave<div id="category"
class="documentByLine">???</div>`plone.belowcontenttitle.keywords`_
plone.belowcontenttitle
`viewlet`_

.. image:: images/image_preview_009.png
  :alt: plone.byline

L?nea de fondo<div id="plone-document-byline" class="documentByLine">...
</div>`plone.belowcontenttitle.documentbyline`_
plone.belowcontenttitle
`viewlet`_

Bloqueo<div id="plone-lock-status" />`plone.lockinfo`_
plone.abovecontent
`viewlet`_

.. image:: images/image_thumb_018.png
  :alt: plone.document_actions

Acciones de documento<div class="documentActions"> ???
</div>`plone.abovecontenttitle.documentactions`_
plone.belowcontentbody
`viewlet`_

.. image:: images/image_thumb_017.png
  :alt: plone.comments

Comentarios<div class="discussion"> ??? </div>`plone.comments`_
plone.belowcontent
`viewlet`_

Historial de contenido<div class="contentHistory" id="content-
history">???</div>`plone.belowcontentbody.contenthistory`_
plone.belowcontentbody
`viewlet`_

.. image:: images/image_thumb_012.png
  :alt: plone.nextprevious

Anterior Siguiente<div class="listingBar">???</div>`plone.nextprevious`_
plone.belowcontent
`viewlet`_

Pie de página<div id="portal-footer">???</div>`plone.footer`_
plone.portalfooter
`viewlet`_

.. image:: images/image_preview_010.png
  :alt: plone.colophon

Colof?n <div id="portal-colophon">???</div>`plone.colophon`_
plone.portalfooter
`viewlet`_


7.6. Page Elements Index - Sunburst Theme - Plone 4
=============================================================================
====================

Un ?ndice visual de los elementos de la página principal.

Por el momento, este ?ndice le ofrece solamente viewlets, pero la intención
es ampliarlo para incluir portlets y los respectivos administradores.

Una alternativa al uso de este ?ndice es la instalación de GloWorm en su
instancia de Plone. Este es un inspector visual que le dar? información sobre
diversos aspectos del tema Plone Default directamente a través de su
explorador, y facilitarle realizar personalizaciones de viewlet a través de
la Web.

ClaveTítuloHTMLNombre del
Tipo
de Administrador

Enlaces para salto<p class="hiddenStructure"> ??? </p>`plone.skip_links`_
plone.portalheader
`viewlet`_

Título de Cabecera HTML<title> ...</title>`plone.htmlhead.title`_
plone.htmlhead
`viewlet`_

Dublin Core Metadata<meta ... />`plone.htmlhead.dublincore`_
plone.htmlhead
`viewlet`_

KSS Base Url<link rel="kss-base-url" ... />`plone.htmlhead.kss-base-url`_
plone.htmlhead
`viewlet`_

Enlaces anterior/siguiente<link title="Go to previous item" ???
/>`plone.nextprevious.links`_
plone.htmlhead.links
`viewlet`_

Enlace Favicon<link rel="shortcut icon" ??? />`plone.links.favicon`_
plone.htmlhead.links
`viewlet`_

Enlace de b?squeda<link rel="search" ??? />`plone.links.search`_
plone.htmlhead.links
`viewlet`_

Enlace de autor<link rel="author" ??? />`plone.links.author`_
plone.htmlhead.links
`viewlet`_

Enlace de navegación<link title="Front Page" ???> and <link title="Site Map"
..>`plone.links.navigation`_
plone.htmlhead.links
`viewlet`_

Enlace RSS<link rel="alternate" title="RSS 1.0" .. />`plone.links.RSS`_
plone.htmlhead.links
`viewlet`_

Analytics(Fragmento de código definido por el administrador del
sitio)`plone.analytics`_
plone.portalfooter
`viewlet`_

Encabezado<div id="portal-header"> ??? </div>`plone.header`_
plone.portaltop
`viewlet`_

Selector de idiomas<ul id="portal-languageselector"> ???
</ul>`plone.app.i18n.locales.languageselector`_
Portal Top
`viewlet`_

.. image:: images/image_preview_007.png
  :alt: plone.siteactions-sunburst

Acciones del sitio<ul id="portal-
siteactions">...</ul>`plonetheme.sunburst.site_actions`_
plone.portalfooter
`viewlet`_

.. image:: images/image_thumb_020.png
  :alt: plone.searchbox-sunburst

Cuadro de b?squeda<div id="portal-searchbox">???</div>`plone.searchbox`_
plone.portalheader
`viewlet`_

.. image:: images/image_thumb_008.png
  :alt: plone.logo-sunburst

Logotipo<a id="portal-logo" ...>... </a>`plone.logo`_
plone.portalheader
`viewlet`_

.. image:: images/image_thumb_007.png
  :alt: plone.global_sections-sunburst

Secciones globales<h5 class="hiddenStructure">Sections</h5> <ul id="portal-
globalnav"> ??? </ul>`plone.global_sections`_
plone.portalheader
`viewlet`_

.. image:: images/image_thumb_015.png
  :alt: plone.personal_bar-sunburst

Barra personal<div id="portal-personaltools-wrapper">
???</div>`plonetheme.sunburst.personal_bar`_
plone.portaltop
`viewlet`_

.. image:: images/image_preview_005.png
  :alt: plone.pathbar-sunburst

Barra de ruta (hilo de Ariadna del portal)<div id="portal-
breadcrumbs">...</div>`plone.path_bar`_
plone.portaltop
`viewlet`_

.. image:: images/image_thumb_003.png
  :alt: plone.contentviews-sunburst

Vistas de contenido<ul class="contentViews"> ??? </ul>`plone.contentviews`_
plone.contentviews
`viewlet`_

.. image:: images/image_thumb_002.png
  :alt: plone.contentactions-sunburst

Acciones de contenido
`plone.contentactions`_
plone.contentviews
`viewlet`_

.. image:: images/image_preview.png
  :alt: plone.toc-sunburst

Tabla de contenidos<dl id="document-toc" class="portlet toc" style="display:
none"> ??? </dl>`plone.tableofcontents`_
plone.abovecontentbody
`viewlet`_

.. image:: images/image_preview_004.png
  :alt: plone.presentation-sunburst

Presentación<p id="link-presentation">...</p>`plone.presentation`_
plone.abovecontentbody
`viewlet`_

.. image:: images/image_thumb_010.png
  :alt: plone.keywords-sunburst

Palabras clave<div id="category"
class="documentByLine">???</div>`plone.belowcontenttitle.keywords`_
plone.belowcontenttitle
`viewlet`_

.. image:: images/image_preview_006.png
  :alt: plone.byline-sunburst

L?nea de fondo<div id="plone-document-byline" class="documentByLine">...
</div>`plone.belowcontenttitle.documentbyline`_
plone.belowcontenttitle
`viewlet`_

Bloqueo<div id="plone-lock-status" />`plone.lockinfo`_
plone.abovecontent
`viewlet`_

Acciones de documento<div class="documentActions"> ???
</div>`plone.abovecontenttitle.documentactions`_
plone.belowcontentbody
`viewlet`_

.. image:: images/image_preview_008.png
  :alt: plone.relateditems-sunburst

Elementos relacionados
<div class="relatedItems"> ??? </div>`plone.belowcontentbody.relateditems`_
plone.belowcontentbody
`viewlet`_

.. image:: images/image_preview_012.png
  :alt: plone.comment-sunburst

Comentarios<div class="discussion"> ??? </div>`plone.comments`_
plone.belowcontent
`viewlet`_

.. image:: images/image_thumb_019.png
  :alt: plone.contenthistory-sunburst

Historial de contenido<div class="contentHistory" id="content-
history">???</div>`plone.belowcontentbody.contenthistory`_
plone.belowcontentbody
`viewlet`_

.. image:: images/image_preview_002.png
  :alt: plone.nextprevious-sunburst

Anterior Siguiente<div class="listingBar">???</div>`plone.nextprevious`_
plone.belowcontent
`viewlet`_

.. image:: images/image_thumb_013.png
  :alt: plone.footer-sunburst

Pie de página<div id="portal-footer">???</div>`plone.footer`_
plone.portalfooter
`viewlet`_

.. image:: images/image_thumb_014.png
  :alt: plone.colophon-sunburst

Colof?n <div id="portal-colophon">???</div>`plone.colophon`_
plone.portalfooter
`viewlet`_


7.7. Elementos estructurales
============================

Elementos que forman la estructura de página subyacente (administradores de
viewlet y portlet).


7.7.1. Encabezado
=================

Llama los administradores de viewlets para el encabezado del sitio

Fragmento:``<div id="portal-header"> ???
</div>``Nombre:plone.headerTipo:`viewlet`_
Personalización a través de la Interfaz de Administración de Zope
--------------------------------------------------------------------

Uso:Configuración de sitio > Interfaz de Administración de Zope >
portal_view_customizationsIr a:plone.header
Personalizando de su propio producto
------------------------------------

Los siguientes detalles le ayudar?n a localizar los archivos que usted tendrá
que copiar en su propio producto. También le ayudar?n a proporcionar la
información correcta para crear sus propias directivas ZCML, clases Python, y
interfaces. Vea `Viewlet`_ para más información.

Ubicado en:

-   [locación de su huevo]/plone/app/layout/viewlets/
-   [locación de su
    huevo]/plone.app.layout-[version].egg/plone/app/layout/viewlets/

Nombre de la plantilla:portal_header.ptNombre de la
clase:noneAdministrador:plone.portaltop (nombre)
plone.app.layout.viewlets.interfaces.IPortalTop (interfaz)
Ejemplos de archivos & directivas
~~~~~~~~~~~

Ponga una versión de portal_header.pt en [su paquete de
tema]/browser/templates)

Conecte su viewlet [su paquete de tema]/browser/configure.zcml

::<browser:viewlet
        name="[your namespace].[your viewlet name]"
        manager="plone.app.layout.viewlets.interfaces.IPortalTop"
        template="templates/[your template name].pt"
        layer=".interfaces.[your theme specific interface]"
        permission="zope2.View"
    />


En [su paquete de tema]/profiles/default/viewlets.xml

Oculte el viewlet original (si lo desea)

::<object>
        <hidden manager="plone.portaltop" skinname="[your skin
        name]">
            <viewlet name="plone.header" />
        </hidden>


Inserte su nuevo viewlet en un administrador de viewlet

::    <order manager="plone.portaltop" skinname="[your skin name]"
               based-on="Plone Default">
            <viewlet name="[your namespace].[your viewlet name]"
                     insert-before="*" />
        </order>
    </object>



7.8. Elementos ocultos
======================

Elementos ocultos de página (que aparecen en la HTMLhead o con css
configurado a display:none).


7.8.1. Enlaces para salto
=========================

Enlaces ocultos en la parte superior de la página para saltar al contenido y
la navegación.



Fragmento:``<p class="hiddenStructure"> ???
</p>``CSS:invisibles.cssNombre:plone.skip_linksTipo:`viewlet`_
Personalización a través de la Interfaz de Administración de Zope
--------------------------------------------------------------------

Uso:Configuración de sitio > Interfaz de Administración de Zope >
portal_view_customizationsIr a:plone.skip_links
Personalizando de su propio producto
------------------------------------

Los siguientes detalles le ayudar?n a localizar los archivos que usted tendrá
que copiar en su propio producto. También le ayudar?n a proporcionar la
información correcta para crear sus propias directivas ZCML, clases Python, y
interfaces. Vea `Viewlet`_ para más información.

Ubicado en:

-   [locación de su huevo]/plone/app/layout/viewlets/
-   [locación de su
    huevo]/plone.app.layout-[version].egg/plone/app/layout/viewlets/

Nombre de la plantilla:skip_links.ptNombre de la clase:plone.app.layout.viewl
ets.common.SkipLinksViewletAdministrador:plone.portalheader (nombre)
plone.app.layout.viewlets.interfaces.IPortalHeader (interfaz)
Ejemplos de archivos & directivas
~~~~~~~~~~~

Coloque una versión de skip_links.pt en [your theme
package]/browser/templates)

Cree su propia versión de la clase en [su paquete de tema]/browser/[su
modulo].py

::from plone.app.layout.viewlets.common import SkipLinksViewlet
    from Products.Five.browser.pagetemplatefile import
    ViewPageTemplateFile
    class [your class name](SkipLinksViewlet):
        render = ViewPageTemplateFile("[your template name]")


Conecte su viewlet [su paquete de tema]/browser/configure.zcml

::<browser:viewlet
        name="[your namespace].[your viewlet name]"
        manager="plone.app.layout.viewlets.interfaces.IPortalHeader"
        class=".[your module].[your class name]"
        layer=".interfaces.[your theme specific interface]"
        permission="zope2.View"
    />


En [su paquete de tema]/profiles/default/viewlets.xml

Oculte el viewlet original (si lo desea)

::<object>
        <hidden manager="plone.portalheader" skinname="[your skin
        name]">
            <viewlet name="plone.skip_links" />
        </hidden>


Inserte su nuevo viewlet en un administrador de viewlet

::    <order manager="plone.portalheader" skinname="[your skin name]"
               based-on="Plone Default">
            <viewlet name="[your namespace].[your viewlet name]"
                     insert-before="*" />
        </order>
    </object>



7.8.2. Título de Cabecera HTML
===============================

El título de la página HTML en la cabecera.

Fragmento:``<title>
...</title>``CSS:noneNombre:plone.htmlhead.titleTipo:`viewlet`_
Personalización a través de la Interfaz de Administración de Zope
--------------------------------------------------------------------

Uso:Configuración de sitio > Interfaz de Administración de Zope >
portal_view_customizationsIr a:plone.htmlhead.title
Personalizando de su propio producto
------------------------------------

Los siguientes detalles le ayudar?n a localizar los archivos que usted tendrá
que copiar en su propio producto. También le ayudar?n a proporcionar la
información correcta para crear sus propias directivas ZCML, clases Python, y
interfaces. Vea `Viewlet`_ para más información.

Ubicado en:

-   [locación de su huevo]/plone/app/layout/viewlets/
-   [locación de su
    huevo]/plone.app.layout-[version].egg/plone/app/layout/viewlets/

Nombre de la plantilla:noneNombre de la clase:plone.app.layout.viewlets.commo
n.TitleViewletAdministrador:plone.htmlhead (nombre)
plone.app.layout.viewlets.interfaces.IHtmlHead (interfaz)
Ejemplos de archivos & directivas
~~~~~~~~~~~

Cree su propia versión de la clase en [su paquete de tema]/browser/[su
modulo].py

::from plone.app.layout.viewlets.common import TitleViewlet
    from Products.Five.browser.pagetemplatefile import
    ViewPageTemplateFile

    class [your class name](TitleViewlet):
        [your code here]


Conecte su viewlet [su paquete de tema]/browser/configure.zcml

::<browser:viewlet
        name="[your namespace].[your viewlet name]"
        manager="plone.app.layout.viewlets.interfaces.IHtmlHead"
        class=".[your module].[your class name]"
        layer=".interfaces.[your theme specific interface]"
        permission="zope2.View"
    />


En [su paquete de tema]/profiles/default/viewlets.xml

Oculte el viewlet original (si lo desea)

::<object>
        <hidden manager="plone.htmlhead" skinname="[your skin name]">
            <viewlet name="plone.htmlhead.title" />
        </hidden>


Inserte su nuevo viewlet en un administrador de viewlet

::    <order manager="plone.htmlhead" skinname="[your skin name]"
               based-on="Plone Default">
            <viewlet name="[your namespace].[your viewlet name]"
                     insert-before="*" />
        </order>
    </object>



7.8.3. Enlaces anterior/siguiente
=================================

Proporciona enlaces anterior/siguiente en la cabecera HTML.

Fragmento:``<link title="Go to previous item" ???
/>``CSS:noneNombre:plone.nextprevious.linksTipo:`viewlet`_
Personalización a través de la Interfaz de Administración de Zope
--------------------------------------------------------------------

Uso:Configuración de sitio > Interfaz de Administración de Zope >
portal_view_customizationsIr a:plone.nextprevious.links
Personalizando de su propio producto
------------------------------------

Los siguientes detalles le ayudar?n a localizar los archivos que usted tendrá
que copiar en su propio producto. También le ayudar?n a proporcionar la
información correcta para crear sus propias directivas ZCML, clases Python, y
interfaces. Vea `Viewlet`_ para más información.

Ubicado en:

-   [locación de su huevo]/plone/app/layout/nextprevious/
-   [locación de su
    huevo]/plone.app.layout-[version].egg/plone/app/layout/nextprevious/

Nombre de la plantilla:links.ptNombre de la clase:plone.app.layout.nextprevio
us.view.NextPreviousLinksViewletAdministrador:plone.htmlhead.links (nombre)
plone.app.layout.viewlets.interfaces.IHtmlHeadLinks (interfaz)
Ejemplos de archivos & directivas
~~~~~~~~~~~

Put a version of links.pt in [your theme package]/browser/templates)

Cree su propia versión de la clase en [su paquete de tema]/browser/[su
modulo].py

::from plone.app.layout.nextprevious.view import NextPreviousLinksViewlet
    from Products.Five.browser.pagetemplatefile import
    ViewPageTemplateFile
    class [your class name](NextPreviousLinksViewlet):
        render = ViewPageTemplateFile("[your template name]")


Conecte su viewlet [su paquete de tema]/browser/configure.zcml

::<browser:viewlet
        name="[your namespace].[your viewlet name]"
        manager="plone.app.layout.viewlets.interfaces.IHtmlHeadLinks"
        class=".[your module].[your class name]"
        layer=".interfaces.[your theme specific interface]"
        permission="zope2.View"
    />


En [su paquete de tema]/profiles/default/viewlets.xml

Oculte el viewlet original (si lo desea)

::<object>
        <hidden manager="plone.htmlhead.links" skinname="[your skin
        name]">
            <viewlet name="plone.nextprevious.links" />
        </hidden>


Inserte su nuevo viewlet en un administrador de viewlet

::    <order manager="plone.htmlhead.links" skinname="[your skin name]"
               based-on="Plone Default">
            <viewlet name="[your namespace].[your viewlet name]"
                     insert-before="*" />
        </order>
    </object>



7.8.4. Enlace Favicon
=====================

El enlace favicon en la cabecera HTML.

Fragmento:``<link rel="shortcut icon" ???
/>``CSS:noneNombre:plone.links.faviconTipo:`viewlet`_
Personalización a través de la Interfaz de Administración de Zope
--------------------------------------------------------------------

Uso:Configuración de sitio > Interfaz de Administración de Zope >
portal_view_customizationsIr a:plone.links.favicon
Personalizando de su propio producto
------------------------------------

Los siguientes detalles le ayudar?n a localizar los archivos que usted tendrá
que copiar en su propio producto. También le ayudar?n a proporcionar la
información correcta para crear sus propias directivas ZCML, clases Python, y
interfaces. Vea `Viewlet`_ para más información.

Ubicado en:

-   [locación de su huevo]/plone/app/layout/links/
-   [locación de su
    huevo]/plone.app.layout-[version].egg/plone/app/layout/links/

Nombre de la plantilla:favicon.ptNombre de la clase:plone.app.layout.links.vi
ewlets.FaviconViewletAdministrador:plone.htmlhead.links (nombre)
plone.app.layout.viewlets.interfaces.IHtmlHeadLinks (interfaz)
Ejemplos de archivos & directivas
~~~~~~~~~~~

Ponga una versión de favicon.pt en [su paquete de tema]/browser/templates)

Cree su propia versión de la clase en [su paquete de tema]/browser/[su
modulo].py

::from plone.app.layout.links.viewlets import FaviconViewlet
    from Products.Five.browser.pagetemplatefile import
    ViewPageTemplateFile
    class [your class name](FaviconViewlet):
        render = ViewPageTemplateFile("[your template name]")


Conecte su viewlet [su paquete de tema]/browser/configure.zcml

::<browser:viewlet
        name="[your namespace].[your viewlet name]"
        manager="plone.app.layout.viewlets.interfaces.IHtmlHeadLinks"
        class=".[your module].[your class name]"
        layer=".interfaces.[your theme specific interface]"
        permission="zope2.View"
    />


En [su paquete de tema]/profiles/default/viewlets.xml

Oculte el viewlet original (si lo desea)

::<object>
        <hidden manager="plone.htmlhead.links" skinname="[your skin
        name]">
            <viewlet name="plone.links.favicon" />
        </hidden>


Inserte su nuevo viewlet en un administrador de viewlet

::    <order manager="plone.htmlhead.links" skinname="[your skin name]"
               based-on="Plone Default">
            <viewlet name="[your namespace].[your viewlet name]"
                     insert-before="*" />
        </order>
    </object>



7.8.5. Enlace de b?squeda
==========================

El enlace de b?squeda en la cabecera HTML.

Fragmento:``<link rel="search" ???
/>``CSS:noneNombre:plone.links.searchTipo:`viewlet`_
Personalización a través de la Interfaz de Administración de Zope
--------------------------------------------------------------------

Uso:Configuración de sitio > Interfaz de Administración de Zope >
portal_view_customizationsIr a:plone.links.search
Personalizando de su propio producto
------------------------------------

Los siguientes detalles le ayudar?n a localizar los archivos que usted tendrá
que copiar en su propio producto. También le ayudar?n a proporcionar la
información correcta para crear sus propias directivas ZCML, clases Python, y
interfaces. Vea `Viewlet`_ para más información.

Ubicado en:

-   [locación de su huevo]/plone/app/layout/links/
-   [locación de su
    huevo]/plone.app.layout-[version].egg/plone/app/layout/links/

Nombre de la plantilla:search.ptNombre de la clase:plone.app.layout.links.vie
wlets.SearchViewletAdministrador:plone.htmlhead.links (nombre)
plone.app.layout.viewlets.interfaces.IHtmlHeadLinks (interfaz)
Ejemplos de archivos & directivas
~~~~~~~~~~~

Ponga una versión de search.pt en [su paquete de tema]/browser/templates)

Cree su propia versión de la clase en [su paquete de tema]/browser/[su
modulo].py

::from plone.app.layout.links.viewlets import SearchViewlet
    from Products.Five.browser.pagetemplatefile import
    ViewPageTemplateFile
    class [your class name](SearchViewlet):
        render = ViewPageTemplateFile("[your template name]")


Conecte su viewlet [su paquete de tema]/browser/configure.zcml

::<browser:viewlet
        name="[your namespace].[your viewlet name]"
        manager="plone.app.layout.viewlets.interfaces.IHtmlHeadLinks"
        class=".[your module].[your class name]"
        layer=".interfaces.[your theme specific interface]"
        permission="zope2.View"
    />


En [su paquete de tema]/profiles/default/viewlets.xml

Oculte el viewlet original (si lo desea)

::<object>
        <hidden manager="plone.htmlhead.links" skinname="[your skin
        name]">
            <viewlet name="plone.links.search" />
        </hidden>


Inserte su nuevo viewlet en un administrador de viewlet

::    <order manager="plone.htmlhead.links" skinname="[your skin name]"
               based-on="Plone Default">
            <viewlet name="[your namespace].[your viewlet name]"
                     insert-before="*" />
        </order>
    </object>



7.8.6. Enlace de autor
======================

El enlace de autor en la cabecera HTML.

Fragmento:``<link rel="author" ???
/>``CSS:noneNombre:plone.links.authorTipo:`viewlet`_
Personalización a través de la Interfaz de Administración de Zope
--------------------------------------------------------------------

Uso:Configuración de sitio > Interfaz de Administración de Zope >
portal_view_customizationsIr a:plone.links.author
Personalizando de su propio producto
------------------------------------

Los siguientes detalles le ayudar?n a localizar los archivos que usted tendrá
que copiar en su propio producto. También le ayudar?n a proporcionar la
información correcta para crear sus propias directivas ZCML, clases Python, y
interfaces. Vea `Viewlet`_ para más información.

Ubicado en:

-   [locación de su huevo]/plone/app/layout/links/
-   [locación de su
    huevo]/plone.app.layout-[version].egg/plone/app/layout/links/

Nombre de la plantilla:author.ptNombre de la clase:plone.app.layout.links.vie
wlets.AuthorViewletAdministrador:plone.htmlhead.links (nombre)
plone.app.layout.viewlets.interfaces.IHtmlHeadLinks (interfaz)
Ejemplos de archivos & directivas
~~~~~~~~~~~

Ponga una versión de author.pt en [su paquete de tema]/browser/templates)

Cree su propia versión de la clase en [su paquete de tema]/browser/[su
modulo].py

::from plone.app.layout.links.viewlets import AuthorViewlet
    from Products.Five.browser.pagetemplatefile import
    ViewPageTemplateFile
    class [your class name](AuthorViewlet):
        render = ViewPageTemplateFile("[your template name]")


Conecte su viewlet [su paquete de tema]/browser/configure.zcml

::<browser:viewlet
        name="[your namespace].[your viewlet name]"
        manager="plone.app.layout.viewlets.interfaces.IHtmlHeadLinks"
        class=".[your module].[your class name]"
        layer=".interfaces.[your theme specific interface]"
        permission="zope2.View"
    />


En [su paquete de tema]/profiles/default/viewlets.xml

Oculte el viewlet original (si lo desea)

::<object>
        <hidden manager="plone.htmlhead.links" skinname="[your skin
        name]">
            <viewlet name="plone.links.author" />
        </hidden>


Inserte su nuevo viewlet en un administrador de viewlet

::    <order manager="plone.htmlhead.links" skinname="[your skin name]"
               based-on="Plone Default">
            <viewlet name="[your namespace].[your viewlet name]"
                     insert-before="*" />
        </order>
    </object>



7.8.7. Enlace de navegación
============================

El enlace de navegación en la cabecera HTML.

Fragmento:``<link title="Front Page" ???> and <link title="Site Map"
..>``CSS:noneNombre:plone.links.navigationTipo:`viewlet`_
Personalización a través de la Interfaz de Administración de Zope
--------------------------------------------------------------------

Uso:Configuración de sitio > Interfaz de Administración de Zope >
portal_view_customizationsIr a:plone.links.navigation
Personalizando de su propio producto
------------------------------------

Los siguientes detalles le ayudar?n a localizar los archivos que usted tendrá
que copiar en su propio producto. También le ayudar?n a proporcionar la
información correcta para crear sus propias directivas ZCML, clases Python, y
interfaces. Vea `Viewlet`_ para más información.

Ubicado en:

-   [locación de su huevo]/plone/app/layout/links/
-   [locación de su
    huevo]/plone.app.layout-[version].egg/plone/app/layout/links/

Nombre de la plantilla:navigation.ptNombre de la clase:plone.app.layout.links
.viewlets.NavigationViewletAdministrador:plone.htmlhead.links (nombre)
plone.app.layout.viewlets.interfaces.IHtmlHeadLinks (interfaz)
Ejemplos de archivos & directivas
~~~~~~~~~~~

Ponga una versión de navigation.pt en [su paquete de tema]/browser/templates)

Cree su propia versión de la clase en [su paquete de tema]/browser/[su
modulo].py

::from plone.app.layout.links.viewlets import NavigationViewlet
    from Products.Five.browser.pagetemplatefile import
    ViewPageTemplateFile
    class [your class name](NavigationViewlet):
        render = ViewPageTemplateFile("[your template name]")


Conecte su viewlet [su paquete de tema]/browser/configure.zcml

::<browser:viewlet
        name="[your namespace].[your viewlet name]"
        manager="plone.app.layout.viewlets.interfaces.IHtmlHeadLinks"
        class=".[your module].[your class name]"
        layer=".interfaces.[your theme specific interface]"
        permission="zope2.View"
    />


En [su paquete de tema]/profiles/default/viewlets.xml

Oculte el viewlet original (si lo desea)

::<object>
        <hidden manager="plone.htmlhead.links" skinname="[your skin
        name]">
            <viewlet name="plone.links.navigation" />
        </hidden>


Inserte su nuevo viewlet en un administrador de viewlet

::    <order manager="plone.htmlhead.links" skinname="[your skin name]"
               based-on="Plone Default">
            <viewlet name="[your namespace].[your viewlet name]"
                     insert-before="*" />
        </order>
    </object>



7.8.8. Analytics
==============================================================

Fragmento de código de Google Analytics.

Notas:Proporciona el fragmento de código para su sitio a través de la web:
Configuración de sitio > SitioFragmento:``(Fragmento de código definido por
el administrador del sitio)``CSS:noneNombre:plone.analyticsTipo:`viewlet`_
Personalización a través de la Interfaz de Administración de Zope
--------------------------------------------------------------------

Uso:Configuración de sitio > Interfaz de Administración de Zope >
portal_view_customizationsIr a:plone.analytics
Personalizando de su propio producto
------------------------------------

Los siguientes detalles le ayudar?n a localizar los archivos que usted tendrá
que copiar en su propio producto. También le ayudar?n a proporcionar la
información correcta para crear sus propias directivas ZCML, clases Python, y
interfaces. Vea `Viewlet`_ para más información.

Ubicado en:

-   [locación de su huevo]/plone/app/layout/analytics/
-   [locación de su
    huevo]/plone.app.layout-[version].egg/plone/app/layout/analytics/

Nombre de la plantilla:noneNombre de la clase:plone.app.layout.analytics.view
.AnalyticsViewletAdministrador:plone.portalfooter (nombre)
plone.app.layout.viewlets.interfaces.IPortalFooter (interfaz)
Ejemplos de archivos & directivas
~~~~~~~~~~~

Cree su propia versión de la clase en [su paquete de tema]/browser/[su
modulo].py

::from plone.app.layout.analytics.view import AnalyticsViewlet
    from Products.Five.browser.pagetemplatefile import
    ViewPageTemplateFile

    class [your class name](AnalyticsViewlet):
        [your code here]


Conecte su viewlet [su paquete de tema]/browser/configure.zcml

::<browser:viewlet
        name="[your namespace].[your viewlet name]"
        manager="plone.app.layout.viewlets.interfaces.IPortalFooter"
        class=".[your module].[your class name]"
        layer=".interfaces.[your theme specific interface]"
        permission="zope2.View"
    />


En [su paquete de tema]/profiles/default/viewlets.xml

Oculte el viewlet original (si lo desea)

::<object>
        <hidden manager="plone.portalfooter" skinname="[your skin
        name]">
            <viewlet name="plone.analytics" />
        </hidden>


Inserte su nuevo viewlet en un administrador de viewlet

::    <order manager="plone.portalfooter" skinname="[your skin name]"
               based-on="Plone Default">
            <viewlet name="[your namespace].[your viewlet name]"
                     insert-before="*" />
        </order>
    </object>



7.8.9. Dublin Core Metadata
=========================================================================

Metadatos Dublin Core en la cabecera HTML.

Fragmento:``<meta ....
/>``CSS:noneNombre:plone.htmlhead.dublincoreTipo:`viewlet`_
Personalización a través de la Interfaz de Administración de Zope
--------------------------------------------------------------------

Uso:Configuración de sitio > Interfaz de Administración de Zope >
portal_view_customizationsIr a:plone.htmlhead.dublincore
Personalizando de su propio producto
------------------------------------

Los siguientes detalles le ayudar?n a localizar los archivos que usted tendrá
que copiar en su propio producto. También le ayudar?n a proporcionar la
información correcta para crear sus propias directivas ZCML, clases Python, y
interfaces. Vea `Viewlet`_ para más información.

Ubicado en:

-   [locación de su huevo]/plone/app/layout/viewlets/
-   [locación de su
    huevo]/plone.app.layout-[version].egg/plone/app/layout/viewlets/

Nombre de la plantilla:dublin_core.pt
Nombre de la clase:plone.app.layout.viewlets.common.DublinCoreViewletAdminist
rador:plone.htmlhead (nombre)
plone.app.layout.viewlets.interfaces.IHtmlHead (interfaz)
Ejemplos de archivos & directivas
~~~~~~~~~~~

Cree su propia versión de la clase en [su paquete de tema]/browser/[su
modulo].py

::from plone.app.layout.viewlets.common import DublinCoreViewlet
    from Products.Five.browser.pagetemplatefile import
    ViewPageTemplateFile

    class [your class name](DublinCoreViewlet):
        [your code here]


Conecte su viewlet [su paquete de tema]/browser/configure.zcml

::<browser:viewlet
        name="[your namespace].[your viewlet name]"
        manager="plone.app.layout.viewlets.interfaces.IHtmlHead"
        class=".[your module].[your class name]"
        layer=".interfaces.[your theme specific interface]"
        permission="zope2.View"
    />


En [su paquete de tema]/profiles/default/viewlets.xml

Oculte el viewlet original (si lo desea)

::<object>
        <hidden manager="plone.htmlhead" skinname="[your skin name]">
            <viewlet name="plone.htmlhead.dublincore" />
        </hidden>


Inserte su nuevo viewlet en un administrador de viewlet

::    <order manager="plone.htmlhead" skinname="[your skin name]"
               based-on="Plone Default">
            <viewlet name="[your namespace].[your viewlet name]"
                     insert-before="*" />
        </order>
    </object>



7.8.10. KSS Base Url
==================================================================

Enlace rel tag en la cabecera HTML con el URL real de la página publicada.

Fragmento:``<link rel="kss-base-url" .... />``CSS:noneNombre:plone.htmlhead
.kss-base-urlTipo:`viewlet`_
Personalización a través de la Interfaz de Administración de Zope
--------------------------------------------------------------------

Uso:Configuración de sitio > Interfaz de Administración de Zope >
portal_view_customizationsIr a:plone.htmlhead.kss-base-url
Personalizando de su propio producto
------------------------------------

Los siguientes detalles le ayudar?n a localizar los archivos que usted tendrá
que copiar en su propio producto. También le ayudar?n a proporcionar la
información correcta para crear sus propias directivas ZCML, clases Python, y
interfaces. Vea `Viewlet`_ para más información.

Ubicado en:

-   [locación de su huevo]/plone/app/kss/
-   [locación de su huevo]/plone.app.kss-[version].egg/plone/app/kss/

Nombre de la plantilla:noneNombre de la clase:plone.app.kss.headerViewlet.KSS
BaseUrlViewletAdministrador:plone.htmlhead (nombre)
plone.app.layout.viewlets.interfaces.IHtmlHead (interfaz)
Ejemplos de archivos & directivas
~~~~~~~~~~~

Cree su propia versión de la clase en [su paquete de tema]/browser/[su
modulo].py

::from plone.app.kss.headerViewlet import KSSBaseUrlViewlet
    from Products.Five.browser.pagetemplatefile import
    ViewPageTemplateFile

    class [your class name](KSSBaseUrlViewlet):
        [your code here]


Conecte su viewlet [su paquete de tema]/browser/configure.zcml

::<browser:viewlet
        name="[your namespace].[your viewlet name]"
        manager="plone.app.layout.viewlets.interfaces.IHtmlHead"
        class=".[your module].[your class name]"
        layer=".interfaces.[your theme specific interface]"
        permission="zope2.View"
    />


En [su paquete de tema]/profiles/default/viewlets.xml

Oculte el viewlet original (si lo desea)

::<object>
        <hidden manager="plone.htmlhead" skinname="[your skin name]">
            <viewlet name="plone.htmlhead.kss-base-url" />
        </hidden>


Inserte su nuevo viewlet en un administrador de viewlet

::    <order manager="plone.htmlhead" skinname="[your skin name]"
               based-on="Plone Default">
            <viewlet name="[your namespace].[your viewlet name]"
                     insert-before="*" />
        </order>
    </object>



7.8.11. Enlace RSS
==================

El enlace RSS en la cabecera HTML.

Fragmento:``<link rel="alternate" title="RSS 1.0" ...
/>``CSS:noneNombre:plone.links.RSSTipo:`viewlet`_
Personalización a través de la Interfaz de Administración de Zope
--------------------------------------------------------------------

Uso:Configuración de sitio > Interfaz de Administración de Zope >
portal_view_customizationsIr a:plone.links.RSS
Personalizando de su propio producto
------------------------------------

Los siguientes detalles le ayudar?n a localizar los archivos que usted tendrá
que copiar en su propio producto. También le ayudar?n a proporcionar la
información correcta para crear sus propias directivas ZCML, clases Python, y
interfaces. Vea `Viewlet`_ para más información.

Ubicado en:

-   [locación de su huevo]/plone/app/layout/links/
-   [locación de su
    huevo]/plone.app.layout-[version].egg/plone/app/layout/links/

Nombre de la plantilla:rsslink.ptNombre de la clase:plone.app.layout.links.vi
ewlets.RSSViewletAdministrador:plone.htmlhead.links (nombre)
plone.app.layout.viewlets.interfaces.IHtmlHeadLinks (interfaz)
Ejemplos de archivos & directivas
~~~~~~~~~~~

Ponga una versión de navigation.pt en [su paquete de tema]/browser/templates)

Cree su propia versión de la clase en [su paquete de tema]/browser/[su
modulo].py

::from plone.app.layout.links.viewlets import RSSViewlet
    from Products.Five.browser.pagetemplatefile import
    ViewPageTemplateFile
    class [your class name](RSSViewlet):
        render = ViewPageTemplateFile("[your template name]")


Conecte su viewlet [su paquete de tema]/browser/configure.zcml

::<browser:viewlet
        name="[your namespace].[your viewlet name]"
        manager="plone.app.layout.viewlets.interfaces.IHtmlHeadLinks"
        class=".[your module].[your class name]"
        layer=".interfaces.[your theme specific interface]"
        permission="zope2.View"
    />


En [su paquete de tema]/profiles/default/viewlets.xml

Oculte el viewlet original (si lo desea)

::<object>
        <hidden manager="plone.htmlhead.links" skinname="[your skin
        name]">
            <viewlet name="plone.links.RSS" />
        </hidden>


Inserte su nuevo viewlet en un administrador de viewlet

::    <order manager="plone.htmlhead.links" skinname="[your skin name]"
               based-on="Plone Default">
            <viewlet name="[your namespace].[your viewlet name]"
                     insert-before="*" />
        </order>
    </object>



7.9. Elementos visibles de página
==================================

Elementos de página visibles en la página (logotipo, acciones de sitio,
cuadro de b?squeda, etc.)


7.9.1. Selector de idiomas
==========================

Proporciona una lista desplegable para seleccionar un idioma.

Fragmento:``<ul id="portal-languageselector"> ???
</ul>``Nombre:plone.app.i18n.locales.languageselectorTipo:`viewlet`_
Personalización a través de la Interfaz de Administración de Zope
--------------------------------------------------------------------

Uso:Configuración de sitio > Interfaz de Administración de Zope >
portal_view_customizationsIr a:plone.app.i18n.locales.languageselector
Personalizando de su propio producto
------------------------------------

Los siguientes detalles le ayudar?n a localizar los archivos que usted tendrá
que copiar en su propio producto. También le ayudar?n a proporcionar la
información correcta para crear sus propias directivas ZCML, clases Python, y
interfaces. Vea `Viewlet`_ para más información.

Ubicado en:

-   [locación de su huevo]/plone/app/i18n/locales/browser/
-   [locación de su
    huevo]/plone.app.i18n-[version].egg/plone/app/i18n/locales/browser/

Nombre de la plantilla:languageselector.ptNombre de la clase:plone.app.i18n.l
ocales.browser.selector.LanguageSelectorAdministrador:Portal Top (name)
plone.app.layout.viewlets.interfaces.IPortalTop (interfaz)
Ejemplos de archivos & directivas
~~~~~~~~~~~

Ponga una versión de languageselector.pt en [su paquete de
tema]/browser/templates)

Cree su propia versión de la clase en [su paquete de tema]/browser/[su
modulo].py

::from plone.app.i18n.locales.browser.selector import LanguageSelector
    from Products.Five.browser.pagetemplatefile import
    ViewPageTemplateFile
    class [your class name](LanguageSelector):
        render = ViewPageTemplateFile("[your template name]")


Conecte su viewlet [su paquete de tema]/browser/configure.zcml

::<browser:viewlet
        name="[your namespace].[your viewlet name]"
        manager="plone.app.layout.viewlets.interfaces.IPortalTop"
        class=".[your module].[your class name]"
        layer=".interfaces.[your theme specific interface]"
        permission="zope2.View"
    />


En [su paquete de tema]/profiles/default/viewlets.xml

Oculte el viewlet original (si lo desea)

::<object>
        <hidden manager="Portal Top" skinname="[your skin name]">
            <viewlet
            name="plone.app.i18n.locales.languageselector" />
        </hidden>


Inserte su nuevo viewlet en un administrador de viewlet

::    <order manager="Portal Top" skinname="[your skin name]"
               based-on="Plone Default">
            <viewlet name="[your namespace].[your viewlet name]"
                     insert-before="*" />
        </order>
    </object>



7.9.2. Acciones del sitio
=========================

Enlaces disponibles en cada página, para proporcionar funcionalidad o
información específica.

Notas:Puede cambiar el orden, añadir o eliminar acciones individuales del
sitio

-   a través de la Web: Configuración de sitio > Interfaz de
    Administración de Zope > portal_actions > site_actions
-   En su producto: profiles/default/actions.xml

Fragmento:``<ul id="portal-
siteactions">...</ul>``CSS:public.cssNombre:plone.site_actionsTipo:`viewlet`_
Personalización a través de la Interfaz de Administración de Zope
--------------------------------------------------------------------

Uso:Configuración de sitio > Interfaz de Administración de Zope >
portal_view_customizationsIr a:plone.site_actions
Personalizando de su propio producto
------------------------------------

Los siguientes detalles le ayudar?n a localizar los archivos que usted tendrá
que copiar en su propio producto. También le ayudar?n a proporcionar la
información correcta para crear sus propias directivas ZCML, clases Python, y
interfaces. Vea `Viewlet`_ para más información.

Ubicado en:

-   [locación de su huevo]/plone/app/layout/viewlets/
-   [locación de su
    huevo]/plone.app.layout-[version].egg/plone/app/layout/viewlets/

Nombre de la plantilla:site_actions.ptNombre de la clase:plone.app.layout.vie
wlets.common.SiteActionsViewletAdministrador:plone.portalheader (nombre)
plone.app.layout.viewlets.interfaces.IPortalHeader (interfaz)
Ejemplos de archivos & directivas
~~~~~~~~~~~

Ponga una versión de site_actions.pt en [su paquete de
tema]/browser/templates)

Cree su propia versión de la clase en [su paquete de tema]/browser/[su
modulo].py

::from plone.app.layout.viewlets.common import SiteActionsViewlet
    from Products.Five.browser.pagetemplatefile import
    ViewPageTemplateFile
    class [your class name](SiteActionsViewlet):
        render = ViewPageTemplateFile("[your template name]")


Conecte su viewlet [su paquete de tema]/browser/configure.zcml

::<browser:viewlet
        name="[your namespace].[your viewlet name]"
        manager="plone.app.layout.viewlets.interfaces.IPortalHeader"
        class=".[your module].[your class name]"
        layer=".interfaces.[your theme specific interface]"
        permission="zope2.View"
    />


En [su paquete de tema]/profiles/default/viewlets.xml

Oculte el viewlet original (si lo desea)

::<object>
        <hidden manager="plone.portalheader" skinname="[your skin
        name]">
            <viewlet name="plone.site_actions" />
        </hidden>


Inserte su nuevo viewlet en un administrador de viewlet

::    <order manager="plone.portalheader" skinname="[your skin name]"
               based-on="Plone Default">
            <viewlet name="[your namespace].[your viewlet name]"
                     insert-before="*" />
        </order>
    </object>



7.9.3. Cuadro de b?squeda
==========================

Facilidad de b?squeda en el sitio

Notas:Para personalizar el comportamiento del cuadro de b?squeda

-   a través de la Web: Configuración de sitio > B?squeda
-   En su producto: profiles/default/propertiestool.xml

Fragmento:``<div id="portal-
searchbox">???</div>``CSS:public.cssNombre:plone.searchboxTipo:`viewlet`_
Personalización a través de la Interfaz de Administración de Zope
--------------------------------------------------------------------

Uso:Configuración de sitio > Interfaz de Administración de Zope >
portal_view_customizationsIr a:plone.searchboxPara más
información:`http://plone.org/documentation/kb/the-search-box`_
Personalizando de su propio producto
------------------------------------

Los siguientes detalles le ayudar?n a localizar los archivos que usted tendrá
que copiar en su propio producto. También le ayudar?n a proporcionar la
información correcta para crear sus propias directivas ZCML, clases Python, y
interfaces. Vea `Viewlet`_ para más información.

Ubicado en:

-   [locación de su huevo]/plone/app/layout/viewlets/
-   [locación de su
    huevo]/plone.app.layout-[version].egg/plone/app/layout/viewlets/

Nombre de la plantilla:searchbox.ptNombre de la clase:plone.app.layout.viewle
ts.common.SearchBoxViewletAdministrador:plone.portalheader (nombre)
plone.app.layout.viewlets.interfaces.IPortalHeader (interfaz)
Ejemplos de archivos & directivas
~~~~~~~~~~~

Ponga una versión de searchbox.pt en [su paquete de tema]/browser/templates)

Cree su propia versión de la clase en [su paquete de tema]/browser/[su
modulo].py

::from plone.app.layout.viewlets.common import SearchBoxViewlet
    from Products.Five.browser.pagetemplatefile import
    ViewPageTemplateFile
    class [your class name](SearchBoxViewlet):
        render = ViewPageTemplateFile("[your template name]")


Conecte su viewlet [su paquete de tema]/browser/configure.zcml

::<browser:viewlet
        name="[your namespace].[your viewlet name]"
        manager="plone.app.layout.viewlets.interfaces.IPortalHeader"
        class=".[your module].[your class name]"
        layer=".interfaces.[your theme specific interface]"
        permission="zope2.View"
    />


En [su paquete de tema]/profiles/default/viewlets.xml

Oculte el viewlet original (si lo desea)

::<object>
        <hidden manager="plone.portalheader" skinname="[your skin
        name]">
            <viewlet name="plone.searchbox" />
        </hidden>


Inserte su nuevo viewlet en un administrador de viewlet

::    <order manager="plone.portalheader" skinname="[your skin name]"
               based-on="Plone Default">
            <viewlet name="[your namespace].[your viewlet name]"
                     insert-before="*" />
        </order>
    </object>
     '


7.9.4. Logotipo
===============

El logotipo del sitio.

Fragmento:``<a id="portal-logo" ...>...
</a>``CSS:public.cssNombre:plone.logoTipo:`viewlet`_
Personalización a través de la Interfaz de Administración de Zope
--------------------------------------------------------------------

Uso:Configuración de sitio > Interfaz de Administración de Zope >
portal_view_customizationsIr a:plone.logoPara más
información:`http://plone.org/documentation/kb/where-is-what/the-logo`_
Ver también la sección Comienzo rápido de este manual.
Personalizando de su propio producto
------------------------------------

Los siguientes detalles le ayudar?n a localizar los archivos que usted tendrá
que copiar en su propio producto. También le ayudar?n a proporcionar la
información correcta para crear sus propias directivas ZCML, clases Python, y
interfaces. Vea `Viewlet`_ para más información.

Ubicado en:

-   [locación de su huevo]/plone/app/layout/viewlets/
-   [locación de su
    huevo]/plone.app.layout-[version].egg/plone/app/layout/viewlets/

Nombre de la plantilla:logo.ptNombre de la clase:plone.app.layout.viewlets.co
mmon.LogoViewletAdministrador:plone.portalheader (nombre)
plone.app.layout.viewlets.interfaces.IPortalHeader (interfaz)
Ejemplos de archivos & directivas
~~~~~~~~~~~

Ponga una versión de logo.pt en [su paquete de tema]/browser/templates)

Modifique el logo.pt para satisfacer sus necesidades. Por ejemplo, si desea
utilizar una imagen con otro nombre que logo.jpg, puede utilizar este código
y estilo #header en el archivo mytheme.css.

::<a metal:define-macro="portal_logo"
       id="portal-logo"
       accesskey="1"
       tal:attributes="href view/navigation_root_url"
       i18n:domain="plone">
        <!-- <img src="logo.jpg" alt=""
             tal:replace="structure view/logo_tag" /> --> <!--
             commenting out the code that normally looks for logo.jpg -->
        <div id="banner"><!-- style this div in your mytheme.css
        --></div></a>

Cree su propia versión de la clase en [su paquete de tema]/browser/[su
modulo].py

::from plone.app.layout.viewlets.common import LogoViewlet
    from Products.Five.browser.pagetemplatefile import
    ViewPageTemplateFile
    class [your class name](LogoViewlet):
        render = ViewPageTemplateFile("[your template name]")

Conecte su viewlet [su paquete de tema]/browser/configure.zcml

::<browser:viewlet
        name="[your namespace].[your viewlet name]"
        manager="plone.app.layout.viewlets.interfaces.IPortalHeader"
        class=".[your module].[your class name]"
        layer=".interfaces.[your theme specific interface]"
        permission="zope2.View"
    />

En [su paquete de tema]/profiles/default/viewlets.xml

Oculte el viewlet original (si lo desea)

::<object>
        <hidden manager="plone.portalheader" skinname="[your skin
        name]">
            <viewlet name="plone.logo" />
        </hidden>

Inserte su nuevo viewlet en un administrador de viewlet

::    <order manager="plone.portalheader" skinname="[your skin name]"
               based-on="Plone Default">
            <viewlet name="[your namespace].[your viewlet name]"
                     insert-before="*" />
        </order>
    </object> '


7.9.5. Secciones globales
=========================

Las secciones de nivel superior del sitio.

Notas:Las secciones son generadas automáticamente a partir de los elementos
de contenido de nivel superior o pueden configurarse manualmente

-   a través de la Web: Configuración de sitio > Navigación (para auto-
    generación)
Configuración de sitio > Interfaz de Administración de Zope > portal_tabs
(para definir manualmente las secciones)
-   En su producto: profiles/default/actions.xml and propertiestool.xml

Fragmento:``<h5 class="hiddenStructure">Sections</h5> <ul id="portal-
globalnav"> ???
</ul>``CSS:public.cssNombre:plone.global_sectionsTipo:`viewlet`_
Personalización a través de la Interfaz de Administración de Zope
--------------------------------------------------------------------

Uso:Configuración de sitio > Interfaz de Administración de Zope >
portal_view_customizationsIr a:plone.global_sectionsPara más
información:`http://plone.org/documentation/kb/where-is-what/the-navigation-
tabs`_
Personalizando de su propio producto
------------------------------------

Los siguientes detalles le ayudar?n a localizar los archivos que usted tendrá
que copiar en su propio producto. También le ayudar?n a proporcionar la
información correcta para crear sus propias directivas ZCML, clases Python, y
interfaces. Vea `Viewlet`_ para más información.

Ubicado en:

-   [locación de su huevo]/plone/app/layout/viewlets/
-   [locación de su
    huevo]/plone.app.layout-[version].egg/plone/app/layout/viewlets/

Nombre de la plantilla:sections.ptNombre de la clase:plone.app.layout.viewlet
s.common.GlobalSectionsViewletAdministrador:plone.portalheader (nombre)
plone.app.layout.viewlets.interfaces.IPortalHeader (interfaz)
Ejemplos de archivos & directivas
~~~~~~~~~~~

Ponga una versión de sections.pt en [su paquete de tema]/browser/templates)

Cree su propia versión de la clase en [su paquete de tema]/browser/[su
modulo].py

::from plone.app.layout.viewlets.common import GlobalSectionsViewlet
    from Products.Five.browser.pagetemplatefile import
    ViewPageTemplateFile
    class [your class name](GlobalSectionsViewlet):
        render = ViewPageTemplateFile("[your template name]")

Conecte su viewlet [su paquete de tema]/browser/configure.zcml

::<browser:viewlet
        name="[your namespace].[your viewlet name]"
        manager="plone.app.layout.viewlets.interfaces.IPortalHeader"
        class=".[your module].[your class name]"
        layer=".interfaces.[your theme specific interface]"
        permission="zope2.View"
    />

En [su paquete de tema]/profiles/default/viewlets.xml

Oculte el viewlet original (si lo desea)

::<object>
        <hidden manager="plone.portalheader" skinname="[your skin
        name]">
            <viewlet name="plone.global_sections" />
        </hidden>

Inserte su nuevo viewlet en un administrador de viewlet

::    <order manager="plone.portalheader" skinname="[your skin name]"
               based-on="Plone Default">
            <viewlet name="[your namespace].[your viewlet name]"
                     insert-before="*" />
        </order>
    </object> '


7.9.6. Barra personal
=====================

Proporciona el enlace para Inicio de sesión y otros enlaces una vez que el
usuario ha iniciado sesión.

Notas:Puede cambiar el orden, añadir o eliminar enlaces específicos en la
barra personal

-   a través de la Web: Configuración de sitio > Interfaz de
    Administración de Zope > portal_actions > user
-   En su producto: profiles/default/actions.xml

Fragmento:``<div id="portal-personaltools-wrapper">
???</div>``CSS:public.cssNombre:plone.personal_barTipo:`viewlet`_
Personalización a través de la Interfaz de Administración de Zope
--------------------------------------------------------------------

Uso:Configuración de sitio > Interfaz de Administración de Zope >
portal_view_customizationsIr a:plone.personal_barPara más
información:`http://plone.org/documentation/kb/where-is-what/the-personal-
bar`_
Personalizando de su propio producto
------------------------------------

Los siguientes detalles le ayudar?n a localizar los archivos que usted tendrá
que copiar en su propio producto. También le ayudar?n a proporcionar la
información correcta para crear sus propias directivas ZCML, clases Python, y
interfaces. Vea `Viewlet`_ para más información.

Ubicado en:

-   [locación de su huevo]/plone/app/layout/viewlets/
-   [locación de su
    huevo]/plone.app.layout-[version].egg/plone/app/layout/viewlets/

Nombre de la plantilla:personal_bar.ptNombre de la clase:plone.app.layout.vie
wlets.common.PersonalBarViewletAdministrador:plone.portaltop (nombre)
plone.app.layout.viewlets.interfaces.IPortalTop (interfaz)
Ejemplos de archivos & directivas
~~~~~~~~~~~

Ponga una versión de personal_bar.pt en [su paquete de
tema]/browser/templates)

Cree su propia versión de la clase en [su paquete de tema]/browser/[su
modulo].py

::from plone.app.layout.viewlets.common import PersonalBarViewlet
    from Products.Five.browser.pagetemplatefile import
    ViewPageTemplateFile
    class [your class name](PersonalBarViewlet):
        render = ViewPageTemplateFile("[your template name]")

Conecte su viewlet [su paquete de tema]/browser/configure.zcml

::<browser:viewlet
        name="[your namespace].[your viewlet name]"
        manager="plone.app.layout.viewlets.interfaces.IPortalTop"
        class=".[your module].[your class name]"
        layer=".interfaces.[your theme specific interface]"
        permission="zope2.View"
    />

En [su paquete de tema]/profiles/default/viewlets.xml

Oculte el viewlet original (si lo desea)

::<object>
        <hidden manager="plone.portaltop" skinname="[your skin
        name]">
            <viewlet name="plone.personal_bar" />
        </hidden>

Inserte su nuevo viewlet en un administrador de viewlet

::    <order manager="plone.portaltop" skinname="[your skin name]"
               based-on="Plone Default">
            <viewlet name="[your namespace].[your viewlet name]"
                     insert-before="*" />
        </order>
    </object> '


7.9.7. Barra de ruta (hilo de Ariadna del portal)
=================================================

Proporciona el hilo de Ariadna

Fragmento:``<div id="portal-breadcrumbs">...</div>`` Nota:En el tema
Sunburst, el hilo de Ariadna ha sido dise?ado para no aparecer hasta el
tercer nivel abajo. Personalice el CSS para cambiar este comportamiento.
CSS:public.cssNombre:plone.path_barTipo:`viewlet`_
Personalización a través de la Interfaz de Administración de Zope
--------------------------------------------------------------------

Uso:Configuración de sitio > Interfaz de Administración de Zope >
portal_view_customizationsIr a:plone.path_barPara más
información:`http://plone.org/documentation/kb/where-is-what/the-path-bar`_
Personalizando de su propio producto
------------------------------------

Los siguientes detalles le ayudar?n a localizar los archivos que usted tendrá
que copiar en su propio producto. También le ayudar?n a proporcionar la
información correcta para crear sus propias directivas ZCML, clases Python, y
interfaces. Vea `Viewlet`_ para más información.

Ubicado en:

-   [locación de su huevo]/plone/app/layout/viewlets/
-   [locación de su
    huevo]/plone.app.layout-[version].egg/plone/app/layout/viewlets/

Nombre de la plantilla:path_bar.ptNombre de la clase:plone.app.layout.viewlet
s.common.PathBarViewletAdministrador:plone.portaltop (nombre)
plone.app.layout.viewlets.interfaces.IPortalTop (interfaz)
Ejemplos de archivos & directivas
~~~~~~~~~~~

Ponga una versión de path_bar.pt en [su paquete de tema]/browser/templates)

Cree su propia versión de la clase en [su paquete de tema]/browser/[su
modulo].py

::from plone.app.layout.viewlets.common import PathBarViewlet
    from Products.Five.browser.pagetemplatefile import
    ViewPageTemplateFile
    class [your class name](PathBarViewlet):
        render = ViewPageTemplateFile("[your template name]")

Conecte su viewlet [su paquete de tema]/browser/configure.zcml

::<browser:viewlet
        name="[your namespace].[your viewlet name]"
        manager="plone.app.layout.viewlets.interfaces.IPortalTop"
        class=".[your module].[your class name]"
        layer=".interfaces.[your theme specific interface]"
        permission="zope2.View"
    />

En [su paquete de tema]/profiles/default/viewlets.xml

Oculte el viewlet original (si lo desea)

::<object>
        <hidden manager="plone.portaltop" skinname="[your skin
        name]">
            <viewlet name="plone.path_bar" />
        </hidden>

Inserte su nuevo viewlet en un administrador de viewlet

::    <order manager="plone.portaltop" skinname="[your skin name]"
               based-on="Plone Default">
            <viewlet name="[your namespace].[your viewlet name]"
                     insert-before="*" />
        </order>
    </object> '


7.9.8. Vistas de contenido
==========================

La vista, edición, y las otras pestañas en la interfaz de edición.

Fragmento:``<ul class="contentViews"> ???
</ul>``CSS:authoring.cssNombre:plone.contentviewsTipo:`viewlet`_
Personalización a través de la Interfaz de Administración de Zope
--------------------------------------------------------------------

Uso:Configuración de sitio > Interfaz de Administración de Zope >
portal_view_customizationsIr a:plone.contentviews
Personalizando de su propio producto
------------------------------------

Los siguientes detalles le ayudar?n a localizar los archivos que usted tendrá
que copiar en su propio producto. También le ayudar?n a proporcionar la
información correcta para crear sus propias directivas ZCML, clases Python, y
interfaces. Vea `Viewlet`_ para más información.

Ubicado en:

-   [locación de su huevo]/plone/app/layout/viewlets/
-   [locación de su
    huevo]/plone.app.layout-[version].egg/plone/app/layout/viewlets/

Nombre de la plantilla:contentviews.ptNombre de la
clase:noneAdministrador:plone.contentviews (nombre)
plone.app.layout.viewlets.interfaces.IContentViews (interfaz)
Ejemplos de archivos & directivas
~~~~~~~~~~~

Ponga una versión de contentviews.pt en [su paquete de
tema]/browser/templates)

Conecte su viewlet [su paquete de tema]/browser/configure.zcml

::<browser:viewlet
        name="[your namespace].[your viewlet name]"
        manager="plone.app.layout.viewlets.interfaces.IContentViews"
        template="templates/[your template name].pt"
        layer=".interfaces.[your theme specific interface]"
        permission="zope2.View"
    />


En [su paquete de tema]/profiles/default/viewlets.xml

Oculte el viewlet original (si lo desea)

::<object>
        <hidden manager="plone.contentviews" skinname="[your skin
        name]">
            <viewlet name="plone.contentviews" />
        </hidden>


Inserte su nuevo viewlet en un administrador de viewlet

::    <order manager="plone.contentviews" skinname="[your skin name]"
               based-on="Plone Default">
            <viewlet name="[your namespace].[your viewlet name]"
                     insert-before="*" />
        </order>
    </object>



7.9.9. Acciones de contenido
============================

Proporciona la pantalla desplegable y otras acciones en el modo de edición.
Hay tres componentes de acciones de contenido, registrados para diferentes
interfaces de vista (igual que diferentes conjuntos de acciones son
necesarios en diferentes contextos).

Nombre:plone.contentactionsTipo:`viewlet`_
Personalización a través de la Interfaz de Administración de Zope
--------------------------------------------------------------------

Uso:Configuración de sitio > Interfaz de Administración de Zope >
portal_view_customizationsIr a:plone.contentactions
Personalizando de su propio producto
------------------------------------

Los siguientes detalles le ayudar?n a localizar los archivos que usted tendrá
que copiar en su propio producto. También le ayudar?n a proporcionar la
información correcta para crear sus propias directivas ZCML, clases Python, y
interfaces. Vea `Viewlet`_ para más información.

Ubicado en:

-   [locación de su huevo]/plone/app/layout/viewlets/
-   [locación de su
    huevo]/plone.app.layout-[version].egg/plone/app/layout/viewlets/

Nombre de la plantilla:contentactions_blank.pt & contentactions.ptNombre de
la clase:plone.app.layout.viewlets.common.ContentActionsViewletAdministrador:
plone.contentviews (nombre)
plone.app.layout.viewlets.interfaces.IContentViews (interfaz)
Ejemplos de archivos & directivas
~~~~~~~~~~~

Ponga una versión de contentactions_blank.pt & contentactions.pt en [su
paquete de tema]/browser/templates)

Cree su propia versión de la clase en [su paquete de tema]/browser/[su
modulo].py

::from plone.app.layout.viewlets.common import ContentActionsViewlet
    from Products.Five.browser.pagetemplatefile import
    ViewPageTemplateFile
    class [your class name](ContentActionsViewlet):
        render = ViewPageTemplateFile("[your template name]")


Conecte su viewlet [su paquete de tema]/browser/configure.zcml

::<browser:viewlet
        name="[your namespace].[your viewlet name]"
        manager="plone.app.layout.viewlets.interfaces.IContentViews"
        class=".[your module].[your class name]"
        layer=".interfaces.[your theme specific interface]"
        permission="zope2.View"
    />


En [su paquete de tema]/profiles/default/viewlets.xml

Oculte el viewlet original (si lo desea)

::<object>
        <hidden manager="plone.contentviews" skinname="[your skin
        name]">
            <viewlet name="plone.contentactions" />
        </hidden>


Inserte su nuevo viewlet en un administrador de viewlet

::    <order manager="plone.contentviews" skinname="[your skin name]"
               based-on="Plone Default">
            <viewlet name="[your namespace].[your viewlet name]"
                     insert-before="*" />
        </order>
    </object>



7.9.10. Tabla de contenidos
===========================

Proporciona un conjunto de marcadores en la página actual.

Notas:Activado por elemento de contenido en Edición >
Configuración.Fragmento:``<dl id="document-toc" class="portlet toc"
style="display: none"> ???
</dl>``CSS:portlets.cssNombre:plone.tableofcontentsTipo:`viewlet`_
Personalización a través de la Interfaz de Administración de Zope
--------------------------------------------------------------------

Uso:Configuración de sitio > Interfaz de Administración de Zope >
portal_view_customizationsIr a:plone.tableofcontents
Personalizando de su propio producto
------------------------------------

Los siguientes detalles le ayudar?n a localizar los archivos que usted tendrá
que copiar en su propio producto. También le ayudar?n a proporcionar la
información correcta para crear sus propias directivas ZCML, clases Python, y
interfaces. Vea `Viewlet`_ para más información.

Ubicado en:

-   [locación de su huevo]/plone/app/layout/viewlets/
-   [locación de su
    huevo]/plone.app.layout-[version].egg/plone/app/layout/viewlets/

Nombre de la plantilla:toc.ptNombre de la clase:plone.app.layout.viewlets.com
mon.TableOfContentsViewletAdministrador:plone.abovecontentbody (nombre)
plone.app.layout.viewlets.interfaces.IAboveContentBody (interfaz)
Ejemplos de archivos & directivas
~~~~~~~~~~~

Ponga una versión de toc.pt en [su paquete de tema]/browser/templates)

Cree su propia versión de la clase en [su paquete de tema]/browser/[su
modulo].py

::from plone.app.layout.viewlets.common import TableOfContentsViewlet
    from Products.Five.browser.pagetemplatefile import
    ViewPageTemplateFile
    class [your class name](TableOfContentsViewlet):
        render = ViewPageTemplateFile("[your template name]")


Conecte su viewlet [su paquete de tema]/browser/configure.zcml

::<browser:viewlet
        name="[your namespace].[your viewlet name]"
manager="plone.app.layout.viewlets.interfaces.IAboveContentBody"
        class=".[your module].[your class name]"
        for="Products.ATContentTypes.interface.IATDocument"
        layer=".interfaces.[your theme specific interface]"
        permission="zope2.View"
    />


En [su paquete de tema]/profiles/default/viewlets.xml

Oculte el viewlet original (si lo desea)

::<object>
        <hidden manager="plone.abovecontentbody" skinname="[your skin
        name]">
            <viewlet name="plone.tableofcontents" />
        </hidden>


Inserte su nuevo viewlet en un administrador de viewlet

::    <order manager="plone.abovecontentbody" skinname="[your skin name]"
               based-on="Plone Default">
            <viewlet name="[your namespace].[your viewlet name]"
                     insert-before="*" />
        </order>
    </object>



7.9.11. Presentación
=====================

Proporciona un enlace a una vista de presentación de un documento.

Notas:Disponible sólo para documentos El enlace de vista de presentación
puede ser activado o desactivado

-   a través de la Web: sobre un elemento individual (Edición >
    Configuración > Presentación )
o Configuración de sitio > Tipos (tipos para todo el sitio)
-   En su producto: profiles/default/types (por tipo)

Fragmento:``<p id="link-
presentation">...</p>``CSS:noneNombre:plone.presentationTipo:`viewlet`_
Personalización a través de la Interfaz de Administración de Zope
--------------------------------------------------------------------

Uso:Configuración de sitio > Interfaz de Administración de Zope >
portal_view_customizationsIr a:plone.presentation
Personalizando de su propio producto
------------------------------------

Los siguientes detalles le ayudar?n a localizar los archivos que usted tendrá
que copiar en su propio producto. También le ayudar?n a proporcionar la
información correcta para crear sus propias directivas ZCML, clases Python, y
interfaces. Vea `Viewlet`_ para más información.

Ubicado en:

-   [locación de su huevo]/plone/app/layout/presentation/
-   [locación de su
    huevo]/plone.app.layout-[version].egg/plone/app/layout/presentation/

Nombre de la plantilla:noneNombre de la clase:plone.app.presentation.Presenta
tionViewletAdministrador:plone.abovecontentbody (nombre)
plone.app.layout.viewlets.interfaces.IAboveContentBody (interfaz)
Ejemplos de archivos & directivas
~~~~~~~~~~~

Cree su propia versión de la clase en [su paquete de tema]/browser/[su
modulo].py

::from plone.app.presentation import PresentationViewlet
    from Products.Five.browser.pagetemplatefile import
    ViewPageTemplateFile

    class [your class name](PresentationViewlet):
        [your code here]


Conecte su viewlet [su paquete de tema]/browser/configure.zcml

::<browser:viewlet
        name="[your namespace].[your viewlet name]"
manager="plone.app.layout.viewlets.interfaces.IAboveContentBody"
        class=".[your module].[your class name]"
        for="Products.ATContentTypes.interface.IATDocument"
        layer=".interfaces.[your theme specific interface]"
        permission="zope2.View"
    />


En [su paquete de tema]/profiles/default/viewlets.xml

Oculte el viewlet original (si lo desea)

::<object>
        <hidden manager="plone.abovecontentbody" skinname="[your skin
        name]">
            <viewlet name="plone.presentation" />
        </hidden>


Inserte su nuevo viewlet en un administrador de viewlet

::    <order manager="plone.abovecontentbody" skinname="[your skin name]"
               based-on="Plone Default">
            <viewlet name="[your namespace].[your viewlet name]"
                     insert-before="*" />
        </order>
    </object>



7.9.12. Palabras clave
======================

Las categor?as (conocidas también como palabras clave / etiquetas / r?tulos)
que han sido asignadas al elemento.

Notas:Esto sólo aparecer? si algunas categor?as han sido asignadas mediante
Edición > Categor?as.Fragmento:``<div id="category" class="documentByLine">??
?</div>``CSS:public.cssNombre:plone.belowcontenttitle.keywordsTipo:`viewlet`_
Personalización a través de la Interfaz de Administración de Zope
--------------------------------------------------------------------

Uso:Configuración de sitio > Interfaz de Administración de Zope >
portal_view_customizationsIr a:plone.belowcontenttitle.keywords
Personalizando de su propio producto
------------------------------------

Los siguientes detalles le ayudar?n a localizar los archivos que usted tendrá
que copiar en su propio producto. También le ayudar?n a proporcionar la
información correcta para crear sus propias directivas ZCML, clases Python, y
interfaces. Vea `Viewlet`_ para más información.

Ubicado en:

-   [locación de su huevo]/plone/app/layout/viewlets/
-   [locación de su
    huevo]/plone.app.layout-[version].egg/plone/app/layout/viewlets/

Nombre de la plantilla:keywords.ptNombre de la
clase:noneAdministrador:plone.belowcontenttitle (nombre)
plone.app.layout.viewlets.interfaces.IBelowContentTitle (interfaz)
Ejemplos de archivos & directivas
~~~~~~~~~~~

Ponga una versión de keywords.pt en [su paquete de tema]/browser/templates)

Conecte su viewlet [su paquete de tema]/browser/configure.zcml

::<browser:viewlet
        name="[your namespace].[your viewlet name]"
manager="plone.app.layout.viewlets.interfaces.IBelowContentTitle"
        template="templates/[your template name].pt"
        layer=".interfaces.[your theme specific interface]"
        permission="zope2.View"
    />


En [su paquete de tema]/profiles/default/viewlets.xml

Oculte el viewlet original (si lo desea)

::<object>
        <hidden manager="plone.belowcontenttitle" skinname="[your
        skin name]">
            <viewlet name="plone.belowcontenttitle.keywords" />
        </hidden>


Inserte su nuevo viewlet en un administrador de viewlet

::    <order manager="plone.belowcontenttitle" skinname="[your skin name]"
               based-on="Plone Default">
            <viewlet name="[your namespace].[your viewlet name]"
                     insert-before="*" />
        </order>
    </object>



7.9.13. L?nea de fondo
=======================

La información "acerca de" (quien ha creado el elemento de contenido y cuando
fue la última vez que modific?).

Notas:Puede desactivar la línea de fondo para visitantes an?nimos.

-   a través de la Web: Configuración de sitio > Seguridad
-   En su producto: profiles/default/propertiestool.xml

Fragmento:``<div id="plone-document-byline" class="documentByLine">... </div>
``CSS:public.cssNombre:plone.belowcontenttitle.documentbylineTipo:`viewlet`_
Personalización a través de la Interfaz de Administración de Zope
--------------------------------------------------------------------

Uso:Configuración de sitio > Interfaz de Administración de Zope >
portal_view_customizationsIr a:plone.belowcontenttitle.documentbyline
Personalizando de su propio producto
------------------------------------

Los siguientes detalles le ayudar?n a localizar los archivos que usted tendrá
que copiar en su propio producto. También le ayudar?n a proporcionar la
información correcta para crear sus propias directivas ZCML, clases Python, y
interfaces. Vea `Viewlet`_ para más información.

Ubicado en:

-   [locación de su huevo]/plone/app/layout/viewlets/
-   [locación de su
    huevo]/plone.app.layout-[version].egg/plone/app/layout/viewlets/

Nombre de la plantilla:document_byline.ptNombre de la clase:plone.app.layout.
viewlets.content.DocumentBylineViewletAdministrador:plone.belowcontenttitle
(nombre)
plone.app.layout.viewlets.interfaces.IBelowContentTitle (interfaz)
Ejemplos de archivos & directivas
~~~~~~~~~~~

Ponga una versión de document_byline.pt en [su paquete de
tema]/browser/templates)

Cree su propia versión de la clase en [su paquete de tema]/browser/[su
modulo].py

::from plone.app.layout.viewlets.content import DocumentBylineViewlet
    from Products.Five.browser.pagetemplatefile import
    ViewPageTemplateFile
    class [your class name](DocumentBylineViewlet):
        render = ViewPageTemplateFile("[your template name]")


Conecte su viewlet [su paquete de tema]/browser/configure.zcml

::<browser:viewlet
        name="[your namespace].[your viewlet name]"
manager="plone.app.layout.viewlets.interfaces.IBelowContentTitle"
        class=".[your module].[your class name]"
        layer=".interfaces.[your theme specific interface]"
        permission="zope2.View"
    />


En [su paquete de tema]/profiles/default/viewlets.xml

Oculte el viewlet original (si lo desea)

::<object>
        <hidden manager="plone.belowcontenttitle" skinname="[your
        skin name]">
            <viewlet
            name="plone.belowcontenttitle.documentbyline" />
        </hidden>


Inserte su nuevo viewlet en un administrador de viewlet

::    <order manager="plone.belowcontenttitle" skinname="[your skin name]"
               based-on="Plone Default">
            <viewlet name="[your namespace].[your viewlet name]"
                     insert-before="*" />
        </order>
    </object>



7.9.14. Bloqueo
===============

Indica que el elemento de contenido est? bloqueado para su edición.

Fragmento:``<div id="plone-lock-status"
/>``CSS:public.cssNombre:plone.lockinfoTipo:`viewlet`_
Personalización a través de la Interfaz de Administración de Zope
--------------------------------------------------------------------

Uso:Configuración de sitio > Interfaz de Administración de Zope >
portal_view_customizationsIr a:plone.lockinfo
Personalizando de su propio producto
------------------------------------

Los siguientes detalles le ayudar?n a localizar los archivos que usted tendrá
que copiar en su propio producto. También le ayudar?n a proporcionar la
información correcta para crear sus propias directivas ZCML, clases Python, y
interfaces. Vea `Viewlet`_ para más información.

Ubicado en:

-   [locación de su huevo]/plone/locking/browser/
-   [locación de su
    huevo]/plone.locking-[version].egg/plone/locking/browser/

Nombre de la plantilla:info.ptNombre de la clase:plone.locking.browser.info.L
ockInfoViewletAdministrador:plone.abovecontent (nombre)
plone.app.layout.viewlets.interfaces.IAboveContent (interfaz)
Ejemplos de archivos & directivas
~~~~~~~~~~~

Ponga una versión de info.pt en [su paquete de tema]/browser/templates)

Cree su propia versión de la clase en [su paquete de tema]/browser/[su
modulo].py

::from plone.locking.browser.info import LockInfoViewlet
    from Products.Five.browser.pagetemplatefile import
    ViewPageTemplateFile
    class [your class name](LockInfoViewlet):
        render = ViewPageTemplateFile("[your template name]")


Conecte su viewlet [su paquete de tema]/browser/configure.zcml

::<browser:viewlet
        name="[your namespace].[your viewlet name]"
        manager="plone.app.layout.viewlets.interfaces.IAboveContent"
        class=".[your module].[your class name]"
        for="plone.locking.interfaces.ITTWLockable"
        layer=".interfaces.[your theme specific interface]"
        permission="zope2.View"
    />


En [su paquete de tema]/profiles/default/viewlets.xml

Oculte el viewlet original (si lo desea)

::<object>
        <hidden manager="plone.abovecontent" skinname="[your skin
        name]">
            <viewlet name="plone.lockinfo" />
        </hidden>


Inserte su nuevo viewlet en un administrador de viewlet

::    <order manager="plone.abovecontent" skinname="[your skin name]"
               based-on="Plone Default">
            <viewlet name="[your namespace].[your viewlet name]"
                     insert-before="*" />
        </order>
    </object>



7.9.15. Historial del flujo de trabajo
======================================

Un resumen de las transiciones de flujo de trabajo en el elemento actual de
contenido.

Fragmento:``<div class="reviewHistory" id="review-history">???</div>``CSS:aut
horing.cssNombre:plone.belowcontentbody.workflowhistoryTipo:`viewlet`_
Personalización a través de la Interfaz de Administración de Zope
--------------------------------------------------------------------

Uso:Configuración de sitio > Interfaz de Administración de Zope >
portal_view_customizationsIr a:plone.belowcontentbody.workflowhistory
Personalizando de su propio producto
------------------------------------

Los siguientes detalles le ayudar?n a localizar los archivos que usted tendrá
que copiar en su propio producto. También le ayudar?n a proporcionar la
información correcta para crear sus propias directivas ZCML, clases Python, y
interfaces. Vea `Viewlet`_ para más información.

Ubicado en:

-   [locación de su huevo]/plone/app/layout/viewlets/
-   [locación de su
    huevo]/plone.app.layout-[version].egg/plone/app/layout/viewlets/

Nombre de la plantilla:review_history.ptNombre de la clase:plone.app.layout.v
iewlets.content.WorkflowHistoryViewletAdministrador:plone.belowcontentbody
(nombre)
plone.app.layout.viewlets.interfaces.IBelowContentBody (interfaz)
Ejemplos de archivos & directivas
~~~~~~~~~~~

Ponga una versión de review_history.pt en [su paquete de
tema]/browser/templates)

Cree su propia versión de la clase en [su paquete de tema]/browser/[su
modulo].py

::from plone.app.layout.viewlets.content import WorkflowHistoryViewlet
    from Products.Five.browser.pagetemplatefile import
    ViewPageTemplateFile
    class [your class name](WorkflowHistoryViewlet):
        render = ViewPageTemplateFile("[your template name]")


Conecte su viewlet [su paquete de tema]/browser/configure.zcml

::<browser:viewlet
        name="[your namespace].[your viewlet name]"
manager="plone.app.layout.viewlets.interfaces.IBelowContentBody"
        class=".[your module].[your class name]"
        layer=".interfaces.[your theme specific interface]"
        permission="zope2.View"
    />


En [su paquete de tema]/profiles/default/viewlets.xml

Oculte el viewlet original (si lo desea)

::<object>
        <hidden manager="plone.belowcontentbody" skinname="[your skin
        name]">
            <viewlet
            name="plone.belowcontentbody.workflowhistory" />
        </hidden>


Inserte su nuevo viewlet en un administrador de viewlet

::    <order manager="plone.belowcontentbody" skinname="[your skin name]"
               based-on="Plone Default">
            <viewlet name="[your namespace].[your viewlet name]"
                     insert-before="*" />
        </order>
    </object>



7.9.16. Historial de contenido
==============================

Un resumen de las transiciones de flujo de trabajo e historia de versionado
en el elemento actual de contenido (esto remplaza el flujo de trabajo en
Plone 3.3).

Fragmento:``<div class="contentHistory" id="content-history">???</div>``CSS:a
uthoring.cssNombre:plone.belowcontentbody.contenthistoryTipo:`viewlet`_
Personalización a través de la Interfaz de Administración de Zope
--------------------------------------------------------------------

Uso:Configuración de sitio > Interfaz de Administración de Zope >
portal_view_customizationsIr a:plone.belowcontentbody.contenthistory
Personalizando de su propio producto
------------------------------------

Los siguientes detalles le ayudar?n a localizar los archivos que usted tendrá
que copiar en su propio producto. También le ayudar?n a proporcionar la
información correcta para crear sus propias directivas ZCML, clases Python, y
interfaces. Vea `Viewlet`_ para más información.

Ubicado en:

-   [locación de su huevo]/plone/app/layout/viewlets/
-   [locación de su
    huevo]/plone.app.layout-[version].egg/plone/app/layout/viewlets/

Nombre de la plantilla:content_history.ptNombre de la clase:plone.app.layout.
viewlets.content.ContentHistoryViewletAdministrador:plone.belowcontentbody
(nombre)
plone.app.layout.viewlets.interfaces.IBelowContentBody (interfaz)
Ejemplos de archivos & directivas
~~~~~~~~~~~

Ponga una versión de review_history.pt en [su paquete de
tema]/browser/templates)

Cree su propia versión de la clase en [su paquete de tema]/browser/[su
modulo].py

::from plone.app.layout.viewlets.content import ContentHistoryViewlet
    from Products.Five.browser.pagetemplatefile import
    ViewPageTemplateFile
    class [your class name](ContentHistoryViewlet):
        render = ViewPageTemplateFile("[your template name]")


Conecte su viewlet [su paquete de tema]/browser/configure.zcml

::<browser:viewlet
        name="[your namespace].[your viewlet name]"
manager="plone.app.layout.viewlets.interfaces.IBelowContentBody"
        class=".[your module].[your class name]"
        layer=".interfaces.[your theme specific interface]"
        permission="zope2.View"
    />


En [su paquete de tema]/profiles/default/viewlets.xml

Oculte el viewlet original (si lo desea)

::<object>
        <hidden manager="plone.belowcontentbody" skinname="[your skin
        name]">
            <viewlet name="plone.belowcontentbody.contenthistory"
            />
        </hidden>


Inserte su nuevo viewlet en un administrador de viewlet

::    <order manager="plone.belowcontentbody" skinname="[your skin name]"
               based-on="Plone Default">
            <viewlet name="[your namespace].[your viewlet name]"
                     insert-before="*" />
        </order>
    </object>



7.9.17. Acciones de documento
=============================

Los enlaces para impresión y RSS

Notas:Puede cambiar el orden, añadir o eliminar acciones individuales del
documento

-   a través de la Web: Configuración de sitio > Interfaz de
    Administración de Zope > portal_actions > document_actions
-   En su producto: profiles/default/actions.xml

Fragmento:``<div class="documentActions"> ??? </div>``CSS:public.cssNombre:pl
one.abovecontenttitle.documentactionsTipo:`viewlet`_
Personalización a través de la Interfaz de Administración de Zope
--------------------------------------------------------------------

Uso:Configuración de sitio > Interfaz de Administración de Zope >
portal_view_customizationsIr a:plone.abovecontenttitle.documentactionsPara
más información:`http://plone.org/documentation/kb/where-is-what/document-
actions`_
Personalizando de su propio producto
------------------------------------

Los siguientes detalles le ayudar?n a localizar los archivos que usted tendrá
que copiar en su propio producto. También le ayudar?n a proporcionar la
información correcta para crear sus propias directivas ZCML, clases Python, y
interfaces. Vea `Viewlet`_ para más información.

Ubicado en:

-   [locación de su huevo]/plone/app/layout/viewlets/
-   [locación de su
    huevo]/plone.app.layout-[version].egg/plone/app/layout/viewlets/

Nombre de la plantilla:document_actions.ptNombre de la clase:plone.app.layout
.viewlets.content.DocumentActionsViewletAdministrador:plone.belowcontentbody
(nombre)
plone.app.layout.viewlets.interfaces.IBelowContentBody (interfaz)
Ejemplos de archivos & directivas
~~~~~~~~~~~

Ponga una versión de document_actions.pt en [su paquete de
tema]/browser/templates)

Cree su propia versión de la clase en [su paquete de tema]/browser/[su
modulo].py

::from plone.app.layout.viewlets.content import DocumentActionsViewlet
    from Products.Five.browser.pagetemplatefile import
    ViewPageTemplateFile
    class [your class name](DocumentActionsViewlet):
        render = ViewPageTemplateFile("[your template name]")

Conecte su viewlet [su paquete de tema]/browser/configure.zcml

::<browser:viewlet
        name="[your namespace].[your viewlet name]"
manager="plone.app.layout.viewlets.interfaces.IBelowContentBody"
        class=".[your module].[your class name]"
        layer=".interfaces.[your theme specific interface]"
        permission="zope2.View"
    />

En [su paquete de tema]/profiles/default/viewlets.xml

Oculte el viewlet original (si lo desea)

::<object>
        <hidden manager="plone.belowcontentbody" skinname="[your skin
        name]">
            <viewlet
            name="plone.abovecontenttitle.documentactions" />
        </hidden>

Inserte su nuevo viewlet en un administrador de viewlet

::    <order manager="plone.belowcontentbody" skinname="[your skin name]"
               based-on="Plone Default">
            <viewlet name="[your namespace].[your viewlet name]"
                     insert-before="*" />
        </order>
    </object> '


7.9.18. Elementos relacionados
==============================

Los elementos relacionados al contenido

Notas:Este viewlet muestra enlaces a los elementos de contenido adicionales
seleccionados por el editor bajo la pestaña de
categorización.Fragmento:``<div class="relatedItems"> ??? </div>``CSS:public.
cssNombre:plone.belowcontentbody.relateditemsTipo:`viewlet`_
Personalización a través de la Interfaz de Administración de Zope
--------------------------------------------------------------------

Uso:Configuración de sitio > Interfaz de Administración de Zope >
portal_view_customizationsIr a:plone.belowcontentbody.relateditems
Personalizando de su propio producto
------------------------------------

Los siguientes detalles le ayudar?n a localizar los archivos que usted tendrá
que copiar en su propio producto. También le ayudar?n a proporcionar la
información correcta para crear sus propias directivas ZCML, clases Python, y
interfaces. Vea `Viewlet`_ para más información.

Ubicado en:

-   [locación de su huevo]/plone/app/layout/viewlets/
-   [locación de su
    huevo]/plone.app.layout-[version].egg/plone/app/layout/viewlets/

Nombre de la plantilla:document_relateditems.ptNombre de la clase:plone.app.l
ayout.viewlets.content.ContentRelatedItemsAdministrador:plone.belowcontentbod
y (nombre)
plone.app.layout.viewlets.interfaces.IBelowContentBody (interfaz)
Ejemplos de archivos & directivas
~~~~~~~~~~~

Ponga una versión dedocument_relateditems.pt en [su paquete de
tema]/browser/templates)

Cree su propia versión de la clase en [su paquete de tema]/browser/[su
modulo].py

::from plone.app.layout.viewlets.content import ContentRelatedItems
    from Products.Five.browser.pagetemplatefile import
    ViewPageTemplateFile
    class [your class name](ContentRelatedItems):
        render = ViewPageTemplateFile("[your template name]")

Conecte su viewlet [su paquete de tema]/browser/configure.zcml

::<browser:viewlet
        name="[your namespace].[your viewlet name]"
manager="plone.app.layout.viewlets.interfaces.IBelowContentBody"
        class=".[your module].[your class name]"
        layer=".interfaces.[your theme specific interface]"
        permission="zope2.View"
    />

En [su paquete de tema]/profiles/default/viewlets.xml

Oculte el viewlet original (si lo desea)

::<object>
        <hidden manager="plone.belowcontentbody" skinname="[your skin
        name]">
            <viewlet name="plone.belowcontentbody.relateditems"
            />
        </hidden>

Inserte su nuevo viewlet en un administrador de viewlet

::    <order manager="plone.belowcontentbody" skinname="[your skin name]"
               based-on="Plone Default">
            <viewlet name="[your namespace].[your viewlet name]"
                     insert-before="*" />
        </order>
    </object> '


7.9.19. Comentarios
===================

Proporciona una interfaz de comentarios.

Notas:Los comentarios pueden ser activados o desactivados

-   a través de la Web: en un elemento individual (Edición >
    Configuraciones > Permitir comentarios )
o Configuración de sitio > Tipos (tipos para todo el sitio)
-   En su producto: profiles/default/types (por tipo)

Fragmento:``<div class="discussion"> ???
</div>``CSS:public.cssNombre:plone.commentsTipo:`viewlet`_
Personalización a través de la Interfaz de Administración de Zope
--------------------------------------------------------------------

Uso:Configuración de sitio > Interfaz de Administración de Zope >
portal_view_customizationsIr a:plone.comments
Personalizando de su propio producto
------------------------------------

Los siguientes detalles le ayudar?n a localizar los archivos que usted tendrá
que copiar en su propio producto. También le ayudar?n a proporcionar la
información correcta para crear sus propias directivas ZCML, clases Python, y
interfaces. Vea `Viewlet`_ para más información.

Ubicado en:

-   [locación de su huevo]/plone/app/layout/viewlets/
-   [locación de su
    huevo]/plone.app.layout-[version].egg/plone/app/layout/viewlets/

Nombre de la plantilla:comments.ptNombre de la clase:plone.app.layout.viewlet
s.comments.CommentsViewletAdministrador:plone.belowcontent (nombre)
plone.app.layout.viewlets.interfaces.IBelowContent (interfaz)
Ejemplos de archivos & directivas
~~~~~~~~~~~

Ponga una versión de comments.pt en [su paquete de tema]/browser/templates)

Cree su propia versión de la clase en [su paquete de tema]/browser/[su
modulo].py

::from plone.app.layout.viewlets.comments import CommentsViewlet
    from Products.Five.browser.pagetemplatefile import
    ViewPageTemplateFile
    class [your class name](CommentsViewlet):
        render = ViewPageTemplateFile("[your template name]")


Conecte su viewlet [su paquete de tema]/browser/configure.zcml

::<browser:viewlet
        name="[your namespace].[your viewlet name]"
        manager="plone.app.layout.viewlets.interfaces.IBelowContent"
        class=".[your module].[your class name]"
        for="Products.CMFCore.interfaces.IContentish"
        layer=".interfaces.[your theme specific interface]"
        permission="zope2.View"
    />


En [su paquete de tema]/profiles/default/viewlets.xml

Oculte el viewlet original (si lo desea)

::<object>
        <hidden manager="plone.belowcontent" skinname="[your skin
        name]">
            <viewlet name="plone.comments" />
        </hidden>


Inserte su nuevo viewlet en un administrador de viewlet

::    <order manager="plone.belowcontent" skinname="[your skin name]"
               based-on="Plone Default">
            <viewlet name="[your namespace].[your viewlet name]"
                     insert-before="*" />
        </order>
    </object>



7.9.20. Anterior Siguiente
==========================

Proporciona la funcionalidad anterior/siguiente para una carpeta.

Notas:Active esto es una carpeta mediante Editar >
Configuraciones.Fragmento:``<div class="listingBar">???</div>``CSS:public.css
Nombre:plone.nextpreviousTipo:`viewlet`_
Personalización a través de la Interfaz de Administración de Zope
--------------------------------------------------------------------

Uso:Configuración de sitio > Interfaz de Administración de Zope >
portal_view_customizationsIr a:plone.nextprevious
Personalizando de su propio producto
------------------------------------

Los siguientes detalles le ayudar?n a localizar los archivos que usted tendrá
que copiar en su propio producto. También le ayudar?n a proporcionar la
información correcta para crear sus propias directivas ZCML, clases Python, y
interfaces. Vea `Viewlet`_ para más información.

Ubicado en:

-   [locación de su huevo]/plone/app/layout/nextprevious/
-   [locación de su
    huevo]/plone.app.layout-[version].egg/plone/app/layout/nextprevious/

Nombre de la plantilla:nextprevious.ptNombre de la clase:plone.app.layout.nex
tprevious.view.NextPreviousViewletAdministrador:plone.belowcontent (nombre)
plone.app.layout.viewlets.interfaces.IBelowContent (interfaz)
Ejemplos de archivos & directivas
~~~~~~~~~~~

Ponga una versión de nextprevious.pt en [su paquete de
tema]/browser/templates)

Cree su propia versión de la clase en [su paquete de tema]/browser/[su
modulo].py

::from plone.app.layout.nextprevious.view import NextPreviousViewlet
    from Products.Five.browser.pagetemplatefile import
    ViewPageTemplateFile
    class [your class name](NextPreviousViewlet):
        render = ViewPageTemplateFile("[your template name]")


Conecte su viewlet [su paquete de tema]/browser/configure.zcml

::<browser:viewlet
        name="[your namespace].[your viewlet name]"
        manager="plone.app.layout.viewlets.interfaces.IBelowContent"
        class=".[your module].[your class name]"
        layer=".interfaces.[your theme specific interface]"
        permission="zope2.View"
    />


En [su paquete de tema]/profiles/default/viewlets.xml

Oculte el viewlet original (si lo desea)

::<object>
        <hidden manager="plone.belowcontent" skinname="[your skin
        name]">
            <viewlet name="plone.nextprevious" />
        </hidden>


Inserte su nuevo viewlet en un administrador de viewlet

::    <order manager="plone.belowcontent" skinname="[your skin name]"
               based-on="Plone Default">
            <viewlet name="[your namespace].[your viewlet name]"
                     insert-before="*" />
        </order>
    </object>



7.9.21. Pie de página
======================

Contiene la información sobre los derechos de autor.

Fragmento:``<div id="portal-
footer">???</div>``CSS:public.cssNombre:plone.footerTipo:`viewlet`_
Personalización a través de la Interfaz de Administración de Zope
--------------------------------------------------------------------

Uso:Configuración de sitio > Interfaz de Administración de Zope >
portal_view_customizationsIr a:plone.footer
Personalizando de su propio producto
------------------------------------

Los siguientes detalles le ayudar?n a localizar los archivos que usted tendrá
que copiar en su propio producto. También le ayudar?n a proporcionar la
información correcta para crear sus propias directivas ZCML, clases Python, y
interfaces. Vea `Viewlet`_ para más información.

Ubicado en:

-   [locación de su huevo]/plone/app/layout/viewlets/
-   [locación de su
    huevo]/plone.app.layout-[version].egg/plone/app/layout/viewlets/

Nombre de la plantilla:footer.ptNombre de la
clase:noneAdministrador:plone.portalfooter (nombre)
plone.app.layout.viewlets.interfaces.IPortalFooter (interfaz)
Ejemplos de archivos & directivas
~~~~~~~~~~~

Ponga una versión de footer.pt en [su paquete de tema]/browser/templates)

Conecte su viewlet [su paquete de tema]/browser/configure.zcml

::<browser:viewlet
        name="[your namespace].[your viewlet name]"
        manager="plone.app.layout.viewlets.interfaces.IPortalFooter"
        template="templates/[your template name].pt"
        for="*"
        layer=".interfaces.[your theme specific interface]"
        permission="zope2.View"
    />


En [su paquete de tema]/profiles/default/viewlets.xml

Oculte el viewlet original (si lo desea)

::<object>
        <hidden manager="plone.portalfooter" skinname="[your skin
        name]">
            <viewlet name="plone.footer" />
        </hidden>


Inserte su nuevo viewlet en un administrador de viewlet

::    <order manager="plone.portalfooter" skinname="[your skin name]"
               based-on="Plone Default">
            <viewlet name="[your namespace].[your viewlet name]"
                     insert-before="*" />
        </order>
    </object>



7.9.22. Colof?n
================

Contiene enlaces a plone.org, etc.

Fragmento:`` <div id="portal-
colophon">???</div>``CSS:public.cssNombre:plone.colophonTipo:`viewlet`_
Personalización a través de la Interfaz de Administración de Zope
--------------------------------------------------------------------

Uso:Configuración de sitio > Interfaz de Administración de Zope >
portal_view_customizationsIr a:plone.colophon
Personalizando de su propio producto
------------------------------------

Los siguientes detalles le ayudar?n a localizar los archivos que usted tendrá
que copiar en su propio producto. También le ayudar?n a proporcionar la
información correcta para crear sus propias directivas ZCML, clases Python, y
interfaces. Vea `Viewlet`_ para más información.

Ubicado en:

-   [locación de su huevo]/plone/app/layout/viewlets/
-   [locación de su
    huevo]/plone.app.layout-[version].egg/plone/app/layout/viewlets/

Nombre de la plantilla:colophon.ptNombre de la
clase:noneAdministrador:plone.portalfooter (nombre)
plone.app.layout.viewlets.interfaces.IPortalFooter (interfaz)
Ejemplos de archivos & directivas
~~~~~~~~~~~

Ponga una versión de colophon.pt en [su paquete de tema]/browser/templates)

Conecte su viewlet [su paquete de tema]/browser/configure.zcml

::<browser:viewlet
        name="[your namespace].[your viewlet name]"
        manager="plone.app.layout.viewlets.interfaces.IPortalFooter"
        template="templates/[your template name].pt"
        for="*"
        layer=".interfaces.[your theme specific interface]"
        permission="zope2.View"
    />


En [su paquete de tema]/profiles/default/viewlets.xml

Oculte el viewlet original (si lo desea)

::<object>
        <hidden manager="plone.portalfooter" skinname="[your skin
        name]">
            <viewlet name="plone.colophon" />
        </hidden>


Inserte su nuevo viewlet en un administrador de viewlet

::    <order manager="plone.portalfooter" skinname="[your skin name]"
               based-on="Plone Default">
            <viewlet name="[your namespace].[your viewlet name]"
                     insert-before="*" />
        </order>
    </object>



8. ¿Dónde est? qu??
=======================

Cómo localizar las partes y piezas que usted necesita. Enlaces a ayudas
visuales útiles para la identificación de elementos de página, referencias a
la localización de su producto y directorios de huevos, diagramas de un huevo
de tema en el sistema de archivos.


8.1. ¿Dónde est? qu? en una página?
========================================

¿Cómo puede localizar a los archivos relacionados a un elemento de página
individual?

En este momento (de escribir esto), no hay una varita mágica incorporada para
apuntar a un elemento en una página Web de Plone y saber exactamente que
plantillas y código están involucrados en su creación. No obstante puede que
la haya pronto, y los aventureros gustar?an de explorar `Weblion's Gloworm
tool`_.

Si no est? listo para una aventura todavía, entonces hay una serie de buenos
tutoriales disponibles con diagramas y guías para dónde est? qu?.


Comprendiendo cómo CSS traza mapas a la página
------------------------------------------------

El proyecto Weblion tiene una página Wiki excelente para ayudarle con esto



-   `https://weblion.psu.edu/trac/weblion/wiki/PloneThreeWhereIsWhat`_



Firebug (producto adicional para Firefox), obviamente, es una herramienta
esencial para la inspección de código y CSS de una página.



-   ` http://www.getfirebug.com/`_




Elementos de página
--------------------

Los elementos de página son constantemente mencionados en Plone, así que una
vez que conozca el nombre de un ?rea de página, usted est? en buen camino
para localizar los archivos relevantes.

-   usted puede encontrar una clave visual para elementos de página en la
    sección Elementos de este manual
-   también encontrará un excelente resumen en el tutorial `What Controls
    What You See (¿Qué controla lo que se ve?)`_ en Plone.org
-   y un mapeo de los administradores de viewlet y portlet en `Weblion
    wiki`_





8.2. ¿Dónde est? mi Instancia Zope?
======================================

La ubicación de su instancia Zope depende del instalador de Plone o el
proceso de instalación que haya utilizado.


De Plone 3.1.2 en adelante
--------------------------

Buildout  En una instalación basada en Buildout, no tiene que preocuparse
mucho acerca de su instancia Zope. Si realmente quiere investigar encontrará
su instancia en [your buildout]/parts/instance. Sin embargo la mayoría de los
detalles clave (sus productos Plone, productos de terceros , y Data.fs) no se
alojan all?. Todos ellos están reunidos de varias partes de su sistema de
archivos por el archivo zope.conf que se genera cuando ejecuta Buildout.
Plone 3.1.1 o anteriores
------------------------

Instalador de Plone Los instaladores de Plone (aparte del Instalador
Universal de Plone 3.1 Universal) suele situar un directorio de instancia
Zope junto a los directorios de software Zope y Python. Así que por ejemplo,
una instalación estándar de Windows, localiza la instancia de Zope en
c:\Program Files\Plone 3\Data. En una Mac, llamar? "instance" y probablemente
será ubicada en una carpeta Plone en la carpeta de aplicaciones.
Sin embargo el instalador Universal de Plone 3.1, le dar? una instalación
basada en Buildout. Paquete de producto Plone Si ha instalado Zope usted
mismo, se le habrá pedido crear (por terminal) una instancia Zope, por lo que
debe tener una buena idea de dónde est? en el sistema.


8.3. ¿Dónde est? mi directorio de productos?
===============================================

Cómo localizar su directorio de productos. Esto varia de acuerdo al
instalador de Plone o el proceso de instalación que haya utilizado.

El directorio de productos es donde los productos 2.5 de viejo estilo se
ubican. Para encontrar este, primero tendrá que saber dónde est? su instancia
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

Productos que descarg? usted mismo Estos deberían estar en


-   [su buildout]/products.

If you find you haven't got a products directory there, then it is OK to
create one yourself.  Productos que le pidi? a Buildout que descargara Si le
pidi? buildout a Buildout que buscara algunos productos viejo-estilo,
entonces estos se ubicaran en


-   [su buildout]/parts/[nombre de directorio].

(Buildout también crear? el directorio y lo llamar? algo así como
"productdistros").
Plone 3.1.1 o anteriores
------------------------

Instalador de Plone y paquete de producto Plone  debería ser fácil de
localizar todos los productos (aquellos que pertenecen a la instalación de
núcleo de Plone y aquellos que se han descargado) en


-   [su instancia zope]/products

Sin embargo, si usted utiliza el Instalador Universal de Plone 3.1 su
instalación será basada en Buildout.


8.4. ¿Dónde se encuentra mi locación de Huevo?
=================================================

Es lo suficientemente fácil para Zope encontrar los huevos, más difácil para
humanos.


De Plone 3.1.2 en adelante
--------------------------

Productos Core (núcleo) de Plone Default Para los productos de núcleo
utilizados en el tema Plone Default, buildout tiene un directorio de huevos


-   [su buildout]/eggs

que es donde los huevos se ubican automáticamente cuando se instala Plone. Su
propio producto de tema Debido a que su propio producto de tema estar? bajo
desarrollo, esto estar? en un lugar distinto en su Buildout

-   [su buildout]/[zinstance|zeocluster|]/src

(Tenga en cuenta que para compartir huevos entre Buildouts puede especificar
una ubicación diferente para esto en un archivo buildout por defecto, revise
`buildout tutorial en plone.org`_ para más información).


Usando Omelette para obtener sus huevos rápidamente.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Es más o menos una navegación de arrastre a través de todos los huevos usados
por Plone. La receta de Omelette por David Glick crea una estructura de
directorio unificado de todos los paquetes de espacio de nombres, realizando
enlaces simb?licos a los contenidos, a través de Buildout. Instrucciones
completas y documentación sobre esto se puede encontrar aquí:

`http://pypi.python.org/pypi/collective.recipe.omelette`_

Una vez que haya ejecutado nuevamente Buildout con la receta de omelette, se
dar? cuenta que tiene una nueva sección aquí:

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
=========================================================

El huevo creado para usted por la plantilla paster de plone3_theme debe tener
un diseño de sistema de archivos muy similar a este diagrama.

Si el diagrama no funciona, consulte las siguientes páginas donde las
secciones del diagrama están combinadas con una explicación textual.

.. image:: images/your_theme_egg.gif
  :alt: su huevo de tema





8.6. Archivos para el skin
==========================

Estos archivos y directorios serán relevantes cuando se trabaja en la parte
del skin de su tema.

/skins/[su espacio de nombre de tema].[su espacio de tema]_custom_templates |
custom_images | styles Estos directorios formar?n las capas de skins. Sus
plantillas, imágenes, y hojas de estilo pueden ir aquí. Si usted pidi? por
esto, la plantilla de pegado plone3_theme proveer? una hoja de estilo en
blanco para sustituir los por defecto de Plone. /skins.zcml Cuando la
instancia de Zope arranca, esto convierte sus directorios en las capas de
skin. /profiles/default/skins.xml | cssregistry.xml | jsregistry.xml Cuando
su tema est? instalado en el sitio Plone, este configura la jerarqu?a de las
capas de skin, y registra sus hojas de estilo y JavaScript con los
registros

.. image:: images/your_theme_egg_skin.gif
  :alt: su huevo de tema; archivos del skin





8.7. Archivos para componentes
==============================

Estos archivos y directorios serán relevantes cuando se trabaja en la parte
de Componentes de su tema.

/browser/viewlet.py | viewlet.pt Un ejemplo de un componente viewlet
/browser/interfaces.py Esto se utiliza para crear su interfaz de tema (y
cualquier otra interfaz que pueda necesitar)
/profiles/default/viewlets.xml Utilice este archivo para ordenar sus viewlets
dentro de los administradores de viewlets /browser/configure.zcml Utilice
este archivo para conectar los componentes /browser/templates | styles Estos
directorios pueden usarse para plantillas, estilos, e imágenes. Usted tendrá
que registrar estos como directorios para recursos en configure.zcml.

.. image:: images/your_theme_egg_components.gif
  :alt: su huevo de tema; archivos de componentes





8.8. Archivos para configuración
=================================

Estos archivos y directorios serán relevantes cuando se trabaja en la parte
de Configuración de su tema.

/profiles/default/ Este directorio contiene el código XML para Generic Setup.
La plantilla paster plone3_theme le proporcionar? algunos archivos ya hechos;
para definir sus capas de skin, registrar sus hojas de estilo y JavaScript, y
ordenar los viewlets.
/profiles.zcml Cuando la instancia de Zope inicia, este archivo hace que el
perfil est? disponible para el uso de Generic Setup.

.. image:: images/your_theme_egg_config.gif
  :alt: su huevo de tema; archivos de configuración





8.9. Archivos para la instalación de su huevo
==============================================

Estos son los archivos y directorios necesarios para instalar el huevo en la
ruta de python y ponerlo a disposición en el arranque de Zope.

.. image:: images/your_theme_egg_egg_installation.gif
  :alt: su huevo de tema; archivos utilizados para la instalación de su
    huevo



8.10. Archivos para la instalación de su tema
==============================================

Estos son los archivos que se usan cuando se instala el producto de tema
mediante Configuración de sitio > Agregar/Quitar productos o Interfaz de
Administración de Zope > portal_quickinstaller

/profiles/default/ Generic Setup instalar? su perfil de tema cuando su tema
se haya instalado. import_steps.xml apunta a un "controlador" para pasos de
instalación los cuales no son parte a?n de Generic Setup o no pueden ser
expresados como XML. /setuphandlers.py Esto contiene el "controlador" para
pasos no gen?ricos de la instalación Generic Setup

.. image:: images/your_theme_egg_qi_installation.gif
  :alt: su huevo de tema; archivos utilizados por el quick installer



9. Ilustraciones
================

Las ilustraciones utilizadas en este manual; si desea mirar las fotos.


9.1. Elementos
==============

Fragmentos de imágenes de elementos de página individual


10. Tematización base-reglas
=============================

Una visión general de cómo aplicar un tema a un sitio con un enfoque de
transformación.


10.1. collective.xdv
==================================================================

La documentación collective.xdv se ha trasladado a su propia ?rea en la
sección de descargas del sitio Web de Plone.

`http://plone.org/products/collective.xdv/documentation`_

Referencias
===========

- `Plone Theme Reference`_.


.. _plone.net: http://plone.net/
.. _Products section: http://plone.org/documentation/products
.. _ guía de actualización: http://plone.org/documentation/manual/upgrade-guide (Guía de actualización de Plone)
.. _  : http://plone.org/documentation/manual/theme-reference/images/mindmap.gif/view
.. _estas herramientas las describiremos aquí:http://plone.org/documentation/manual/theme-reference/quick-start/sharpen/firefox-mozilla-ui-development-tools
.. _modo depuración/desarrollo: http://plone.org/documentation/manual/theme-reference/quick-start/sharpen/how-to-make-your-css-changes-take-effect-instantly
.. _proceso de sustituir el estilo del título de la página: http://plone.org/documentation/manual/theme-reference/quick-start/change-the-font-colours
.. _reemplazando la imagen del logotipo de Plone: http://plone.org/documentation/manual/theme-reference/quick-start/change-the-logo
.. _desarrollador web: http://chrispederick.com/work/firefox/webdeveloper/
.. _Aardvark: http://www.karmatics.com/aardvark/
.. _ColorZilla: https://addons.mozilla.org/firefox/271/
.. _FireBug: http://getfirebug.com/
.. _extensión x-ray de firefox: https://addons.mozilla.org/en-US/firefox/addon/1802?id=1802
.. _View formatted source: https://addons.mozilla.org/extensions/moreinfo.php?id=697
.. _View source with: https://addons.mozilla.org/firefox/394
.. _Web development bookmarklets: http://www.squarefree.com/bookmarklets/webdevel.html
.. _JavaScript Shell: http://www.squarefree.com/shell/
.. _JavaScript Development Environment: http://www.squarefree.com/jsenv/
.. _Mouseover DOM Inspector: http://slayeroffice.com/tools/modi/v2.0/modi_help.html
.. _Javascript Object Tree Favelet: http://slayeroffice.com/?c=/content/tools/js_tree.html
.. _favelet que combina la mayoría de [slayeroffice] favelets de desarrollo: http://slayeroffice.com/?c=/content/tools/suite.html
.. _profundidad en la sección de capas Skin: http://plone.org/documentation/manual/theme-reference/buildingblocks/skin/layers/precedence
.. _Plantillas y Componentes para página: http://plone.org/documentation/manual/theme-reference/page/css/overview
.. _Sección del viewlet del Logotipo: http://plone.org/documentation/manual/theme-reference/elements (Elementos de página)
.. _http://www.openplans.org/projects/ootb-plone-themes/summary: http://www.openplans.org/projects/ootb-plone-themes/summary
.. _          http://www.openplans.org/projects/deliverance/summary : http://www.openplans.org/projects/deliverance/summary
.. _          http://blog.repoze.org/setting-up-deliverance-screencast-20071025.html        : http://blog.repoze.org/setting-up-deliverance-screencast-20071025.html
.. _http://plone.org/products/textmate-support/:
    http://plone.org/products/textmate-support/
.. _http://dev.plone.org/collective/browser/textmate-support: http://dev.plone.org/collective/browser/textmate-support
.. _http://www.e-texteditor.com/: http://www.e-texteditor.com/
.. _http://docs.neuroinf.de/PloneBook/ch6.rst#conducting-syntax-checks: http://docs.neuroinf.de/PloneBook/ch6.rst#conducting-syntax-checks
.. _http://wiki.python.org/moin/PythonEditors: http://wiki.python.org/moin/PythonEditors
.. _            http://plone.org/documentation/how-to/developing-plone-with-eclipse-ide          : http://plone.org/documentation/how-to/developing-plone-with-eclipse-ide
.. _            http://plone.org/documentation/tutorial/debugging-plone-products-with-pida          : http://plone.org/documentation/tutorial/debugging-plone-products-with-pida
.. _http://www.wingware.com/: http://www.wingware.com/
.. _http://www.activestate.com/Products/komodo_ide/index.mhtml:
    http://www.activestate.com/Products/komodo_ide/index.mhtml
.. _CSS and JavaScript to Page section: http://plone.org/documentation/manual/theme-reference/page/css
.. _plone.reload: http://pypi.python.org/pypi/plone.reload/0.9
.. _Práctica 1: Cómo crear un producto de Tema de Plone 3 en el Sistema de archivos: http://plone.org/documentation/manual/theme-reference/tools/egg1/practical1 (Práctica 1: Cómo crear un producto de Tema de Plone 3 en el Sistema de archivos)
.. _Práctica 2: Cómo instalar su tema de Plone 3 usando buildout: http://plone.org/documentation/manual/theme-
    reference/tools/egg1/practical2 (Práctica 2: Cómo instalar su tema de Plone 3 usando Buildout)
.. _http://paster.joelburton.com/: http://paster.joelburton.com/
.. _instalar Paster y/o ZopeSkel: http://plone.org/documentation/how-to/how-to-create-a-plone-3-theme-product-on-the-filesystem/use-paster
.. _Guía rápida para los huevos Python: http://peak.telecommunity.com/DevCenter/PythonEggs
.. _Hatch Python Eggs (Huevos Python) con SetupTools: http://www.ibm.com/developerworks/library/l-cppeak3.html
.. _Comprensión y uso de GenericSetup en Plone: http://plone.org/documentation/tutorial/genericsetup
.. _Mejoras de GenericSetup: http://theploneblog.org/blog/archive/2007/06/21/genericsetup-improvements
.. _Aproveche AHORA el uso de GenericSetup y Tecnolog?as Z3: http://plone.org/documentation/tutorial/benefit-now-from-using-genericsetup-and-zope-3-technologies/?searchterm=benefit%20NOW
.. _Personalización para desarrolladores: http://plone.org/documentation/how-to/how-to-create-a-plone-3-theme-product-on-the-filesystem/plone.org/documentation/tutorial/customization-for-developers
.. _lea esta tutorial: http://plone.org/documentation/tutorial/customizing-main-template-viewlets
.. _Paster: http://plone.org/how-to/use-paster
.. _Zope Page Templates tutorial on plone.org (Tutorial de Plantillas de página Zope en plone.org): http://plone.org/documentation/tutorial/zpt/
.. _ZPT Reference on Zope.org (Referencia de ZPT en Zope.org): http://www.zope.org/Documentation/Books/ZopeBook/2_6Edition/AppendixC.stx
.. _Zope Page Template Tutorial on plone.org - Advanced Usage (Tutorial de Plantillas de página Zope en plone.org; uso avanzado): http://plone.org/documentation/tutorial/zpt/advanced-usage
.. _Plantillas y componentes para página: http://plone.org/documentation/manual/theme-reference/buildingblocks/page/templates
.. _útil introducción: http://plone.org/documentation/plone-2.5-user-manual/managing-content/folder-view/
.. _ The Zope Book (el Libro de Zope): http://www.zope.org/Documentation/Books/ZopeBook/current/ExternalTools.stx
.. _artículo WebDAV: http://www.zope.org/Documentation/Articles/WebDAV
.. _Emacs: http://www.gnu.org/software/emacs/
.. _cadaver: http://www.webdav.org/cadaver/
.. _Zope Book: http://www.zope.org/Documentation/Books/ZopeBook/
.. _Zope Corporation: http://www.zope.com/
.. _esta página en zope.org wiki: http://wiki.zope.org/zope2/REQUESTX
.. _http://www.python.org: http://www.python.org/
.. _the relevant chapter of the Zope Book: http://www.zope.org/Documentation/Books/ZopeBook/current/DTML.stx
.. _Zope Security Guide (Guía de Seguridad de Zope): http://www.zope.org/Documentation/Books/ZDG/current/Security.stx
.. _Zope Book: http://docs.zope.org/zope2/zope2book/source/index.html
.. _Zope Developers Community.: http://docs.zope.org/zope2/zope2book/source/Contributions.html
.. _Products.CMFPlone.browser.interfaces.IPlone: http://dev.plone.org/plone/browser/Plone/branches/3.2/Products/CMFPlone/browser/interfaces.py#L199
.. _The ATViewTutorial product: http://plone.org/documentation/manual/theme-reference/buildingblocks/skin/templates/customizing-at-templates/atviewtutorial.tgz
.. _[1]: http://plone.org/documentation/manual/theme-reference/buildingblocks/skin/templates/customizing-at-templates/what-makes-it-tick#ref1
.. _Archetypes Quick Reference Manual (Manual rápido de referencia para Arquetipos): http://plone.org/products/archetypes/documentation/manual/quickref
.. _RichDocument tutorial: http://plone.org/tutorial/richdocument
.. _[1]: http://localhost:8080/samplecontent/test-page#ref1
.. _[2]: http://localhost:8080/samplecontent/test-page#ref2
.. _http://plone.org/documentation/tutorial/working-with-css: http://plone.org/documentation/manual/tutorial/working-with-css
.. _haga clic aquí: http://www.evotech.net/blog/2007/06/introduction-to-firebug/
.. _creando productos personalizados: http://plone.org/documentation/manual/theme-reference/buildingblocks/skin/how-to/how-to-create-a-plone-3-theme-product-on-the-filesystem
.. _Austin Neon: http://www.austinneon.com/
.. _Capitulo 7 de la guía definitiva para Plone: http://docs.neuroinf.de/PloneBook/ch7.rst
.. _Componentes: http://plone.org/documentation/manual/theme-reference/buildingblocks/skin/components
.. _partes de componentes: http://plone.org/documentation/manual/theme-reference/buildingblocks/components/componentparts
.. _Five Tutorial on WorldCookery.com: http://worldcookery.com/files/ploneconf05-five/step2.html
.. _sección más adelante: http://plone.org/documentation/manual/theme-reference/buildingblocks/components/componentparts/interfaces
.. _http://apidoc.zope.org/++apidoc++/: http://apidoc.zope.org/++apidoc++/
.. _http://wiki.zope.org/zope3/ZCMLStyleGuide: http://wiki.zope.org/zope3/ZCMLStyleGuide
.. _Anatomía de un Viewlet: http://plone.org/documentation/manual/theme-reference/elements/viewlet/anatomy
.. _http://plone.org/documentation/tutorial/customization-for-developers/viewlets/: http://plone.org/documentation/tutorial/customization-for-developers/viewlets/
.. _Anatomy of a Portlet: http://plone.org/documentation/manual/theme-reference/elements/portlet/anatomy
.. _http://plone.org/documentation/how-to/override-the-portlets-in-plone-3.0/: http://plone.org/documentation/how-to/override-the-portlets-in-plone-3.0/
.. _http://plone.org/documentation/tutorial/customization-for-developers/portlet-renderers/: http://plone.org/documentation/tutorial/customization-for-developers/portlet-renderers/
.. _http://plone.org/documentation/how-to/adding-portlet-managers: http://plone.org/documentation/how-to/adding-portlet-managers
.. _sección de skin: http://plone.org/documentation/manual/theme-reference/buildingblocks/skin
.. _explicación técnica: http://plone.org/plone-developer-reference/patterns/views/
.. _armar una página: http://plone.org/documentation/manual/theme-reference/page
.. _Skin o Componentes?: http://plone.org/documentation/manual/theme-reference/buildingblocks/components/skinorcomponents
.. _Elementos: http://plone.org/documentation/manual/theme-reference/elements/elementsindex
.. _¿Dónde encontrar lo que usted necesita?: http://plone.org/documentation/manual/theme-reference/buildingblocks/components/locations (¿Dónde encontrar lo que usted necesita?)
.. _Elementos: http://plone.org/documentation/manual/theme-reference/elements
.. _http://wiki.python.org/moin/HowToEditPythonCode: http://wiki.python.org/moin/HowToEditPythonCode
.. _Si se siente valiente o quiere saber más, una introducción clara se puede encontrar aquí:: http://www.diveintopython.org/object_oriented_framework/defining_classes.html
.. _http://plone.org/documentation/tutorial/understanding-permissions/: http://plone.org/documentation/tutorial/understanding-permissions/
.. _gran discusión: http://www.openplans.org/projects/ootb-plone-themes/lists/ootb-plone-themes-discussion/archive/2008/05/1209686168874/forum_view
.. _¿Dónde est? qu??: http://plone.org/documentation/manual/theme-reference/whereiswhat/egglocation
.. _http://api.plone.org: http://api.plone.org/
.. _Understanding and Using Generic Setup on plone.org: http://plone.org/tutorial/genericsetup/exports-snapshots-and-comparisons
.. _Zope book: http://www.plope.com/Books/2_7Edition/SearchingZCatalog.stx
.. _The Definitive Guide to Plone: http://docs.neuroinf.de/PloneBook/ch11.rst#searching-and-categorizing-content
.. _Plantillas y el lenguaje de plantillas: http://plone.org/documentation/manual/theme-reference/page/buildingblocks/skin/templates
.. _http://plone.org/documentation/manual/archetypes-developer-manual/fields/fields-reference: http://plone.org/kb/manual/archetypes-developer-manual/fields/fields-reference
.. _http://plone.org/documentation/tutorial/richdocument/pil: http://plone.org/kb/tutorial/richdocument/pil
.. _Skin: http://plone.org/documentation/manual/theme-reference/page/buildingblocks/skin
.. _Skin o Componentes: http://plone.org/documentation/manual/theme-reference/page/buildingblocks/components/skinorcomponents
.. _ siguiente sección : http://plone.org/documentation/manual/theme-reference/page/css/resource-registries
.. _TALES: http://docs.zope.org/zope2/zope2book/source/AppendixC.html#tales-overview
.. _global template variables (variables globales de plantilla): http://plone.org/documentation/tutorial/zpt/global-template-variables/
.. _ dentro de ellas.: http://plone.org/documentation/how-to/cmf-expressions
.. _global template variables (variables globales de plantilla): http://plone.org/documentation/tutorial/zpt/global-template-variables
.. _ http://msdn.microsoft.com/en-us/library/ms537512.aspx: http://msdn.microsoft.com/en-us/library/ms537512.aspx
.. _Lea más acerca de las configuraciones de medios de CSS en w3.org: http://www.w3.org/TR/CSS21/media.html
.. _http://developer.mozilla.org/en/docs/Properly_Using_CSS_and_JavaScript_in_XHTML_Documents: http://developer.mozilla.org/en/docs/Properly_Using_CSS_and_JavaScript_in_XHTML_Documents
.. _ http://dean.edwards.name/packer/usage/: http://dean.edwards.name/packer/usage/
.. _Sección: Utilizando otra información sobre su sitio: http://plone.org/documentation/manual/theme-reference/page/otherinfo (Utilizando otra información sobre su sitio en una página)
.. _el modo de depuración: http://plone.org/documentation/kb/how-to-make-your-css-changes-take-effect-instantly
.. _Guía de actualización: http://plone.org/documentation/manual/upgrade-guide/version/upgrading-plone-3-x-to-4.0/updating-add-on-products-for-plone-4.0/no-more-global-definitions-in-templates
.. _jQuery: http://jquery.com/
.. _ Herramientas jQuery : http://flowplayer.org/tools/index.html
.. _http://api.jquery.com: http://api.jquery.com/
.. _plone.app.jquerytools: http://pypi.python.org/pypi/plone.app.jquerytools/
.. _Viewlet de presentación: http://plone.org/documentation/manual/theme-reference/elements/visibleelements/plone.presentation
.. _Acciones de contenido: http://plone.org/documentation/manual/theme-reference/elements/visibleelements/plone.contentactions
.. _                      http://plone.org/documentation/tutorial/customizing-main-template-viewlets/reordering-and-hiding-viewlets: http://plone.org/documentation/manual/tutorial/customizing-main-template-viewlets/reordering-and-hiding-viewlets
.. _Configuración: http://plone.org/documentation/manual/theme-reference/elements/buildingblocks/configuration
.. _GloWorm: http://plone.org/products/gloworm
.. _este artículo: http://plone.org/documentation/kb/customizing-main-template-viewlets/adding-a-viewlet/
.. _GloWorm: http://plone.org/documentation/products/gloworm
.. _http://plone.org/documentation/tutorial/where-is-what/portlets-1/: http://plone.org/documentation/tutorial/where-is-what/portlets-1/
.. _http://plone.org/products/plone/roadmap/203/ : http://plone.org/products/plone/roadmap/203/
.. _ Personalización de viewlets en main_template : http://plone.org/how-to/override-the-portlets-in-plone-3.0/.org/documentation/tutorial/customizing-main-template-viewlets
.. _plone.skip_links: http://plone.org/documentation/manual/theme-reference/elements/hiddenelements/plone.skip_links
.. _viewlet: http://plone.org/documentation/manual/theme-reference/elements/viewlet
.. _plone.htmlhead.title: http://plone.org/documentation/manual/theme-reference/elements/hiddenelements/plone.htmlhead.title
.. _plone.nextprevious.links: http://plone.org/documentation/manual/theme-reference/elements/hiddenelements/plone.nextprevious.links
.. _plone.links.favicon: http://plone.org/documentation/manual/theme-reference/elements/hiddenelements/plone.links.favicon
.. _plone.links.search: http://plone.org/documentation/manual/theme-reference/elements/hiddenelements/plone.links.search
.. _plone.links.author: http://plone.org/documentation/manual/theme-reference/elements/hiddenelements/plone.links.author
.. _plone.links.navigation: http://plone.org/documentation/manual/theme-reference/elements/hiddenelements/plone.links.navigation
.. _plone.analytics: http://plone.org/documentation/manual/theme-reference/elements/hiddenelements/plone.analytics
.. _plone.header: http://plone.org/documentation/manual/theme-reference/elements/structuralelements/plone.header
.. _plone.app.i18n.locales.languageselector:
    http://plone.org/documentation/manual/theme-reference/elements/visibleelements/plone.app.i18n.locales.languageselector
.. _plone.site_actions: http://plone.org/documentation/manual/theme-reference/elements/visibleelements/plone.site_actions
.. _plone.searchbox: http://plone.org/documentation/manual/theme-reference/elements/visibleelements/plone.searchbox
.. _plone.logo: http://plone.org/documentation/manual/theme-reference/elements/visibleelements/plone.logo
.. _plone.global_sections: http://plone.org/documentation/manual/theme-reference/elements/visibleelements/plone.global_sections
.. _plone.personal_bar: http://plone.org/documentation/manual/theme-reference/elements/visibleelements/plone.personal_bar
.. _plone.path_bar: http://plone.org/documentation/manual/theme-reference/elements/visibleelements/plone.path_bar
.. _plone.contentviews: http://plone.org/documentation/manual/theme-reference/elements/visibleelements/plone.contentviews
.. _plone.tableofcontents: http://plone.org/documentation/manual/theme-reference/elements/visibleelements/plone.tableofcontents
.. _plone.belowcontenttitle.keywords: http://plone.org/documentation/manual/theme-reference/elements/visibleelements/plone.belowcontenttitle.keywords
.. _plone.belowcontenttitle.documentbyline: http://plone.org/documentation/manual/theme-reference/elements/visibleelements/plone.belowcontenttitle.documentbyline
.. _plone.lockinfo: http://plone.org/documentation/manual/theme-reference/elements/visibleelements/plone.lockinfo
.. _plone.abovecontenttitle.documentactions: http://plone.org/documentation/manual/theme-reference/elements/visibleelements/plone.abovecontenttitle.documentactions
.. _plone.comments: http://plone.org/documentation/manual/theme-reference/elements/visibleelements/plone.comments
.. _plone.belowcontentbody.contenthistory: http://plone.org/documentation/manual/theme-reference/elements/visibleelements/plone.belowcontentbody.contenthistory
.. _plone.nextprevious: http://plone.org/documentation/manual/theme-reference/elements/visibleelements/plone.nextprevious
.. _plone.footer: http://plone.org/documentation/manual/theme-reference/elements/visibleelements/plone.footer
.. _plone.colophon: http://plone.org/documentation/manual/theme-reference/elements/visibleelements/plone.colophon
.. _plone.htmlhead.dublincore: http://plone.org/documentation/manual/theme-reference/elements/hiddenelements/plone.htmlhead.dublincore
.. _plone.htmlhead.kss-base-url: http://plone.org/documentation/manual/theme-reference/elements/hiddenelements/plone.htmlhead.kss-base-url
.. _plone.links.RSS: http://plone.org/documentation/manual/theme-reference/elements/hiddenelements/plone.links.RSS
.. _plone.belowcontentbody.relateditems: http://plone.org/documentation/manual/theme-reference/elements/visibleelements/plone.belowcontentbody.relateditems
.. _viewlet: http://plone.org/documentation/manual/theme-reference/elements/elements/viewlet
.. _http://plone.org/documentation/kb/the-search-box: http://plone.org/documentation/tutorial/where-is-what/the-search-box
.. _http://plone.org/documentation/kb/where-is-what/the-logo: http://plone.org/documentation/kb/where-is-what/the-logo
.. _http://plone.org/documentation/kb/where-is-what/the-navigation-tabs: http://plone.org/documentation/kb/where-is-what/the-navigation-tabs%27
.. _http://plone.org/documentation/kb/where-is-what/the-personal-bar: http://plone.org/documentation/kb/where-is-what/the-personal-bar%27
.. _http://plone.org/documentation/kb/where-is-what/the-path-bar: http://plone.org/documentation/kb/where-is-what/the-path-bar%27
.. _http://plone.org/documentation/kb/where-is-what/document-actions: http://plone.org/documentation/kb/where-is-what/document-actions%27
.. _Weblion's Gloworm tool: http://weblion.psu.edu/blog/esteele/gloworm-0-1-alpha1-now-available
.. _https://weblion.psu.edu/trac/weblion/wiki/PloneThreeWhereIsWhat: https://weblion.psu.edu/trac/weblion/wiki/PloneThreeWhereIsWhat
.. _          http://www.getfirebug.com/: http://www.getfirebug.com/
.. _What Controls What You See (¿Qué controla lo que se ve?): http://plone.org/documentation/tutorial/where-is-what/introduction
.. _buildout tutorial en plone.org: http://plone.org/documentation/tutorial/buildout/creating-a-buildout-defaults-file
.. _http://pypi.python.org/pypi/collective.recipe.omelette: http://pypi.python.org/pypi/collective.recipe.omelette
.. _http://plone.org/products/collective.xdv/documentation: http://plone.org/products/collective.xdv/documentation
.. _Anne Bowtell: http://plone.org/author/anneb
.. _chat rooms: http://plone.org/support/chat
.. _support forums: http://plone.org/support/forums
.. _Plone training sessions: http://plone.org/events/training
.. _plone-docs@lists.sourceforge.net: mailto:plone-docs@lists.sourceforge.net
.. _         : http://plone.org/ (Plone CMS, the open source content
    management system)
.. _Six Feet Up: http://www.sixfeetup.com/
.. _Downloads: http://plone.org/products
.. _Get Plone: http://plone.org/download
.. _Themes: http://plone.org/products?getCategories=themes
.. _Development tools: http://plone.org/products?getCategories=dev
.. _Authentication: http://plone.org/products?getCategories=auth
.. _Documentación: http://plone.org/documentation
.. _FAQs: http://plone.org/documentation/faq/
.. _Tutorial videos: http://plone.org/documentation/movies/
.. _Manuals: http://plone.org/documentation/manual
.. _Books: http://plone.org/documentation/books
.. _Error Reference: http://plone.org/documentation/error
.. _Sites using Plone: http://plone.net/sites
.. _Developers: http://dev.plone.org/plone
.. _Roadmap: http://dev.plone.org/plone/roadmap
.. _Report website issues: http://dev.plone.org/plone.org
.. _Latest changes: http://dev.plone.org/plone/timeline
.. _Browse source: http://dev.plone.org/plone/browser
.. _Community blogs: http://planet.plone.org/
.. _Plone Foundation: http://plone.org/foundation
.. _Donate: http://plone.org/foundation/foundation-donations
.. _Sponsors: http://plone.org/foundation/donors
.. _Meeting minutes: http://plone.org/foundation/meetings/minutes
.. _Current board: http://plone.org/team/FoundationBoard
.. _Foundation members: http://plone.org/foundation/members
.. _Apply for membership: http://plone.org/foundation/membership
.. _Contact: http://plone.org/foundation#contact
.. _Support: http://plone.org/support
.. _Commercial services: http://plone.net/providers
.. _Sector-specific forums: http://plone.org/support/for
.. _Region-specific forums: http://plone.org/support/region
.. _Local user groups: http://plone.org/support/local-user-groups
.. _Plone Theme Reference: http://plone.org/documentation/manual/theme-reference
