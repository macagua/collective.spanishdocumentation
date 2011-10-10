.. -*- coding: utf-8 -*-

=======================
GenericSetup y Perfiles
=======================

.. contents :: :local:

Introduccion
-------------

GenericSetup es un mecanismo basado en XML para importar y exportar
configuraciones de sitios Plone.

Se utiliza principalmente para modificar la configuración de un sitio al
momento de instalar un producto. Entre otras cosas permite:

* Registrar CSS
* Registrar Javascript
* Modificar los valores de diversas propiedades del sitio
* Registrar portlets
* Registrar índices de búsqueda del portal_catalog
* Y mas...

Usualmente los archivos de configuración para GenericSetup se guardan bajo la
carpeta *profiles/default* dentro del producto.

Toda la configuración que puede realizarse a través del panel de control de
Plone y del ZMI, como por ejemplo el orden de los viewlets elegido en
/@@manage-viewlets, puede guardarse y ser reutilizada mediante un perfil de
GenericSetup.

No es necesario editar manualmente los archivos XML del perfil de
GenericSetup, pues siempre es posible modificar la configuración de Plone
desde el sitio y después exportarla completa o en partes a XML. La herramienta
*portal_setup* en el ZMI permite exportar, importar y generar copias de las
configuraciones.

Modificar los archivos de configuración en XML de un producto no ocasiona
cambios inmediatos en el sitio de Plone, aun reiniciando el servidor. La
configuración `real` del portal se almacena en la ZODB, por lo que es
necesario reimportar los perfiles desde portal_setup o reinstalar el
producto en cuestión desde el panel de control de Plone. Solo en ese momento
sera modificada la configuración.

.. note::

    Diferencias entre ZCML y GenericSetup

    Cambios realizados mediante configuración de ZCML afectan el código
    Python de todos los sitios presentes en una instancia de Zope, mientras
    que los cambios en perfiles de GenericSetup solo afectan el sitio de
    Plone en que se hacen. Al importar un perfil de GenericSetup, se
    realizan cambios directamente en la base de datos del sitio, mientras que
    al cargar archivos de configuración de ZCML solo se modifica el código
    cargado en memoria.

* `GenericSetup tutorial <http://plone.org/documentation/tutorial/genericsetup>`_

* `GenericSetup product page <http://pypi.python.org/pypi/Products.GenericSetup/1.4.5>`_.

* `Source code <http://svn.zope.org/Products.GenericSetup/trunk/Products/GenericSetup/README.txt?rev=87436&view=auto>`_.


Creación de un perfil
---------------------

Un perfil se declara utilizando la directriz <genericsetup> en el archivo
configure.zcml del producto. El instalador de Plone importara la
configuración almacenada en el perfil llamado "default", pero es posible
declarar otros perfiles con diferentes nombres e importarlos por separado, por
ejemplo para ejecutar pruebas.

Los archivos XML del perfil se colocan en el directorio profiles/default
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

También es posible registrar un "Import various step" que ejecute código
Python cada vez que se instale el perfil de un producto.

Mas información sobre ejecutar steps:

* http://n2.nabble.com/indexing-of-content-created-by-Generic-Setup-tp4454703p4454703.html

Como obtener el listado de perfiles disponibles
-----------------------------------------------

Ejemplo::

        setup_tool = self.portal.portal_setup

        profiles = setup_tool.listProfileInfo()
        for profile in profiles:
            print  str(profile)

Resultados::

    {'product': 'PluggableAuthService', 'description': 'Content for an empty PAS (plugins registry only).', 'for': <InterfaceClass Products.PluggableAuthService.interfaces.authservice.IPluggableAuthService>, 'title': 'Empty PAS Content Profile', 'version': 'PluggableAuthService-1.5.3', 'path': 'profiles/empty', 'type': 1, 'id': 'PluggableAuthService:empty'}
    {'product': 'Products.CMFDefault', 'description': u'Profile for a default CMFSite.', 'for': <InterfaceClass Products.CMFCore.interfaces._content.ISiteRoot>, 'title': u'CMFDefault Site', 'version': 'CMF-2.1.1', 'path': u'profiles/default', 'type': 1, 'id': u'Products.CMFDefault:default'}
    {'product': 'Products.CMFPlone', 'description': u'Profile for a default Plone.', 'for': <InterfaceClass Products.CMFPlone.interfaces.siteroot.IPloneSiteRoot>, 'title': u'Plone Site', 'version': u'3.1.7', 'path': u'/home/moo/sits/parts/plone/CMFPlone/profiles/default', 'type': 1, 'id': u'Products.CMFPlone:plone'}
    {'product': 'Products.Archetypes', 'description': u'Extension profile for default Archetypes setup.', 'for': None, 'title': u'Archetypes', 'version': u'1.5.7', 'path': u'/home/moo/sits/parts/plone/Archetypes/profiles/default', 'type': 2, 'id': u'Products.Archetypes:Archetypes'}
    ...

Como instalar un perfil desde Python
====================================

Para instalar un perfil desde Python, por ejemplo para pruebas, se puede
llamar por su nombre, en el formato *profile-${product_name}:${profile_id}*

Ejemplo::

    setup_tool.runAllImportStepsFromProfile('profile-miproducto.miperfil')

Dependencias
------------

GenericSetup permite declarar como dependencias los perfiles de otros
productos, de manera que estos sean instalados antes del perfil de nuestro
producto.

* `Mas información sobre dependencias <http://plone.org/products/plone/roadmap/195/>`_.


