.. -*- coding: utf-8 -*-

==========================
Traducciones de contenidos
==========================

.. contents :: :local:

Términos básicos
================

Existe una serie de terminologías que debe conocer para entender el proceso de traducciones

.. glossary::

  Herramientas CAT
    Según el termino `Herramientas CAT en Wikipedia <http://es.wikipedia.org/wiki/CAT>`_, es el término 
    con el que se designa la traducción realizada con ayuda de programas informáticos específicos; por 
    ejemplo, los que crean y organizan memorias de traducción y los editores de recursos interactivos de 
    software de tipo textual, también llamados herramienta de localización.

  Memorias de traducción    
    Según el termino `Memorias de traducción en Wikipedia <http://es.wikipedia.org/wiki/Memoria_de_traducción>`_, 
    Las memorias de traducción son almacenes compuestos de textos originales en una lengua alineados con 
    su traducción en otra(s). Esta definición de memorias de traducción coincide literalmente con una de las
    definiciones más aceptadas de corpus lingüístico de tipo paralelo (Baker, 1995). Por esto se puede 
    decir que las memorias de traducción son corpus paralelos.

  Estándar TMX
    Según el `Estándar TMX en Wikipedia <http://es.wikipedia.org/wiki/TMX>`_, Acrónimo en inglés de Translation 
    Memory eXchange. Este estándar de XML es un DTD que sirve para el intercambio de memorias de traducción. 
    Creado por el comité OSCAR (Open Standards for Container/Content Allowing Re-use). Mediante la aplicación del
    formato TMX es más viable la colaboración en proyectos de traducción de personas o empresas que usan Sistemas 
    de traducción asistida diferentes seleccionadas en función de sus necesidades y preferencias. 

    El formato TMX también hace más fácil la migración de un sistema de traducción asistida a otro, lo que 
    favorece la competitividad entre las tecnologías ofertadas y el desarrollo constante de las mismas para 
    marcar diferencias con respecto a sus competidores. Como otros estándares abiertos, este formato se desarrolla 
    con vistas a reducir los problemas de compatibilidad, impulsar la reutilización de los recursos lingüísticos,
    simplificar el intercambio de datos y estimular, de esta manera, la innovación tecnológica (Gómez, 2001).

  Terminología
    Según el termino `Terminología en Wikipedia <http://es.wikipedia.org/wiki/Terminología>`_, La terminología 
    es un campo de estudio interdisciplinario que se nutre de un conjunto específico de conocimientos 
    conceptualizado en otras disciplinas (lingüística, ciencia del conocimiento, ciencias de la información y 
    ciencias de la comunicación). La palabra terminología se utiliza también para hacer referencia tanto a la 
    tarea de recolectar, describir y presentar términos de manera sistemática (la también llamada terminografía) 
    como al vocabulario del campo de una especialidad en particular.

  Gestor de terminología
    Según el termino `Gestor de terminología en Wikipedia <http://es.wikipedia.org/wiki/Gestores_de_terminología>`_, 
    Un gestor de terminología, también llamado gestor de bases terminológicas, es un programa de software compuesto 
    de una base de datos extensible que permite la gestión —creación, extracción y modificación de los datos por 
    parte de los usuarios.

  Extractores de terminología
    Según el termino `Extractores de terminología en Wikipedia <http://es.wikipedia.org/wiki/Extractores_de_terminología>`_, 
    son herramientas que permiten la identificación y extracción de candidatos a términos de los textos explorados. 
    Estas herramientas están abocadas a generar material para las bases terminológicas y que requieren del análisis y 
    evaluación del usuario para la inclusión definitiva en la base de datos.

  Glosarios
    Según el termino `Glosario en Wikipedia <http://es.wikipedia.org/wiki/Glosario>`_, Glosario (del latín 
    glossarĭum) es un anexo que se agrega al final de libros o enciclopedias, en donde se definen y comentan 
    ciertos términos utilizados en dicho texto, con el fin de ayudar al lector a comprender mejor los significados 
    de algunas palabras.

  Diccionario de tipo Especializados
    Según el termino `Diccionario en Wikipedia <http://es.wikipedia.org/wiki/Diccionario>`_, Se trata de 
    diccionarios que están dedicados a palabras o términos que pertenecen a un campo o técnica determinados como, 
    por ejemplo, la informática, la jardinería, la ingeniería, la computación, la genética, la heráldica, 
    el lenguaje SMS, pesos y medidas o abreviaturas, etc. Proporcionan breve información sobre el significado 
    de tales palabras o términos. Pueden ser también diccionarios de idiomas en los que se indica la traducción 
    a otra lengua o a otras lenguas de las palabras o términos que incluyen.
    

Obtener y memorias de traducción
================================

El almacenamiento de las memorias de traducción disponibles para este material 
está disponible en el servidor de Subversion `"collective"
<https://svn.plone.org/svn/collective/>`_ de los contribuyentes 
a Plone. Si usted tiene una credenciales en este servidor y desea convertirse 
en un colaborador ejecute el siguiente comando:

.. code-block:: sh

  $ svn co https://svn.plone.org/svn/collective/spanishdocs/cat spanishdocs-omegat

Si usted no tiene las credenciales de acceso al repositorio SVN `"collective"
<https://svn.plone.org/svn/collective/>`_ de Plone o simplemente solo desea obtener 
y compilar esta documentación ejecute el siguiente comando:

.. code-block:: sh

  $ svn export http://svn.plone.org/svn/collective/spanishdocs/cat spanishdocs-omegat


Acerca de OmegaT
================

Según Wikipedia `OmegaT <http://es.wikipedia.org/wiki/OmegaT>`_, es una herramienta de memoria de traducción, 
es decir, un programa CAT que registra equivalencias entre lenguas. Está herramienta pensada para ser utilizada 
por traductores profesionales. 

Sus características incluyen la segmentación personalizable utilizando expresiones regulares, memorias de traducción con 
coincidencia aproximada y búsqueda de material de referencia, coincidencia del glosario, coincidencia del diccionario, y 
en línea con la corrección ortográfica usa los diccionarios ortográficos de Hunspell.

Mas información en http://omegat.org/


Herramientas CAT en Python
==========================

Una de las mas maduras herramientas CAT es Virtaal la cual es una herramienta gráfica de traducción diseñada para unir 
potencia y facilidad de uso. Aunque la meta inicial se centra en la traducción de programas (localización o l10n), tenemos 
la intención de que también sirva como una herramienta para varios propósitos. Virtaal se construye sobre la poderosa API 
de Translate Toolkit.

Mas información en http://translate.sourceforge.net/wiki/es/virtaal/index

.. tip::
    La herramienta actual usado es OmegaT, se recomienda usarla si desea que sus contribuciones en traducciones se 
    apliquen directamente a los proyectos actuales de trabajo.

Instalando OmegaT
=================

Para instalarlo debe ejecutar los siguientes comandos:

.. code-block:: sh

  $ wget http://hivelocity.dl.sourceforge.net/project/omegat/OmegaT%20-%20Standard/OmegaT%202.5.5%20update%202/OmegaT_2.5.5_02_Linux.tar.bz2
  $ tar -xjvvf OmegaT_2.5.5_02_Linux.tar.bz2 -C $HOME


Ejecutando OmegaT
=================

Para ejecutar OmegaT debe ejecutar el siguiente comando:

.. code-block:: sh

  $ $HOME/OmegaT/jre/bin/java -jar $HOME/OmegaT/OmegaT.jar &


Instalando diccionarios en OmegaT
=================================

Debes cuidar los siguientes aspectos:

- Instalar diccionarios en Castellano, Español (ES) como se explica en este `articulo <http://traduccionymundolibre.com/2010/03/18/utilizar-diccionarios-y-glosarios-en-omegat/>`_.
- En sistema Unix/Linux debes tener configurado su **locales** de tu sistema operativo en Castellano, Español (ES), para que OmegaT habilite la comprobación ortográfica.


FAQ
===

**Pregunta :** ¿Por que usar OmegaT en ves de Virtaal?

**Respuesta :** La razones son muchas y están orientadas en dos aspectos principales que describo a continuación: 

**Productividad de trabajo**

  OmegaT debido a que es una herramienta con mas tiempo que Virtaal, el nivel de madures y estabilidad que ofrece hacen 
  el proceso de traducción mas productivo y ágil ya que todo lo tengo en una misma interfaz de usuario.

**Filosofía de gestión de proyectos**

  **OmegaT** le ofrece un mecanismo gestión de proyectos mas amigable al usuario, debido a que al crear un 
  proyecto usted puede: 
  
  * **Importar sus archivos a traducir** en el directorio "sources" del proyecto creado y el software 
    lo analiza, genera las segmentaciones de traducciones automáticamente y generar el archivo de memorias 
    de traducción al cual usted va a alimentar con sus traducciones.
  
  * **Gestionar los recursos de traducción** usted puede colocar sus glosarios de términos en el directorio 
    "glossary", esto es muy útil para mantener un estándar terminológico y opcionalmente puedes usar archivos 
    de diccionarios de glosarios o dialectos específicos para la corrección ortográfica ubicando estos en el 
    directorio "dictionary".
  
  * **Agilizar la traducción**, usando las memorias de traducción con coincidencia aproximada o exacta puede 
    marcar al diferencia en los tiempo de culminación de la traducción de documento extenso. Además del apoyo 
    de los glosarios terminológicos existe la posibilidad de usar traducciones automáticas generadas desde 
    maquinas de traducción desde los servicios en la Web como Google translate o Aperteium.
  
  * **Generación de documentos finales** en cualquier momento de su trabajo de traducción usted puede generar 
    los documentos traducidos en el mismo formato original, estoy es una funcionalidad genial debido a que por 
    lo general usted no le interesa cambiar el formato del documento en que se esta traduciendo y la herramienta 
    simplemente aplica sus cambios en la memoria de traducción.
  
  En cambios en **Virtaal** esta pensada para proyectos en los cuales los archivos están generados en formatos 
  de memoria de traducción TMX, catálogos .POT / .PO, entre otros. en base a estos formatos es que usted puede 
  hacer el trabajo de traducción y no genera los documentos finales debido a que no se basa en formatos 
  manipulables por seres humanos sino que las traducciones realizadas son generadas en formatos que tienen que 
  se procesadas por otros programas que se encargan de presentar estas traducciones en base a las configuraciones 
  de los *locales* del sistema operativo que lo esta ejecutando.
