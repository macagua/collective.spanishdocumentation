.. -*- coding: utf-8 -*-

==========================
Traducciones de contenidos
==========================

Términos básicos
----------------

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
en un colaborador ejecute el siguiente comando:

.. code-block:: sh

  $ svn co https://svn.plone.org/svn/collective/spanishdocs/cat spanishdocs-omegat

Si usted no tiene las credenciales de acceso al repositorio SVN `"collective"
<https://svn.plone.org/svn/collective/>`_ de Plone o simplemente solo desea obtener 
y compilar esta documentación ejecute el siguiente comando:

.. code-block:: sh

  $ svn export http://svn.plone.org/svn/collective/spanishdocs/cat spanishdocs-omegat


Instalando OmegaT
-----------------

Para instalarlo debe ejecutar los siguientes comandos:

.. code-block:: sh

  $ wget http://ufpr.dl.sourceforge.net/project/omegat/OmegaT%20-%20Standard/OmegaT%202.3.0/OmegaT_2.3.0_Linux.tar.bz2
  $ tar -xjvvf OmegaT_2.3.0_Linux.tar.bz2 -C $HOME


Ejecutando OmegaT
-----------------

Para ejecutar OmegaT debe ejecutar el siguiente comando:

.. code-block:: sh

  $ $HOME/OmegaT/jre/bin/java -jar $HOME/OmegaT/OmegaT.jar &


Instalando diccionarios en OmegaT
---------------------------------

Debes cuidar los siguientes aspectos:

- Instalar diccionarios en Castellano, Español (ES) como se explica en este `articulo <http://traduccionymundolibre.com/2010/03/18/utilizar-diccionarios-y-glosarios-en-omegat/>`_.
- En sistema Unix/Linux debes tener configurado su **locales** de tu sistema operativo en Castellano, Español (ES), para que OmegaT habilite la comprobación ortográfica.


