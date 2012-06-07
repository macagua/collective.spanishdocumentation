.. -*- coding: utf-8 -*-

=========================
Base de datos SQL y Plone
=========================

.. contents :: :local:

Existen muchos mecanismos de conexión a base de datos SQL desde Plone CMS, en este articulo se enfoca en la amplia usada libreria `SQLAlchemy`_ y sus mecanismos de integracion.

¿Qué es SQLAlchemy?
===================

`SQLAlchemy`_, es un toolkit de SQL en Python para hacer mapas de objetos relacionales (`ORM`_ - Object Relational Mapper) que le permite a los desarrolladores de aplicaciones incorporar toda la potencia e flexibilidad del estándar SQL.

¿Qué son los ZSQL Methods?
==========================

Del ingles `ZSQL Methods`_, los métodos ZSQL son un objeto similar a un método `DTML`_ de `Zope`_ o scripts de Python especializados para su uso con bases de datos relacionales. Son la forma más fácil de conectar `RDBMS`_ en Zope. Contiene comandos SQL y DTML en combinación.

Productos disponibles en Plone
==============================

 * Alchemist
 * collective.saconnect
 * collective.lead
 * **z3c.saconfig**

Configuración
=============

 * La configuración de la conexión se realiza en el fichero configure.zcml. 
 * Se usan la utilidad global y utilidad local.
 * Pueden ser configuradas como conexiones globales - por una instancia de Zope. 
 * O locales para cada sitio Plone.
 
Configuración ZCML
==================

A continuación un ejemplo del archivo ``configure.zcml``:

.. code-block:: xml

    <include package="z3c.saconfig" file="meta.zcml"/>
    <db:engine name="cliente1_registros" 
               url="postgresql://usuario:contrasena@127.0.0.1/db_cliente1_registros?charset=utf8" />
    <db:session name="cliente1.registros" engine="cliente1_registros" />

Configuración del paquete
=========================

A continuación un ejemplo del archivo ``config.py``:

.. code-block:: python

    from sqlalchemy.ext.declarative import declarative_base
    from z3c.saconfig import named_scoped_session
    
    Base = declarative_base()
    SCOPED_SESSION_NAME = 'cliente1.registros'
    session = named_scoped_session(SCOPED_SESSION_NAME)


Interfaces del paquetes
=======================

A continuación un ejemplo del archivo ``interfaces.py``:

.. code-block:: python

    from zope import interface, schema
    from cliente1.registros import MessageFactory as _
    
    class IProject(interface.Interface):
        """Defines Project form interface.
        """
        fullname = schema.TextLine(
            title=_(u'Project name'),
            required=True)
        
        email = schema.TextLine(
            title=_(u"Project e-mail"),
            required=True)
        
        type = schema.Choice(
            title=_(u'Category'),
            vocabulary=vocabulary.member_types,
            default='profissional',
            description=_(u'''Please select a project category.'''),
            required=True)
            
        status = schema.TextLine(
            title=_(u'Project status'),
            required=True)
            
        created_date = schema.TextLine(
            title=_(u'Project created date'),
            required=True)
        
        organization = schema.TextLine(
            title=_(u'Organization'),
            description=_(u'Please advise which organization '\
                'you belong. eg company, university or entity.'),
            required=False)

Mapeo objeto-relacional de la tabla
===================================

A continuación un ejemplo del archivo ``models.py``:

.. code-block:: python

    import datetime
    import sqlalchemy as sa

    from cliente1.registros.config import Base

    class Project(Base):
        """A project"""
        
        implements(IProject)
        __tablename__ = 'project'
        
        id = Column(sa.Integer,nullable=False,index=True,primary_key=True)
        fullname = Column(sa.String(64))
        email = Column(sa.String(64), unique=True)
        type = Column(sa.String(64))
        status = Column(sa.String(64), default='pending')
        created_date = Column(sa.DateTime, default=datetime.datetime.now())
        organization = Column(sa.String(255))
        

Formulario CRUD
===============

El objetivo general de z3c.form y hacer que el desarrollo de formularios lo más 
simples posible, mientras que proporciona hooks para permitir la personalización 
de los formularios en cualquier nivel de acuerdo a las necesidades reales de 
los diferentes casos de uso. 

Los principales componentes (módulos):

form
    formularios base: Form, AddForm, EditForm, DisplayForm
    
groups
    formularios compuestos de los grupos de campos (fieldsets)

subform
    formularios anidados

field
    API para manipulación de los campos del formulario
    
button
    API para manipulación de los botones del formulario

validator
    API para la validación de los datos del formulario

widget
    API para la creación de los widgets

action
    API para definición e manipulación de actions handlers

procesamento del formulario
---------------------------

A continuacion los elementos principales del procesamento del formulario:

self.request
    objeto que representa la actual solicitud HTTP
    
self.context
    Elemento relacionado al formulario según el contexto en el que se invoca;
    
self.getContent()
    Los objetos sacados de contexto y que serán manejado por el formulario, a menos ignoreContext se establece en True;
    
self.status
    El mensaje se mostrará en la parte superior de la región de Contenido cuando el formulario se representa.
    
updateWidgets
    actualizaciones de todos los widgets de acuerdo a los datos enviados.
    
updateActions
    invoca los actions handlers del formulariode acuerdo con el boton presionado
    
render
    invoca la plantilla Padre que genera el formulario HTML y devuelve dicho contenido



Creación de la base de datos
============================

Para esto se usa la receta zc.buildout llamada collective.recipe.pgcreatedb el cual crea una base de datos Postgresql a través de SQLAlchemy, a continuación ejemplo de su configuración:

.. code-block:: cfg

    [buildout]
    parts =  
        ...
        rdbs-requeriments
        rdbs-createdb
    ...
    # This recipe helps to install Postgresql pre-requeriments
    # For options see http://pypi.python.org/pypi/plone.recipe.command
    [rdbs-requeriments]
    recipe = plone.recipe.command
    command = 
        sudo aptitude install -y postgresql postgresql-server-dev-all libpq-dev phppgadmin
    stop-on-error = false
    update-command = ${rdbs-requeriments:command} 
    ...
    # This recipe helps to create a database Postgresql with SQLAlchemy
    # For options see https://svn.plone.org/svn/collective/collective.recipe.pgcreatedb/trunk
    [rdbs-createdb]
    recipe = collective.recipe.pgcreatedb
    default-template = template1
    user = postgres
    password = postgres
    database = db_cliente1_registros
    host = 127.0.0.1
    create-tables = off
    eggs = ${instance:eggs}
    extra-paths  =  ${buildout:parts-directory}/
    ...

En la sección buildout llamada ``rdbs-requeriments`` instala el servidor postgresql con sus librerías de desarrollo y adicionalmente instala phppgadmin para la gestion remota del mismo.

En la sección buildout llamada ``rdbs-createdb`` crea crea una base de datos Postgresql a través de SQLAlchemy.

Creación de las tablas
======================

A continuación se demuestra un ejemplo del archivo ``import_steps.xml`` para la creación de las tablas:

Perfil de importación Generic Setup
-----------------------------------

 * La creación de las tablas se lleva a cabo al disparar el perfil de importación del producto.
 * El archivo **import_steps.xml**

.. code-block:: xml

    <?xml version="1.0"?>
    <import-steps>
        <import-step id="identificador-create_tables" version="20101020-11"
                     handler="cliente1.registros.setuphandlers.create_tables"
                     title="Create Base Tables">
            <dependency step="toolset" />
        </import-step>
    </import-steps>


Lanzador del perfil de importación
----------------------------------

A continuación un ejemplo del archivo ``setuphandlers.py``:

.. code-block:: python

    from z3c.saconfig import named_scoped_session
    from cliente1.registros.config import Base
    from cliente1.registros.config import SCOPED_SESSION_NAME
    
    Session = named_scoped_session(SCOPED_SESSION_NAME)

    class create_tables(context):
        '''Called at profile import time to create necessary tables'''
        
        if isNotOurProfile(context):
            return
        
        Base.metadata.create_all(bind=Session.bind)
        
Referencias
===========
 * http://readthedocs.org/docs/plone-spanish-docs/en/latest/plone/mini_db.html
 * https://github.com/pythonbrasil/apyb.members
 * http://www.slideshare.net/simplesconsultoria/sqlalchemy-e-plone-no-more-zsql-methods
 * http://www.slideshare.net/rudaporto/formulrios-para-plone-um-passeio-pelo-framework-z3cform
 
.. _SQLAlchemy: http://www.sqlalchemy.org/
.. _ORM: http://es.wikipedia.org/wiki/ORM
.. _RDBMS: http://es.wikipedia.org/wiki/RDBMS
.. _ZSQL Methods: http://wiki.zope.org/zope2/ZSQLMethods
.. _DTML: http://wiki.zope.org/zope2/DTML
.. _Zope: http://www.zope.org/

..
  .. _: 
