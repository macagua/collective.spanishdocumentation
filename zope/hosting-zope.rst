.. -*- coding: utf-8 -*-

=========================
Configuraciones generales
=========================

La siguientes son configuraciones adicionales al servidor Zope que son de gran utilidad:

Zona horaria
============

Debe agregar en la sección [instance] en su archivo de configuración de buildout.cfg: 

.. code-block:: cfg

  zope-conf-additional=
      <environment>
          TZ America/Caracas
      </environment>

