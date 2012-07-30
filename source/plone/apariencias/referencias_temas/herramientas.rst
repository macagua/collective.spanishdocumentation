.. -*- coding: utf-8 -*-

.. _4_seccion:

Herramientas
============

Llegó el momento de afilar sus lapices. Herramientas de autor, poniendo su
sitio Plone en modo de depuración, cómo crear un producto de tema (para
trabajar en el sistema de archivos).


Herramientas de autor
---------------------

Si está trabajando con el sistema de archivos, puede usar cualquier editor de
texto para escribir las plantillas, archivos de configuración (xml, zcml) y
las pequeñas cantidades de códigos en Python que necesitará.

Usted puede encontrar los siguiente útil:


Soporte Zope/Plone TextMate
...........................

-   `http://plone.org/products/textmate-support/`_

-   `http://dev.plone.org/collective/browser/textmate-support`_


Tendrá que revisar esto en el collective svn; instrucciones de cómo hacer
esto pueden encontrarse en http://svn.plone.org. Además hay una versión para
Windows de Textmate (`http://www.e-texteditor.com/`_).


Revisando la sintaxis de plantillas
...................................

Una ruta rápida y sucia para encontrar que hay de malo con una plantilla que
haya escrito usted mismo, es personalizarla a través de la Interfaz de
Administración de Zope. Sin embargo usted también puede configurar su propia
revisión, para correrla antes de que instale una plantilla en su sitio:

-   `http://docs.neuroinf.de/PloneBook/ch6.rst#conducting-syntax-checks`_

esto es un poco complejo si no se siente cómodo con Python, pero vale la pena
el esfuerzo a largo plazo.


Editores de código Python
.........................

Algo un poco más avanzado que el Bloc de notas le dará el resaltado de código
para Python. Encontrará una lista completa aquí:

-   `http://wiki.python.org/moin/PythonEditors`_.


Entorno de Desarrollo Integrado
...............................

Si le apetece usar un IDE (Del inglés Integrated Development Environments),
tiene un montón de opciones, aunque estas están directamente orientadas al
desarrollo de Python más que a la escritura de plantillas para
personalización:

-   `http://plone.org/documentation/kb/developing-plone-with-eclipse`_
-   `http://plone.org/documentation/kb/debugging-plone-products-with-pida`_

Otros IDE incluyen Wing (`http://www.wingware.com/`_), BoaConstructor y
Komodo (`http://www.activestate.com/Products/komodo_ide/index.mhtml`_).


Modo de depuración
------------------

Es inevitable no hacer las cosas bien la primera vez, por lo que necesita
asegurarse de que su sitio está funcionando en modo de depuración.

Modo de depuración CSS
......................

Plone empaqueta todos su archivos CSS dentro de uno o dos archivos para
eficiencia mediante el uso de un registro de recurso (para más información de
cómo funciona revise la sección :ref:`CSS y JavaScript a la página <63_seccion>`). Es mucho más
fácil ver lo que está haciendo, si usted desactiva esta función cuando está
diseñando. Puede hacer lo mismo para JavaScript.

-   Vaya a la :menuselection:`Configuración del sitio --> Interfaz de Administración de Zope --> portal_css` o :menuselection:`Configuración del sitio --> Interfaz de Administración de Zope --> portal_javascripts`

-   Marque la casilla de verificación para depuración


Modo de depuración Zope
.......................

Si esta creando su propio producto de tema, se dará cuenta que es útil correr
Zope en modo de depuración. Esto se configura en el archivo zope.conf el cual
puede encontrar en /etc en su instancia Zope. simplemente quite el # de esta
linea: 

.. code-block:: cfg

    #debug-mode = on

si está utilizando buildout, puede configurarlo en buildout.cfg: 

.. code-block:: cfg

    [instance]
    debug-mode = on

Igualmente deberá reiniciar de tanto en tanto, aunque los cambios en la Skin
de su tema hechos sobre el sistema de archivo se actualizarán inmediatamente.

¿No puede ver sus cambios?
..........................

+-----------------+---------------------------------+------------------------------------+
| Cambios a....   |  A través de la Web             | En el Sistema de archivos          |
+=================+=================================+====================================+
| Componentes     | Debe verlos inmediatamente      | Reinicie Zope                      |
+-----------------+---------------------------------+------------------------------------+
| Skins           |  Debe verlos inmediatamente     | Ejecute Zope en modo de depuración |
+-----------------+---------------------------------+------------------------------------+
| Hojas de estilo | Cambie portal_css y             | Cambie portal_css y                |
| y JavaScript    | portal_javascripts a depuración | portal_javascripts a depuración    |
+-----------------+---------------------------------+------------------------------------+
|  Configuración  | Debe verlos inmediatamente      | Reinstale el producto con el quick |
|                 |                                 | installer (instalador rápido)      |
+-----------------+---------------------------------+------------------------------------+


Mensajes de error
.................

Plone trae un modulo de reporte de errores - PloneErrorReporting. Cuando
usted crea un sitio Plone, esta característica estará lista para instalarse

-   :menuselection:`Configuración del sitio --> Agregar/Quitar Productos`

Asegúrese de desinstalarla antes de ponga el sitio en modo de producción.


Evite reiniciar todo el tiempo
..............................

Si usted está haciendo un trabajo extenso componentes del sistema, pronto se
cansará de reiniciar Zope. `plone.reload`_ le ahorrará tiempo. Agreguelo a su
configuración de buildout como cualquier otro huevo, vuelva a ejecutar
buildout y verá que puede recargar su código a través de su navegador.


Sobre el Sistema de archivos: Creando un producto de Tema
---------------------------------------------------------

Si usted desea trabajar sobre el sistema de archivos, aquí está la magia que
necesita para sostenerse sobre un cimiento de archivos y códigos


Resumen
........

Si usted desea trabajar sobre el sistema de archivos, aquí está la magia que
necesita para sostenerse sobre un cimiento de archivos y códigos

Esta sección lo guiará a través del proceso requerido para crear su propio
tema en el sistema de archivos y la instalación de este en su propio sitio
Plone.

Las buena noticia es que usted mismo no tiene que escribir grandes cantidades
de código para crear el marco de su tema en el sistema de archivos, usted
puede usar un generador (Paster from ZopeSkel) para que haga el trabajo por
usted. Este le dará un directorio que contiene un conjunto previamente
preparado de directorios y archivos,que puede aumentar o reescribir con sus
propias personalizaciones.

-   En la sección :ref:`432_resumen_practica1`, usted usará el generador de 
    código para construir su cimiento. Esta práctica también le ayudará con 
    los archivos disponibles y sus respectivas funciones.

-   En la sección :ref:`433_resumen_practica2`, usted hará que este producto está 
    disponible para su sitio Plone con respecto a su instalación y uso.

.. _432_resumen_practica1:

Práctica 1: Cómo crear un producto de Tema de Plone 3 en el Sistema de archivos
................................................................................


Realice un jumpstart a su tema de desarrollo usando Paster
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La manera más rápida y eficiente de comenzar no es creando las carpetas de su
tema y asociando los archivos hechos desde cero, sino tomando ventaja del
generador de un producto el cual le creará el marco automáticamente para el
producto de tema, basado en las respuestas que proporcione a unas preguntas
interactivas.


Usando Paster a través de la Web
:::::::::::::::::::::::::::::::::

Nuevos usuarios se pueden sentir más cómodos usando una herramienta a través
de la web, que le permita generar un producto de tema. Una herramienta como
se encuentra en `http://paster.joelburton.com/`_. Es posible que desee hacer
referencia a parte de la información a continuación, para obtener más
detalles sobre lo que está sucediendo a medida que responde estas preguntas.


Usando Paster en su computadora local
:::::::::::::::::::::::::::::::::::::

Usuarios que se sienten más cómodos usando la línea de comandos, tienen la
tendencia a usar una herramienta llamada ZopeSkel las plantillas Paster que
contiene. ZopeSkel es una colección de plantillas PasteScript las cuales
pueden usarse para generar rápidamente Zope y Plone como buildouts, productos
de arquetipos, y lo que más nos interesa, temas de Plone.


Ubique o Instale Paster
:::::::::::::::::::::::

Para determinar si usted tiene Paster y ZopeSkel instalado, en la línea de
comandos pruebe con: 

.. code-block:: sh

    $ paster create --list-templates

o para verificar si Paster o ZopeSkel han sido instalados en el Python que
vino con su instalación Plone (de la versión 3.2 en adelante) 

.. code-block:: sh

    $ [ruta a su buildout]/python-[version]/paster create --list-templates


Si "plone3_theme" no está en la lista de plantillas disponibles, tendrá
entonces que :ref:`instalar Paster y/o ZopeSkel <skel_plone>`, como lo explica Daniel Nouri.

Cree su producto de Tema
::::::::::::::::::::::::

Si tiene Paster y ZopeSkel instalados, navegue al directorio donde le
gustaría crear su producto (nosotros recomendamos [your
buildout]/[zinstance|zeocluster/src]) y ejecute de la línea de comandos:

.. code-block:: sh

    $ paster create -t plone3_theme plonetheme.mytheme

o si tiene Paster en su instalación Plone:

.. code-block:: sh

    $ [ruta a su buildout]/python-[version]/paster create -t plone3_theme plonetheme.mytheme

Esto iniciará una serie de preguntas por el script de Paster. Las
predeterminadas son verdaderamente apropiadas para su primer tema, así en la
mayoría de los casos simplemente presione enter. este es un ejemplo del
resultado de una sesión interactiva.

.. code-block:: sh

    Selected and implied templates:
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
    Enter description (One-line description of the package) ['An installable theme for Plone 3.0']:
    Enter long_description (Multi-line description (in reST)) ['']:
    Enter author (Author name) ['Plone Collective']:
    Enter author_email (Author email) ['product-developers@lists.plone.org']:
    Enter keywords (Space-separated keywords/tags) ['web zope plone theme']:
    Enter url (URL of homepage) ['http://svn.plone.org/svn/collective/']:
    Enter license_name (License name) ['GPL']:
    Enter zip_safe (True/False: if the package can be distributed as a .zip file) [False]:


Usted no puede utilizar la tecla de "borrar" para corregir un error de
escritura durante la sesión interactiva. Si comente un error entonces
presione ctrl-c para detener el script y empiece nuevamente.


Opciones de Paster
******************

Algunas de estas preguntas requieren una explicación más detallada:

.. glossary::

  Enter namespace_package
    Es una buena practica si usa el namespace (espacio de nombres) "temaplone" para su tema. 
    Obviamente puede usar otros espacio de nombres, ("productos" puede ser otro), si tiene 
    una razón valida, sino, use "temaplone".

  Enter package
    El "package" (paquete) es simplemente el nombre en minúsculas de su producto de tema, 
    sin espacio o subguiones. 

  Enter skinname
    El "skinname" (nombreskin) es el nombre legible (alfabeto latino) para el nombre
    de su tema. Es adecuado usar espacios y mayúsculas

  Enter skinbase
    En la mayoría de los casos debería dejar esto como 'Plone Default'.

  Enter empty_styles
    Responder "True" (Verdad) tendrá como resultado que las stylesheets (hojas de estilo) 
    vacías se añadan a su producto, lo que sustituirá los archivos por defecto: base.css, 
    public.css, y portlets.css que están incluidos en cualquier sitio Plone que use el 
    skin "Plone Default". "False" (Falso) no agregará ninguna stylesheet vacía. Para 
    propósitos de esta practica le recomendamos introducir "False"

  Enter include_doc
    Responder "True" causará que la documentación en línea se agregue a los archivos 
    creados por ZopeSkel. Vale la pena hacer esto al menos una vez, como parte de la 
    documentación es bastante útil.

  Enter zope2product
    Responder "True" hará que el paquete se pueda utilizar como un huevo, listandose en la ZMI, 
    carpetas de skin se registrarán como capas con la herramienta de Skins ("portal_skins"), 
    y el perfil de Generic Setup (configuración genérica) para el producto se puede cargar a 
    través de la herramienta de Instalación ("portal_setup"). Estudiaremos esto más adelante,
    por ahora basta con decir que aquí siempre responderá "true" cuando quiera
    generar un tema de Plone.

  Enter zip_safe
    Quédese con el valor por defecto aquí.

  :ref:`Creando nuevos huevos y paquetes rápidamente con Paster <skel_python>`
    Cómo utilizar el comando Paster para crear nuevos paquetes con las apropiadas setuptools
    (herramientas de configuración) y diseños filesystem (archivos de sistema) huevo-compatible 
    e manera rápida y fácil.


Huevos Python, Instalación Genérica y Zope 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Notas informativas sobre los cambios entre Plone 2.5 y Plone 3.

Productos, en el lenguaje de Plone, son análogos a los módulos o extensiones
para otras aplicaciones. En el paso de Plone 2.5 a Plone 3, varios cambios
importantes se hicieron para la forma en que Plone manipula productos. En
primer lugar, algunos productos comenzaron a ser empaquetados como huevos
de Python, lo que los hizo más fáciles de administrar, distribuir e instalar.
En segundo lugar, los productos comenzaron a utilizar GenericSetup
(Instalación genérica) como medio para la instalación. Y en tercer lugar, los
productos incorporan cada vez más tecnologías Zope 3 (Z3) tales como vistas
del explorador.


Huevos Python
:::::::::::::

Un huevo python es simplemente un conjunto de archivos y directorios los
cuales constituyen un paquete de python. Estos huevos simplemente pueden
comprimirse, en tal caso aparecen como un sólo archivo \*.egg, o pueden
descomprimirse. Huevos poseen un concepto y función similar a archivos JAR de
Java.

Los huevos son instalados a través de los marcos setuptools, un proyecto
paralelo de Python Enterprise Application Kit (Peak: Kit de Aplicación de
Empresa de Python) que provee administración y distribución para paquete (y
dependencia).

Si está usando un control de versiones, querrá agregar \*.egg-info y \*.pyc a
los patrones ignorados en su instalación, para que los metadatos del huevo y
archivos python compilados no sean añadidos a su repositorio.

.. glossary::

  `Guía rápida para los huevos Python`_
    Un buen resumen de huevos y setuptools por la gente de PEAK.

  `Hatch Python Eggs (Huevos Python) con SetupTools`_
    David Metz revisa el marco de setuptools.


GenericSetup
::::::::::::

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
Quickinstaller, no obstante, asumiendo que un método para desinstalar está
presente.

Ya que nuestro producto de tema base utiliza GenericSetup para instalarse 
así mismo, en breve estaremos configurando archivos xml requeridos por la GS.

.. glossary::

  `Comprensión y uso de GenericSetup en Plone`_
    Aunque ya está un poco desactualizada, el tutorial de Rob Miller para GS sigue 
    siendo un recurso útil para la formación en GS.

  `Mejoras de GenericSetup`_
    Más información de Rob Miller sobre GS.

  `Aproveche AHORA el uso de GenericSetup y Tecnologías Z3`_
    ¡Impresione a su colegas utilizando GenericSetup y vistas Zope 3 eficientemente 
    y con mínimo esfuerzo! En este tutorial se muestra cómo agregar un nueva vista, 
    cómo usarla, cómo agregar un nuevo tipo de contenido y cómo conectar y relacionar todo.

Tecnología Zope 3
:::::::::::::::::

A pesar de cualquier confusión con cualquier versión número-inducida,
recuerde que Plone 3 funciona con Zope 2. Zope 3 es una versión
dramáticamente cambiada de Zope 2, y algunas funcionalidades de Zope 3 se han
trabajado (Backport) para que funcionen con Zope 2. Para un completa
explicación de las tecnologías Zope 3 involucradas, consulte este tutorial:

.. glossary::

  `Personalización para desarrolladores`_
    Un breve recorrido de las personalizaciones de Plone 3 por Martin Aspeli.


Anatomía de un producto de Tema en Plone
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Estructura del directorio y explicación de la funcionalidad de todos estos
archivos.

Asumiendo que usted haya creado su producto de tema con éxito, usted debería
tener una estructura de directorios que se ve más o menos así: 

.. code-block:: sh

    plonetheme.mytheme
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
:::::::::::::

.. glossary::

  docs/
    El directorio docs contiene instrucciones para instalación
    (INSTALL.txt),, archivos de licencia, y el desarrollo del ingreso
    (HISTORY.txt). 

  README.txt
    El archivo de texto de nivel-superior contiene la
    descripción en una-línea del producto que ingresó durante la sesión
    interactiva con ZopeSkel. Otros archivos README se encuentran contenidos por
    todo el producto.

Paquete Python
::::::::::::::

.. glossary::

  plonetheme/
    Este es un paquete espacio de nombres, que sirve para agrupar
    otros paquetes.

  mytheme/
    Este es nombre real de su tema, habitualmente el
    nombre del cliente o proyecto en el cual está trabajando.

  tests.py
    La evaluación de Python para nuestro paquete va aquí. Normalmente,
    los temas no tienen mucho código Python, por lo que no tienen que 
    hacer en el proceso de evaluación.

  version.txt
    La versión de nuestro producto. De igual manera esta información se 
    puede encontrar en /profiles/default/metadata.xml.

Huevo Python
::::::::::::

.. glossary::

  plonetheme.mytheme.egg-info/
    Los metadatos del huevo se almacenan aquí setup.cfg
    Este archivo de configuración contiene información que se
    utiliza para crear archivos de información de huevo.

  setup.py
    Si quisiéramos que setuptools maneje la instalación del paquete 
    y las dependencias, se podría instalar a través de 
    "python setup.py install" (pero por el momento, no lo haremos).

GenericSetup
::::::::::::

.. glossary::

  profiles.zcml
    Registro de perfiles GenericSetup apropiados.

  profiles/
    "Default" es el perfil de configuración actual (solamente un perfil 
    es automáticamente creado, pero otros pueden ser añadidos) Dentro de 
    nuestro perfil de configuración tenemos archivos XML los cuales le 
    comunican a GS cómo configurar archivos CSS (cssregistry.xml), 
    archivos Javascript (jsregistry.xml), capas skin (skins.xml), y 
    viewlets (viewlets.xml). Metadata.xml rastrea el número de versión del 
    producto y otros metadatos, import_steps.xml _____ y la presencia de 
    plonetheme.mytheme-various.txt le transmite a GS para que 
    busque setuphandlers.py por métodos adicionales.

Zope 3
::::::

.. glossary::

  plonetheme.mytheme-configure.zcml
    Este es el slug ZCML (Lenguaje de Marcado de Configuración Zope) el 
    cual deberá estar localizado en el etc/package-includes si nuestro 
    tema es instalado como un paquete Python (en nuestro caso no lo será).

  configure.zcml
    TODO
    
  skins.zcml
   Registrar capas skin (imágenes, estilos, plantillas) como vistas de
   directorios de filesystem (archivos de sistema)

  browser/
    TODO

Stylesheets (hojas de estilo), Plantillas y más
:::::::::::::::::::::::::::::::::::::::::::::::

Una vez que tenga el producto de tema posicionado, el próximo paso es
modificar las piezas que Plone le otorga, específicamente plantillas,
stylesheets, y viewlets.

.. glossary::

  Templates/
    Las plantillas de Plone, específicamente la main_template que
    controla el diseño del sitio Plone, puede ser tomada del directorio
    parts/plone/CMFPlone/skins/plone_templates. La mayoría de las plantillas que
    están contenidas aquí en 2,5 se han trasladado a huevos y son controladas por
    viewlets. Para modificar una plantilla en este directorio, cópielo a su
    producto de tema, dentro la carpeta skins/templates y haga sus modificaciones
    allá.

  Stylesheets/
    La stylesheets por defecto de Plone se pueden encontrar en su
    directorio buildout/parts/plone/CMFPlone/skins/plone_styles. Generalmente es
    recomendable crear stylesheet específicas para su producto de tema, ej.
    "mytheme.css" (donde "mytheme" es el nombre del produco de su tema), para
    luego tomar cualquier estilo relevante de las stylesheets de CMFPlone y
    personalizarlas en su propio producto, en vez de sustituir completamente las
    stylesheets de CMFPlone. La excepción aquí puede ser IEFixes.css, la cual
    posiblemente estará de acuerdo en mantener intacta como un sólo archivo, ya
    que explícitamente se le llama del main_template.

  Viewlets/
    Es una gran simplificación afirmar que con mayor frecuencia usted
    estará sustituyendo viewlets de huevos comúnmente denominados
    plone.app.layout, plone.app.portlets y plone.app.content. Esos viewlets,
    pueden encontrarse en su buildout/eggs/ en paquetes llamados
    "plone.app.layout[xx]," "plone.app.portlets[xx]," y "plone.app.content[xx],"
    donde [xx] es el número de versión. Cuando esos viewlets y sus respectivos
    códigos son modificados pertenecen en el directorio de su producto de tema
    browser/. Para más información de cómo trabajar con viewlets, `lea esta tutorial`_.

Si modifica plantillas de páginas, no necesitará reiniciar Zope para que los
cambios surtan efecto. Sin embargo, cambios a Python, XML o ZCML, si
requieren reiniciar.

  `Personalización para desarrolladores`_
    Un breve recorrido de las personalizaciones de Plone 3 por Martin Aspeli.

.. _433_resumen_practica2:

Práctica 2: Cómo instalar su tema de Plone 3 usando Buildout
............................................................


Instalando su producto de Tema de base-huevo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

En esta sección, examinaremos como instalar temas de base-huevo usando
buildout. En relación a Plone 3.1.2, todos los instaladores Plone crean un
buildout que contiene su instancia Plone. Al instalar o desarrollar temas,
buildout es muy recomendable.

 Para instalar el producto de tema creado en la práctica 1:

-   En primer lugar, si todavía no está ahí, copie su producto de tema a
    [your buildout]/[zinstance|zeocluster]/src (en el caso de que este
    directorio no exista, puede crearlo usted mismo)

-   Luego, usando un editor de texto, edite su buildout.cfg (lo
    encontrará en [your buildout]/[zinstance|zeocluster]) y agregue la
    siguiente información dentro del buildout, y secciones de ZCML. El
    archivo buildout.cfg real será mucho más largo que los fragmentos de
    código a continuación:

    .. code-block:: cfg
    
        [buildout]

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

-   Después de actualizar la configuración, detenga su sitio y ejecute el
    comando ''bin/buildout'', el cual actualizará su buildout.

-   Luego, reinicie su sitio y vaya a la página para "Configuración del
    sitio" en la interfaz de Plone y haga clic en el enlace "Add-on Products"
    (Agregar productos). El área de "Configuración del sitio" también se le
    conoce como plone_control_panel, ya que esta es la URL utilizada para
    acceder a "Configuración del sitio".

-   Elija el producto (Mi tema 1.0) seleccionando la casilla que aparece
    junto a ella y haga clic en el botón 'Instalar'.

.. note ::
    Puede que tenga que vaciar la caché del navegador Web para que surtan
    los efectos de la instalación del producto.


Desinstalando un producto de Tema
:::::::::::::::::::::::::::::::::

La deinstalación se puede hacer en la "Configuración del sitio" / en la
página "Add/Remove Products" (Agregar/remover productos) , pero sólo si usted
utilizá esta misma pantalla ('Add/Remove Products' screen) para la
instalación. No todos los temas se desinstalan correctamente, pero la
reinstalación del tema Plone Default generalmente soluciona cualquier
problema.


Formación: productos de Temas hechos por Terceros.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

En esta sección, revisaremos cómo instalar un tema de Plone que haya
descargado de Plone.org/products, PyPi, etc. También vamos a mostrar cómo se
puede distinguir entre un producto estilo-viejo de 2.5 de uno nuevo base-
huevo.

Hay dos tipos de productos de temas: nuevos **productos base-huevo** , y
viejos productos de tema que se encuentran en el **"magical Products
namespace" ("espacio de nombres mágico de productos")** . El tipo de producto
el tema con cual está trabajando determina los pasos que debe seguir para
instalar el tema. Ahora veamos cómo distinguir la diferencia entre ambos.


¿El producto es base-huevo o está en el namespace de Productos?
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Primero tenemos que entender el significado de base-huevo. Si el tema, cuando
se descomprime, es nombrado "plonetheme.loquesea", o si genera un tema nuevo
usando la receta :ref:`Paster <skel_python>` y responde "yes" a la pregunta "is this a Zope2
product" (¿Es este un producto Zope2?), pues su producto es base-huevo. O
incluso una manera más sencilla es saber si su carpeta root contiene
setup.py, si está el archivo entonces es un huevo. En un típico producto de
tema base-huevo, setup.py lucirá más o menos así. en donde el texto resaltado
es el nombre del huevo.

.. code-block:: python

    from setuptools import setup, find_packages

    version = '1.1'

    setup(name='webcouturier.icompany.theme',

    [...]

Si el producto parece como si hubiera sido creado mediante DIYPloneStyle 3.x
(ahora desactualizado), este está almacenado en namespace. También puede
constatar que está trabajando con un tema en Products namespace si no hay
setup.py en la carpeta root.


Instalando su producto base-huevo
:::::::::::::::::::::::::::::::::

Recomendamos usar buildout para instalar un producto base-huevo. Puede
decidir si quiere descargar el paquete usted mismo o dejar que buildout lo
haga por usted. En caso de la primera opción, siga las instrucciones en la
sección previa. Si desea dejar el tema de la descarga al buildout, la
configuración de este es más simple:

[configuration here]

Dependencias
************

Si otro paquete depende del huevo de tema o tiene su ZCML directamente, no es
necesario especificar nada en la configuración del buildout, ya que lo
detectará automáticamente. Esto se considera un tema más avanzado.
Igualmente, si el tema de huevo depende de otro producto, el buildout se
encargará de esto también.


Instalando un producto si se encuentra en los namespace de Productos 2.x
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Siempre que el producto de tema sea un tema más viejo de 3.x y que se
encuentra en el namespace de los Productos, todo lo que tiene que hacer es
localizar el producto de tema en el directorio del buildout "products/" y
reiniciar su instancia Zope. No hay necesidad de volver a ejecutar el
buildout, porque no hemos cambiado ningún código ZCML.

Entonces, después de que su Zope se ha reiniciado, vaya a la página de
"Configuración del sitio" en la interfaz de Plone y haga clic en el enlace
"Añadir/Eliminar productos". El área de "Configuración del sitio" también se
le conoce como plone_control_panel, ya que esta es la URL utilizada para
acceder a "Configuración del sitio".

Escoja el producto seleccionando la casilla que aparece junto a ella y haga
clic en el botón de instalar.

Temas más viejos en el namespace de Productos pueden aparecer dos veces en el
portal_quickinstaller, pero esto es un bug (error) que ha sido arreglado en
una versión más reciente de ZopeSkel. Usted puede ignorar el bug o
solucionarlo mediante la eliminación de esta línea de su archivo de producto
de tema configure.zcml para luego reiniciar su instancia Zope.

.. code-block:: xml

    <five:registerPackage package="." initialize=".initialize" />


.. note ::
    Puede que tenga que vaciar la caché del navegador Web para que surtan
    los efectos de la instalación del producto.


.. _http://plone.org/products/textmate-support/: http://plone.org/products/textmate-support/
.. _http://dev.plone.org/collective/browser/textmate-support: http://dev.plone.org/collective/browser/textmate-support
.. _http://www.e-texteditor.com/: http://www.e-texteditor.com/
.. _http://docs.neuroinf.de/PloneBook/ch6.rst#conducting-syntax-checks: http://docs.neuroinf.de/PloneBook/ch6.rst#conducting-syntax-checks
.. _http://wiki.python.org/moin/PythonEditors: http://wiki.python.org/moin/PythonEditors
.. _http://plone.org/documentation/kb/developing-plone-with-eclipse : http://plone.org/documentation/kb/developing-plone-with-eclipse
.. _http://plone.org/documentation/kb/debugging-plone-products-with-pida : http://plone.org/documentation/kb/debugging-plone-products-with-pida
.. _http://www.wingware.com/: http://www.wingware.com/
.. _http://www.activestate.com/Products/komodo_ide/index.mhtml: http://www.activestate.com/Products/komodo_ide/index.mhtml
.. _plone.reload: http://pypi.python.org/pypi/plone.reload/0.9
.. _http://paster.joelburton.com/: http://paster.joelburton.com/
.. _Guía rápida para los huevos Python: http://peak.telecommunity.com/DevCenter/PythonEggs
.. _Hatch Python Eggs (Huevos Python) con SetupTools: http://www.ibm.com/developerworks/library/l-cppeak3.html
.. _Comprensión y uso de GenericSetup en Plone: http://plone.org/documentation/kb/genericsetup
.. _Mejoras de GenericSetup: http://theploneblog.org/blog/archive/2007/06/21/genericsetup-improvements
.. _Aproveche AHORA el uso de GenericSetup y Tecnologías Z3: http://plone.org/documentation/kb/benefit-now-from-using-genericsetup-and-zope-3-technologies?searchterm=benefit%20NOW
.. _Personalización para desarrolladores: http://plone.org/documentation/kb/customization-for-developers
.. _lea esta tutorial: http://plone.org/documentation/kb/customizing-main-template-viewlets
