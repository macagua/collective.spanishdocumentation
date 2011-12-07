.. -*- coding: utf-8 -*-

==============================================================
Registrar niveles de arranque en el programa de inicio a Plone
==============================================================

.. contents :: :local:

Introducción
============

Cuando se realizan `instalaciones unificadas de Plone`_ o desde **proyectos de Buildout** 
como usuario **"root"** en `Debian GNU/Linux`_ o distribuciones basadas en Debian como
`Ubuntu Linux`_, `Canaima GNU/Linux`_, entre otras, es muy común hay que
configurar tu instalación como servicio para cada ves que arranque el sistema
operativo inicie el servicio de Zope que sirve a nuestro(s) portal(es) de
Plone.


Paso a paso
===========

Para este caso de uso es necesario seguir los siguientes pasos:


Realice un enlace simbólico del script de servicio de Zope desde directorio
de instalación al directorio de arranque de los servicios (demonios) con el siguiente comando: 

.. code-block:: sh

  # ln -s /usr/local/Plone/zinstance/bin/plonectl /etc/init.d/plonectl

Otorgue permisos de ejecución al scrtip con el siguiente comando: 

.. code-block:: sh

  # chmod +x /usr/local/Plone/zinstance/bin/plonectl

Acceda al directorio de arranque de los servicios (demonios) con el siguiente comando: 

.. code-block:: sh

  # cd /etc/init.d/

Registre este servicio en los niveles de arranque por defecto, estos niveles
son los mismo que utiliza el `paquete nativo de Zope en Debian`_ con el siguiente comando: 

.. code-block:: sh

  # update-rc.d plonectl defaults

Inicie / Reinicie / Detenga el servicio Zope desde el directorio de arranque
de sus sistema con el siguiente comando: 

.. code-block:: sh

  # /etc/init.d/plonectl start
  ...
  # /etc/init.d/plonectl stop

De esta forma ya tienes configurado como un servicio en los niveles de
arranque por defecto de tu sistema y si reinicia, debería arrancar
automáticamente el servicio y acceder por medio del navegador a su sitio
Plone.


Referencias
===========

-   `How-To Managing services with update-rc.d`_
-   `Editor de niveles de ejecución en Debian`_

.. _instalaciones unificadas de Plone: http://plone.org/countries/conosur/documentacion/instalando-plone-3-con-el-instalador-unificado
.. _Debian GNU/Linux: http://es.wikipedia.org/wiki/Debian
.. _Ubuntu Linux: http://es.wikipedia.org/wiki/Ubuntu
.. _Canaima GNU/Linux: http://es.wikipedia.org/wiki/Canaima_%28distribuci%F3n_Linux%29
.. _paquete nativo de Zope en Debian: http://packages.debian.org/search?keywords=zope
.. _How-To Managing services with update-rc.d: http://www.debuntu.org/how-to-manage-services-with-update-rc.d
.. _Editor de niveles de ejecución en Debian: http://www.solusan.com/como-va-update-rcd-niveles-de-ejecucion-en-debian.html
