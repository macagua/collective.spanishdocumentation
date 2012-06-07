.. -*- coding: utf-8 -*-

.. _2_seccion:


Comienzo rápido
===============

El inicio, y algunas técnicas para que se familiarice con las cosas básicas

Resumen
-------

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

.. glossary::

En primer lugar afile sus lápices 
  Hay una serie de herramientas que facilitarán bastante el proceso de 
  tematización, :ref:`estas herramientas las describiremos aquí <221_firefox-mozilla-ui-development-tools>`. 
  Para ver sus personalizaciones tiene que asegurarse que está ejecutando su sitio 
  en :ref:`modo depuración/desarrollo <222_seccion>`.  
Ahora trate algunas personalizaciones de CCS
  Lo acompañaremos en el :ref:`proceso de sustituir el estilo del título de la página <23_seccion>`, 

  por medio de la personalización y edición del estilo de hoja ploneCustom.css 
  Todo esto se hace en línea a través-de-la-web vía la Interfaz de Administración 
  de Zope.

Por último remplace el logotipo
  Revisaremos y desplegaremos las técnicas de personalización y edición CCS 
  :ref:`reemplazando la imagen del logotipo de Plone <24_seccion>` con su propio logotipo.


Afilando sus lápices
--------------------

Breve recorrido de las herramientas que usted encontrará útiles.

.. _221_firefox-mozilla-ui-development-tools:

Herramientas de la UI (Interfaz de Usuario) de Firefox/mozilla
...............................................................

Firefox y mozilla tienen un conjunto de extensiones que realmente le pueden
ayudar en el trabajo de desarrollo en la Interfaz de Usuario. Un conjunto
básico es listado aquí.

La vieja y confiable opción de "ver código fuente" era antes el camino de
depurar html de mala apariencia. Ahora hay extensiones de mozilla/firefox que
resultan en un desarrollo html mucho más productivo. Un conjunto básico es
listado aquí para que se ponga al día.

.. glossary::

  Web developer
    La extensión `Web developer`_ agrega una barra de herramientas a su firefox 
    con casi todo lo que quiera hacer o saber. Información de CSS, validación, 
    cambio de tamaño para probar otras resoluciones de pantalla, conversión de 
    POSTs a GETs. **Algo esencial**.

  Aardvark
    Cuando se habilita `Aardvark`_ para una página, y pasa el cursor por un elemento 
    se muestra información de clase/identificación Por ejemplo al presionar la tecla 
    ``v`` se mostrará el código fuente del elemento donde está posado el cursor. 
    Comience el demo de su sitio y experimente con las funciones de teclas. 
    Es una herramienta elegante y ligera.

  ColorZilla
    `ColorZilla`_ es sorprendentemente útil. Hace lo que el nombre sugiere: provee un 
    selector de color que muestra el código hexadecimal del píxel por donde pase el cursor 
    en la barra de estado. Aún hay más: se muestra el tamaño de caja del elemento actual de 
    caja; mostrando el elemento, clase e identificación del elemento actual, y distancia entre 
    dos puntos. Todo en la barra de estado.

  FireBug
    `FireBug`_ muestra constantemente el número de errores que encuentre en su página. 
    Provechoso durante el desarrollo de encontrar clases CSS mal escritas o sentencias 
    defectuosas de javascript. También incluye una revisión de CSS y código fuente, 
    pero Aardvark tiende a ser un poco mejor para eso.

  X-ray
    La `extensión x-ray de firefox`_ es bastante beneficiosa para entender el diseño 
    del sitio Plone. Muestra las etiquetas, las identificaciones y clases en línea, 
    concibiéndole una sorprendente y buena idea de lo que está pasando tras bambalinas.

  View formatted source
    `View formatted source`_ le da una buena vista del código fuente de la página. 
    Más importante es que cuando pasa sobre una etiqueta desplegable, le muestra 
    la CSS que se usa para esa etiqueta. Y con múltiples archivos CSS (¿alguien con Plone?) 
    le muestra el orden en que estos son usados (y sobrescritos).

  View source with
    `View source with`_ le permite hacer clic derecho sobre cualquier área de texto 
    o vista de código fuente y seleccionar un programa para editarlo/verlo. Parecido 
    a ExternalEditor, pero sobre **cualquier** Área de texto. No es 100% orientada a 
    desarrolladores, pero igualmente útil para cambios pequeños y evaluación de archivos 
    CSS en la carpeta de skin por defecto. 

Otros tipos de gadgets (herramientas) útiles son los **bookmarklets** (marcadores).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dos fuentes de estos son http://squarefree.com y http://slayeroffice.com. Vea
para ejemplos:

.. glossary::

  Bookmarklets para desarrollo Web
    Los `Web development bookmarklets`_ proveen el mismo tipo de funcionalidad que la 
    barra de herramientas Web para desarrolladores. El `JavaScript Shell`_ y 
    el `JavaScript Development Environment`_ merecen ser mencionados.

  Mouse-over DOM (Modelo de Objetos del Documento) Inspector
    El `Mouseover DOM Inspector`_ , o abreviado MODI , es un favelet (también conocido 
    como bookmarklet) que le permite ver y manipular el DOM de una página web simplemente 
    posicionándose con el cursor sobre todo el documento.

  Javascript Object Tree Favelet
    El `Javascript Object Tree Favelet`_ sobrepondrá su documento actual con un elemento 
    DIV que contiene una lista contraída de todos los tipos de objetos javascript actualmente 
    referenciados por la página, desde funciones a cadenas de caracteres y booleanos y todo 
    aquello que este en el medio.

  Favelet Suite
    Esto es un `favelet que combina la mayoría de [slayeroffice] favelets de desarrollo`_ . 
    Cuando se invoca, un elemento DIV aparecerá en la esquina superior izquierda del navegador 
    Web con una lista de todos los favalets que se han mencionado. Simplemente haga clic en el 
    enlace para invocar el favalet.

.. _222_seccion:

¿Cómo hacer para que los cambios de CCS surtan efecto inmediatamente?
.....................................................................

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

2.  agregue "/manage" al URL para accesar a la ZMI (Interfaz de Administración de Zope) 

3.  Navegue a :menuselection:`ZMI --> portal_css`

En Plone 3:

1.  haga clic en la casilla de verificación para modo depuración/desarrollo

2.  haga clic en el botón Guardar

En Plone 4:

1.  asegúrese que la casilla de verificación para el modo desarrollo está
    confirmada; si usted inició la instancia de Zope en modo desarrollo, pues
    esta estará automáticamente confirmada.

2.  haga clic en el botón Guardar

Cuando haya finalizado con las modificaciones de CSS debería desactivar el
modo depuración/desarrollo, ya que este afecta el rendimiento de su sitio
Plone.

.. _23_seccion:

Cambiar los colores de fuente
-----------------------------

¿Cómo cambiar los colores de fuente?: un enfoque a través-de-la-web.

Aquí se presentarán algunas técnicas sencillas para la personalización del
CSS de Plone a través-de-la-web.

-   ¿Cómo encontrar los estilos que usted quiere cambiar?
-   ¿Cómo en sustituir estos estilos mediante el uso del estilo de hoja ploneCustom.css?

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
cómo poner su sitio en `modo depuración/desarrollo <222_seccion>`.


Encontrando los estilos que quiere cambiar
..........................................

-   Si todavía no tiene una página en su sitio Plone, agregue una,
    guárdela e inspecciónela en modo vista.
-   Use `Firebug`_, o alguna herramienta similar, para localizar el
    nombre de la clase del título de la página; en este caso es
    h1.documentFirstHeading.


Localizando la hoja de estilo ploneCustom.css
.............................................

Como algo natural, la hoja de estilo que se carga de último en cada página
Plone es ploneCustom.css. Usted puede ver esto si inspecciona la etiqueta de
encabezado HTML de su página usando Firebug. Si escarba un poco más,
probablemente encontrará que esta hoja de estilo está completamente vacía.
Según las reglas de precedencia de la Cascada CSS, cualquier estilo
especificado en esta hoja sustituirá esos estilos en la hoja precedente.
Entonces aquí tiene una "hoja en blanco" para sus propias personalizaciones.

El truco ahora es encontrar el archivo, para que está disponible para su
respectiva edición.

-   Para hacer la vida más sencilla, quizás quiera abrir una segunda
    pestaña o ventana de su navegador Web; luego puede retornar rápidamente a
    la primera pestaña para observar sus cambios.

-   Vaya a la :menuselection:`Configuración del sitio --> Interfaz de Administración de Zope --> portal_skins`

-   Use la opción de Buscar en las pestañas de la parte superior para
    encontrar ploneCustom.css:

-   Escriba *ploneCustom.css* en la caja "with ids:" y haga clic en
    buscar
    
-   Puede que obtenga más de un resultado, pero no es importante la que
    elija, sin embargo la mejor manera es escoger aquella opción que está
    marcada con un asterisco rojo.


Editando y Personalizando ploneCustom.css
.........................................

Cuando hace clic en ploneCustom.css se dará cuenta que no puede editarlo. El
próximo paso es poner ploneCustom.css en un lugar donde la edición sea
posible. Usted verá una opción de Personalizar justo arriba del área gris de
texto, haga clic en el botón de Personalización y verá que el estilo de hoja
se ha copiado automáticamente a portal_skins/custom.

Ahora ya es libre de editar el archivo a su gusto. Para cambiar el color de
los títulos de nuestra página, agregue: 

.. code-block:: css

  h1.documentFirstHeading {
    color: #0AAE95;
  }

y guarde.

Si usted instala Plone 4 con el tema Sunburst, el archivo ploneCustom.css
trae una serie de estilos pre-empaquetados comentados con los que puede
experimentar si desea. Usted puede sustituir los estilos de diseños para un
ancho fijo y modificar los colores de los enlaces.


Revocar sus cambios
...................

Usted cuenta con un par de opciones para revertir a la CSS original:

-   comente sus estilos en el ploneCustom.css; se aplica la sintaxis
    habitual de CSS para comentar

-   elimine (o si quiere mantener un registro de lo que hizo, entonces
    renombre) su versión de ploneCustom.css que encontrará aquí:

-   :menuselection:`Configuración de sitio --> Interfaz de Administración de Zope --> portal_skins --> custom`

-   puede escoger entre las opciones de eliminar o renombrar: trate de 
    renombrar ploneCustom.css.old
    
-   luego puede volver al comienzo del proceso para localizar y
    personalizar ploneCustom.css

Más información
...............

De hecho aquí ha encontrado dos tipos de personalización.

1.  El primero es un método estándar mediante el uso del orden de
    precedencia, la Cascada, para sobrescribir estilos CSS tal y como llegan
    al navegador Web.
2.  El segundo es un método específico de Plone/Zope para cambios en las
    mismas hojas de estilo mediante la colocación de estas en la carpeta
    predeterminada de portal_skins. Este método también pude ser usado con
    platillas y otros recursos, y es explicado con más 
    :ref:`profundidad en la sección de capas Skin <5242_seccion>` en este manual.

Técnicas más avanzadas que incluyen la incorporación de sus propias hojas de
estilo dentro de un producto de tema, son descritas posteriormente en este
manual.

Puede descubrir más acerca de cómo el CSS Registry (Registro CSS)
(portal_css) empaqueta los hojas de estilo para montarlos a la página en la
sección de :ref:`Plantillas y Componentes para página <63_seccion>` de este manual.

.. _24_seccion:

Cambiar el logotipo
-------------------

¿Cómo substituir el logotipo estándar de Plone con su propio logotipo?; un
enfoque a través-de-la-web.


Los fundamentos
...............

En Plone 3 y 4 el logotipo es simplemente una imagen que contiene un enlace a
la página de inicio (solamente hay una pequeña diferencia entre versiones, y
es que en Plone 3 se llama logo.jpg y en Plone 4 logo.png).

.. code-block:: html

    <a id="portal-logo" href="http://[your site]" accesskey="1">

        <img width="252" height="57" title="Plone" alt=""
             src="http://[your site]/logo.jpg"/>

    </a>

Si le parece bien este enfoque entonces no tendrá que cambiar el HTML ya que
todos los atributos en este fragmento se generan automáticamente. Siga las
instrucciones en la Sección 1: Cambiando la Imagen y su Título.

Si quiere hacer algún cambio pequeño en los estilos vaya a la Sección 2:
Cambiando el estilo de portal_logo.

Si prefiere montar su logotipo con un estilo diferente y necesita reescribir
el HTML, pues puede hacer esto a través de la personalización de la plantilla
del logotipo; siga las instrucciones en la Sección 3: Cambiando el HTML.


1. Cambiando la Imagen y su Título
..................................

La imagen del Logotipo: logo.jpg (Plone 3) logo.png (Plone 4). Se encuentra
en la carpeta plone_images en portal_skins. La manera más rápida de remplazar
esta imagen es simplemente subiendo su propia imagen y dándole el mismo
Nombre: 

-   Vaya a la ZMI (Interfaz de Administración de Zope) en 
    :menuselection:`Configuración del sitio --> Interfaz de Administración de Zope`
    
-   Luego a  :menuselection:`portal_skins --> plone_images`

-   Haga clic en logo.jpg (Plone 3) o logo.png (Plone 4) y después clic
    en el botón de Personalizar.

-   Ahora remplace la imagen haciendo clic en el botón de buscar y así
    escoger su propia imagen en su sistema de archivos

-   Edite el campo del título (esto asegurará que el atributo del título
    cambie en el HTML)

-   Guarde los cambios y actualice su navegador para observar los
    modificaciones en su sitio.

Enfoque alternativo (sólo Plone 3)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El nombre (ID: identificación) del logotipo está especificado en
base_properties (propiedades_básicas); una lista de valores útiles que en
Plone 3 se seleccionan y se usan en las hojas de estilo del tema de Plone por
defecto. Esto le da la posibilidad de subir su propia imagen de logotipo,
otorgarle cualquier nombre, y luego personalizar la base_properties con ese
nombre.

-   Vaya a la ZMI (Interfaz de Administración de Zope) en 
    :menuselection:`Configuración de sitio --> Interfaz de Administración de Zope`

-   Asegúrese de haber cambiado su CSS Registry (Registro CSS) a modo depuración 
    (:menuselection:`Configuración de sitio --> Interfaz de Administración de Zope --> portal_css`)

-   Vaya a :menuselection:`portal_skins --> custom` y escoja Image en la lista desplegable a la derecha

-   Escoja la imagen que quiera y le da una Identificación y un Título, ej.: ::

        ID (Identificación) = MyLogo.jpg
        Title (Título) = My Logo

-   Vaya a :menuselection:`portal_skins --> plone_styles`, haga clic base_properties y luego
    clic en el botón de Personalizar

-   En este momento tendrá una versión personalizada de base_properties
    en la carpeta predeterminada de portal_skins la cual puede cambiar si
    desea. Encuentre el campo logoName y reemplace el valor *logo.jpg* con la
    ID que le haya dado a su imagen (asegúrese de haber introducido a su ID
    una terminación .jpg o .gif, y recuerde que toma en cuenta la mayúsculas
    y minúsculas) por ejemplo: ::

        logoName = MyLogo.jpg

-   Guarde sus cambios y recargue o actualice su navegador Web

En Plone 4 base_properties sigue existiendo pero tiene un uso bastante
limitado.

.. note ::
    Note que cuando usted se devuelva a su base_properties personalizado en
    :menuselection:`portal_skins --> custom`, se verá como una carpeta vacía. Haga clic en la
    pestaña de propiedades para retornar a la lista de propiedades.


2. Cambiando el estilo de portal_logo
.....................................

No hay ningunos estilos definidos para *#portal-logo*, pero hay algunos para
*#portal-logo img* en basic.css. Investigue esto con Firebug, la extensión de
Firefox. El enfoque más simple es sustituir estos con su propios estilos en
ploneCustom.css.

-   Vaya a la ZMI (Interfaz de Administración de Zope) (:menuselection:`Configuración del
    sitio --> Interfaz de Administración de Zope`)
    
-   Como siempre asegúrese de estar en modo de depuración/desarrollo
    activado en el CSS Registry (Registro CSS) (:menuselection:`Configuración del
    sitio --> Interfaz de Administración de Zope --> portal_css`)
    
-   Haga clic en :menuselection:`portal_skins --> plone_styles --> ploneCustom.css`
    y luego en el botón de Personalizar.
    
-   Ahora tendrá una versión editable de ploneCustom.css en la carpeta
    predeterminada de portal_skins
    
-   Agregue su propios estilos aquí, y haga clic en guardar, y recargue o
    actualice su navegador Web para salvar los cambios

3. Cambiando el HTML
....................

El HTML para el logotipo es generado mediante logo.pt; una plantilla de
página parte del viewlet denominado plone.logo. Para personalizar esto a
través de la web, necesitará usar portal_view_customizations.

-   Vaya a portal_view_customizations en la ZMI (Interfaz de Administración de Zope) (:menuselection:`Configuración del sitio --> Interfaz de Administración de Zope --> portal_view_customizations`)

-   Haga clic en plone.logo en el botón de Personalizar

-   Ahora tendrá una plantilla que puede reescribir. Hemos resaltado los
    detalles importantes en la sección de teoría que está más adelante,
    mostrándole algunos ejemplos para que comience.

-   Guarde sus cambios y actualice o recargue su navegador Web para
    verlos

.. note ::
    si en algún momento quiere retornar y hacer más cambios, verá que
    plone.logo está resaltado en la lista portal_view_customizations, haga clic
    en él para editarlo. Si quiere quitar completamente sus personalizaciones use
    las pestaña de contenido de portal_view_customizations, marque la casilla al
    lado de su plantilla y haga clic en Eliminar.


La Teoría
~~~~~~~~~

Aquí esta la plantilla logo.pt. Está escrita en lenguaje de plantillas que
usa Plone - TAL (o ZPT). Es saludable aprender esto (y no toma mucho tiempo
en aprenderse) pero nos explicaremos a través de este ejemplo: 

.. code-block:: html

    <a metal:define-macro="portal_logo"
       id="portal-logo"
       accesskey="1"
       tal:attributes="href view/navigation_root_url"
       i18n:domain="plone">
        <img src="logo.jpg" alt=""
             tal:replace="structure view/logo_tag" />
    </a>

Primero tenemos la etiqueta del enlace:

Usted puede hacer caso omiso de *metal:define-macro="portal_logo"* esto
simplemente está conteniendo o envolviendo el código en algo que pueda ser
re-usado nuevamente si es necesario.

El detalle importante es *tal:attributes="href view/navigation_root_url"*,
este el código que proporciona su sitio URL al atributo href.

Aquí hay una variable mágica, *view/navigation_root_url* , que paciera haber
surgido de la nada. De hecho, *vista* es una colección de propiedades
computados por el viewlet plone.logo viewlet and seamlessly passed to the
logo.pt template. Aquí están las propiedades disponibles:

.. glossary::

  navigation_root_url
    Proporciona la URL de su sitio (podría ser potencialmente
    diferente si usted ha configurado un root de navegación distinta)

  logo_tag
    busca el nombre de la imagen del logotipo en base_properties,
    encuentra la imagen, determina sus dimensiones y título y convierte todo esto
    en una etiqueta de imagen HTML con los atributos apropiados. Revise
    nuevamente el enfoque alternativo en la Sección 1 de este Cómo hacer para más
    información en relación a base_properties.

  portal_title
    Busca y proporciona el título de su sitio

Ahora mire la etiqueta de imagen en la plantilla.

La clave aquí es *tal:replace="structure view/logo_tag"*. Esto significa que
la plantilla no cargará la etiqueta de imagen escrita aquí, sino que
**reemplazará todo** con la generada del viewlet plone.logo. Si usted no
quiere que esto pase, pues debería borrar esta linea.

.. note ::
    La *estructura* significa tratar el valor como HTML en lugar de una cadena de texto.


Ejemplo 1: Un título de texto corriente
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Aquí tiene una versión personalizada de la plantilla, usando
*view/portal_title* en vez de *view/logo_tag*, para darle un encabezado de
texto en su lugar (si ha usado Plone 2, esto le puede parecer familiar) 

.. code-block:: html

    <h1 metal:define-macro="portal_logo" 
        id="portal-logo">
       <a accesskey="1"
          tal:attributes="href view/navigation_root_url"
          tal:content="view/portal_title"
          i18n:domain="plone">
        </a>
    </h1>

Por supuesto que querrá proporcionar sus estilos propios, regrese a la
Sección 2 de este Cómo hacer para información de cómo definir estos en
ploneCustom.css. Puede ajustar este ejemplo para utilizar una técnica de
sustitución de imagen accesible en la CSS.


Ejemplo 2: Proporcionando su propia etiqueta de imagen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No tiene que utilizar logo_tag si no lo desea: 

.. code-block:: html

    <a metal:define-macro="portal_logo"
       id="portal-logo"
       accesskey="1"
       tal:attributes="href view/navigation_root_url"
       i18n:domain="plone">
        <img src="[My logo ID]" alt="[My Logo]"
             width="[My Width]" height="[My Height]"
             tal:attributes="title view/portal_title" />
    </a>

Obviamente necesitará subir su propio logotipo en la carpeta predeterminada
en portal_skins, revise las instrucciones en la Sección 1 de este Cómo hacer:


Más información
...................

-   En la sección Logotipo de la documentación de Plone hay más
    descripciones de Como hacer relacionados a métodos de personalización más
    avanzados.
    
-   Una mayor orientación sobre TAL y ZPT se puede encontrar en el
    tutorial de ZPT.
    
-   Si desea transferir los cambios al sistema de archivos en su propio
    producto de tema, a continuación, en las secciones siguientes de este
    manual de referencia, mostraremos un resumen de los archivos y plantillas
    que necesitará (:ref:`Sección del viewlet del Logotipo <7_seccion>`).


.. _Web developer: http://chrispederick.com/work/firefox/webdeveloper/
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
