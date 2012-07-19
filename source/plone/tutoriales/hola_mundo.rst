.. -*- coding: utf-8 -*-

.. _hola_mundo_plone3:

=====================
Hola Mundo en Plone 3
=====================

.. contents :: :local:

Introducción
============

Este es tutorial trata de explicar como crear un :ref:`Plone Theme product <producto_tema>` 
para Plone 3 usando las :ref:`plantillas de ZopeSkel <skel_plone>` y explica como generar 
un programa típico `Hola Mundo`_ para Plone como una ``view`` llamado 
``hello`` como una vista de aplicación.


Instalación
===========

Puedes instalar ZopeSkel usando :ref:`pip <que_es_pip>` (es recomendable 
hacerlo dentro de un :ref:`entorno virtual <creacion_entornos_virtuales>`):

.. code-block:: sh

    $ pip install 'ZopeSkel==2.21.2'

Debe crear una configuración :ref:`zc.buildout <buildout_plone3>` para una 
instancia de Zope para Plone 3 usando el comando ``paster``, 
ejecutando los siguientes comandos:

.. code-block:: sh

    $ paster create --template plone3_buildout plone3.buildout
    $ cd plone3.buildout
    $ python bootstrap.py
    $ ./bin/buildout -vN


Más opciones con el siguiente comando: 

.. code-block:: sh

    $ paster create --list-template

Cree un :ref:`Plone Theme <producto_tema>` en su carpeta ``src/`` dentro de su proyecto 
plone 3 llamado ``plone3.buildout``, con los siguientes comandos:

.. code-block:: sh

    $ cd src
    $ paster create --template plone3_theme collective.mydemoapp


Acceder a la carpeta ``browser/`` de su paquete ``collective.mydemoapp`` 
y cree un archivo python con el nombre ``hello.py``

.. code-block:: sh

    $ cd collective.mydemoapp/collective/mydemoapp/
    $ vim ./browser/hello.py

Más opciones con el siguiente comando:
    
.. code-block:: sh
    
    $ paster addcontent --list-all


Edite su Vista controladora en el archivo ``hello.py`` de la siguiente forma:

.. code-block:: python

    from Products.Five import BrowserView

    class HelloWorld(BrowserView):
        """
        Hello word browser view, as simple string
        """
        
        def __init__(self, context, request):
            self.context = context
            self.request = request
        
        def __call__(self):
            return "hello word"


Edite su configuración ZCML en el ``configure.zcml`` de la siguiente forma:

.. code-block:: xml

    <browser:page
        name="hello"
        for="*"
        class=".hello.HelloWorld"
        permission="zope2.Public"
       />


Edite su configuración Buildout en el ``buildout.cfg`` de la siguiente forma:

.. code-block:: cfg

    [buildout]
    ...
    eggs = 
        ...
        collective.mydemoapp
        ...
    ...
    zcml = 
        ...
        collective.mydemoapp
        ...
    ...
    develop = 
        ...
        src/collective.mydemoapp
        ...

Reconstruye la instancia de Zope y Plone 3, ejecutando el siguiente comando:

.. code-block:: sh

    $ ./bin/buildout -vN

Iniciar instancia Zope

.. code-block:: sh

    ./bin/instance fg

Acceda a su **sitio Plone** :menuselection:`Configuración del sitio --> Complementos --> Custom Theme --> Activar`

Para finalizar acceda por su navegador a la siguiente dirección: ``http://localhost:8080/Plone/hello``

Y de esta forma ya tiene generado una vista generada desde Python y otra 
vista generada de Python y incrustada en la diagramación de Plone generado 
con los ``localcommand`` de la plantilla ``plone3_theme`` del paquete ``ZopeSkel``.


Ejemplo de un viewlet básico
============================

- Accede al archivo de la clase Python viewlet ``browser/viewlets.py`` 
  generado en este paquete y quiete el comentario la pieza de código disponible 
  allí (clase de Python viewlet).

  .. code-block:: python

      class MyHelloWorldViewlet(ViewletBase):
          render = ViewPageTemplateFile('myhelloworldviewlet.pt')

          def update(self):
              self.computed_value = 'Hello world'
              self.company = 'Plone Fundation'

- Renombra el archivo plantilla viewlet ubicado en ``browser/viewlet.pt`` a 
  ``browser/myviewlet.pt`` y si es necesario edite el código python acorde a 
  la plantilla viewlet.

  .. code-block:: html

      <div align="center">
        <span tal:content="view/computed_value|nothing" />,  
        <b tal:content="view/company|nothing" />
      </div>

- Edite la clase y la plantilla asegurándose que cumpla lo que necesita.
- Asegúrese que su viewlet este correctamente registrado en el ``browser/configure.zcml``.

  .. code-block:: xml

      <browser:viewlet
          name="collective.mydemoapp.helloworld""
          manager="plone.app.layout.viewlets.interfaces.IPortalFooter"
          class=".viewlets.MyHelloWorldViewlet"
          layer=".interfaces.IThemeSpecific"
          permission="zope2.View"
          />

- Si usted necesito que aparezca en un orden especifico dentro de un viewlet manager, 
  entonces edite ``profiles/default/viewlets.xml`` acordemente.
- Reinicie su instancia Zope, ejecutando el siguiente comando:

  .. code-block:: sh

      $ ./bin/buildout -vN

- Si usted edito algún archivo en la carpeta ``profiles/default/``, debe reiniciar su 
  paquete.
- Una ves que este feliz con su implementación viewlet, remueva cualquier documentación 
  relacionada en su clase y plantilla viewlet.


Descarga código fuente
======================

Para descargar el código fuente de este ejemplo ejecute el siguiente comando:

.. code-block:: sh

  $ svn co https://svn.plone.org/svn/collective/spanishdocs/trunk/src/mini-tutoriales/collective.mydemoapp collective.mydemoapp


Conclusiones
============

Este ejemplo ofrece un acercamiento a crear productos Plone desde una 
`Views`_ y un `Viewlets`_ dentro de un manager viewlet.


Referencias
===========

-   `Plone for python programmers`_.
-   `Hello World in Plone`_.

.. _Hola Mundo: http://es.wikipedia.org/wiki/Hola_Mundo
.. _Views: http://collective-docs.readthedocs.org/en/latest/views/browserviews.html
.. _Viewlets: http://collective-docs.readthedocs.org/en/latest/views/viewlets.html
.. _Plone for python programmers: http://www.slideshare.net/djay/plone-for-python-programmers
.. _Hello World in Plone: https://github.com/aclark4life/hello_plone
