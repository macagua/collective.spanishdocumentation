.. -*- coding: utf-8 -*-

========================================================
Crear gráficas a partir de datos de un tipo de contenido
========================================================

En este ejemplo utilizaremos un tipo de contenido de Plone para capturar
información y crearemos una vista para el tipo donde se muestre una gráfica
de pastel que refleje los datos capturados.

Requisitos previos
==================

Para definir el tipo de contenido, agregaremos dos productos a la sección
de eggs del buildout, que nos permitirán utilizar una tabla para capturar 
la información y seleccionar el color de la gráfica:

.. code-block:: cfg

    eggs = 
        ...
        Products.SmartColorWidget
        Products.DataGridField<=1.7
        ...

Google ofrece una serie de APIs muy útiles para el desarrollo web. En este
caso, utilizaremos el servicio de Charts. No se requiere instalar nada en
Plone para usarlo.

Tipo de contenido
=================

En el tipo de contenido incluimos un campo para el color general de la
gráfica y una tabla para capturar información, utilizando los widgets y
campos que agregamos al buildout.

.. code-block:: python

    from zope.interface import implements

    from Products.Archetypes import atapi
    from Products.ATContentTypes.content import base
    from Products.ATContentTypes.content import schemata

    from Products.SmartColorWidget.Widget import SmartColorWidget
    from Products.DataGridField import DataGridField, DataGridWidget
    from Products.DataGridField.Column import Column

    from tic.contenido.interfaces import IEjemplodeTipo
    from tic.contenido.config import PROJECTNAME

    EjemplodeTipoSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

        atapi.StringField(
            'color',
            storage=atapi.AnnotationStorage(),
            default='#ffffff',
            widget=SmartColorWidget(
                label=_(u"Color"),
                description=_(u"Seleccione el color"),
            ),
        ),

        DataGridField('ingresosPresupuestoProyectado',
            searchable=True,
            required=True,
            allow_empty_row=False,
            fixed_rows=None,
            columns=("concepto", "valor", "porcentaje"),
            default=({'concepto': '', 'valor': '', 'porcentaje': ''},),
            widget=DataGridWidget(
                    label=_(u"Ingresos del presupuesto proyectado"),
                    columns={
                        'concepto': Column("concepto"),
                        'valor': Column("valor"),
                        'porcentaje': Column("porcentaje"),
                    },
            ),
        ),

    ))

    schemata.finalizeATCTSchema(EjemplodeTipoSchema, moveDiscussion=False)

    class EjemplodeTipo(base.ATCTContent):
        """Ejemplo"""
        implements(IEjemplodeTipo)

        meta_type = "EjemplodeTipo"
        schema = EjemplodeTipoSchema

    atapi.registerType(EjemplodeTipo, PROJECTNAME)

Vista Python
============

A continuación generamos una vista exclusiva para este tipo de contenido,
donde mostraremos la gráfica generada.

.. code-block:: python

    from Products.Five import BrowserView
    from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

    class TipoEjemploView(BrowserView):

        template = ViewPageTemplateFile('tipoejemplo.pt')

        def __init__(self, context, request):
            self.context = context
            self.request = request

        def __call__(self):
            return self.template()

        def apiCallString(self):
            """
            tomar valores de la tabla y crear string para img
            """
            api_template = "http://chart.apis.google.com/chart?cht=p3&chd=t:%s&chs=650x250&chl=%s&chdl=%s&chtt=%s&chts=%s,32&chco=%s"
            data = self.context.getIngresosPresupuestoProyectado()
            labels = [row['concepto'] for row in data]
            data_labels = [row['valor'] for row in data]
            values = [row['porcentaje'] for row in data]
            return api_template % (','.join(values),
                '|'.join(data_labels),
                '|'.join(labels),
                self.context.schema['ingresosPresupuestoProyectado'].widget.label,
                self.context.getColor()[1:],
                self.context.getColor()[1:],
               )

Template ZPT
============

El template es muy simple, porque únicamente pasamos a una imagen el URL
generado por la vista.

.. code-block:: html

    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en"
          lang="en"
          metal:use-macro="here/main_template/macros/master"
          i18n:domain="plonetheme.cursoplone">
    <body>
      <div metal:fill-slot="main">
        <h1 tal:content="here/title"></h1>
        <img tal:attributes="src view/apiCallString" />    
      </div>
    </body>
    </html>

Configuración
=============

Configuramos la vista para usarla solamente con nuestro tipo de ejemplo:

.. code-block:: xml

    <browser:page
        for="..interfaces.IEjemploDeTipo"
        name="tipoejemplo_view"
        class=".tipoejemplo.TipoEjemploView"
        permission="zope2.View"
    />


Referencia
==========

- `Crear gráficas a partir de datos de un tipo de contenido`_

.. _Crear gráficas a partir de datos de un tipo de contenido: http://www.plone.mx/docs/mini_gcharts.html

