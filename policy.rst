*********************************************
Pasos para crear un producto de configuración
*********************************************

Se detallan los pasos para crear un producto de configuración y se describe
cada uno de los directorios y archivos importantes generados.

Un producto de configuración (policy product) incluye toda la configuración
general del sitio. Representa las reglas generales de manejo de sitios Plone
de una organización y puede incluir:

* Configuraciones del sitio y propiedades de navegación.
* Productos propios y de terceros que deben instalarse automáticamente con el
  sitio.
* Configuraciones de viewlets.
* Estructura inicial de contenido del sitio.
* Pasos adicionales a la instalación del producto, como creación de cuentas de
  usuarios y contenido personalizado.
* Portlets utilizados en el sitio.
* Workflows generales de la organización.

El primer paso para la creación del producto se hace utilizando el esqueleto
de paquete para Plone proporcionado por paster::

    $ paster create -t plone ejemplo.policy
    Selected and implied templates:
       ZopeSkel#basic_namespace A project with a namespace package
       ZopeSkel#plone                    A Plone project
    Variables:
       egg:        ejemplo.policy
       package: ejemplopolicy
       project: ejemplo.policy
    Enter namespace_package (Namespace package (like plone)) ['plone']: ejemplo
    el espacio de nombres se usa para poder agrupar varios paquetes bajo un
    mismo nombre
    Enter package (The package contained namespace package (like example))
    ['example']: policy
    el nombre del paquete en sí
    Enter zope2product (Are you creating a Zope 2 Product?) [False]: True
    <siempre debe ser True para funcionar en Zope 2>
    Enter version (Version) ['0.1']:
    <el número de versión que aparece en la sección de productos adicionales
    de Plone>
    Enter description (One-line description of the package) ['']:
    <este y los datos que siguen son para los metadatos del proyecto en el
    PyPI>
    Enter long_description (Multi-line description (in reST)) ['']:
    Enter author (Author name) ['Plone Foundation']:
    Enter author_email (Author email) ['plone-developers@lists.sourceforge.net']:
    Enter keywords (Space-separated keywords/tags) ['']:
    Enter url (URL of homepage) ['http://svn.plone.org/svn/plone/plone.example']:
    Enter license_name (License name) ['GPL']:
    Enter zip_safe (True/False: if the package can be distributed as a .zip file)
    [False]:
    <debe ser False para funcionar bien en Zope 2>
    Creating template basic_namespace
    ...
    Running /usr/bin/python2.4 setup.py egg_info

Este comando genera un directorio de distribución donde se encuentra la
información y código para distribuir el paquete resultante como egg. Dentro de
ese directorio se encuentra un subdirectorio con el espacio de nombres general
(en este ejemplo sería 'ejemplo') y dentro de ese último el verdadero directorio
del producto para Zope (en este ejemplo, 'policy').

Dentro del directorio del producto se encuentran los dos archivos
imprescindibles para crear un producto para Zope 2, junto con un esqueleto de
módulo para tests:

* __init__.py, incluye un método llamado 'initialize' para que Zope reconozca
  el paquete como producto.
* configure.zcml, el archivo de configuración con XML, que permite al producto
  utilizar código basado en Zope 3.
* tests.py, esqueleto de módulo para tests.

Una vez generado el producto, debemos agregar un directorio para almacenar la
configuración de Generic Setup::

    $ cd ejemplo.policy/ejemplo/policy
    $ mkdir profiles
    $ mkdir profiles/default

Después registramos ese directorio como perfil, dentro del archivo
configure.zcml:

.. code-block:: xml

    <genericsetup:registerProfile
         name="default"
         title="UNAM site policy"
         directory="profiles/default"
         description="Turn a Plone site into the UNAM site."
         provides="Products.GenericSetup.interfaces.EXTENSION"
         />

Ahora ya es posible agregar dentro del directorio del perfil toda la
configuración deseada. La manera recomendada de generar los archivos xml
necesarios para ello, es crear un sitio nuevo de Plone y a continuación
modificar toda la configuración que se quiere incluir en el producto. Una vez
hecho esto, se debe exportar la configuración modificada desde la herramienta
de portal_setup, que se puede accesar desde la raiz del portal desde la
administración de Zope (ZMI):

Al seleccionar los pasos deseados y presionar el botón de 'export selected
steps', se obtiene un archivo comprimido que contiene la configuración
expresada en XML para todos los pasos seleccionados. Este archivo debe
descomprimirse en el directorio del perfil creado en el paso anterior::

    $ cd profiles/default
    $ tar xzf setuptool_20080630134421.tar.gz

Como ejecutar codigo Python en import steps
===========================================

Finalmente, en algunas ocasiones hay pasos que queremos realizar al momento de
la instalación de un producto de configuración que no son manejables con
Generic Setup. En esos casos, existe un mecanismo para ejecutar código Python
en el momento que se instala un perfil. Se crea un archivo setuphandlers.py en
la raiz del producto, con el siguiente código:

.. code-block:: python

    from Products.CMFCore.utils import getToolByName

    def setupVarious(context):
        if context.readDataFile('ejemplo.policy_various.txt') is None:
            return
    site = context.getSite()
    # aquí va el código especial

El método setupVarious es donde se coloca el código especial para la
instalación, que puede hacer cualquier cosa que se necesite dentro del portal.
Para prevenir la ejecución de este código durante la instalación de otros
productos, se agrega un archivo de texto vacío, llamado
ejemplo.policy_various.txt, dentro de profiles/setup y se verifica su
existencia dentro de este método.

Para enlazar este código con los pasos de importación, existe un paso especial
en Generic Setup, llamado import_steps. Para activarlo, debemos agregar el
siguiente código dentro del archivo import_steps.xml, dentro del directorio
profiles/default:

.. code-block:: xml

    <?xml version="1.0"?>
    <import-steps>
       <import-step id="ejemplo.policy.various"
                    version="20080625-01"
                    handler="ejemplo.policy.setuphandlers.setupVarious"
                    title="UNAM Policy: miscellaneous import steps">
         <dependency step="plone-content" />
         Various import steps that are not handled by GS import/export
         handlers.
       </import-step>
    </import-steps>

Lo único que puede variar dependiendo de lo que necesitemos hacer, es la
parte donde se listan los steps de dependencia, marcados por la etiqueta
dependency en el XML. En el atributo step de esa etiqueta se debe colocar el
nombre del paso que necesitamos sea ejecutado antes que nuestro código. Se
pueden agregar varias etiquetas dependency con distintos pasos para el caso de'
que nuestro código dependa de varios pasos.

