.. -*- coding: utf-8 -*-

.. _perfiles_genericsetup:

=======================
GenericSetup y Perfiles
=======================

.. contents :: :local:

Introducción
============

GenericSetup es un mecanismo basado en XML para importar y exportar
configuraciones de sitios Plone.

Se utiliza principalmente para modificar la configuración de un sitio al
momento de instalar un producto. Entre otras cosas permite:

* Registrar CSS en el ``portal_css``.
* Registrar Javascript en el ``portal_javascript``.
* Modificar los valores de diversas propiedades del sitio en el ``portal_properties``.
* Registrar portlets
* Registrar índices de búsqueda del ``portal_catalog``.
* Y mas...

Usualmente los archivos de configuración para GenericSetup se guardan bajo la
carpeta ``profiles/default`` dentro del producto.

Toda la configuración que puede realizarse a través del panel de control de
Plone y del ZMI, como por ejemplo el orden de los viewlets elegido en
``/@@manage-viewlets``, puede guardarse y ser reutilizada mediante un perfil de
GenericSetup.

No es necesario editar manualmente los archivos XML del perfil de
``GenericSetup``, pues siempre es posible modificar la configuración de Plone
desde el sitio y después exportarla completa o en partes a XML. La herramienta
``portal_setup`` en el ZMI permite exportar, importar y generar copias de las
configuraciones.

Modificar los archivos de configuración en XML de un producto no ocasiona
cambios inmediatos en el sitio de Plone, aun reiniciando el servidor. La
configuración `real` del portal se almacena en la ZODB, por lo que es
necesario reimportar los perfiles desde ``portal_setup`` o reinstalar el
producto en cuestión desde el panel de control de Plone. Solo en ese momento
sera modificada la configuración.

.. note::

    Diferencias entre ZCML y GenericSetup

    Cambios realizados mediante configuración de ``ZCML`` afectan el código
    Python de todos los sitios presentes en una instancia de ``Zope``, mientras
    que los cambios en perfiles de ``GenericSetup`` solo afectan el sitio de
    Plone en que se hacen. Al importar un perfil de ``GenericSetup``, se
    realizan cambios directamente en la base de datos del sitio, mientras que
    al cargar archivos de configuración de ``ZCML`` solo se modifica el código
    cargado en memoria.

* `GenericSetup tutorial <http://plone.org/documentation/tutorial/genericsetup>`_

* `GenericSetup product page <http://pypi.python.org/pypi/Products.GenericSetup/1.4.5>`_.

* `Source code <http://svn.zope.org/Products.GenericSetup/trunk/Products/GenericSetup/README.txt?rev=87436&view=auto>`_.


Términos importantes
====================

.. glossary::

  perfil base.
    El perfil base es el perfil que todos los otros perfiles extenderá. 
    Para usuarios de Plone este es el perfil ``plone`` desde el producto ``CMFPlone``.

  perfil de extensión
    Un perfil extensión es un conjunto de información de configuración que extiende 
    el perfil base. Las mayoría de los productos define al menos un perfil de extensión
    para definir sus producto.

  perfil de versión
    El perfil de versión puede definirse en el archivo ``metadata.xml``. Este le dice al
    programa ``GenericSetup`` cual es la versión actual del perfil.

  pasos de importar
    Del Ingles ``import steps``, son los pasos de importar que le dice al programa GenericSetup como leer la configuración exportada para un perfil dado y aplicarlo en su sitio.

  pasos de exportar
    Del Ingles ``export steps``, son los pasos de exportar que le dice al programa ``GenericSetup`` como exportar la actual configuración de su sitio.

  manipulador de instalación
    Del Ingles ``setup handler``, un manipulador de instalación es un termino dado a un paso de importar que ejecuta algún código de personalización Python. Este es otra forma de crear un paso de importar.

  pasos de actualizar
    Del Ingles ``upgrade step``, un paso de actualizar da a usted la habilidad para actualizar el código desde una versión del perfil a otro. Esto es muy útil This is useful for one time changes that need to be made between versions.

  snapshot
    Un ``snapshot`` puede tomar la configuración actual en el ``portal_setup``.
    Este puede después ser usada para comparar a otro ``snapshot`` o perfil. Esto puede ser útil cuando usted hace cambios a su sitio y quiere saber como afecta a su perfil.

Referenciando a Perfiles
========================

GenericSetup referencia a los perfiles con el siguiente formato:

.. code-block:: text

  profile-<package name>:<profile name>

Un ejemplo podría ser el perfil desde el producto CMFPlone:

.. code-block:: text

  profile-Products.CMFPlone:plone

Esta es la sintaxis que es usada para dependencias en el archivo  metadata.xml. Por ejemplo, si usted siempre quiere ejecutar por defecto la dependencia ‘my.dependency’ antes de su perfil, usted podría usar:

.. code-block:: text

  <?xml version=”1.0”?>
  <metadata>
     <version>VERSION_NUMBER</version>
     <dependencies>
        <dependency>profile-my.dependency:default</dependency>
     </dependencies>
  </metadata>

Creación de un perfil
=====================

Un perfil se declara utilizando la directriz <genericsetup> en el archivo
``configure.zcml`` del producto. El instalador de Plone importara la
configuración almacenada en el perfil llamado ``default``, pero es posible
declarar otros perfiles con diferentes nombres e importarlos por separado, por
ejemplo para ejecutar pruebas.

Los archivos XML del perfil se colocan en el directorio ``profiles/default``
dentro del producto.

.. code-block:: xml

	<configure
	    xmlns="http://namespaces.zope.org/zope"
	    xmlns:genericsetup="http://namespaces.zope.org/genericsetup"
	    i18n_domain="gomobile.mobile">

	    <genericsetup:registerProfile
	      name="default"
	      title="Plone Go Mobile"
	      directory="profiles/default"
	      description='Mobile CMS add-on'
	      provides="Products.GenericSetup.interfaces.EXTENSION"
	      />

	</configure>

También es posible registrar un ``Import various step`` que ejecute código
Python cada vez que se instale el perfil de un producto.

Mas información sobre ejecutar steps:

* http://n2.nabble.com/indexing-of-content-created-by-Generic-Setup-tp4454703p4454703.html


Generación de Contenido
=======================
El programa ``GenericSetup`` le permite a usted importar y exportar contenido por la forma llamada ``structure``. Allí puede haber muchos archivos que controlan como este trabaja:

.. glossary::

  .objects
    El archivo ``.objects`` contiene una lista de objeto IDs 
    y su ``portal_types`` que la estructura necesita crear 
    los objetos. Los IDs también listan dentro de la estructura de 
    carpeta con más información acerca de cual crear. Por defecto 
    todos los elementos listados serán removido y se agregaran 
    de nuevo.

    Ejemplo de un archivo ``.objects`` que toma desde el perfil ``Products.CMFPlone:plone``:

      .. code-block:: ini

        Members,Large Plone Folder
        front-page,Document

  .preserve
    El archivo ``.preserve`` es una lista de IDs que, si están 
    presente, no debería ser removido. Este podría ser usado 
    si usted conoce el perfil que puede ser ejecutado otra ves 
    y posiblemente remover su contenido.

    El archivo ``.preserve`` típicamente contiene información que ``GenericSetup``
    usará para cuidar dos objetos existentes:

      .. code-block:: ini

        front-page
        Members

  .delete
    El archivo ``.delete`` es una lista de IDs que puede ser 
    borrado desde el sitio.

    Al igual que el archivo ``.preserve``, el archivo ``.delete`` usan la misma sintaxis. El siguiente podría ser valido para borrar dos objetos:

      .. code-block:: ini

        front-page
        Members

  .properties
    El archivo ``.properties`` típicamente contiene información que ``GenericSetup`` utilizará para crear la carpeta en la que reside. Esto le permite la exportación a estar representados en una jerarquía como lo es en el sitio.

    Ejemplo de un archivo ``.properties`` tomada desde el perfil de ``Products.CMFPlone:plone`` para la carpeta ``Members``:

      .. code-block:: ini

        [DEFAULT]
        description = Site Users
        title = Users

Obtener el listado de perfiles disponibles
==========================================

Ejemplo:

.. code-block:: python

  setup_tool = self.portal.portal_setup

  profiles = setup_tool.listProfileInfo()
  for profile in profiles:
      print  str(profile)

Resultados:

.. code-block:: python

  {'product': 'PluggableAuthService', 'description': 'Content for an empty PAS (plugins registry only).', 'for': <InterfaceClass Products.PluggableAuthService.interfaces.authservice.IPluggableAuthService>, 'title': 'Empty PAS Content Profile', 'version': 'PluggableAuthService-1.5.3', 'path': 'profiles/empty', 'type': 1, 'id': 'PluggableAuthService:empty'}
  {'product': 'Products.CMFDefault', 'description': u'Profile for a default CMFSite.', 'for': <InterfaceClass Products.CMFCore.interfaces._content.ISiteRoot>, 'title': u'CMFDefault Site', 'version': 'CMF-2.1.1', 'path': u'profiles/default', 'type': 1, 'id': u'Products.CMFDefault:default'}
  {'product': 'Products.CMFPlone', 'description': u'Profile for a default Plone.', 'for': <InterfaceClass Products.CMFPlone.interfaces.siteroot.IPloneSiteRoot>, 'title': u'Plone Site', 'version': u'3.1.7', 'path': u'/home/moo/sits/parts/plone/CMFPlone/profiles/default', 'type': 1, 'id': u'Products.CMFPlone:plone'}
  {'product': 'Products.Archetypes', 'description': u'Extension profile for default Archetypes setup.', 'for': None, 'title': u'Archetypes', 'version': u'1.5.7', 'path': u'/home/moo/sits/parts/plone/Archetypes/profiles/default', 'type': 2, 'id': u'Products.Archetypes:Archetypes'}
    ...

Instalación un perfil desde Python
==================================

Para instalar un perfil desde Python, por ejemplo para pruebas, se puede
llamar por su nombre, en el formato *profile-${product_name}:${profile_id}*

Ejemplo:

.. code-block:: python

  setup_tool.runAllImportStepsFromProfile('profile-miproducto.miperfil')

Dependencias
============

GenericSetup permite declarar como dependencias los perfiles de otros
productos, de manera que estos sean instalados antes del perfil de nuestro
producto.

* `Mas información sobre dependencias <http://plone.org/products/plone/roadmap/195/>`_.

Otros Consejos
==============

* Cuando instale un producto de tercero, siempre debe asegurarse de tener un respaldo de su sitio.

* Pruebe la instalación del producto en un entorno local antes de aplicarlo en el entorno de producción.

* Cuando escriba un manipulador de instalación de un perfil especifico como **importVarious**, asegúrese que ellos solamente ejecute el perfil usando ``context.readDataFile``.


Referencias
===========

- `GenericSetup y Perfiles`_.
- `Generic Setup Quick Reference`_.

.. _GenericSetup y Perfiles: http://www.plone.mx/docs/gs.html
.. _Generic Setup Quick Reference: http://www.sixfeetup.com/company/technologies/plone-content-management/swag/swag-images-files/generic_setup.pdf
