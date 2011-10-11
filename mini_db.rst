.. -*- coding: utf-8 -*-

=====================================================
Presentar información de una base de datos relacional
=====================================================

Demostración de como conectarse a una base de datos relacional desde una
vista de Plone, utilizando ``SQLAlchemy`` y ``SQLite``.

Requisitos previos
==================

Se necesita tener instalada una base de datos relacional, incluyendo las
librerías de desarrollo. En este ejemplo se utiliza ``SQLite``. Necesitamos
también el driver de SQL para Python y ``SQLAlchemy``, que es una librería para
generalizar y facilitar al acceso a diversas bases de datos.

Para este ejemplo, es necesario agregar los siguientes paquetes a la sección
de eggs en el buildout:

.. code-block:: cfg

    eggs = 
        ...
        SQLAlchemy
        zope.sqlalchemy
        pysqlite
        ...

Vista Python
============

Primero definimos una vista que se conectará a ``SQLite``:

.. code-block:: python

    from sqlalchemy import *
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import scoped_session, sessionmaker, relation
    from zope.sqlalchemy import ZopeTransactionExtension
    import transaction

    from Products.Five import BrowserView
    from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

    TEST_DSN = 'sqlite:///usuarios.db'
    Base = declarative_base()

    class User(Base):
        __tablename__ = 'test_users'
        id = Column('id', Integer, primary_key=True)
        name = Column('name', String(50))
        addresses = relation("Address", backref="user")

    class Address(Base):
        __tablename__ = 'test_addresses'
        id = Column('id', Integer, primary_key=True)
        email = Column('email', String(50))
        user_id = Column('user_id', Integer, ForeignKey('test_users.id'))

    engine = create_engine(TEST_DSN, convert_unicode=True)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    Session = scoped_session(sessionmaker(bind=engine,
                                          extension=ZopeTransactionExtension()
    ))
    session = Session()
    session.add(User(name='bob'))
    session.add(User(name='joe'))
    bob = session.query(User).all()[0]
    bob.addresses.append(Address(email='bob@bob.bob'))
    joe = session.query(User).all()[1]
    bob.addresses.append(Address(email='joe@joe.joe'))
    transaction.commit()

    class DB(BrowserView):
        """
        Obtener usuarios de base de datos
        """

        template = ViewPageTemplateFile('db.pt')

        def __init__(self, context, request):
            self.context = context
            self.request = request

        def __call__(self):
            session = Session()
            self.users = session.query(User).all()
            return self.template()


Template ZPT
============

En el template de ``ZPT``, simplemente presentamos las filas de datos:

.. code-block:: html

    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en"
          lang="en"
          metal:use-macro="here/main_template/macros/master"
          i18n:domain="plonetheme.cursoplone">
    <body>
      <div metal:fill-slot="main">
        <div tal:condition="view/users|nothing">
          <table class="listing">
            <tr>
              <th>Usuario</th>
              <th>Email</th>
            </tr>
            <tr tal:repeat="user view/users">
              <td><p tal:content="user/name"></p></td>
              <td><p tal:repeat="address user/addresses"
                     tal:content="address/email"></p>
              </td>
            </tr>
          </table>
        </div>
      </div>
    </body>
    </html>

Configuración
=============

La configuración de la vista es como sigue:

.. code-block:: xml

    <browser:page
        for="*"
        name="db"
        class=".db.DB"
        permission="zope2.View"
    />


Referencia
==========

- `Presentar información de una base de datos relacional`_

.. _Presentar información de una base de datos relacional: http://www.plone.mx/docs/mini_db.html

