.. -*- coding: utf-8 -*-

***************************************************
Traducir un documento a otro idioma automáticamente
***************************************************

Google ofrece un servicio de traducción de idiomas con el que podemos
traducir automáticamente cualquier texto desde uno de los idiomas disponibles
a cualquier otro de ellos. Agregaremos esta funcionalidad a cualquier tipo
de contenido que tenga un campo de texto específico.

Requisitos previos
==================

Para agilizar el acceso al servicio de traducción, utilizaremos una librería
de Python que envuelve el API de Google. Necesitamos agregar lo siguiente en
la sección de *eggs* de nuestro buildout::

    simplejson
    goopytrans

Además, requeriremos que el tipo de contenido utilizado tenga un campo de
texto llamado *text*.

Vista Python
============

La vista es muy simple. Únicamente agregamos un método para traducir el texto
utilizando goopytrans.

.. code-block:: python

    import goopytrans

    from Products.Five import BrowserView
    from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

    class Traducir(BrowserView):

        template = ViewPageTemplateFile('traducir.pt')

        def __init__(self, context, request):
            self.context = context
            self.request = request

        def __call__(self):
            return self.template()

        def translate(self, src, dest):
            text = getattr(self.context,'getText',None)
            if text is None:
                return ''
            return goopytrans.translate(text(), source=src, target=dest)

Template ZPT
============

Por supuesto, el template es igual de sencillo, pues para este ejemplo solo
nos interesa mostrar el texto traducido.

.. code-block:: html

    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en"
          lang="en"
          metal:use-macro="here/main_template/macros/master"
          i18n:domain="plonetheme.cursoplone">
    <body>
      <div metal:fill-slot="main">
        <h1 tal:content="here/title"></h1> 
        <p tal:define="src request/src|string:es;
                       dest request/dest|string:en"
           tal:content="structure python:view.translate(src, dest)">
          Texto
        </p>
      </div>
    </body>
    </html>

Configuración
=============

La configuración de la vista es la siguiente:

.. code-block:: xml

    <browser:page
        for="*"
        name="traducir"
        class=".traducir.Traducir"
        permission="zope2.View"
    />


