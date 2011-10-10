.. -*- coding: utf-8 -*-

Virtual hosting
---------------

Zope tiene un componente llamado `VirtualHostMonster`_ el cual hace el mapeo de 
host virtuales dentro de Zope 


Suprimiendo virtual host monster
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

En el caso de que usted ha establecido reglas de virtual hosting de modo 
que ya no se Zope le permiten acceder a la interfaz de gestión, puede agregar
_SUPPRESS_ACCESSRULE" a la URL para desactivar VirtualHostMonster.


.. _VirtualHostMonster: https://plone.dcri.duke.edu/info/faq/vhm
