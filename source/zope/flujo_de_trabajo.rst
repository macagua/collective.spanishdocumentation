.. -*- coding: utf-8 -*-

.. _flujo_trabajo:

================
Flujo de trabajo
================

.. contents :: :local:

Introducción
============

Esta es una introducción al flujo de trabajo de Plone y explicación de las opciones
básicas de configuración y creación de flujo de trabajos.

El editor de flujos de trabajo de Plone se encuentra dentro del ZMI de Zope,
bajo portal_workflow. Permite definir el proceso que sigue un documento desde
su creación hasta su terminación. A lo largo del proceso pueden intervenir
diversos actores y el documento puede atravesar por uno o varios estados,
dependiendo de diversas condiciones. También es necesario en ocasiones
notificar a algún usuario o grupo sobre un cambio de estado de un formulario.

Usuarios, roles y grupos
========================

Para entender el manejo de flujos del motor de workflow es necesario
comprender primero el mecanismo de usuarios del sistema. Un usuario tiene
asignados diversos permisos, pero estos permisos no se le asignan
directamente, sino a través de roles y grupos.  Los grupos a los que pertenece
cada usuario están definidos por el mecanismo de control de acceso. La
cantidad de grupos puede cambiar en cualquier momento y es posible agregar o
eliminar a un usuario de un grupo determinado utilizando la administración de
Plone. En este sentido, los grupos son variables.

Tanto a un grupo como a un usuario se le pueden asignar roles. Los roles son
estáticos, en el sentido de que agregar nuevos roles es una actividad de
desarrollo. Los permisos específicos de un usuario o grupo dependen de los
roles que tenga asignados.

Para asignar correctamente los permisos de modificación en el flujo de trabajo
es necesario conocer los roles del sistema, que son los siguientes:

`Anonymous`
    Este rol es asignado automáticamente por el motor de flujo de trabajo a cualquier
    usuario no autenticado en el sistema.
`Authenticated`
    Este rol es asignado automáticamente por el motor de flujo de trabajo a todos los
    usuarios que han sido autenticados por el sistema. Sirve para distinguir
    entre usuarios conectados y anónimos, cuando no importa el rol en sí sino
    la autenticación.
`Manager`
    Se asigna a los usuarios con permisos de administrar el sistema, agregar,
    eliminar y modificar contenido. Solo los usuarios que tienen este rol
    pueden crear formularios y editar flujos de trabajo.
`Member`
    Este rol es para distinguir entre usuarios dados de alta en el servidor de
    aplicaciones donde se ejecuta el motor de flujo de trabajo y usuarios del motor de
    workflow en sí.
`Owner`
    Este rol se asigna al creador de un formulario u otro tipo de contenido.
    Sirve para otorgar permisos especiales al dueño del contenido, como por
    ejemplo cancelar el envío del mismo.
`Reviewer`
    Este rol sirve para otorgar a un grupo o usuario permisos especiales para
    cambios de estado de un formulario, sin tener que dar permisos totales de
    manager.

Mediante la combinación de los roles descritos arriba es posible crear flujos
de trabajo complejos, donde distintos usuarios o grupos cambien sus permisos
de acceso y modificación dependiendo del estado del documento.

Estados y transiciones
======================

Los flujos del motor de workflow están basados en los conceptos de estados y
transiciones. Un formulario tiene uno o varios estados posibles, entre los
cuales puede pasar a través de transiciones activadas por los usuarios o por
el sistema, dependiendo de condiciones específicas asignadas a cada
transición.

Antes de editar un flujo es aconsejable estar seguros de los diversos estados
que puede tener el formulario en cuestión. Por ejemplo, una autorización de
vacaciones podría tener un estado inicial que asumiría al momento de su
creación, después tal vez un estado pendiente en lo que define si se autoriza
o no y finalmente un estado aceptada o rechazada dependiendo de su aprobación
o rechazo.

Para cada estado hay que definir una transición o más que nos permitan cambiar
a otro estado. Por ejemplo, en la solicitud de vacaciones podría usarse una
transición para aprobarla, y por tanto pasar de pendiente a aceptada; otra
transición distinta se usaría para pasar de pendiente a rechazada.

Hay que notar que si bien una transición dada sirve para pasar a uno y sólo un
estado determinado, es posible que más de una transición cambie a un mismo
estado, de forma tal que se puede llegar a un estado específico del formulario
pasando por diversos caminos.

Estado inicial de un flujo
==========================

Exite un estado especial para cada flujo de trabajo, que es el estado marcado
como inicial para un formulario específico. Por ejemplo, en el caso de la
solicitud de vacaciones comentado anteriormente, el estado inicial se asume al
crear el documento y sirve como punto de partida para cualquier cambio a otro
estado.

Generalmente, el estado inicial representa la creación del documento. Para
indicar al motor de flujo de trabajo cuál es el estado inicial de un flujo específico,
basta seleccionarlo en la lista de estados que aparece en la parte de arriba a
la izquierda del tab de estados y presionar el botón de estado inicial.

Propiedades de un estado
========================

Al cambiar de un estado a otro, un formulario puede redefinir una serie de
permisos que permiten otorgarle a diversos usuarios o grupos (a través de los
roles explicados arriba) algunos permisos especiales dependiendo del estado.
Por ejemplo, al momento de crear la solicitud de vacaciones, el usuario dueño
debe tener permiso de modificar el formulario, pero cuando ya envió el mismo y
se encuentra en un estado de revisión, lo mejor es que ya no pueda
modificarlo.

Este tipo de permisos se asigna en la ventana de propiedades por estado. Dicha
ventana muestra una lista breve de permisos básicos del formulario cruzada con
la lista de roles del sistema, para seleccionar uno por uno que permisos se
aplican a cada rol. Por default, se toman los permisos establecidos en el
motor de flujo de trabajo, pero casi siempre es aconsejable modificarlos para tomar en
cuenta el estado y el flujo específicos que se estén trabajando.

La lista de permisos especiales requiere mayor explicación:

`Access contents information`
    Este permiso es para que los datos publicados en las búsquedas puedan ser
    visibles para el usuario que se le asigna.
`List folder contents`
    Este permiso es para que los usuarios que lo tengan puedan ver el
    contenido de un folder del sistema.
`Modify portal content`
    Permiso para poder cambiar el contenido de un formulario. Los usuarios que
    lo tienen pueden hacer modificaciones.
`View`
    Permiso básico para poder ver un formulario.
`Change portal events`
    Este permiso no se utiliza en el motor de flujo de trabajo.

En el motor de flujo de trabajo los permisos que más se utilizarán son los de ver y
modificar contenido. Por ejemplo, a la hora de crear el formulario, el dueño
del mismo debe tener el permiso de modificar contenido. Tal vez un manager
también pueda tener este permiso, pero sería recomendable que los demás roles
no lo tuvieran. Al pasar el estado de revisión, en cambio, el dueño ya no debe
tener permiso de modificar, pero el manager debe conservarlo. Incluso, en
algunos flujos el rol reviewer podría tener el permiso también es este estado,
para actuar como editor.

Es preciso determinar con cuidado los distintos permisos que se tendrán en
cada estado para no tener agujeros de seguridad en algún flujo definido.

Propiedades de una transición
=============================

Una transición esencialmente define el cambio de un estado a otro.
Generalmente, un usuario que cumple con determinadas condiciones decide
ejecutar la transición, con lo que se pasa el formulario al nuevo estado. Las
transiciones tienen más opciones de configuración que los estados pues
representan un movimiento en el flujo y no cualquier usuario puede ejecutar
todas las transiciones.

Primero que nada, es muy recomendable colocar un título y descripción
adecuados para la transición, lo que no requiere de mayor explicación. Las
demás propiedades de la transición, sin embargo, sí la requieren y se
discuten a continuación.

`Activación de la transición`
    Hay dos maneras de activar una transición: de forma automática o manual.
    La primera es poco usual, pero podría utilizarse para ejecutar scripts sin
    cambiar de estado, por ejemplo. Usualmente será de forma manual, a través
    de la ejecución directa de usuario, como se llevará a cabo una transición,
    por lo que esta opción rara vez necesita ser modificada del valor por
    defecto.
`Scripts de la transición`
    Al ejecutar una transición es posible ejecutar un script, ya sea justo
    antes o justo después de cambiar de estado. Un script típico es para
    notificar por correo electrónico sobre cambios de estado, por lo que es
    mucho más seguro utilizar el script después de la transición.  Los scripts
    se agregan como scripts de Python normales desde el tab marcado scripts.
`Protección`
    La propiedad más importante de una transición es la protección, pues es lo
    que define que usuarios tendrán derecho a ejecutarla. El derecho de
    ejecución es lo que ocasiona que una transición determinada aparezca o no
    en el menú de opciones de un usuario específico. La protección tiene
    cuatro partes: permisos, roles, grupos y expresión. Cada una de las partes
    puede tener un valor o estar vacía. En caso de que todas estén vacías
    todos los usuarios del motor de flujo de trabajo podrán ejecutar la transición así
    definida.

    En el campo de permisos se pude incluir uno o más de los permisos
    definidos al inicio de este capítulo, utilizando el nombre completo, tal
    como aparece en la tabla de permisos. Si se desea utilizar más de uno
    deben separarse con punto y coma. Por ejemplo, si se utiliza el permiso de
    “Modify portal content”, únicamente los usuarios que tengan permiso de
    modificar el formulario podrán ejecutar la transición.

    El campo de roles es similar al de permisos, pero utiliza los roles
    definidos al inicio del capítulo, como Manager o Owner. Es común, por
    ejemplo, que una transición para cancelar el envío de un formulario sea
    reservada solamente al usuario creador de contenido (Owner) por lo que
    colocando ese rol en este espacio se asegura que solo el dueño del
    formulario pueda retractarlo.

    En el campo de grupos se puede colocar cualquier grupo definido en el
    control de acceso. Si se desea, por ejemplo, que solo los miembros del
    grupo de soporte reciban una petición de ayuda, se deberá definir primero
    el grupo y luego utilizar el mismo nombre en este espacio, con lo que
    cualquier miembro del grupo tendrá derecho a ejecutar la transición.

    Finalmente, el mecanismo más poderoso para proteger una transición es el
    de expresión, el cual acepta expresiones de todo tipo en el lenguaje
    Python. Solo cuando la expresión definida sea verdadera se tendrá derecho
    a ejecutar la transición protegida por ella.



Referencias
===========

-   `Flujo de trabajo`_ desde la comunidad Plone Mexico.

.. _Flujo de trabajo: http://www.plone.mx/docs/workflow.html
