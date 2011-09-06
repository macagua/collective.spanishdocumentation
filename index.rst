=========================================
Documentación oficial de Plone en Español
=========================================

Esta sección intenta recoger todo la documentación que hasta el momento esta traducida al Español, como resultado de la iniciativa llamada *traducciones plone* creada en 2008 en el sitio CoActivate.org por miembros de la comunidad Plone Conosur. A continuación se listan los documentos traducidos hasta el momento:


Instalación de Plone
--------------------

Este sección se dedica a recopilar las diversas formas de instalación de Plone 
en diversos Sistemas operativos como Windows, OS X, Linux, BSD (distribución de 
software Berkeley) y prácticamente cualquier otra plataforma.

.. toctree::
   :maxdepth: 2

   instalando_plone



Uso de Plone
------------

Plone es un Sistema de gestión de contenidos muy completo y útil,
por lo que es muy importante conocerlo para poder tomar máxima ventaja de
estos CMS.  

En esta sección tenemos el tutorial traducción oficial a los manuales de usuario 
y administración de elementos de Plone.

.. toctree::
   :maxdepth: 2

   Manual de Usuario de Plone 3 <manual-usuario/plone3/index>


==========================
Mejores Practicas de Plone
==========================

Esta sección intenta recoger todo la documentación disponible en en Español, sobre las *Mejores Practicas de Plone*, esta es resultado de la iniciativa de *Carlos de la Guardia* que publica esta documentación en busca de promover la documentación en Español, desde entonces esta documentación es mantenida por miembros de la comunidad Plone Conosur. A continuación se listan los documentos traducidos hasta el momento:

Introducción
------------

Desarrollar un sitio con Plone requiere de la combinación de una serie de
tecnologías y conocimientos, desde HTML hasta desarrollo avanzado con Python.
A lo largo del tiempo, la comunidad de Plone ha ido experimentando y
adoptando diversas formas de trabajar un proyecto, las cuales hoy en día
pueden considerarse como las mejores practicas de desarrollo con Plone.

Algunas de estas practicas se refieren por supuesto a la programación con
Python y a la construcción de aplicaciones administración de contenido con
Plone, pero hay algunas otras que rebasan el ámbito de Plone y son útiles
para cualquier ambiente de desarrollo.

En este texto vamos a abordar una por una diversas practicas que consideramos
invaluables para el trabajo profesional con Plone. La intención es demostrar
la manera en que se integra un ambiente de desarrollo ideal para desarrollar
con Plone.

Además de las mejores practicas, conoceremos en detalle algunas de las
principales tecnologías de Zope y Plone.

En particular, conoceremos:

Python
------

Python es el lenguaje con el que están desarrollados tanto Zope como Plone,
por lo que es muy importante conocerlo para poder tomar máxima ventaja de
estos sistemas. Es imprescindible programar en Python para poder crear
productos y tipos de contenido para Plone.

En esta sección tenemos el tutorial oficial de Python, preparado por la
asociación de Python de Argentina y la fundación de Python.

.. toctree::
   :maxdepth: 2

   Tutorial de Python <python/python-tutorial/index>

Tutorial de Control de versiones
--------------------------------

Para tener un ambiente de desarrollo productivo, en especial cuando se
trabaje en equipo, es muy importante contar con un sistema de control de
versiones. Subversion es el utilizado por plone.org y el plone collective,
por lo que consideramos necesario conocerlo, aunque recientemente la
popularidad de sistemas distribuidos como Git y Mercurial ha aumentado.

.. toctree::
   :maxdepth: 2

   subversion

Buildout y setuptools
---------------------

Buildout es un sistema que permite definir ambientes de desarrollo
que pueden ser replicados, incluyendo dependencias y configuración. Buildout se apoya
fuertemente en setuptools, que permite instalar paquetes de Python a través
de Internet. Es recomendable utilizar buildout para cualquier proyecto de
Plone que se quiera emprender.

.. toctree::
   :maxdepth: 2

   setuptools
   buildout

Tecnologías de Zope
-------------------

Plone esta basado en el servidor de aplicaciones Zope y en un toolkit de
desarrollo de portales llamado CMF. Para trabajar con Plone es necesario
conocer diversas tecnologías provenientes de estos sistemas.

.. toctree::
   :maxdepth: 2

   zca/zca-es
   zpt
   zcatalog
   workflow
   gs

Temas varios de Plone
---------------------

Existen muchos temas importantes para el desarrollo con Plone, en esta
sección tocaremos algunos de ellos.

.. toctree::
   :maxdepth: 2

   productos
   policy
   tema
   minituts

Otros recursos
--------------

.. toctree::
   :maxdepth: 2

   links
   presentaciones


============================
Acerca de esta documentación
============================

Instrucciones acerca de esta documentación.

Obtener y compilar la documentación
-----------------------------------

El almacenamiento de este material está disponible en el servidor de Subversion
`"collective" <https://svn.plone.org/svn/collective/>`_ de los contribuyentes a 
Plone. Si usted tiene una credenciales en este servidor y desea convertirse en 
un colaborador ejecute el siguiente comando: ::

  $ svn co https://svn.plone.org/svn/collective/spanishdocs/buildout spanishdocs-buildout

Si usted no tiene las credenciales de acceso al repositorio SVN `"collective"
<https://svn.plone.org/svn/collective/>`_ de Plone o simplemente solo desea obtener 
y compilar esta documentación ejecute el siguiente comando: ::

  $ svn export http://svn.plone.org/svn/collective/spanishdocs/buildout spanishdocs-buildout

Crear entorno virtual de Python para reconstruir este proyecto: ::

  # aptitude install python-setuptools subversion
  # easy_install virtualenv
  # exit
  $ cd $HOME ; mkdir $HOME/virtualenv ; cd $HOME/virtualenv
  $ virtualenv --no-site-packages --python=/usr/bin/python sphinx
  $ cd -

Ahora puede generar la documentación de HTML, con los siguiente comandos: ::

  $ source virtualenv/sphinx/bin/activate
  (sphinx)$ cd spanishdocs-buildout/
  (sphinx)$ python bootstrap.py
  (sphinx)$ ./bin/buildout -vN
  (sphinx)$ ./bin/sphinx

Ahora se puede abrir ``spanishdocs-buildout/build/html/index.html`` desde 
su navegador Web favorito.

Para obtener la documentación en PDF : ::

  $ source virtualenv/sphinx/bin/activate
  (sphinx)$ cd ./spanishdocs-buildout/build
  (sphinx)$ make latex
  (sphinx)$ cd ./latex
  (sphinx)$ make all-pdf

Ahora se puede abrir ``spanishdocs-buildout/sphinx/build/latex/DocumentacionEspanolPlone.pdf`` 
con sus programas de visor de PDF favorito (Evince, Acrobat Reader, ...)


Reglas de redacción
-------------------

En primer lugar, debe aprender los `fundamentos de Sphinx
<http://sphinx.pocoo.org/contents.html>`_ que es un reStructuredText extendido.


Codificación
------------

Su editor debe codificar el texto en **utf-8** si le gusta lo que está leyendo. 
Si su editor de texto favorito no reconoce esta codificación 
(en la actualidad, eso es bien extraño), entonces cambie de editor de texto.

.. admonition::
   Truco

   Para ``vi``, ``emacs`` y algunos otros editores de texto soportan
   utf-8 de forma automática al abrir un archivo de Sphinx, el lugar en
   primera línea de la siguiente marca (como en este archivo)::

     .. -*- coding: utf-8 -*-


Desplazamientos y indentaciones
-------------------------------

El uso del carácter de tabulación en el texto fuente para las distintas
desplazamientos y indentaciones está **estrictamente prohibido**. Utilice siempre
espacios para este fin. Todos los editores de texto ofrecen opciones avanzadas
para insertar espacios al pulsar la tecla TAB. No tiene
excusa si es necesario.

Estilos de subrayado
--------------------

Sphinx y ReStructuredText no imponer estilo de subrayado para
diferentes niveles de secciones de un documento. Todo se deja a la discreción
editores. Para mantener la coherencia nosotros adoptamos la siguiente convención: ::

  ==============================================
  Titulo de capitulo (uno solo por cada archivo)
  ==============================================
  ...
  Sección del nivel 1
  ===================
  ...
  Sección del nivel 2
  -------------------
  ...
  Sección del nivel 3
  ...................
  ...
  Sección del nivel 4
  ~~~~~~~~~~~~~~~~~~~

No es necesario ni deseable ir más allá del nivel 4. Cuando la generación del 
documento allá completado, el nivel de las secciones básicas de un archivo
depende del nivel de anidamiento del archivo en la estructura general de
documento. Para generar el HTML, no es un problema, pero en LaTeX limita
la superposición de las secciones a 6 niveles.

Contribuciones SVN
------------------

Wow, estás contento con tu excelente trabajo. Y le gustaría compartirlo con
todo el mundo. Al igual que cuando "contribuidor" de código fuente, las pruebas
unitarias no deben mostrar ningún error, compruebe en primer lugar:

* Que el comando ``make html`` no genere ningún error o advertencia.
* Que su redacción no posea ningún error de ortografía.
* Los enlaces de hipertexto que se ha agregado o cambiado (glosario, enlaces
  externos explícitos, referencias a las secciones, ...) funcionan correctamente.

Imágenes
--------

Aparte de las capturas de pantalla - ¡Uy, lo siento - las capturas de pantalla!, 
las imágenes Sphinx se inserta en el documento debe ir acompañada de su versión
"Fuente" en un formato público interoperables, y para que el editor pueda abrir
el archivo fuente que este disponible. Las imágenes deben estar preferentemente en el formato
PNG.

Además, durante cada inserción o cambio de imagen, usted **debe**
verificar y ajustar si es necesario la representación PDF, a sabiendas de las limitaciones
la imagen a tamaño del papel final.

**Ejemplo :** ::

   .. gs-map.mm: imagen de mapa mental de los servicios de GenericSetup. Creado con FreeMind

   .. image:: gs-map.png

**Aplicaciones gráficas recomendadas**

Diagramas : `Graphviz <http://www.graphviz.org/>`_


Algunas de las herramientas recomendadas
----------------------------------------

Emacs : usted puede agregar a emacs el módulo `rst.el
<http://svn.berlios.de/svnroot/repos/docutils/trunk/docutils/tools/editors/emacs/rst.el>`_
que añade un par de comandos y la sintaxis de la documentación a los escritores 
simpatizantes de Sphinx y reStructuredText.

Traducciones de contenidos
--------------------------

Existe una serie de terminologías que debe conocer para entender el proceso de traducciones 

Herramientas CAT
    Según el termino `Herramientas CAT en Wikipedia <http://es.wikipedia.org/wiki/CAT>`_, es el término con el que se designa la traducción 
    realizada con ayuda de programas informáticos específicos; por ejemplo, los que crean y organizan memorias de traducción y los editores de 
    recursos interactivos de software de tipo textual, también llamados herramienta de localización.

Memorias de traducción    
    Según el termino `Memorias de traducción en Wikipedia <http://es.wikipedia.org/wiki/Memoria_de_traducción>`_, Las memorias de traducción son 
    almacenes compuestos de textos originales en una lengua alineados con su traducción en otra(s). Esta definición de memorias de traducción 
    coincide literalmente con una de las definiciones más aceptadas de corpus lingüístico de tipo paralelo (Baker, 1995). Por esto se puede 
    decir que las memorias de traducción son corpus paralelos.

Estándar TMX
    Según el `Estándar TMX en Wikipedia <http://es.wikipedia.org/wiki/TMX>`_, Acrónimo en inglés de Translation Memory eXchange. Este estándar 
    de XML es un DTD que sirve para el intercambio de memorias de traducción. Creado por el comité OSCAR (Open Standards for Container/Content 
    Allowing Re-use). Mediante la aplicación del formato TMX es más viable la colaboración en proyectos de traducción de personas o empresas 
    que usan Sistemas de traducción asistida diferentes seleccionadas en función de sus necesidades y preferencias. El formato TMX también 
    hace más fácil la migración de un sistema de traducción asistida a otro, lo que favorece la competitividad entre las tecnologías ofertadas 
    y el desarrollo constante de las mismas para marcar diferencias con respecto a sus competidores. Como otros estándares abiertos, este formato 
    se desarrolla con vistas a reducir los problemas de compatibilidad, impulsar la reutilización de los recursos lingüísticos, simplificar el
    intercambio de datos y estimular, de esta manera, la innovación tecnológica (Gómez, 2001).

Terminología
    Según el termino `Terminología en Wikipedia <http://es.wikipedia.org/wiki/Terminología>`_, La terminología es un campo de estudio
    interdisciplinario que se nutre de un conjunto específico de conocimientos conceptualizado en otras disciplinas (lingüística, ciencia 
    del conocimiento, ciencias de la información y ciencias de la comunicación). La palabra terminología se utiliza también para hacer 
    referencia tanto a la tarea de recolectar, describir y presentar términos de manera sistemática (la también llamada terminografía) 
    como al vocabulario del campo de una especialidad en particular.

Gestor de terminología
    Según el termino `Gestor de terminología en Wikipedia <http://es.wikipedia.org/wiki/Gestores_de_terminología>`_, Un gestor de terminología, 
    también llamado gestor de bases terminológicas, es un programa de software compuesto de una base de datos extensible que permite 
    la gestión —creación, extracción y modificación de los datos por parte de los usuarios.

Extractores de terminología
    Según el termino `Extractores de terminología en Wikipedia <http://es.wikipedia.org/wiki/Extractores_de_terminología>`_, son herramientas 
    que permiten la identificación y extracción de candidatos a términos de los textos explorados. Estas herramientas están abocadas 
    a generar material para las bases terminológicas y que requieren del análisis y evaluación del usuario para la inclusión definitiva 
    en la base de datos.

Glosarios
    Según el termino `Glosario en Wikipedia <http://es.wikipedia.org/wiki/Glosario>`_, Glosario (del latín glossarĭum) es un anexo que se agrega al 
    final de libros o enciclopedias, en donde se definen y comentan ciertos términos utilizados en dicho texto, con el fin de ayudar al 
    lector a comprender mejor los significados de algunas palabras.

Diccionario de tipo Especializados
    Según el termino `Diccionario en Wikipedia <http://es.wikipedia.org/wiki/Diccionario>`_, Se trata de diccionarios que están dedicados a palabras 
    o términos que pertenecen a un campo o técnica determinados como, por ejemplo, la informática, la jardinería, la ingeniería, la computación, 
    la genética, la heráldica, el lenguaje SMS, pesos y medidas o abreviaturas, etc. Proporcionan breve información sobre el significado 
    de tales palabras o términos. Pueden ser también diccionarios de idiomas en los que se indica la traducción a otra lengua o a otras 
    lenguas de las palabras o términos que incluyen.


Obtener y memorias de traducción
--------------------------------

El almacenamiento de las memorias de traducción disponibles para este material 
está disponible en el servidor de Subversion `"collective"
<https://svn.plone.org/svn/collective/>`_ de los contribuyentes 
a Plone. Si usted tiene una credenciales en este servidor y desea convertirse 
en un colaborador ejecute el siguiente comando: ::

  $ svn co https://svn.plone.org/svn/collective/spanishdocs/cat spanishdocs-omegat

Si usted no tiene las credenciales de acceso al repositorio SVN `"collective"
<https://svn.plone.org/svn/collective/>`_ de Plone o simplemente solo desea obtener 
y compilar esta documentación ejecute el siguiente comando: ::

  $ svn export http://svn.plone.org/svn/collective/spanishdocs/cat spanishdocs-omegat


Instalando OmegaT
-----------------

Para instalarlo debe ejecutar los siguientes comandos: ::

  $ wget http://ufpr.dl.sourceforge.net/project/omegat/OmegaT%20-%20Standard/OmegaT%202.3.0/OmegaT_2.3.0_Linux.tar.bz2
  $ tar -xjvvf OmegaT_2.3.0_Linux.tar.bz2 -C $HOME


Ejecutando OmegaT
-----------------

Para ejecutar OmegaT debe ejecutar el siguiente comando: ::

  $ $HOME/OmegaT/jre/bin/java -jar $HOME/OmegaT/OmegaT.jar &


Instalando diccionarios en OmegaT
---------------------------------

Debes cuidar los siguientes aspectos:

- Instalar diccionarios en Castellano, Español (ES) como se explica en este `articulo <http://traduccionymundolibre.com/2010/03/18/utilizar-diccionarios-y-glosarios-en-omegat/>`_.
- En sistema Unix/Linux debes tener configurado su **locales** de tu sistema operativo en Castellano, Español (ES), para que OmegaT habilite la comprobación ortográfica.


FAQ
---

**Pregunta :** He añadido una entrada del índice o un nuevo término en el glosario y
no se actualiza cuando compilo el documento.

**Respuesta :** El índice de Sphinx es a veces es desorientado y la gestión de la dependencia
a veces, mejor. Por lo tanto, todo se debe reiniciar ejecutando el comando ``make clean`` 
dentro del directorio ``spanishdocs-buildout/sphinx/build/``.

   
Índices y tablas
================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

