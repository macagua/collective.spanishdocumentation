.. -*- coding: utf-8 -*-

******************************
Creacion de un paquete de tema
******************************

Un tema de Plone es un conjunto de templates, imágenes, estilos y código
Python que dan la apariencia visual al sitio de Plone. Usualmente se le da
también el nombre de `skin`.

Plone utiliza dos mecanismos generales para definir los elementos de un tema:
skins de CMF y vistas de Python. 

Skins de CMF
============

El Content Management Framework (CMF) es un producto de Zope que forma parte
de las dependencias básicas de Plone. Un skin de CMF consiste en uno o mas
directorios que contienen los templates, scripts y recursos del sitio Plone.
El conjunto de directorios del skin esta ordenado por prioridad, del mas alto
al mas bajo. Para mostrar un recurso determinado del sitio, por ejemplo el
logotipo, Plone busca por nombre en todos los directorios del skin comenzando
con el de prioridad mas alta, hasta encontrar el primero que contenga el
nombre buscado.

Es posible incluir capas para el skin del sitio en un producto de Plone y
definir su prioridad como máxima, de tal manera que cualquier elemento de
Plone que se incluya en el producto tendrá precedencia sobre los de Plone o
cualquier otro producto que se encuentre mas abajo en la lista de capas.

Vistas y viewlets en Python
===========================

En los skins de CMF es posible colocar scripts de Python, pero estos están
restringidos en cuanto a utilización de librerías y acceso al sistema en
general. Es por eso que cuando se requiere un procesamiento mas complejo de
datos es mejor utilizar Python directamente y no a través del skin. Plone
tiene un mecanismo para generar paginas utilizando Python y opcionalmente un
template de ZPT, mediante vistas y viewlets.

Una vista es una clase de Python que usualmente se asocia con un template
para producir una pagina web. Un viewlet es un fragmento de HTML generado por
una clase de Python y un template, de manera similar a las vistas. La
diferencia es que los viewlets se integran en una estructura de pagina
definida por una serie de contenedores conocidos como `viewlet managers`,
mientras que las vistas son totalmente independientes.

Generacion del tema con paster
==============================

Un tema es un conjunto de skins, vistas y viewlets definidos dentro de un
paquete de Python. La manera mas fácil de crear uno es utilizar los templates
para paster del paquete ZopeSkel:

Lo primero que hacemos es mandar llamar el template plone3_theme, pasándole el
nombre del paquete que crearemos. El template utiliza una estructura de
directorios de dos niveles, por lo que hay que usar un nombre compuesto. Por
lo general, la primera parte del nombre define la `marca` o la categoría
general del paquete y la segunda parte el nombre "verdadero" del mismo. En
este ejemplo el nombre es `plonetheme.ejemplo`::

    $ paster create -t plone3_theme plonetheme.ejemplo
    Selected and implied templates:
      ZopeSkel#basic_namespace  A basic Python project with a namespace package
      ZopeSkel#plone            A project for Plone products
      ZopeSkel#plone3_theme     A theme for Plone 3

    Variables:
      egg:      plonetheme.ejemplo
      package:  plonethemeejemplo
      project:  plonetheme.ejemplo

A continuación, paster realiza algunas preguntas para personalizar la
generación del paquete. La primera es si deseamos contestar todas las
preguntas (all) o solo algunas (easy). Contestemos `all`::

    Expert Mode? (What question mode would you like? (easy/expert/all)?) ['easy']: all

Después nos pregunta el los nombres del paquete Namespace (primera parte del
nombre pasado al template) y el nombre del paquete (segunda parte). Como los
valores por omisión son los mismos que pasamos arriba, basta presiona la
tecla `enter`::

    Namespace Package Name (Name of outer namespace package) ['plonetheme']: 
    Package Name (Name of the inner namespace package) ['ejemplo']: 

A continuación necesitamos dar el nombre del skin que se mostrara en los
paneles de control de Plone para referirse a nuestro paquete::

    Skin Name (Name of the theme (human facing, added to portal_skins)) ['']: Tema de Ejemplo

La siguiente pregunta permite definir el skin base para el nuestro, desde
donde se copiaran todas las capas registradas, de manera que no sea necesario
para nosotros definir toda la lista. Usualmente usáramos la de Plone::

    Skin Base (Name of the theme from which this is copied) ['Plone Default']: 

Si queremos cambiar la apariencia visual del sitio totalmente, tal vez sea
aconsejable comenzar con hojas de estilos vacías. Si no lo hacemos así, las
hojas de estilos del sitio de Plone estarán activas y todas sus definiciones
afectaran la vista final del sitio. En este caso basta utilizar las de Plone,
por lo que se deja vacia la respuesta::

    Empty Styles? (Override default public stylesheets with empty ones?) [False]: 

El template puede incluir directamente en el código algunos comentarios
descriptivos sobre las operaciones que realiza, para ayudar al desarrollador a
comprender lo que esta sucediendo. Por defecto se incluirán dichos
comentarios::

    Include Documentation? (Include in-line documentation in generated code?) [True]: 

La versión del paquete se utiliza en el panel de control de Plone para mostrar
al usuario la versión instalada del producto::

    Version (Version number for project) ['1.0']: 

Después, se pide una corta descripción del tema::

    Description (One-line description of the project) ['An installable theme for Plone 3']: Tema de Ejemplo

Algunos temas requieren además de la apariencia visual modificar la
configuración del sitio de Plone, para lo que es necesario incluir un perfil
de generic setup::

    Register Profile (Should this package register a GS Profile) [True]: 

Las siguientes preguntas son para definir un perfil de registro para subir
el paquete a un repositorio como el Python Package Index::

    Long Description (Multi-line description (in ReST)) ['']: 
    Author (Name of author for project) ['']: Juan Perez
    Author Email (Email of author for project) ['']: jperez@ejemplo.com
    Keywords (List of keywords, space-separated) ['web zope plone theme']: 
    Project URL (URL of the homepage for this project) ['http://svn.plone.org/svn/collective/']: 
    Project License (Name of license for the project) ['GPL']: 

Finalmente, las ultimas dos preguntas siempre ocuparan los valores defecto::

    Zip-Safe? (Can this project be used as a zipped egg? (true/false)) [False]: 
    Zope2 Product? (Are you creating a product for Zope2/Plone or an Archetypes Product?) [True]:

