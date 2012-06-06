.. -*- coding: utf-8 -*-

.. _configuraciones_generales:

=========================
Configuraciones generales
=========================

.. contents :: :local:

La siguientes son configuraciones adicionales al servidor Zope que son de gran utilidad:

Zona horaria
============

Debe agregar en la sección **[instance]** en su archivo de configuración de ``buildout.cfg``: 

.. code-block:: cfg

  zope-conf-additional=
      <environment>
          TZ America/Caracas
      </environment>


Habilitar los idiomas necesarios en Plone
=========================================

Si solo necesita ofrecer soporte a i18n para N. numero de idiomas en específicos usted puede configurar esto agregando en la sección **[instance]** en su archivo de configuración de ``buildout.cfg``:

.. code-block:: cfg

  environment=
      PTS_LANGUAGES=en es pt

De esta forma se esta habilitando el soporte a los idiomas Ingles, Español y Portugués, estoy puede ser muy conveniente por que ahorra recursos computo al momento de iniciar su instancias Zope.
