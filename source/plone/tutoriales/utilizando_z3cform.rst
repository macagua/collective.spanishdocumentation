.. -*- coding: utf-8 -*-

.. _utilizando_z3cform:

========================================
Utilizando formularios z3c.form en Plone
========================================

:Traductor(es): Leonardo J. Caballero G.
:Correo(s): leonardocaballero@gmail.com
:Lanzamiento: |version|
:Fecha: |today|

.. contents :: :local:

Introducción
============

¿Qué es z3cform? y ¿por qué debo considerar el uso de la misma?.

El paquete `z3c.form`_ es un framework avanzado para construcción y
utilización de formularios y widgets dentro de Zope / Plone. El provee una
forma fácil y flexible para mostrar formularios y manejar sus etapas de
creación, validación y posibles acciones posteriores.


¿Qué es plone.app.z3cform?
--------------------------

El `plone.app.z3cform`_ es un paquete que proporciona widgets y otras
utilidades para hacer formularios dentro de Plone. También contiene las
plantillas para su hermano mayor, el paquete `plone.z3cform`_, que a su vez
es una capa muy delgada que encapsula el paquete `z3c.form`_.

Los formularios que usted va hacer con `plone.app.z3cform`_ son esencialmente
los mismos formularios Zope 3 puros construido con el paquete `z3c.form`_. No
hay cláusulas secretas o hacks especiales de Zope 2 y Plone (cosas como
*self.context.aq_inner*).

El paquete `z3c.form`_ viene con una excelente `documentación`_.

z3c.form vs arquetipos
----------------------

Los formularios arquetipos son difíciles de usar, independientemente de los
tipos de contenido. Esto llevó a varios hacks en el pasado cuando los tipos
de contenidos arquetipos fueron utilizados erróneamente como herramientas,
formularios de encuesta, etc.

z3c.form vs formlib
-------------------

El paquete `zope.formlib`_ a veces cubiertos por inflexible o hacks, debido a
su falta de capacidad de adaptación y un sólido conjunto de widgets.

¿Qué voy a aprender en este tutorial?
=====================================

Este tutorial le mostrará cómo crear un formulario z3c.form simple de
comentarios, que luego se ampliará y se mostrará dentro de un Viewlet.

Más información
---------------

Puede encontrar más información en las páginas de PyPI de los paquetes
`plone.z3cform`_ y `plone.app.z3cform`_.

El nuevo `Plone Developers Manual`_ también proporciona `documentación para
el z3c.form`_.

El código fuente para este ejemplo está disponible en el repositorio SVN
`collective`_.

Además, el paquete z3c.form se utiliza ampliamente en el producto
`plone.app.discussion`_. En el código fuente de este paquete, encontrará
toneladas de ejemplos de formularios z3c.form.


Creación de un buildout para el desarrollo z3c.form
===================================================
Algunas cosas que usted necesita antes de comenzar.

Antes de que podamos crear un formulario z3c.form dentro de Plone necesita
para crear un `buildout Plone`_ como paquete de dependencias necesarias.
Asegúrese de que tiene `Python`_, `Setuptools`_, virtualenv y ZopeSkel
instalados. Instrucciones se pueden encontrar en el `tutorial sobre buildout`_.
También asegúrese de tener la última versión de ZopeSkel
instalado, con el siguiente comando:

.. code-block:: sh

  $ easy_install-2.4 "ZopeSkel==2.21.2"


Crear un ambiente de buildout
-----------------------------

Inicialmente se crea un nuevo buildout Plone 3 con la ayuda del script
paster, con el siguiente comando:

.. code-block:: sh

  $ paster create -t plone3_buildout z3cformtutorial-buildout


Sólo tienes que introducir las respuestas a todas las preguntas para
seleccionar los valores por defecto. Sólo prestan atención a la cuestión de
la contraseña de Zope, el que debe completar individual.

.. code-block:: sh

  Selected and implied templates:
     ZopeSkel#plone3_buildout  A buildout for Plone 3 projects

    Variables:
     egg:      z3cformtutorial_buildout
     package:  z3cformtutorialbuildout
     project:  z3cformtutorial-buildout
    Enter plone_version (Which Plone version to install) ['3.3.1']:
    Enter zope2_install (Path to Zope 2 installation; leave blank to fetch one) ['']:
    Enter plone_products_install (Path to directory containing Plone products; leave blank to fetch one) ['']:
    Enter zope_user (Zope root admin user) ['admin']:
    Enter zope_password (Zope root admin password) ['']: admin 
    Enter http_port (HTTP port) [8080]:
    Enter debug_mode (Should debug mode be "on" or "off"?) ['off']:
    Enter verbose_security (Should verbose security be "on" or "off"?) ['off']:
    Creating template plone3_buildout
    Creating directory ./z3cformtutorial-buildout
     Copying README.txt to ./z3cformtutorial-buildout/README.txt
     Copying bootstrap.py to ./z3cformtutorial-buildout/bootstrap.py
     Copying buildout.cfg_tmpl to ./z3cformtutorial-
     buildout/buildout.cfg
     Recursing into products
     Creating ./z3cformtutorial-buildout/products/
     Copying README.txt to ./z3cformtutorial-
     buildout/products/README.txt
     Recursing into src
     Creating ./z3cformtutorial-buildout/src/
     Copying README.txt to ./z3cformtutorial-buildout/src/README.txt
     Recursing into var
     Creating ./z3cformtutorial-buildout/var/
     Copying README.txt to ./z3cformtutorial-buildout/var/README.txt
    -----------------------------------------------------------
    Generation finished
    You probably want to run python bootstrap.py and then edit
    buildout.cfg before running bin/buildout -v

    See README.txt for details
    -----------------------------------------------------------

Ajustar versiones de paquetes necesarios para trabajar con z3c.form
-------------------------------------------------------------------

Para hacer que funcione z3c.form en Plone necesita instalar algunos paquetes
con un conjunto específico de las versiones. Para facilitar las cosas,
podemos extender su buildout con el `Known Good Set - (KGS) de plone.autoform`_. 
Sólo tienes que añadir la siguiente dirección url 
"http://good-py.appspot.com/release/plone.autoform/1.0b2" que extiende 
a la línea de su buildout.

``buildout.cfg``

  .. code-block:: ini

    extends =
        http://good-py.appspot.com/release/plone.autoform/1.0b2
    ...


Para Plone 4, no necesitamos un KGS. Basta con establecer la versión del
paquete zope.schema en su configuración ``buildout.cfg``:

.. code-block:: ini

  [versions]
  zope.schema = 3.6.0


Ejecutar el buildout
--------------------

Después de ajustar las versiones, puede ejecutar el script de buildout, con
el siguiente comando:

.. code-block:: sh

  $ cd z3cformtutorial-buildout
  $ python bootstrap
  $ ./bin/buildout -vvvvvN
  
Ahora luego de tener construido el proyecto plone 3, esta listo
para crear un paquete Python que contiene el formulario que creará el
siguiente paso.


Creación de paquete Python para un formulario z3c.form
------------------------------------------------------

Ahora cree un nuevo paquete de Python que contiene un simple formulario.

Para crear un nuevo paquete de Python, ir al directorio ``src/`` de su entorno
buildout y permita que el script paster haga el trabajo por usted, con los
siguientes comandos:

.. code-block:: sh

  $ cd src
  $ paster create -t plone example.z3cformtutorial

Entrar en ``example`` como un espacio de nombres y ``z3cformtutorial`` como el
nombre del paquete. La salida se verá algo así:

.. code-block:: sh

  Selected and implied templates:
    ZopeSkel#basic_namespace  A project with a namespace package
    ZopeSkel#plone            A Plone project

    Variables:
      egg:      example.z3cformtutorial
      package:  examplez3cformtutorial
      project:  example.z3cformtutorial
    Enter namespace_package (Namespace package (like plone)) ['plone']: example
    Enter package (The package contained namespace package (like example)) ['example']: z3cformtutorial
    Enter zope2product (Are you creating a Zope 2 Product?) [False]:
    Enter version (Version) ['1.0']:
    Enter description (One-line description of the package) ['']:
    Enter long_description (Multi-line description (in reST)) ['']:
    Enter author (Author name) ['Plone Foundation']:
    Enter author_email (Author email) ['plone-developers@lists.sourceforge.net']:
    Enter keywords (Space-separated keywords/tags) ['']:
    Enter url (URL of homepage) ['http://svn.plone.org/svn/plone/plone.example']:
    Enter license_name (License name) ['GPL']:
    Enter zip_safe (True/False: if the package can be distributed as a .zip file) [False]:
    Creating template basic_namespace
    Creating directory ./example.z3cformtutorial
      Recursing into +namespace_package+
        Creating ./example.z3cformtutorial/example/
        Recursing into +package+
          Creating
          ./example.z3cformtutorial/example/z3cformtutorial/
          Copying __init__.py_tmpl to
          ./example.z3cformtutorial/example/z3cformtutorial/__init__.py
        Copying __init__.py_tmpl to
        ./example.z3cformtutorial/example/__init__.py
      Copying README.txt_tmpl to ./example.z3cformtutorial/README.txt
      Recursing into docs
        Creating ./example.z3cformtutorial/docs/
        Copying HISTORY.txt_tmpl to
        ./example.z3cformtutorial/docs/HISTORY.txt
      Copying setup.cfg to ./example.z3cformtutorial/setup.cfg
      Copying setup.py_tmpl to ./example.z3cformtutorial/setup.py
    Creating template plone
      Recursing into +namespace_package+
        Recursing into +package+ 
          ./example.z3cformtutorial/example/z3cformtutorial/__init__.py
          already exists (same content)
          Copying configure.zcml_tmpl to
          ./example.z3cformtutorial/example/z3cformtutorial/configure.zcml
          Copying tests.py_tmpl to
          ./example.z3cformtutorial/example/z3cformtutorial/tests.py
      Recursing into docs
        Copying INSTALL.txt_tmpl to
        ./example.z3cformtutorial/docs/INSTALL.txt
        Copying LICENSE.GPL to
        ./example.z3cformtutorial/docs/LICENSE.GPL
        Copying LICENSE.txt_tmpl to
        ./example.z3cformtutorial/docs/LICENSE.txt
    Replace 1022 bytes with 1272 bytes (0/32 lines changed; 8 lines added)
      Copying setup.py_tmpl to ./example.z3cformtutorial/setup.py
    ------------------------------------------------------------------------------
    The project you just created has local commands. These can be used
    from within
    the product.

    usage: paster COMMAND

    Commands:
      addcontent  Adds plone content types to your project

    For more information: paster help COMMAND
    ------------------------------------------------------------------------------
    Running /usr/bin/python2.4 setup.py egg_info


Agregar dependencias de z3c.form a la paquete creado
----------------------------------------------------

Ahora agregue el paquete ``plone.app.z3cform`` como una dependencia a su paquete
recién creado Python. A su vez, el paquete se descargará automáticamente como
``plone.z3cform`` dependencia ``plone.app.z3cform``:

``src/example.z3cformtutorial/setup.py``

  .. code-block:: python

    ...
        install_requires=[
            'setuptools',
            # -*- Extra requirements: -*-
            **'plone.app.z3cform',**
        ],
    ...


Después de esto, adiciona el paquete en su configuración en su buildout:

``buildout.cfg``

  .. code-block:: ini

    [buildout]
    ...

    eggs =
        example.z3cformtutorial
        ...

    develop =
        src/example.z3cformtutorial
        ...

    [instance]
    ...
    zcml =
        example.z3cformtutorial


Luego ejecute de nuevo el buildout para bajar las dependencias de su paquete:

.. code-block:: sh

  $ ./bin/buildout -vvvvvN

Ahora esta listo para crear realmente nuestro primer formulario.


Crear un formulario simple con z3c.form
=======================================

Crear un formulario simples para registrar comentarios.

Primeramente debe definir un ``schema`` con tres campos: título, autor y
campo de texto para los comentarios:

.. code-block:: python

  from zope import interface, schema

  class IComment(interface.Interface):
      title = schema.TextLine(title=u"Title")
      author = schema.TextLine(title=u"Author", required=False)
      text = schema.TextLine(title=u"Text")

En formulario de comentarios usa a definición del schema ``IComment`` para
modelar y más tarde renderizar el formulario. En este punto también definir
una etiqueta que aparece encima del formulario de la siguiente forma:

.. code-block:: python

  from z3c.form import form, field

  class CommentForm(form.Form):
      fields = field.Fields(IComment)
      ignoreContext = True # don't use context to get widget data
      label = "Add a comment"


A continuación, agregue el botón de enviar en forma de un método de
decoración que se encargará de la información recibida. Se extrajeron los
datos de la solicitud y enviar el formulario, si los errores de validación,
en caso contrario prosiga de la siguiente forma:

.. code-block:: python

  from z3c.form import button
  @button.buttonAndHandler(u'Post comment')
  @button.buttonAndHandler(u'Post comment')
  def handleApply(self, action):
      data, errors = self.extractData()
      if errors:
          return
      if data.has_key('text'):
          print data['text'] # ... or do stuff

Como último paso, es necesario envolver el formulario en una página por defecto de Plone:

.. code-block:: python

  from plone.z3cform.layout import wrap_form
  wrap_form(CommentForm)


Colocando todos estos pasos previos juntos, en un archivo llamado
``comment.py`` debe aparecer como el siguiente mensaje:

.. code-block:: python

  from zope import interface, schema
  from z3c.form import form, field, button
  from plone.z3cform.layout import wrap_form

  class IComment(interface.Interface):
      title = schema.TextLine(title=u"Title")
      author = schema.TextLine(title=u"Author", required=False)
      text = schema.TextLine(title=u"Text")

  class CommentForm(form.Form):
      fields = field.Fields(IComment)
      ignoreContext = True # don't use context to get widget data
      label = u"Add a comment"

      @button.buttonAndHandler(u'Post comment')
      def handleApply(self, action):
          data, errors = self.extractData()
          if data.has_key('title') and data.has_key('text'):
              print data['title'] # ... or do stuff

  CommentView = wrap_form(CommentForm)

Para conocer mas detalles del **schema** de ``z3c.form``, consulte el
siguiente enlace `http://docs.zope.org/z3c.form/browser/README.html`_.

Una única cosa que falta por hacer para usar este formulario y es registrar
en el archivo configure.zcml de su paquete:

.. code-block:: xml

  <configure
        xmlns="http://namespaces.zope.org/zope"
        xmlns:five="http://namespaces.zope.org/five"
        xmlns:browser="http://namespaces.zope.org/browser"
        i18n_domain="example.z3cformtutorial">

        <!-- Include z3c.form as dependency -->
        <include package="plone.app.z3cform" />

        <!-- Register the comment form -->
        <browser:page
            for="Products.CMFPlone.interfaces.IPloneSiteRoot"
            name="comment_form"
            class=".comment.CommentView"
            permission="zope2.View"
            />

    </configure>

Inicie la instancia Zope en modo foreground:

.. code-block:: sh

  $ ./bin/instance fg


Acceda al ZMI y cree un sitio de Plone con el nombre ``test`` y con el perfil
de Generic Setup ``Plone z3c.form support``. Luego abra la siguiente dirección
en su navegador de preferencia: ::

  http://localhost:8080/test/comment_form


Mostrar formulario z3c.form dentro de un Viewlet en Plone
=========================================================

Ahora es debe mostrar el formulario de comentarios dentro de un Viewlet en
Plone.

A fin de mostrar el formulario de comentarios dentro de un Viewlet,
primeramente debe crea un nuevo archivo llamado ``commentviewlet.py`` que
contiene un Viewlet que tendrá una page template asociado y un título:

.. code-block:: python

  from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
  from plone.app.layout.viewlets import ViewletBase

  class CommentViewlet(ViewletBase):
      index = ViewPageTemplateFile('commentviewlet.pt')
      label = 'Add Comment'


Para mostrar el formulario de contactos dentro del Viewlet, tiene que
actualizar el ``request`` definiendo un método ``update`` de la siguiente forma:

.. code-block:: python

    def update(self):
        super(CommentViewlet, self).update()
        z2.switch_on(self, request_layer=IFormLayer)
        self.form = CommentForm(aq_inner(self.context), self.request)
        self.form.update()


Considerando las importaciones necesarias, el archivo ``commentviewlet.py``
debe verse como el siguiente:

.. code-block:: python

  from Acquisition import aq_inner

  from z3c.form.interfaces import IFormLayer

  from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

  from plone.app.layout.viewlets import ViewletBase

  from plone.z3cform import z2

  from example.z3cformtutorial.comment import CommentForm

  class CommentViewlet(ViewletBase):
      index = ViewPageTemplateFile('commentviewlet.pt')
      label = 'Add Comment'
      def update(self):
          super(CommentViewlet, self).update()
          z2.switch_on(self, request_layer=IFormLayer)
          self.form = CommentForm(aq_inner(self.context), self.request)
          self.form.update()

En seguida, cree una nueva page template llamado ``commentviewlet.pt`` para
mostrar el formulario llamando y el método **render** del formulario:

.. code-block:: html

  <h2 tal:content="view/label">View Title</h2>
  <div id="layout-contents">
    <div tal:replace="structure view/form/render" />
  </div>

Una única cosa que falta por hacer es registrar el nuevo Viewlet en su
archivo ``configure.zcml`` de la siguiente forma:

.. code-block:: xml

  <browser:viewlet
        name="comment_viewlet"
        for="Products.CMFCore.interfaces.IContentish"
        manager="plone.app.layout.viewlets.interfaces.IBelowContent"
        class=".commentviewlet.CommentViewlet"
        permission="zope2.View"
        />


Reinicie su instancia Zope:

.. code-block:: sh

  $ ./bin/instance restart

y acceda a la siguiente URL para ver su nuevo viewlet como formulario de
comentarios en: ::

  http://localhost:8080/test


OBS: plone.z3cform >= 0.6.0
---------------------------

Si usted está usando el paquete plone.z3cform >= 0.6.0, el formulario de
comentarios precisa fornecer una interfaz IWrappedForm, de lo contrario Plone
levantará una excepción de "maximum recursion error". Adicione el siguiente
código en con la marca ``### copy ... ###`` para hacer al formulario que 
funcione en todas las versiones de plone.z3cform:

.. code-block:: python

  from Acquisition import aq_inner

  from zope.interface import alsoProvides ### copy this lines ### 

  from z3c.form.interfaces import IFormLayer

  from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

  from plone.app.layout.viewlets import ViewletBase

  from plone.z3cform import z2

  from example.z3cformtutorial.comment import CommentForm

  ### copy from here ###
  # starting from 0.6.0 version plone.z3cform has IWrappedForm interface
  try:
      from plone.z3cform.interfaces import IWrappedForm
      HAS_WRAPPED_FORM = True
  except ImportError:
      HAS_WRAPPED_FORM = False
  ### copy until here ###

  class CommentViewlet(ViewletBase):
      index = ViewPageTemplateFile('commentviewlet.pt')
      label = 'Add Comment'

      def update(self):
          super(CommentViewlet, self).update()
          z2.switch_on(self, request_layer=IFormLayer)
          self.form = CommentForm(aq_inner(self.context), self.request)
          ### copy from here ###
          if HAS_WRAPPED_FORM:
                alsoProvides(self.form, IWrappedForm)
          ### copy until here ###
          self.form.update()


Referencias
===========

-   `Utilizando z3c.form`_ desde la comunidad Plone Brasil.


.. _z3c.form: http://pypi.python.org/pypi/z3c.form
.. _plone.app.z3cform: http://pypi.python.org/pypi/plone.app.z3cform
.. _plone.z3cform: http://pypi.python.org/pypi/plone.z3cform
.. _documentación: http://docs.zope.org/z3c.form/
.. _zope.formlib: http://pypi.python.org/pypi/zope.formlib
.. _Plone Developers Manual: http://plonemanual.twinapex.fi/
.. _documentación para el z3c.form: http://plonemanual.twinapex.fi/forms/z3c.form.html
.. _collective: http://svn.plone.org/svn/collective/example.z3cformtutorial/
.. _plone.app.discussion: http://plone.org/products/plone.app.discussion
.. _buildout Plone: http://plone.org/documentation/kb/buildout/
.. _Python: http://www.python.org/download/releases/
.. _Setuptools: http://peak.telecommunity.com/DevCenter/setuptools
.. _tutorial sobre buildout: http://coactivate.org/projects/ploneve/gestion-de-proyectos-con-buildout
.. _Known Good Set - (KGS) de plone.autoform: http://good-py.appspot.com/release/plone.autoform/1.0b2
.. _http://docs.zope.org/z3c.form/browser/README.html: http://docs.zope.org/z3c.form/browser/README.html
.. _Utilizando z3c.form: http://coactivate.org/projects/ploneorgbr/utilizando-z3c.form
