.. -*- coding: utf-8 -*-

======================================
Obtener direcciones de manejo con SOAP
======================================

Plone puede conectarse fácilmente a servicios SOAP utilizando el poder de
Python. A continuación veremos como obtener direcciones de manejo dentro de
los Estados Unidos utilizando un servicio web público.

Crearemos una vista de Plone que muestre una forma para capturar dos
direcciones de USA y muestre los pasos para llegar de una a otra al presionar
el botón de enviar.

Requisitos previos
==================

Una librería de Python que permite conectarse a servicios web de un manera
sencilla se llama *suds* y esta disponible en `PYPI <http://pypi.python.org/pypi/suds>`_.
Utilizaremos esta librería para nuestra pequeña aplicación. Si utilizamos Plone
con buildout (como debe ser), simplemente debemos agregar *suds* a la
sección de *eggs* del buildout:

.. code-block:: cfg

    eggs = 
        ...
        suds
        ...


Vista Python
============

El código de la vista es muy sencillo. Primero importamos la clase *Client*
de suds, junto con lo necesario para crear una vista en Plone.

.. code-block:: python

    from suds.client import Client

    from Products.Five import BrowserView
    from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

A continuación podemos definir la vista. El método *__init__* y la
asignación del template se hacen de la manera usual:

.. code-block:: python

    class Rutas(BrowserView):
        """
        Obtener ruta de manejo de una direccion a otra
        """

        template = ViewPageTemplateFile('rutas.pt')

        def __init__(self, context, request):
            self.context = context
            self.request = request

Al llamar a la vista, queremos llamar al servicio web si se incluyen las dos
direcciones en la forma. En ese caso, la vista tendrá las direcciones en los
atributos *de* y *hasta*, mientras que la lista de pasos a seguir para llegar
de una a otra estarán en *como_llegar*. En caso contrario, simplemente
mostramos la forma vacía.

.. code-block:: python

        def __call__(self):
            if self.request.get('de',None) is not None:
                self.de = self.request.get('de')
                self.hasta = self.request.get('hasta')
                self.como_llegar = self.pasos_para_llegar(self.de, self.hasta)
            return self.template()

El método que llama al servicio es la parte importante del código. Primero,
asignamos a *url* la dirección del servicio web al que vamos a conectarnos,
que debe ser un recurso de tipo WSDL. En este caso utilizamos uno que
devuelve la ruta a seguir entre dos direcciones, pero por supuesto es posible
conectarse a cualquier otro servicio SOAP si se tiene la dirección correcta.

Para llamar al servicio, creamos una instancia del cliente, pasándole la url
como parámetro. Después, llamamos el servicio deseado con los parámetros
requeridos. En este caso el servicio se llama *GetDirections* y recibe las
dos direcciones. Lo que nos regresa es una lista de pasos a seguir, con
descripción y distancia. Este último resultado es el que queda en el
atributo *como_llegar* de la vista.

.. code-block:: python

        def pasos_para_llegar(self, de, hasta):
            url='http://www.ecubicle.net/driving.asmx?WSDL'
            client = Client(url)
            result = client.service.GetDirections(de, hasta)
            return result.drivingdirections.route


Template ZPT
============

El template es muy simple. Mostramos primero la forma, incluyendo los valores
de las direcciones si ya se han envíado. Después verificamos con
*tal:condition* si hay instrucciones de manejo presentes en la vista y en
caso afirmativo las mostramos en una table, utilizando *tal:repeat*. Los
atributos *value* y *_distanceToTravel* están definidos en la especificación
del servicio.

.. code-block:: html

    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en"
          lang="en"
          metal:use-macro="here/main_template/macros/master"
          i18n:domain="plonetheme.cursoplone">
    <body>
      <div metal:fill-slot="main">
        <form method="post"
              tal:attributes="action string:${portal_url}/${view/__name__}">
          <p>Desde:</p>
          <textarea name="de" tal:content="view/de|python:''">
          </textarea>
          <p>Hasta:</p>
          <textarea name="hasta" tal:content="view/hasta|python:''">
          </textarea>
          <br />
          <input type="submit" value="Como llegar" />
        </form>
        <div tal:condition="view/como_llegar|nothing">
          <table class="listing">
            <tr>
              <th colspan="2" tal:content="string:Partiendo desde: ${view/de}"></th>
            </tr>
            <tr tal:repeat="paso view/como_llegar">
              <td tal:content="paso/value"></td>
              <td tal:content="paso/_distanceToTravel"></td>
            </tr>
          </table>
        </div>
      </div>
    </body>
    </html>

Configuración
=============

Lo único que hace falta para hacer funcionar el servicio es agregar la vista
en el archivo *configure.zcml* del producto:

.. code-block:: xml

    <browser:page
        for="*"
        name="rutas"
        class=".rutas.Rutas"
        permission="zope2.View"
    />

Donde aprender más
==================

Como puede apreciarse, utilizar un servicio web desde Plone es sumamente
fácil. Para utilizar otro servicio simplemente hay que cambiar el URL y
conocer la especificación para saber qué clase de servicios existen y qué
valores regresan.

Plone también puede utilizarse para publicar servicios, utilizando z3c.soap y
Zolera. Para mayor información:

 * `z3c.soap <http://pypi.python.org/pypi/z3c.soap>`_
 * `Zolera <http://pypi.python.org/pypi/ZSI>`_


Referencia
==========

- `Obtener direcciones de manejo con SOAP`_

.. _Obtener direcciones de manejo con SOAP: http://www.plone.mx/docs/mini_soap.html
