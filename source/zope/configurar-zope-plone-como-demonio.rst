.. -*- coding: utf-8 -*-

.. _configurar_zope_como_demonio:

==================================================
Configurar Zope y Plone como un demonio / servicio
==================================================

.. contents :: :local:

Descripción general
===================

Cuando se realizan `instalaciones unificadas de Plone`_ o desde **proyectos de Buildout** 
como usuario **"root"** en `Debian GNU/Linux`_ o distribuciones basadas en Debian como
`Ubuntu Linux`_, `Canaima GNU/Linux`_, entre otras, es muy común hay que configurar dicha 
instalación como demonio servicio para poder administrar de forma más eficiente 
el arranque del servidor Zope en el sistema operativo huésped para que sirva los diversos 
portal(es) Plone.

Términos básicos
================

.. glossary::

  Demonio / Servicio
    Es un tipo especial de proceso informático no interactivo, es decir, que se ejecuta un programa en segundo plano en vez de ser controlado
    directamente por el usuario. Este tipo de programas se ejecutan de forma continua (infinita), vale decir, que aunque se intente cerrar o 
    matar el proceso, este continuará en ejecución o se reiniciará automáticamente. Todo esto sin intervención de terceros y sin dependencia 
    de consola alguna.

    Los demonios suelen tener las siguientes características:

    * No disponen de una "interfaz" directa con el usuario, ya sea gráfica o textual.
    * No hacen uso de la entradas y salidas estándar para comunicar errores o registrar su funcionamiento, sino que usan archivos del sistema en zonas especiales (``/var/log/`` en los `UNIX`_ más modernos) o utilizan otros demonios especializados en dicho registro como el `syslogd`_.


Paso a paso
===========

Para el caso de configuración de Debian Lenny, es necesario seguir los siguientes pasos:


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
.. _UNIX: http://es.wikipedia.org/wiki/UNIX
.. _syslogd: http://es.wikipedia.org/wiki/Syslogd
.. _paquete nativo de Zope en Debian: http://packages.debian.org/search?keywords=zope
.. _How-To Managing services with update-rc.d: http://www.debuntu.org/how-to-manage-services-with-update-rc.d
.. _Editor de niveles de ejecución en Debian: http://www.solusan.com/como-va-update-rcd-niveles-de-ejecucion-en-debian.html
