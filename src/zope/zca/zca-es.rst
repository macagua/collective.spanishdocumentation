===================================
Arquitectura de Componentes de Zope
===================================

:Author: Baiju M
:Version: 0.5.6
:Printed Book: `http://www.lulu.com/content/1561045
                    <http://www.lulu.com/content/1561045>`_
:PDF en linea: `http://www.muthukadan.net/docs/zca.pdf
                  <http://www.muthukadan.net/docs/zca.pdf>`_
:Traductor(es): Lorenzo Gil Sanchez <lgs@sicem.biz> ; Leonardo J. Caballero G. <leonardocaballero@gmail.com> 2011
:URL en español: `http://www.muthukadan.net/docs/zca-es.pdf
                  <http://www.muthukadan.net/docs/zca-es.pdf>`_

Todos los derechos (C) 2007,2008 Baiju M <baiju.m.mail AT gmail.com>.

Se permite la copia, distribución y/o modificación de este documento
bajo los términos de la Licencia de Documentación Libre GNU, Versión
1.2 o (si lo prefiere) cualquier otra versión posterior publicada por
la Free Software Foundation.

El código fuente en este documento está sujeto a la Licencia
Pública Zope, Versión 2.1 (ZPL).

EL CÓDIGO FUENTE EN ESTE DOCUMENTO SE OFRECE "TAL CUAL" Y ...

THE SOURCE CODE IN THIS DOCUMENT IS PROVIDED "AS IS" AND ANY AND ALL
EXPRESS OR IMPLIED WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST
INFRINGEMENT, AND FITNESS FOR A PARTICULAR PURPOSE.

.. note::

  Gracias a Kent Tenney (Wisconsin, USA) y Brad Allen (Dallas, USA)
  por sus sugerencias.

  Muchas personas me han ayudado a escribir este libro.  EL borrador inicial fue
  revisado por mi colleague Brad Allen.  Cuando yo anuncie este libro
  a través de mi blog, I got many encouraging comments to proceed con
  este trabajo.  Kent Tenney edito la mayor parte del libro, el tambien
  escribio de nuevo la aplicación ejemplo.  Muchos otros me enviaron correcciones y
  comentarios including, Lorenzo Gil Sanchez, Michael Haubenwallner,
  Nando Quintana, Stephane Klein, Tim Cook, Kamal Gill y Thomas
  Herve.  Lorenzo tradujo este trabajo al Español y Stephane
  tranducii este al Frances.  Gracias a todos !

.. contents::


Primeros pasos
---------------

Introducción
~~~~~~~~~~~~

Desarrollar un sistema software grande es siempre muy complicado.  Se
ha visto que un enfoque orientado a objetos para el análisis, diseño
y programación funciona bien al tratar con sistemas grandes.  El diseño
basado en componentes, y la programación utilizando componentes se
están haciendo muy populares últimamente.  Hay muchos marcos de trabajo
que soportan el diseño basado en componentes en diferentes lenguajes,
algunos incluso son neutrales con respecto al lenguaje. Ejemplos de
esto son el COM de Microsoft y el XPCOM de Mozilla.

La Arquitectura de Componentes de Zope (ZCA) es un marco de trabajo
en Python que soporta el diseño y la programación basada en componentes.
La ZCA funciona muy bien al desarrollar sistemas de software grandes en
Python.  La ZCA no es específica al servidor de aplicaciones Zope, se
puede utilizar para desarrollar cualquier aplicación Python. Quizás
debería llamarse la `Arquitectura de Componentes de Python`.

Hay dos paquetes principales relacionados con la arquitectura de
componentes de Zope:

  - ``zope.interface`` utilizado para definir la interfaz de un 
    componente.

  - ``zope.component`` se encarga de registrar y recuperar
    componentes.

El objetivo fundamental de la arquitectura de componentes de Zope es
utilizar objetos Python de forma eficiente. Los componentes son objetos
reusables con introspección para sus interfaces. Un componente provee
una interfaz implementada en una clase, o cualquier objeto llamable.
No importa cómo se implemente el componente, lo que importa es
que cumpla los contratos definidos en su interfaz. Utilizando la
arquitectura de componentes de Zope puedes distribuir la complejidad
de sistemas entre varios componentes cooperantes. La arquitectura de
componentes de Zope te ayuda a crear dos tipos básicos de componentes:
`adaptador` y `utilidad`.

Recuerda, la ZCA no trata sobre los componentes en sí mismo, sino sobre
la creación, registro y recuperación de los componentes.  Recuerda
también, un `adaptador` es una clase Python normal (o una fábrica en
general) y una `utilidad` es un objeto llamable Python normal.

El marco de trabajo de la ZCA se desarrolla como parte del proyecto Zope 3.  La ZCA, como ya se ha mencionado, es un marco de trabajo
puramente Python, por tanto se puede utilizar en cualquier tipo de
aplicación Python.  Actualmente ambos proyectos Zope 3 y Zope 2 utilizan
este marco de trabajo extensívamente.  Hay otros muchos proyectos
incluyendo aplicaciones no web que utilizan la Arquitectura de
Componentes de Zope [#projects]_.

.. [#projects] http://wiki.zope.org/zope3/ComponentArchitecture


Una breve historia
~~~~~~~~~~~~~~~~~~

El proyecto del marco de trabajo ZCA comenzó en 2001 como parte del
proyecto Zope 3.  Fue tomando forma a partir de las lecciones aprendidas
al desarrollar sistemas software grandes usando Zope 2. Jim Fulton fue
el jefe de proyecto de este proyecto. Mucha gente contribuyó al diseño
y a la implementación, incluyendo pero sin limitarse a, Stephan
Richter, Philipp von Weitershausen, Guido van Rossum (también conocido
como *Python BDFL*), Tres Seaver, Phillip J Eby y Martijn Faassen.

Inicialmente la ZCA definía componentes adicionales; `servicios` y
`vistas`, pero los desarrolladores se dieron cuenta de que la utilidad
podía sustituir `servicio` y el multi-adaptador podía sustituir `view`.
Ahora la ZCA tiene un número muy pequeño de tipos de componentes
principales: utilidades, adaptadores, subscriptores y manejadores. En
realidad, subscriptores y manejadores son dos tipos especiales de
adaptadores.

Durante el ciclo de la versión Zope 3.2, Jim Fulton propuso una gran
simplificación de la ZCA [#proposal]_.  Con esta simplificación se creó
una nueva interfaz única (`IComponentRegistry`) para registrar
componentes locales y globales.

.. [#proposal] http://wiki.zope.org/zope3/LocalComponentManagementSimplification

El paquete ``zope.component`` tenía una larga lista de dependencias,
muchas de las cuales no eran necesarias para una aplicación no Zope 3.
Durante la PyCon 2007, Jim Fulton añadió la característica
``extras_require`` de setuptools para permitir la separación de la
funcionalidad básica de la ZCA de las características adicionales [#extras]_.

.. [#extras] http://peak.telecommunity.com/DevCenter/setuptools#declaring-dependencies

Hoy el proyecto de la ZCA es un proyecto independiente con su propio
ciclo de versiones y su repositorio Subversion.  Sin embargo, los problemas y los errores aún se controlan como parte del proyecto
Zope 3 [#bugs]_, y la lista principal zope-dev se utiliza para los
debates de desarrollo [#discussions]_.  Allí tmbien esta otra lista general de usuario para Zope 3 (`zope3-users`) la cual puede ser usada para cualquier consulta acerca del ZCA [#z3users]_.

.. [#bugs] https://bugs.launchpad.net/zope3
.. [#discussions] http://mail.zope.org/mailman/listinfo/zope-dev
.. [#z3users] http://mail.zope.org/mailman/listinfo/zope3-users

Instalación
~~~~~~~~~~~

El paquete ``zope.component``, junto con el paquete ``zope.interface``
son el núcleo de la arquitectura de componentes Zope.  Ofrecen
facilidades para definir, registrar y buscar componentes.  El paquete
``zope.component`` y sus dependencias están disponibles en formato
egg (huevo) desde el Índice de Paquetes Python (PyPI)  [#pypi]_.

.. [#pypi] Repository of Python packages: http://pypi.python.org/pypi

Puedes instalar ``zope.component`` y sus dependencias utilizando
`easy_install` [#easyinstall]_ ::

  $ easy_install zope.component

.. [#easyinstall] http://peak.telecommunity.com/DevCenter/EasyInstall

Este comando descargará ``zope.component`` y sus dependencias desde
PyPI y los instalará en tu ruta Python.

Alternativamente, puedes descargar ``zope.component`` y sus
dependencias desde PyPI y luego instalarlos.  Instala los paquetes en
el siguiente orden.  En Windows, puede que necesitas los paquetes
binarios de ``zope.interface`` y ``zope.proxy``.

  1. ``zope.interface``
  2. ``zope.proxy``
  3. ``zope.deferredimport``
  4. ``zope.event``
  5. ``zope.deprecation``
  6. ``zope.component``

Para instalar estos paquetes, después de haberlos descargados, puedes
utilizar el comando ``easy_install`` con los huevos como argumento.  (También puedes darle todos estos huevos como argumneto en la misma
linea.)::

  $ easy_install /path/to/zope.interface-3.4.x.tar.gz
  $ easy_install /path/to/zope.proxy-3.4.x.tar.gz
  ...

Usted tambien puede instalar esos paquetes despues extrayendolos cada uno separadamente.  Por ejemplo::

  $ tar zxvf /path/to/zope.interface-3.4.x.tar.gz
  $ cd zope.interface-3.4.x
  $ python setup.py build
  $ python setup.py install

Esos metodos instalarán el ZCA en el `Python de su sistema`, en el directorio ``site-packages``, el cual puede causar problemas.  En un correo enviado a la lista de Zope 3, Jim Fulton recomendaba en ves de usar el Python del sistema [#systempython]_.  ``virtualenv`` y/o ``zc.buildout`` son herramientas que instalan la
ZCA en un entorno de trabajo aislado. Esto es una buena práctica
para experimentar con código y el estar familiarizado con estas
herramientas será beneficioso para desarrollar e implantar
aplicaciones.

.. [#systempython] http://article.gmane.org/gmane.comp.web.zope.zope3/21045


Experimentando con código
~~~~~~~~~~~~~~~~~~~~~~~~~

Hay dos buenos paquetes en Python para definir entornos de trabajos ahislados para desarrollos de aplicaciones Python.  ``virtualenv``
creado por Ian Biking y ``zc.buildout`` creado por Jim Fulton son estos dos paquetes.  Usted puede tambien usar esos paquetes juntos.  Usando esos paquetes usted puede instalar ``zope.component`` y otras dependencias dentro de un entorno de trabajo aislado.  Es es una buena practica para experimentar con cualquier código Python, y familiarizarse con
esas herramientas será benefisioso con el desarrollo y implementaciones de aplicaciones.

Usted puede instalar ``virtualenv`` usando ``easy_install``::

  $ easy_install virtualenv

Ahora crea un nuevo entorno así::

  $ virtualenv miev

Esto creará un nuevo entorno virtual en el directorio ``miev``.
Ahora, desde dentro del directorio ``miev``, puedes instalar
``zope.component`` y sus dependencias utilizando el ``easy_install``
que hay dentro del directorio ``miev/bin``::

  $ cd miev
  $ ./bin/easy_install zope.component

Ahora puedes importar ``zope.interface`` y ``zope.component`` desde
el nuevo intérprete ``python`` dentro del directorio ``miev/bin``::

  $ ./bin/python

Este comando ejecutará un intérprete de Python que puedes usar
para ejecutar el código de este libro.

Utilizando ``zc.buildout`` con la receta ``zc.recipe.egg`` se
puede crear un intérprete de Python con los huevos Python especificados.  Primero instala ``zc.buildout`` usando el comando ``easy_install``.  (Puedes hacerlo también dentro de un entorno virtual).  Para crear un nuevo buildout para experimentar con huevos Python, primero crea un
directorio e inicialízalo  usando el comando ``buildout init``::

  $ mkdir mibuildout
  $ cd mibuildout
  $ buildout init

Ahora el nuevo directorio ``mibuildout`` es un buildout.  El archivo
de configuración predeterminado de buildout es `buildout.cfg` .  Después
de la inicialización, tendrá el siguiente contenido::

  [buildout]
  parts =

Puedes cambiarlo a::

  [buildout]
  parts = py

  [py]
  recipe = zc.recipe.egg
  interpreter = python
  eggs = zope.component

Ahora ejecuta el comando ``buildout`` disponible dentro del directorio
``mibuildout/bin`` sin ningún argumento.  Esto creará un nuevo intérprete
Python dentro del directorio ``mibuildout/bin``::

  $ ./bin/buildout
  $ ./bin/python

Este comando ejecutará un intérprete de Python que puedes usar
para ejecutar el código de este libro.


Un ejemplo
----------


Introducción
~~~~~~~~~~~~

Considera una aplicación de gestión para registrar los huéspedes que se
hospedan en un hotel. Python puede implementar esto de varias formas
distintas.  Empezaremos con un mirada breve a un enfoque procedural, y
después cambiaremos a un enfoque orientado a objetos básico.  Mientras
examinamos el enfoque orientado a objetos, veremos como como podemos
beneficiarnos de los patrones de diseño clásicos, `adaptador` e
`interface`.  Esto nos llevará al mundo de la Arquitectura de Componentes
de Zope.


Enfoque procedural
~~~~~~~~~~~~~~~~~~

En una aplicación de gestión, el almacenamiento de los datos es muy
importante.  Por simplicidad, este ejemplo utilizará un diccionario
Python como almacenamiento.  Las claves del diccionario serán
identificadores únicos para un huesped en particular. Y el valor
será otro diccionario cuyas claves son los nombres de las propiedades::

  >>> huespedes_db = {} #clave: id único, valor: detalles en un diccionario

En un método simplista, una función que acepte detalles como argumentos
es suficiente para hacer el registro. También necesitas una función
auxiliar para obtener el próximo identificador de tu almacenamiento de datos.

Esta función auxiliar, para obtener el próximo identificador se puede
implementar así ::

  >>> def proximo_id():
  ...     claves = huespedes_db.keys()
  ...     if claves == []:
  ...         proximo = 1
  ...     else:
  ...         proximo = max(claves) + 1
  ...     return proximo

Como puedes ver, la implementación de la función `proximo_id` es muy
simple. Bueno, no es la forma ideal, pero es suficiente para explicar
conceptos.  La función primero obtiene todas las claves del
almacenamiento en una lista y comprueba si está vacía o no. Si está
vacía, por tanto ningún elemento esta almacenado, devuelve `1` como
el próximo identificador. Y si la lista no está vacía, el próximo
identificador se calcula sumando `1` al valor máximo de la lista.

La función para registrar un huesped puede obtener el próximo
identificador usando la función `proximo_id`, y luego asignando
los detalles de un huesped usando un diccionario. Aquí está la función
para obtener los detalles y almacenar en la base de datos::

  >>> def registrar_huesped(nombre, lugar):
  ...     huesped_id = proximo_id()
  ...     huespedes_db[huesped_id] = {
  ...     'nombre': nombre,
  ...     'lugar': lugar
  ...     }

Los requerimientos de una aplicación de administración de huespeds de un hotel que requiere
considerar datos adicionales:

  - numeros telefonicos
  - opciones de habitación
  - formas de pago
  - ...

Y programar la administración de la data de:

  - cancelar una reservación
  - actualizar una reservación
  - pago para una habitación
  - la persistencia de la data
  - insidentes de seguridad de la data
  - ...

Aqui termina nuestro enfoque procedural. Sería mucho más fácil añadir 
añadir funcionalidades necesarias como almacenamiento de datos,
diseño flexible y código testeable usando objetos.  Como los requerimientos anterior son cambiantes y son agregados, la programación procedural viene a ser dura para el mantenimiento y los errors viene a ser dificil de buscar y corregir.

Nosotros finalizaremos nuestra discusión del enfoque procedural aquí. El siguiente enfoque será mucho más facil para proveer persistencia de data, diseño flexible y pruebas de códigos usando objetos.


Enfoque orientado a objetos
~~~~~~~~~~~~~~~~~~~~~~~~~~~

En una metodología orientada a objetos, puedes pensar en un objeto
registrador que se encargue del registro. Hay muchas ventajas para
crear un objeto que se encargue del registro. La más importante es que
estas consiguiendo más abstracción en el proceso de registro, por lo
que puedes entender mejor tu código. Puedes poner lógicas relacionadas
juntas, quizá heredando de una clase base abstracta. El proceso de
registro puede incluir también cancelación y/o actualización del
registro. El mismo objeto puede hacer todo esto o delegarlo a otros
componentes. En cualquier caso, aqui tenemos los detalles de 
implementación (aquí, una clase) del objeto registrador::

  >>> class RegistradorHuesped(object):
  ...
  ...     def registrar(self, nombre, lugar):
  ...         huesped_id = proximo_id()
  ...         huespedes_db[huesped_id] = {
  ...         'nombre': nombre,
  ...         'lugar': lugar
  ...         }

En esta implementación, el objeto `registradorhuesped` (una instancia de
la clase `RegistradorHuesped`) se encarga del registro. Con este
diseño, un objeto `registradorhuesped` en concreto puede realizar numerosos
registros.  Así es como puedes usar la implementación actual::

  >>> registradorhuesped = RegistradorHuesped()
  >>> registradorhuesped.registrar("Pepito", "Pérez")

Los cambios de requisitos son inevitables en un proyecto real.  Considera
este caso, después de algún tiempo, un nuevo requisito se presenta:
los huespedes también deben dar el número de teléfono para que se les
admita. Necesitarás cambiar la implementación del objeto registrador
para ofrecer esto.

Puedes cumplir este requisito añadiendo un argumento al método
`registrar` y usar ese argumento en el diccionario de valores. Aquí
está la nueva implementación para este requisito::

  >>> class RegistradorHuesped(object):
  ...
  ...     def registrar(self, nombre, lugar, telefono):
  ...         huesped_id = proximo_id()
  ...         huespedes_db[huesped_id] = {
  ...         'nombre': nombre,
  ...         'lugar': lugar,
  ...         'telefono': telefono
  ...         }

Además de migrar los datos al nuevo esquema, ahora tienes que cambiar
la forma de usar `RegistradorHuesped` en todos sitios.  Si puedes
abstraer los detalles de un huesped en un objeto y usarlo en el
registro, los cambios en el código se pueden minimizar. Si sigues este
diseño, tienes que pasarle el objeto huesped a la función en lugar de
más argumentos.

La nueva implementación con el objeto huesped quedaría
así::

  >>> class RegistradorHuesped(object):
  ...
  ...     def registrar(self, huesped):
  ...         huesped_id = proximo_id()
  ...         huespedes_db[huesped_id] = {
  ...         'nombre': huesped.nombre,
  ...         'lugar': huesped.lugar,
  ...         'telefono': huesped.telefono
  ...         }

Bien, incluso con esta implementación tienes que cambiar código.
El cambio de código con nuevos requisitos es inevitable, tu objetivo es
poder minimizar los cambios y hacerlo mantenible.

.. note::

  Debes tener el coraje de hacer cualquier cambio, grande o pequeño,
  en cualquier momento. Retroalimentación inmediata es la única forma
  de que tengas el coraje. El uso de los tests automáticos te dan la
  retroalimentación inmediata y por tanto el coraje para hacer cambios.
  Para más información sobre el tema, puedes leer el libro llamado
  `Extreme Programming Explained` de Kent Beck.

Al introducir el objeto huesped, te has ahorrado un poco de escritura.
Más que eso, la abstracción del objeto invitado ha hecho tu sistema
mucho más simple y fácil de entender.  Cuanto mejor se entienda mejor
se puede restructurar y por tanto mejor se mantiene el código.


El patrón adaptador
~~~~~~~~~~~~~~~~~~~

Como se ha dicho antes, en una aplicación real, el objeto registrador
puede tener funcionalidades de cancelación y/o actualización. Supón
que hay dos método más como, `cancelar_registro` y
`actualizar_registro`. En el nuevo diseño deberás pasar el objeto
huesped a ambos métodos. Puedes solucionar este problema guardando
el objeto huesped como un atributo del objeto registrador.

Aquí tenemos la nueva implementación del objeto registrador que
guarda el objeto huesped en RegistradorHuesped.__init__() como un atributo de la instancia. ::

  >>> class RegistradorHuespedNG(object):
  ...
  ...     def __init__(self, huesped):
  ...         self.huesped = huesped
  ...
  ...     def registrar(self):
  ...         huesped= self.huesped
  ...         huesped_id = proximo_id()
  ...         huespedes_db[huesped_id] = {
  ...         'nombre': huesped.nombre,
  ...         'lugar': huesped.lugar,
  ...         'telefono': huesped.telefono
  ...         }

.. include this bit at the front of the `Adapters` section when I get
    the equivalent quote from the Patterns book to start the 
    `Interfaces` section

    La solución a la que has llegado es un patrón de diseño común llamado, 
    `Adaptador`. Con este diseño, ahora puedes añadir más métodos, es decir
    más funcionalidad, si se necesita.

En esta implementación, al crear la instancia tienes que pasarle el
objeto invitado que tiene los valores como atributos. Ahora es
necesario crear instancias separadas de `RegistradorHuespedNG` para
cada objeto huesped.

Ahora retrocedamos y pensemos de otra forma. Supón que eres el creador
de este software y se lo vendes a muchos hoteles. Considera el caso en
el que tus clientes necesitan distintos almacenamientos. Por ejemplo,
un registrador puede almacenar los detalles en una base de datos
relacional y otro puede almacenarlos en la Base de datos orientada a
Objetos de Zope (ZODB). Sería mejor si puedes sustituir el objeto
registrador por otro que almacena los detalles de los huespedes de
otra forma distinta. Por tanto, un mecanismo para cambiar la
implementación basado en alguna configuración será útil.

La arquitectura de componentes Zope ofrece un mecanismo para sustituir
componentes basado en configuración. Utilizando la arquitectura de
componentes de Zope puedes registrar componentes en un registro llamado
registro de componentes. Después, puede recuperar componentes basandose
en la configuración.

La clase `RegistradorHuespedNG` sigue, como ya has visto, un patrón
llamado `Adaptador`. El `RegistradorHuespedNG` es el adaptador que
adapta el objeto huesped (adaptado). Como puedes ver, el adaptador
debe contener el objeto que adapta (adaptado). Esta es una
implementación típica de un adaptador::

  >>> class Adaptador(object):
  ...
  ...     def __init__(self, adaptado):
  ...         self.adaptado = adaptado

Ahora el adaptador puede usar el adaptado (llamar a sus métodos o
acceder a sus atributos). Un adaptador puede adaptar más de un
componente. La arquitectura de componentes zope ofrece un mecanismo
para utilizar de forma efectiva este tipo de objetos. Así, qué
componente se use se convierte en un problema de configuración.

Este es un escenario común donde quieres usar objetos diferentes
para hacer las mismas cosas, pero los detalles varían. Hay muchas
situaciones en programación donde quieres usar diferentes
implementaciones para el mismo tipo de objetos. Te ofrecemos una
pequeña lista de otros escenarios comunes:

 - Un motor wiki que soporte múltiples marcados (STX, reST, Texto
   plano, etc.)

 - Un objeto navegador que muestre el tamaño de distintos tipos
   de objetos.

 - Diferentes tipos de formatos de salida para datos de texto
   (PDF, HTML etc.)

 - Cuando se desarrolla una aplicación para múltiples clientes, sus
   requisitos pueden cambiar. Mantener distintas versiones del código
   de la misma aplicación para distintos clientes es difícil. Un
   enfoque mejor sería crear distintos componentes reutilizables y
   configurarlos basándose en los requisitos específicos de cada
   cliente.

Todos estos ejemplos señalan situaciones donde quieres hacer
aplicaciones extensibles o enchufables. No utilices componentes
`adaptadores` cuando no quieras extensibilidad o enchufabilidad.

La arquitectura de componentes de Zope ofrece componentes `adaptadores`
para solucionar este tipo de problemas. De hecho,
`RegistradorHuespedNG` es un adaptador sin declaración de interfaz
explícita. Este tutorial tratará los adaptadores después de introducir
el concepto de interfaces. Las interfaces son una de las bases de los
componentes de Zope, por tanto entender el concepto y uso de interfaces
es muy importante.


Interfaces
----------

Introducción
~~~~~~~~~~~~

`Patrones de Diseño` es un libro clásico de ingeniería del software
escrito por la `Banda de los Cuatro` [#patternbook]_. En este libro
se recomienda: "Programa contra un interfaz, no contra una
implementación". Definir interfaces formales te ayuda a entender mejor
el sistema. Además, las interfaces traen consigo todos los beneficios
de la ZCA.

Las interfaces definen el comportamiento y el estado de objetos. Una
interfaz describe como se trabaja con el objeto. Si te gustan las
metáforas, piensa en la interfaz como un `contrato del objeto`. Otra
método que ayuda es `molde de objetos`. En el código, los métodos
y los atributos forman la interfaz del objeto.

La noción de interfaz es muy explícita en lenguajes modernos como
Java, C#, VB.NET etc. Estos lenguajes también ofrecen una sintaxis
para definir interfaces. Python tiene la noción de interfaces, pero
no es muy explícita. Para simular una definición formal de interfaces
en C++, la `Banda de los Cuatro` utiliza clases con funciones
virtuales en el libro `Patrones de Diseño`. De forma similar, la
arquitectura de componentes de Zope utiliza la meta-clase heredada de
``zope.interface.Interface`` para definir una interfaz.

La base de la orientación a objetos es la comunicación entre los
objetos. Se utilizan mensajes para comunicación entre objetos. En
Python, funciones, métodos o cualquier otro llamable, puede usarse
para manipular mensajes.

Por ejemplo, considera esta clase::

  >>> class Anfitrion(object):
  ...
  ...     def buenosdias(self, nombre):
  ...         """Le dice buenos dias a los huespedes"""
  ...
  ...         return "¡Buenos días, %s!" % nombre

En la clase anterior, has definido un método `buenosdias`. Si llamas
al método `buenosdias` desde un objeto creado con esta clase, devolverá
`¡Buenos días, ...!`::

  >>> anfitrion = Anfitrion()
  >>> anfitrion.buenosdias('Pepe')
  '¡Buenos días, Pepe!'

Aquí ``anfitrion`` es el objeto real. Los detalles de implementación de
este objeto es la clase ``Anfitrion``. Ahora, cómo se sabe cómo es el
objeto, es decir, cuáles son los métodos y los atributos del objeto.
Para responder a esto, tienes que ir a los detalles de implementación
(la clase ``Anfitrion``) del objeto o bien necesitas una documentación
externa de la API [#api]_.

Puedes usar el paquete ``zope.interface`` para definir la interfaz de
objetos. Para la clase anterior puedes especificar la interfaz así::

  >>> from zope.interface import Interface

  >>> class IAnfitrion(Interface):
  ...
  ...     def buenosdias(huesped):
  ...         """Le dice buenos dias al huesped"""

Como puedes ver, la interfaz se define usando la sentencia class de
Python. Usamos (¿abusamos de?) la sentencia class de Python para
definir interfaces. Para hacer que una clase sea una interfaz, debe
heredar de ``zope.interface.Interface``. El prefijo ``I`` de la
interfaz es una convención.


Declarando interfaces
~~~~~~~~~~~~~~~~~~~~~

Ya has visto como declarar una interfaz usando ``zope.interface`` en
la sección anterior.  En esta sección se explicarán los conceptos en
detalle.

Considera esta interfaz de ejemplo: ::

  >>> from zope.interface import Interface
  >>> from zope.interface import Attribute

  >>> class IAnfitrion(Interface):
  ...     """Un objeto anfitrion"""
  ...
  ...     nombre = Attribute("""Nombre del anfitrion""")
  ...
  ...     def buenosdias(huesped):
  ...         """Le dice buenos dias al huesped"""

La interfaz, ``IAnfitrion`` tiene dos atributos, ``nombre`` y
``buenosdias``.  Recuerda que, al menos en Python, los métodos
también son atributos de clases. El atributo ``nombre`` se define
utilizando la clase ``zope.interface.Attribute``. Cuando añades
el atributo ``nombre`` a la interfaz ``IAnfitrion``, no especificas
ningún valor inicial. El propósito de definir el atributo ``nombre``
aquí es meramente para indicar que cualquier implementación de
esta interfaz tendrá una atributo llamado ``nombre``. En este
caso, ¡ni siquiera dices el tipo que el atributo tiene que tener!
Puedes pasar una cadena de documentación como primer argumento a
``Attribute``.

El otro atributo, ``buenosdias`` es un método definido usando
una definición de función. Nótese que no hace falta ``self``
en las interfaces, porque ``self`` es un detalle de implementación
de la clase. Por ejemplo, un módulo puede implementar esta
interfaz. Si un módulo implementa esta interfaz, habrá un atributo
``nombre`` y una función ``buenosdias`` definida. Y la función
``buenosdias`` aceptará un argumento.

Ahora verás como conectar `interfaz-clase-objeto`. Así objeto
es la cosa viva y coleante, objetos son instancias de clases. Y
la interfaz es la definición real del objeto, por tanto las
clases son sólo detalles de implementación. Es por esto por lo
que debes programar contra una interfaz y no contra una
implementación.

Ahora deberías familiarizarte con dos términos más para entender
otros conceptos. El primero es `proveer` y el otro es `implementar`-
Los objetos proveen interfaces y las clases implementan interfaces.
En otras palabras, objetos proveen las interfaces que sus clases
implementan. En el ejemplo anterior ``anfitrion`` (objeto) provee
``IAnfitrion`` (interfaz) y ``Anfitrion`` (clase) implementa 
``IAnfitrion`` (interfaz). Un objeto puede proveer más de una
interfaz y también una clase puede implementar más de una interfaz.
Los objetos también pueden proveer interfaces directamente, además
de lo que sus clases implementen.

.. note::

  Las clases son los detalles de implementación de los objetos.
  En Python, las clases son objetos llamables, así que por qué
  otros objetos llamables no pueden implementar una interfaz?
  Sí, es posible. Para cualquier `objeto llamable` puedes declarar
  que produce objetos que proveen algunas interfaces diciendo que
  el `objeto llamable` implementa las interfaces. Generalmente
  los `objetos llamables` son llamados `fábricas`. Como las
  funciones son objetos llamables, una función puede ser la
  `implementadora` de una interfaz.


Implementando interfaces
~~~~~~~~~~~~~~~~~~~~~~~~

Para declarar que una clase implementa una interfaz en particular,
utiliza la función ``zope.interface.implements`` dentro de la
sentencia class.

Considera este ejemplo, aquí ``Anfitrion`` implementa ``IAnfitrion``::

  >>> from zope.interface import implements

  >>> class Anfitrion(object):
  ...
  ...     implements(IAnfitrion)
  ...
  ...     nombre = u''
  ...
  ...     def buenosdias(self, huesped):
  ...         """Le dice buenos dias al huesped"""
  ...
  ...         return "¡Buenos dias, %s!" % huesped

.. note::

  Si te preguntas como funciona la función ``implements``, consulta
  el mensaje del blog de James Henstridge
   (http://blogs.gnome.org/jamesh/2005/09/08/python-class-advisors/) .
  En la sección del adaptador, verás una función ``adapts``, que
  funciona de forma similar.

Como ``Anfitrion`` implementa ``IAnfitrion``, instancias de
``Anfitrion`` proveen ``IAnfitrion``. Hay unos cuantos métodos
de utilidad que introspeccionan las declaraciones. La declaración
se puede escribir fuera de la clase también. Si no escribes
``interface.implements(IAnfitrion)`` en el ejemplo anterior,
entonces después de la sentencia class, puedes escribir algo como::

  >>> from zope.interface import classImplements
  >>> classImplements(Anfitrion, IAnfitrion)


Ejemplo revisado
~~~~~~~~~~~~~~~~

Ahora volvemos a la aplicación de ejemplo.  Ahora veremos como
definir la interfaz del objeto registrador ::

  >>> from zope.interface import Interface

  >>> class IRegistrador(Interface):
  ...     """Un registrador registrará los detalles de un objeto"""
  ...
  ...     def registrar():
  ...         """Registrar detalles de un objeto"""
  ...

Aquí primero has importado la clase ``Interface`` del módulo
``zope.interface``.  Si defines una subclase de esta clase ``Interface``,
será una interfaz desde el punto de vista de la arquitectura de
componentes de Zope.  Una interfaz puede ser implementada, como ya
has visto, en una clase o cualquier otro objeto llamable.

La interfaz registrador definida aquí es ``IRegistrador``.  La cadena
de documentación del interfaz da una idea del objeto.  Al definir un
método en la interfaz, has creado un contrato para el componente, en
el que dice que habrá un método con el mismo nombre disponible.  En
la definición del método en la interfaz, el primer argumento no debe
ser `self`, porque una interfaz nunca será instanciada ni sus métodos
serán llamados jamás.  En vez de eso, la sentencia class de la interfaz
meramente documenta qué métodos y atributos deben aparecer en
cualquier clase normal que diga que la implementa, y el parámetro
`self` es un detalle de implementación que no necesita ser
documentado.

Como sabes, una interfaz puede también especificar atributos
normales: ::

  >>> from zope.interface import Interface
  >>> from zope.interface import Attribute

  >>> class IHuesped(Interface):
  ...
  ...     nombre = Attribute("Nombre del huesped")
  ...     lugar = Attribute("Lugar del huesped")

En esta interfaz, el objeto huesped tiene dos atributos que se
especifican con documentación.  Una interfaz también puede especificar
atributos y métodos juntos.  Una interfaz puede ser implementada por
una clase, un módulo o cualquier otro objeto.  Por ejemplo una
función puede crear dinámicamente el componente y devolverlo, en
este caso la función es una implementadora de la interfaz.

Ahora ya sabes lo que es una interfaz y como definirla y usarla.  En
el próximo capítulo podrás ver como se usa una interfaz para definir
un componente adaptador.


Interfaces de marcado
~~~~~~~~~~~~~~~~~~~~~

Una interfaz se puede usar para declarar que un objeto en particular
pertenece a un tipo especial.  Un interfaz sin ningún atributo o método
se llama `interfaz de marcado`.

Aquí tenemos una `interfaz de marcado`::

  >>> from zope.interface import Interface

  >>> class IHuespedEspecial(Interface):
  ...     """Un huesped especial"""


Esta interfaz se puede usar para declarar que un objeto es un huesped
especial.


Invariantes
~~~~~~~~~~~

A veces te piden usar alguna regla para tu componente que implica
a uno o más atributos normales.  A este tipo de reglas se les llama
`invariantes`.  Puedes usar ``zope.interface.invariant`` para
establecer `invariantes` para tus objetos en sus interfaces.

Considera un ejemplo sencillo, hay un objeto `persona`.  Una persona
tiene los atributos `nombre`, `email` y `telefono`.  ¿Cómo implementas
una regla de validación que diga que o bien el email o bien el
teléfono tienen que existir, pero no necesariamente los dos?

Lo primero es hacer un objeto llamable, bien una simple función o
bien una instancia llamable de una clase como esto::

  >>> def invariante_contactos(obj):
  ...
  ...     if not (obj.email or obj.telefono):
  ...         raise Exception(
  ...             "Al menos una información de contacto es obligatoria")

Ahora defines la interfaz del objeto `persona` de esta manera.
Utiliza la función ``zope.interface.invariant`` para establecer la
invariante::

  >>> from zope.interface import Interface
  >>> from zope.interface import Attribute
  >>> from zope.interface import invariant

  >>> class IPersona(Interface):
  ...
  ...     nombre = Attribute("Nombre")
  ...     email = Attribute("Direccion de email")
  ...     telefono = Attribute("Numero de telefono")
  ...
  ...     invariant(invariante_contactos)

Ahora usas el método `validateInvariants` de la interfaz para
validar::

  >>> from zope.interface import implements

  >>> class Persona(object):
  ...     implements(IPersona)
  ...
  ...     nombre = None
  ...     email = None
  ...     telefono = None

  >>> pepe = Persona()
  >>> pepe.email = u"pepe@algun.sitio.com"
  >>> IPersona.validateInvariants(pepe)
  >>> maria = Persona()
  >>> IPersona.validateInvariants(maria)
  Traceback (most recent call last):
  ...
  Exception: Al menos una información de contacto es obligatoria

Como puedes ver el objeto `pepe` validó sin lanzar ninguna
excepción. Pero el objeto `maria` no validó la restricción de
la invariante, por lo que se lanzó la excepción.

.. [#patternbook] http://en.wikipedia.org/wiki/Design_Patterns
.. [#api] http://en.wikipedia.org/wiki/Application_programming_interface


Adaptadores
-----------


Implementación
~~~~~~~~~~~~~~

This section will describe adapters in detail.  Zope component
architecture, as you noted, helps to effectively use Python objects.
Adapter components are one of the basic components used by Zope
component architecture for effectively using Python objects.  Adapter
components are Python objects, but with well defined interface.

To declare a class is an adapter use `adapts` function defined in
``zope.component`` package.  Aquí un nuevo adaptador `RegistradorHuespedNG` con la declarqción explicita de la interfaz::

  >>> from zope.interface import implements
  >>> from zope.component import adapts

  >>> class RegistradorHuespedNG(object):
  ...
  ...     implements(IRegistrar)
  ...     adapts(IHuesped)
  ...
  ...     def __init__(self, huesped):
  ...         self.huesped = huesped
  ...
  ...     def registrar(self):
  ...         huesped= self.huesped
  ...         huesped_id = proximo_id()
  ...         huespedes_db[huesped_id] = {
  ...         'nombre': huesped.nombre,
  ...         'lugar': huesped.lugar,
  ...         'telefono': huesped.telefono
  ...         }


What you defined here is an `adapter` for `IRegistrador`, which adapts
`IHuesped` object.  La interfaz `IRegistrador` es implementada por la clase
`RegistradorHuespedNG`.  So, an instance of this class will provide
`IRegistrador` interface.

::

  >>> class Huesped(object):
  ...
  ...     implements(IHuesped)
  ...
  ...     def __init__(self, nombre, lugar):
  ...         self.nombre = nombre
  ...         self.lugar = lugar

  >>> pepe = Huesped("Pepe", "España")
  >>> pepe_registradorhuesped = RegistradorHuespedNG(pepe)

  >>> IRegistrador.providedBy(pepe_registradorhuesped)
  True

El `RegistradorHuespedNG` es solo un adaptador creado, usted puede también crear otros adaptadores los cuales manipulen un registro diferente de huesped.


Registro
~~~~~~~~

To use this adapter component, you have to register this in a
component registry also known as site manager.  A site manager
normally resides in a site.  A site and site manager will be more
important when developing a Zope 3 application.  For now you only
required to bother about global site and global site manager ( or
component registry).  A global site manager will be in memory, but a
local site manager is persistent.

To register your component, first get the global site manager::

  >>> from zope.component import getGlobalSiteManager
  >>> gsm = getGlobalSiteManager()
  >>> gsm.registerAdapter(RegistradorHuespedNG,
  ...                     (IHuesped,), IRegistrador, 'ng')

To get the global site manager, you have to call
``getGlobalSiteManager`` function available in ``zope.component``
package.  In fact, the global site manager is available as an
attribute (``globalSiteManager``) of ``zope.component`` package.  So,
you can directly use ``zope.component.globalSiteManager`` attribute.
To register the adapter in component, as you can see above, use
``registerAdapter`` method of component registry.  The first argument
should be your adapter class/factory.  The second argument is a tuple
of `adaptee` objects, i.e, the object which you are adapting.  In this
example, you are adapting only `IHuesped` object.  The third argument is
the interface implemented by the adapter component.  The fourth
argument is optional, that is the name of the particular adapter.
Since you gave a name for this adapter, this is a `named adapter`.  If
name is not given, it will default to an empty string ('').

In the above registration, you have given the adaptee interface and
interface to be provided by the adapter.  Since you have already given
these details in adapter implementation, it is not required to specify
again.  In fact, you could have done the registration like this::

  >>> gsm.registerAdapter(RegistradorHuespedNG, name='ng')

There are some old API to do the registration, which you should avoid.
The old API functions starts with `provide`, eg: ``provideAdapter``,
``provideUtility`` etc.  While developing a Zope 3 application you can
use Zope configuration markup language (ZCML) for registration of
components.  In Zope 3, local components (persistent components) can
be registered from Zope Management Interface (ZMI) or you can do it
programmatically also.

Usted registro `RegistradorHuespedNG` con un nombre `ng`.  Similarly you can
register other adapters with different names.  If a component is
registered without name, it will default to an empty string.

.. note::

  Local components are persistent components but global components are
  in memory.  Global components will be registered based on the
  configuration of application.  Local components are taken to memory
  from database while starting the application.


Patrón de consulta
~~~~~~~~~~~~~~~~~~

Retrieving registered components from component registry is achieved
through two functions available in ``zope.component`` package.  One of
them is ``getAdapter`` and the other is ``queryAdapter`` .  Both
functions accepts same arguments.  The ``getAdapter`` will raise
``ComponentLookupError`` if component lookup fails on the other hand
``queryAdapter`` will return `None`.

You can import the methods like this::

  >>> from zope.component import getAdapter
  >>> from zope.component import queryAdapter

In the previous section you have registered a component for guest
object (adaptee) which provides `IRegistrador` interface with name as
'ng'.  	In the first section of this chapter, you have created a guest
object named `pepe` .

This is how you can retrieve a component which adapts the interface of
`pepe` object (`IHuesped`) and provides `IRegistrador` interface also with
name as 'ng'.  Here both ``getAdapter`` and ``queryAdapter`` works
similarly::

  >>> getAdapter(pepe, IRegistrador, 'ng') #doctest: +ELLIPSIS
  <RegistradorHuespedNG object at ...>
  >>> queryAdapter(pepe, IRegistrador, 'ng') #doctest: +ELLIPSIS
  <RegistradorHuespedNG object at ...>

As you can see, the first argument should be adaptee then, the
interface which should be provided by component and last the name of
adapter component.

If you try to lookup the component with an name not used for
registration but for same adaptee and interface, the lookup will fail.
Here is how the two methods works in such a case::

  >>> getAdapter(pepe, IRegistrador, 'not-exists') #doctest: +ELLIPSIS
  Traceback (most recent call last):
  ...
  ComponentLookupError: ...
  >>> reg = queryAdapter(pepe,
  ...           IRegistrador, 'not-exists') #doctest: +ELLIPSIS
  >>> reg is None
  True

As you can see above, ``getAdapter`` raised a ``ComponentLookupError``
exception, but ``queryAdapter`` returned `None` when lookup failed.

The third argument, the name of registration, is optional.  If the
third argument is not given it will default to empty string ('').
Since there is no component registered with an empty string,
``getAdapter`` will raise ``ComponentLookupError`` .  Similarly
``queryAdapter`` will return `None`, see yourself how it works::

  >>> getAdapter(pepe, IRegistrador) #doctest: +ELLIPSIS
  Traceback (most recent call last):
  ...
  ComponentLookupError: ...
  >>> reg = queryAdapter(pepe, IRegistrador) #doctest: +ELLIPSIS
  >>> reg is None
  True

In this section you have learned how to register a simple adapter and
how to retrieve it from component registry.  These kind of adapters is
called single adapter, because it adapts only one adaptee.  If an
adapter adapts more that one adaptee, then it is called multi
adapter.


Recuperar un adaptador usando una interfaz
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adapters can be directly retrieved using interfaces, but it will only
work for non-named single adapters.  The first argument is the adaptee
and the second argument is a keyword argument.  If adapter lookup
fails, second argument will be returned.

  >>> IRegistrador(pepe, alternate='default-output')
  'default-output'

  Keyword name can be omitted:

  >>> IRegistrador(pepe, 'default-output')
  'default-output'

  If second argument is not given, it will raise `TypeError`:

  >>> IRegistrador(pepe) #doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
  Traceback (most recent call last):
  ...
  TypeError: ('Could not adapt',
    <Huesped object at ...>,
    <InterfaceClass __builtin__.IRegistrador>)

  Aquí `RegistradorHuespedNG` esta registrado sin nombre:

  >>> gsm.registerAdapter(RegistradorHuespedNG)

  Now the adapter lookup should succeed:

  >>> IRegistrador(pepe, 'default-output') #doctest: +ELLIPSIS
  <RegistradorHuespedNG object at ...>

For simple cases, you may use interface to get adapter components.


Patrón de Adaptador
~~~~~~~~~~~~~~~~~~~

The adapter concept in Zope Component Architecture and the classic
`Adapter` pattern as described in Design Patterns book is very
similar.  But the intent of ZCA adapter is more wider than `Adapter`
pattern.  The intent of `Adapter` pattern is to convert the interface
of a class into another interface clients expect.  This allows classes
work together that couldn't otherwise because of incompatible
interfaces.  But in the `Motivation` section, GoF says: "Often the
adapter is responsible for functionality the adapter class doesn't
provide".  ZCA adapter has more focus on adding functionalities than
new interface for existing functionality of adaptee.  So, ZCA adapter
lets adapter classes extend functionality by adding methods.

The major attraction of ZCA adapter are the explicit interface for
components and the component registry.  ZCA adapter components are
registered in component registry and looked up by client objects using
interface and name when required.


Utilidad
--------


Introducción
~~~~~~~~~~~~

Now you know the concept of interface, adapter and component registry.
Sometimes it would be useful to register an object which is not
adapting anything.  Database connection, XML parser, object returning
unique Ids etc. are examples of these kinds of objects.  These kind of
components provided by the ZCA are called ``utility`` components.

Utilities are just objects that provide an interface and that are
looked up by an interface and a name.  This approach creates a global
registry by which instances can be registered and accessed by
different parts of your application, with no need to pass the
instances around as parameters.

You need not to register all component instances like this.  Only
register components which you want to make replaceable.


Utilidad simple
~~~~~~~~~~~~~~~

Before implementing the utility, as usual, define its interface.  Here
is a `greeter` interface::

  >>> from zope.interface import Interface
  >>> from zope.interface import implements

  >>> class ISaludador(Interface):
  ...
  ...     def saludar(name):
  ...         """Decir hola"""

Like an adapter a utility may have more than one implementation.  Here
is a possible implementation of the above interface::

  >>> class Saludador(object):
  ...
  ...     implements(ISaludador)
  ...
  ...     def saludar(self, name):
  ...         return "Hola" + name

The actual utility will be an instance of this class.  To use this
utility, you have to register it, later you can query it using the ZCA
API.  You can register an instance of this class (`utility`) using
``registerUtility``::

  >>> from zope.component import getGlobalSiteManager
  >>> gsm = getGlobalSiteManager()

  >>> saludar = Saludador()
  >>> gsm.registerUtility(saludar, ISaludador)

In this example you registered the utility as providing the `ISaludador`
interface.  You can look the interface up with either `queryUtility`
or `getUtility`::

  >>> from zope.component import queryUtility
  >>> from zope.component import getUtility

  >>> queryUtility(ISaludador).saludar('Pepe')
  'Hola Pepe'

  >>> getUtility(ISaludador).saludar('Jack')
  'Hola Pepe'

As you can see, adapters are normally classes, but utilities are
normally instances of classes.  Only once you are creating the
instance of a utility class, but adapter instances are dynamically
created whenever you query for it.


Utilidad con nombre
~~~~~~~~~~~~~~~~~~~

When registering a utility component, like adapter, you can use a
name.  As mentioned in the previous section, a utility registered with
a particular name is called named utility.

This is how you can register the `greeter` utility with a name::

  >>> saludar = Saludador()
  >>> gsm.registerUtility(saludar, ISaludador, 'new')

In this example you registered the utility with a name as providing
the `ISaludador` interface.  You can look up the interface with either
`queryUtility` or `getUtility`::

  >>> from zope.component import queryUtility
  >>> from zope.component import getUtility

  >>> queryUtility(ISaludador, 'new').saludar('Juan')
  'Hola Juan'

  >>> getUtility(ISaludador, 'new').saludar('Juan')
  'Hola Juan'

As you can see here, while querying you have to use the `name` as
second argument.

Calling `getUtility` function without a name (second argument) is
equivalent to calling with an empty string as the name.  Because, the
default value for second (keyword) argument is an empty string.  Then,
component lookup mechanism will try to find the component with name as
empty string, and it will fail.  When component lookup fails it will
raise ``ComponentLookupError`` exception.  Remember, it will not
return some random component registered with some other name.  The
adapter look up fuctions, `getAdapter` and `queryAdapter` also works
similarly.


Fábrica
~~~~~~~

A ``Factory`` is a utility component which provides ``IFactory``
interface.

To create a factory, first define the interface of the object::

  >>> from zope.interface import Attribute
  >>> from zope.interface import Interface
  >>> from zope.interface import implements

  >>> class IBaseDatos(Interface):
  ...
  ...     def getConexion():
  ...         """Devuelve el objecto conexion"""

Here is fake implementation of `IBaseDatos` interface::

  >>> class FakeDb(object):
  ...
  ...     implements(IBaseDatos)
  ...
  ...     def getConexion(self):
  ...         return "conexion"

You can create a factory using ``zope.component.factory.Factory``::

  >>> from zope.component.factory import Factory

  >>> factory = Factory(FakeDb, 'FakeDb')

Now you can register it like this::

  >>> from zope.component import getGlobalSiteManager
  >>> gsm = getGlobalSiteManager()

  >>> from zope.component.interfaces import IFactory
  >>> gsm.registerUtility(factory, IFactory, 'fakedb')

To use the factory, you may do it like this::

  >>> from zope.component import queryUtility
  >>> queryUtility(IFactory, 'fakedb')() #doctest: +ELLIPSIS
  <FakeDb object at ...>

There is a shortcut to use factory::

  >>> from zope.component import createObject
  >>> createObject('fakedb') #doctest: +ELLIPSIS
  <FakeDb object at ...>


Adaptadores avanzados
---------------------

This chapter discuss some advanced adapters like multi adapter,
subscription adapter and handler.


Multi adaptador
~~~~~~~~~~~~~~~

A simple adapter normally adapts only one object, but an adapter may
adapt more than one object.  If an adapter adapts more than one
objects, it is called `multi-adapter`.

::

  >>> from zope.interface import Interface
  >>> from zope.interface import implements
  >>> from zope.component import adapts

  >>> class IAdaptadoUno(Interface):
  ...     pass

  >>> class IAdaptadoDos(Interface):
  ...     pass

  >>> class IFuncionalidad(Interface):
  ...     pass

  >>> class MiFuncionalidad(object):
  ...     implements(IFuncionalidad)
  ...     adapts(IAdaptadoUno, IAdaptadoDos)
  ...
  ...     def __init__(self, uno, dos):
  ...         self.uno = uno
  ...         self.dos = dos

  >>> from zope.component import getGlobalSiteManager
  >>> gsm = getGlobalSiteManager()

  >>> gsm.registerAdapter(MiFuncionalidad)

  >>> class Uno(object):
  ...     implements(IAdaptadoUno)

  >>> class Dos(object):
  ...     implements(IAdaptadoDos)

  >>> uno = Uno()
  >>> dos = Dos()

  >>> from zope.component import getMultiAdapter

  >>> getMultiAdapter((uno,dos), IFuncionalidad) #doctest: +ELLIPSIS
  <MiFuncionalidad object at ...>

  >>> mifuncionalidad = getMultiAdapter((uno,dos), IFuncionalidad)
  >>> mifuncionalidad.uno #doctest: +ELLIPSIS
  <Uno object at ...>
  >>> mifuncionalidad.dos #doctest: +ELLIPSIS
  <Dos object at ...>


Adaptador de subscripción
~~~~~~~~~~~~~~~~~~~~~~~~~

Unlike regular adapters, subscription adapters are used when we want
all of the adapters that adapt an object to a particular interface.
Subscription adapter is also known as `subscriber`.

Consider a validation problem.  We have objects and we want to assess
whether they meet some sort of standards.  We define a validation
interface::

  >>> from zope.interface import Interface
  >>> from zope.interface import Attribute
  >>> from zope.interface import implements

  >>> class IValidar(Interface):
  ...
  ...     def validar(ob):
  ...         """Determine whether the object is valid
  ...
  ...         Return a string describing a validation problem.
  ...         An empty string is returned to indicate that the
  ...         object is valid.
  ...         """

Perhaps we have documents::

  >>> class IDocumento(Interface):
  ...
  ...     resumen = Attribute("Resumen del Documento")
  ...     cuerpo = Attribute("Texto del Documento")

  >>> class Documento(object):
  ...
  ...     implements(IDocumento)
  ...
  ...     def __init__(self, resumen, cuerpo):
  ...         self.resumen, self.cuerpo = resumen, cuerpo

Now, we may want to specify various validation rules for
documents. For example, we might require that the summary be a single
line::

  >>> from zope.component import adapts

  >>> class ResumenLineaSimple:
  ...
  ...     adapts(IDocumento)
  ...     implements(IValidar)
  ...
  ...     def __init__(self, doc):
  ...         self.doc = doc
  ...
  ...     def validar(self):
  ...         if '\n' in self.doc.resumen:
  ...             return 'Summary should only have one line'
  ...         else:
  ...             return ''

Or we might require the body to be at least 1000 characters in length::

  >>> class LongitudAdecuada(object):
  ...
  ...     adapts(IDocumento)
  ...     implements(IValidar)
  ...
  ...     def __init__(self, doc):
  ...         self.doc = doc
  ...
  ...     def validar(self):
  ...         if len(self.doc.cuerpo) < 1000:
  ...             return 'too short'
  ...         else:
  ...             return ''

We can register these as subscription adapters::

  >>> from zope.component import getGlobalSiteManager
  >>> gsm = getGlobalSiteManager()

  >>> gsm.registerSubscriptionAdapter(ResumenLineaSimple)
  >>> gsm.registerSubscriptionAdapter(LongitudAdecuada)

We can then use the subscribers to validate objects::

  >>> from zope.component import subscribers

  >>> doc = Document("A\nDocument", "blah")
  >>> [adapter.validate()
  ...  for adapter in subscribers([doc], IValidar)
  ...  if adapter.validate()]
  ['Summary should only have one line', 'too short']

  >>> doc = Document("A\nDocument", "blah" * 1000)
  >>> [adapter.validate()
  ...  for adapter in subscribers([doc], IValidar)
  ...  if adapter.validate()]
  ['Summary should only have one line']

  >>> doc = Document("A Document", "blah")
  >>> [adapter.validate()
  ...  for adapter in subscribers([doc], IValidar)
  ...  if adapter.validate()]
  ['too short']


Manejador
~~~~~~~~~

Handlers are subscription adapter factories that don't produce
anything.  They do all of their work when called.  Handlers are
typically used to handle events.  Handlers are also known as event
subscribers or event subscription adapters.

Event subscribers are different from other subscription adapters in
that the caller of event subscribers doesn't expect to interact with
them in any direct way.  For example, an event publisher doesn't
expect to get any return value.  Because subscribers don't need to
provide an API to their callers, it is more natural to define them
with functions, rather than classes.  For example, in a
document-management system, we might want to record creation times for
documents::

  >>> import datetime

  >>> def documentoCreado(event):
  ...     event.doc.created = datetime.datetime.utcnow()

In this example, we have a function that takes an event and performs
some processing.  It doesn't actually return anything.  This is a
special case of a subscription adapter that adapts an event to
nothing.  All of the work is done when the adapter "factory" is
called.  We call subscribers that don't actually create anything
"handlers".  There are special APIs for registering and calling them.

To register the subscriber above, we define a document-created event::

  >>> from zope.interface import Interface
  >>> from zope.interface import Attribute
  >>> from zope.interface import implements

  >>> class IDocumentoCreado(Interface):
  ...
  ...     doc = Attribute("El documento que fue creado")

  >>> class DocumentoCreado(object):
  ...
  ...     implements(IDocumentoCreado)
  ...
  ...     def __init__(self, doc):
  ...         self.doc = doc

We'll also change our handler definition to::

  >>> def documentoCreado(event):
  ...     event.doc.created = datetime.datetime.utcnow()

  >>> from zope.component import adapter

  >>> @adapter(IDocumentoCreado)
  ... def documentoCreado(event):
  ...     event.doc.created = datetime.datetime.utcnow()

This marks the handler as an adapter of `IDocumentoCreado` events.

Now we'll register the handler::

  >>> from zope.component import getGlobalSiteManager
  >>> gsm = getGlobalSiteManager()

  >>> gsm.registerHandler(documentoCreado)

Now, we can create an event and use the `handle` function to call
handlers registered for the event::

  >>> from zope.component import handle

  >>> handle(DocumentCreated(doc))
  >>> doc.created.__class__.__name__
  'datetime'


Uso de la ZCA en Zope
---------------------

Zope Component Architecture is used in both Zope 3 and Zope 2.  This
chapter will go through usage of the ZCA in Zope.


Lenguaje de Marcado de Configuración Zope - ZCML
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The **Zope Configuration Markup Language (ZCML)** is an XML based
configuration system for registration of components.  So, instead of
using Python API for registration, you can use ZCML.  But to use ZCML,
unfortunately, you will be required to install more dependency
packages.

To install these packages::

  $ easy_install "zope.component [zcml]"

To register an adapter::

  <configure xmlns="http://namespaces.zope.org/zope">

  <adapter
      factory=".company.EmployeeSalary"
      provides=".interfaces.ISalary"
      for=".interfaces.IEmployee"
      />

The `provides` and `for` attributes are optional, provided you have
declared it in the implementation::

  <configure xmlns="http://namespaces.zope.org/zope">

  <adapter
      factory=".company.EmployeeSalary"
      />

If you want to register the component as named adapter, you can give a
`name` attribute::


  <configure xmlns="http://namespaces.zope.org/zope">

  <adapter
      factory=".company.EmployeeSalary"
      name="salary"
      />

Utilities are also registered similarly.

To register an utility::

  <configure xmlns="http://namespaces.zope.org/zope">

  <utility
      component=".basedatos.conexion"
      provides=".interfaces.IConexion"
      />

The `provides` attribute is optional, provided you have declared it in
the implementation::

  <configure xmlns="http://namespaces.zope.org/zope">

  <utility
      component=".basedatos.conexion"
      />

If you want to register the component as named utility, you can give a
`name` attribute::


  <configure xmlns="http://namespaces.zope.org/zope">

  <utility
      component=".basedatos.conexion"
      name="Database Connection"
      />

Instead of directly using the component, you can also give a factory::

  <configure xmlns="http://namespaces.zope.org/zope">

  <utility
      factory=".basedatos.Conexion"
      />


Redefiniciones
~~~~~~~~~~~~~~

When you register components using Python API (``register*`` methods),
the last registered component will replace previously registered
component, if both are registered with same type of arguments.  For
example, consider this example::

  >>> from zope.interface import Attribute
  >>> from zope.interface import Interface

  >>> class IA(Interface):
  ...     pass

  >>> class IP(Interface):
  ...     pass

  >>> from zope.interface import implements
  >>> from zope.component import adapts

  >>> from zope.component import getGlobalSiteManager
  >>> gsm = getGlobalSiteManager()

  >>> class AP(object):
  ...
  ...     implements(IP)
  ...     adapts(IA)
  ...
  ...     def __init__(self, context):
  ...         self.context = context

  >>> class AP2(object):
  ...
  ...     implements(IP)
  ...     adapts(IA)
  ...
  ...     def __init__(self, context):
  ...         self.context = context

  >>> class A(object):
  ...
  ...     implements(IA)

  >>> a = A()
  >>> ap = AP(a)

  >>> gsm.registerAdapter(AP)

  >>> getAdapter(a, IP) #doctest: +ELLIPSIS
  <AP object at ...>

If you register another adapter, the existing one will be replaced::

  >>> gsm.registerAdapter(AP2)

  >>> getAdapter(a, IP) #doctest: +ELLIPSIS
  <AP2 object at ...>

But when registering components using ZCML, the second registration
will raise a conflict error.  This is a hint for you, otherwise there
is a chance for overriding registration by mistake.  This may lead to
hard to track bugs in your system.  So, using ZCML is a win for the
application.

Sometimes you will be required to override existing registration.
ZCML provides ``includeOverrides`` directive for this.  Using this,
you can write your overrides in a separate file::

  <includeOverrides file="overrides.zcml" />


NameChooser
~~~~~~~~~~~

Ubicación: `zope.app.container.contained.NameChooser`

This is an adapter for choosing a unique name for an object inside a
container.

The registration of adapter is like this::

  <adapter
      provides=".interfaces.INameChooser"
      for="zope.app.container.interfaces.IWriteContainer"
      factory=".contained.NameChooser"
      />

From the registration, you can see that the adaptee is a
``IWriteContainer`` and the adapter provides ``INameChooser``.

This adapter provides a very convenient functionality for Zope
programmers.  The main implementations of ``IWriteContainer`` in
Zope 3 are ``zope.app.container.BTreeContainer`` and
``zope.app.folder.Folder``.  Normally you will be inheriting from
these implementations for creating your own container classes.
Suppose there is no interface called ``INameChooser`` and
adapter, then you will be required to implement this functionality
for every implementations separately.


LocationPhysicallyLocatable
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ubicación:
``zope.location.traversing.LocationPhysicallyLocatable``

This adapter is frequently used in Zope 3 applications, but
normally it is called through an API in ``zope.traversing.api``.
(Some old code even use ``zope.app.zapi`` functions, which is
again one more indirection)

The registration of adapter is like this::

  <adapter
      factory="zope.location.traversing.LocationPhysicallyLocatable"
      />

The interface provided and adaptee interface is given in the
implementation.

Here is the beginning of implementation::

  class LocationPhysicallyLocatable(object):
      """Provide location information for location objects
      """
      zope.component.adapts(ILocation)
      zope.interface.implements(IPhysicallyLocatable)
      ...

Normally, almost all persistent objects in Zope 3 application
will be providing the ``ILocation`` interface.  This interface
has only two attribute, ``__parent__`` and ``__name__``.  The
``__parent__`` is the parent in the location hierarchy.  And
``__name__`` is the name within the parent.

The ``IPhysicallyLocatable`` interface has four methods:
``getRoot``, ``getPath``, ``getName``, and ``getNearestSite``.

  - ``getRoot`` function will return the physical root object.

  - ``getPath`` return the physical path to the object as a
    string.

  - ``getName`` return the last segment of the physical path.

  - ``getNearestSite`` return the site the object is contained
    in.  If the object is a site, the object itself is returned.

If you learn Zope 3, you can see that these are the important
things which you required very often.  To understand the beauty
of this system, you must see how Zope 2 actually get the physical
root object and how it is implemented.  There is a method called
``getPhysicalRoot`` virtually for all container objects.


DefaultSized
~~~~~~~~~~~~

Ubicación: ``zope.size.DefaultSized``

This adapter is just a default implementation of ``ISized`` interface.
This adapter is registered for all kind of objects.  If you want to
register this adapter for a particular interface, then you have to
override this registration for your implementation.

The registration of adapter is like this::

  <adapter
      for="*"
      factory="zope.size.DefaultSized"
      provides="zope.size.interfaces.ISized"
      permission="zope.View"
      />

As you can see, the adaptee interface is `*`, so it can adapt any kind
of objects.

The ``ISized`` is a simple interface with two method contracts::

  class ISized(Interface):

      def sizeForSorting():
          """Returns a tuple (basic_unit, amount)

          Used for sorting among different kinds of sized objects.
          'amount' need only be sortable among things that share the
          same basic unit."""

      def sizeForDisplay():
          """Returns a string giving the size.
          """

You can see another ``ISized`` adapter registered for ``IZPTPage`` in
``zope.app.zptpage`` package.


ZopeVersionUtility
~~~~~~~~~~~~~~~~~~

Ubicación: ``zope.app.applicationcontrol.ZopeVersionUtility``

This utility gives version of the running Zope.

The registration goes like this::

  <utility
      component=".zopeversion.ZopeVersionUtility"
      provides=".interfaces.IZopeVersion" />

The interface provided, ``IZopeVersion``, has only one method named
``getZopeVersion``.  This method return a string containing the Zope
version (possibly including SVN information).

The default implementation, ``ZopeVersionUtility``, get version info
from a file ``version.txt`` in `zope/app` directory.  If Zope is
running from subversion checkout, it will show the latest revision
number.  If none of the above works it will set it to:
`Development/Unknown`.


Referencia
----------

.. note::

Attribute
~~~~~~~~~

Using this class, you can define normal attribute in an interface.

 - Location: ``zope.interface``

 - Signature: `Attribute(name, doc='')`

Example::

  >>> from zope.interface import Attribute
  >>> from zope.interface import Interface

  >>> class IPerson(Interface):
  ...
  ...     name = Attribute("Name of person")
  ...     email = Attribute("Email Address")


Declaration
~~~~~~~~~~~

Need not to use directly.


Interface
~~~~~~~~~

Using this class, you can define an interface.  To define an
interface, just inherit from ``Interface`` class.

 - Ubicación: ``zope.component``

 - Signature: `Interface(name, doc='')`

Example 1::

  >>> from zope.interface import Attribute
  >>> from zope.interface import Interface

  >>> class IPerson(Interface):
  ...
  ...     name = Attribute("Name of person")
  ...     email = Attribute("Email Address")


Example 2::

  >>> from zope.interface import Interface

  >>> class IHost(Interface):
  ...
  ...     def goodmorning(guest):
  ...         """Say good morning to guest"""


adapts
~~~~~~

This function helps to declare adapter classes.

 - Ubicación: ``zope.component``

 - Firma: `adapts(*interfaces)`

Ejemplo::

  >>> from zope.interface import implements
  >>> from zope.component import adapts

  >>> class RegistradorHuespedNG(object):
  ...
  ...     implements(IRegistrar)
  ...     adapts(IHuesped)
  ...
  ...     def __init__(self, huesped):
  ...         self.huesped = huesped
  ...
  ...     def registrar(self):
  ...         huesped_id = proximo_id()
  ...         huespedes_db[huesped_id] = {
  ...         'nombre': huesped.nombre,
  ...         'lugar': huesped.lugar,
  ...         'telefono': huesped.telefono
  ...         }


alsoProvides
~~~~~~~~~~~~

Declara interfaces declaradas directamente para un objeto.  The arguments
after the object are one or more interfaces.  The interfaces given are
added to the interfaces previously declared for the object.

 - Ubicación: ``zope.interface``

 - Firma: `alsoProvides(object, *interfaces)`

Ejemplo::

  >>> from zope.interface import Attribute
  >>> from zope.interface import Interface
  >>> from zope.interface import implements
  >>> from zope.interface import alsoProvides

  >>> class IPersona(Interface):
  ...
  ...     nombre = Attribute("Nombre de persona")

  >>> class IEstudiante(Interface):
  ...
  ...     colegio = Attribute("Nombre de colegio")

  >>> class Persona(object):
  ...
  ...     implements(IRegistrar)
  ...     nombre = u""

  >>> pepe = Persona()
  >>> pepe.nombre = "Pepe"
  >>> pepe.colegio = "Nuevo Colegio"
  >>> alsoProvides(pepe, IEstudiante)

  Usted puede probar con esto: ::

  >>> from zope.interface import providedBy
  >>> IEstudiante in providedBy(pepe)
  True


Atributo
~~~~~~~~

Usando esta clase, usted puede definir atributos normalesen una interfaz.

 - Ubicación: ``zope.interface``

 - Firma: `Attribute(name, doc='')`

 - Ver también: `Interface`_

Ejemplo::

  >>> from zope.interface import Attribute
  >>> from zope.interface import Interface

  >>> class IPersona(Interface):
  ...
  ...     nombre = Attribute("Nombre de persona")
  ...     email = Attribute("Direccion de email")


classImplements
~~~~~~~~~~~~~~~

Declara interfaces adicionales implementadas por instancias de una clase.
The arguments after the class are one or more interfaces.  The
interfaces given are added to any interfaces previously declared.

 - Ubicación: ``zope.interface``

 - Firma: `classImplements(cls, *interfaces)`

Ejemplo::

  >>> from zope.interface import Attribute
  >>> from zope.interface import Interface
  >>> from zope.interface import implements
  >>> from zope.interface import classImplements

  >>> class IPersona(Interface):
  ...
  ...     nombre = Attribute("Nombre de persona")

  >>> class IEstudiante(Interface):
  ...
  ...     colegio = Attribute("Nombre de colegio")

  >>> class Persona(object):
  ...
  ...     implements(IRegistrar)
  ...     nombre = u""
  ...     colegio = u""

  >>> classImplements(Persona, IStudent)
  >>> pepe = Persona()
  >>> pepe.nombre = "Pepe"
  >>> pepe.colegio = "Nuevo Colegio"

  Usted puede probar con esto: ::

  >>> from zope.interface import providedBy
  >>> IEstudiante in providedBy(pepe)
  True


classImplementsOnly
~~~~~~~~~~~~~~~~~~~

Declara solamente interfaces implementadas por instancias de una clase.  The
arguments after the class are one or more interfaces.  The interfaces
given replace any previous declarations.

 - Ubicación: ``zope.interface``

 - Firma: `classImplementsOnly(cls, *interfaces)`

Ejemplo::

  >>> from zope.interface import Attribute
  >>> from zope.interface import Interface
  >>> from zope.interface import implements
  >>> from zope.interface import classImplementsOnly

  >>> class IPersona(Interface):
  ...
  ...     nombre = Attribute("Nombre de persona")

  >>> class IEstudiante(Interface):
  ...
  ...     colegio = Attribute("Nombre de colegio")

  >>> class Persona(object):
  ...
  ...     implements(IPersona)
  ...     colegio = u""

  >>> classImplementsOnly(Persona, IEstudiante)
  >>> pepe = Persona()
  >>> pepe.colegio = "Nuevo Colegio"

  Usted puede probar con esto: ::

  >>> from zope.interface import providedBy
  >>> IPersona in providedBy(pepe)
  False
  >>> IEstudiante in providedBy(pepe)
  True


classProvides
~~~~~~~~~~~~~

Normally if a class implements a particular interface, the instance of
that class will provide the interface implemented by that class.  But
if you want a class to be provided by an interface, you can declare it
using ``classProvides`` function.

 - Ubicación: ``zope.interface``

 - Firma: `classProvides(*interfaces)`

Ejemplo::

  >>> from zope.interface import Attribute
  >>> from zope.interface import Interface
  >>> from zope.interface import classProvides

  >>> class IPersona(Interface):
  ...
  ...     nombre = Attribute("Nombre de persona")

  >>> class Persona(object):
  ...
  ...     classProvides(IPersona)
  ...     name = u"Pepe"

  Usted puede probar con esto: ::

  >>> from zope.interface import providedBy
  >>> IPersona in providedBy(Persona)
  True


ComponentLookupError
~~~~~~~~~~~~~~~~~~~~

This is the exception raised when a component lookup fails.

Ejemplo::

  >>> class IPersona(Interface):
  ...
  ...     nombre = Attribute("Nombre de persona")

  >>> person = object()
  >>> getAdapter(persona, IPersona, 'not-exists') #doctest: +ELLIPSIS
  Traceback (most recent call last):
  ...
  ComponentLookupError: ...


createObject
~~~~~~~~~~~~

Create an object using a factory.

Finds the named factory in the current site and calls it with the
given arguments.  If a matching factory cannot be found raises
``ComponentLookupError``.  Returns the created object.

A context keyword argument can be provided to cause the factory to be
looked up in a location other than the current site.  (Of course, this
means that it is impossible to pass a keyword argument named "context"
to the factory.

 - Ubicación: ``zope.component``

 - Firma: `createObject(factory_name, *args, **kwargs)`

Ejemplo::

  >>> from zope.interface import Attribute
  >>> from zope.interface import Interface
  >>> from zope.interface import implements

  >>> class IBaseDatos(Interface):
  ...
  ...     def getConexion():
  ...         """Devuelve el objecto conexion"""

  >>> class FakeDb(object):
  ...
  ...     implements(IBaseDatos)
  ...
  ...     def getConexion(self):
  ...         return "conexion"

  >>> from zope.component.factory import Factory

  >>> factory = Factory(FakeDb, 'FakeDb')

  >>> from zope.component import getGlobalSiteManager
  >>> gsm = getGlobalSiteManager()

  >>> from zope.component.interfaces import IFactory
  >>> gsm.registerUtility(factory, IFactory, 'fakedb')

  >>> from zope.component import createObject
  >>> createObject('fakedb') #doctest: +ELLIPSIS
  <FakeDb object at ...>


Declaración
~~~~~~~~~~~

Need not to use directly.


directlyProvidedBy
~~~~~~~~~~~~~~~~~~

This function will return the interfaces directly provided by the
given object.

 - Ubicación: ``zope.interface``

 - Firma: `directlyProvidedBy(object)`

Ejemplo::

  >>> from zope.interface import Attribute
  >>> from zope.interface import Interface

  >>> class IPersona(Interface):
  ...
  ...     nombre = Attribute("Nombre de persona")

  >>> class IEstudiante(Interface):
  ...
  ...     colegio = Attribute("Nombre de colegio")

  >>> class IPersonaInteligente(Interface):
  ...     pass

  >>> class Persona(object):
  ...
  ...     implements(IPersona)
  ...     nombre = u""

  >>> pepe = Persona()
  >>> pepe.nombre = u"Pepe"
  >>> pepe.colegio = "Nuevo Colegio"
  >>> alsoProvides(pepe, IPersonaInteligente, IEstudiante)

  >>> from zope.interface import directlyProvidedBy

  >>> pepe_dp = directlyProvidedBy(pepe)
  >>> IPersona in pepe_dp.interfaces()
  False
  >>> IEstudiante in pepe_dp.interfaces()
  True
  >>> IPersonaInteligente in pepe_dp.interfaces()
  True


directlyProvides
~~~~~~~~~~~~~~~~

Declara interfaces declaradas directamente para un objeto.  The arguments
after the object are one or more interfaces.  The interfaces given
replace interfaces previously declared for the object.

 - Ubicación: ``zope.interface``

 - Firma: `directlyProvides(object, *interfaces)`

Ejemplo::

  >>> from zope.interface import Attribute
  >>> from zope.interface import Interface

  >>> class IPersona(Interface):
  ...
  ...     nombre = Attribute("Nombre de persona")

  >>> class IEstudiante(Interface):
  ...
  ...     colegio = Attribute("Nombre de colegio")

  >>> class IPersonaInteligente(Interface):
  ...     pass

  >>> class Persona(object):
  ...
  ...     implements(IPersona)
  ...     nombre = u""

  >>> pepe = Persona()
  >>> pepe.nombre = u"Pepe"
  >>> pepe.colegio = "Nuevo Colegio"
  >>> alsoProvides(pepe, IPersonaInteligente, IEstudiante)

  >>> from zope.interface import directlyProvidedBy

  >>> pepe_dp = directlyProvidedBy(pepe)
  >>> IPersonaInteligente in pepe_dp.interfaces()
  True
  >>> IPersona in pepe_dp.interfaces()
  False
  >>> IEstudiante in pepe_dp.interfaces()
  True
  >>> from zope.interface import providedBy

  >>> IPersonaInteligente in providedBy(pepe)
  True

  >>> from zope.interface import directlyProvides
  >>> directlyProvides(pepe, IEstudiante)

  >>> pepe_dp = directlyProvidedBy(pepe)
  >>> IPersonaInteligente in pepe_dp.interfaces()
  False
  >>> IPersona in pepe_dp.interfaces()
  False
  >>> IEstudiante in pepe_dp.interfaces()
  True

  >>> IPersonaInteligente in providedBy(pepe)
  False


getAdapter
~~~~~~~~~~

Get a named adapter to an interface for an object.  Returns an adapter
that can adapt object to interface.  If a matching adapter cannot be
found, raises ``ComponentLookupError`` .

 - Ubicación: ``zope.interface``

 - Firma: `getAdapter(object, interface=Interface, name=u'', context=None)`

Ejemplo::

  >>> from zope.interface import Attribute
  >>> from zope.interface import Interface

  >>> class IRegistrador(Interface):
  ...     """Un registrador registrará los detalles de un objeto"""
  ...
  ...     def registrar():
  ...         """Registrar detalles de un objeto"""
  ...

  >>> from zope.interface import implements
  >>> from zope.component import adapts

  >>> class RegistradorHuespedNG(object):
  ...
  ...     implements(IRegistrar)
  ...     adapts(IHuesped)
  ...
  ...     def __init__(self, huesped):
  ...         self.huesped = huesped
  ...
  ...     def registrar(self):
  ...         huesped_id = proximo_id()
  ...         huespedes_db[huesped_id] = {
  ...         'nombre': huesped.nombre,
  ...         'lugar': huesped.lugar,
  ...         'telefono': huesped.telefono
  ...         }

  >>> class Huesped(object):
  ...
  ...     implements(IHuesped)
  ...
  ...     def __init__(self, nombre, lugar):
  ...         self.nombre = nombre
  ...         self.lugar = lugar

  >>> pepe = Huesped("Pepe", "España")
  >>> pepe_registradorhuesped = RegistradorHuespedNG(pepe)

  >>> IRegistrador.providedBy(pepe_registradorhuesped)
  True

  >>> from zope.component import getGlobalSiteManager
  >>> gsm = getGlobalSiteManager()
  >>> gsm.registerAdapter(RegistradorHuespedNG,
  ...                     (IHuesped,), IRegistrador, 'ng')

  >>> getAdapter(pepe, IRegistrador, 'ng') #doctest: +ELLIPSIS
  <RegistradorHuespedNG object at ...>


getAdapterInContext
~~~~~~~~~~~~~~~~~~~

Instead of this function, use `context` argument of `getAdapter`_
function.

 - Ubicación: ``zope.component``

 - Firma: `getAdapterInContext(object, interface, context)`

 - Ver también: `queryAdapterInContext`_

Ejemplo::

  >>> from zope.component.globalregistry import BaseGlobalComponents
  >>> from zope.component import IComponentLookup
  >>> sm = BaseGlobalComponents()

  >>> class Context(object):
  ...     def __init__(self, sm):
  ...         self.sm = sm
  ...     def __conform__(self, interface):
  ...         if interface.isOrExtends(IComponentLookup):
  ...             return self.sm

  >>> context = Context(sm)

  >>> from zope.interface import Attribute
  >>> from zope.interface import Interface

  >>> class IRegistrador(Interface):
  ...     """Un registrador registrará los detalles de un objeto"""
  ...
  ...     def registrar():
  ...         """Registrar detalles de un objeto"""
  ...

  >>> from zope.interface import implements
  >>> from zope.component import adapts

  >>> class RegistradorHuespedNG(object):
  ...
  ...     implements(IRegistrar)
  ...     adapts(IHuesped)
  ...
  ...     def __init__(self, huesped):
  ...         self.huesped = huesped
  ...
  ...     def registrar(self):
  ...         huesped_id = proximo_id()
  ...         huespedes_db[huesped_id] = {
  ...         'nombre': huesped.nombre,
  ...         'lugar': huesped.lugar,
  ...         'telefono': huesped.telefono
  ...         }

  >>> class Huesped(object):
  ...
  ...     implements(IHuesped)
  ...
  ...     def __init__(self, nombre, lugar):
  ...         self.nombre = nombre
  ...         self.lugar = lugar

  >>> pepe = Huesped("Pepe", "España")
  >>> pepe_registradorhuesped = RegistradorHuespedNG(pepe)

  >>> IRegistrador.providedBy(pepe_registradorhuesped)
  True

  >>> from zope.component import getGlobalSiteManager
  >>> gsm = getGlobalSiteManager()
  >>> sm.registerAdapter(RegistradorHuespedNG,
  ...                     (IHuesped,), IRegistrador)

  >>> from zope.component import getAdapterInContext

  >>> getAdapterInContext(pepe, IRegistrador, sm) #doctest: +ELLIPSIS
  <RegistradorHuespedNG object at ...>


getAdapters
~~~~~~~~~~~

Look for all matching adapters to a provided interface for objects.
Return a list of adapters that match. If an adapter is named, only the
most specific adapter of a given name is returned.

 - Ubicación: ``zope.component``

 - Firma: `getAdapters(objects, provided, context=None)`

Ejemplo::

  >>> from zope.interface import implements
  >>> from zope.component import adapts

  >>> class RegistradorHuespedNG(object):
  ...
  ...     implements(IRegistrar)
  ...     adapts(IHuesped)
  ...
  ...     def __init__(self, huesped):
  ...         self.huesped = huesped
  ...
  ...     def registrar(self):
  ...         huesped_id = proximo_id()
  ...         huespedes_db[huesped_id] = {
  ...         'nombre': huesped.nombre,
  ...         'lugar': huesped.lugar,
  ...         'telefono': huesped.telefono
  ...         }

  >>> pepe = Huesped("Pepe", "España")
  >>> pepe_registradorhuesped = RegistradorHuespedNG(pepe)

  >>> from zope.component import getGlobalSiteManager
  >>> gsm = getGlobalSiteManager()

  >>> gsm.registerAdapter(RegistradorHuespedNG, name='ng')

  >>> from zope.component import getAdapters
  >>> list(getAdapters((jack,), IRegistrador)) #doctest: +ELLIPSIS
  [(u'ng', <RegistradorHuespedNG object at ...>)]


getAllUtilitiesRegisteredFor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Return all registered utilities for an interface.  This includes
overridden utilities.  The returned value is an iterable of utility
instances.

 - Ubicación: ``zope.component``

 - Firma: `getAllUtilitiesRegisteredFor(interface)`

Ejemplo::

  >>> from zope.interface import Interface
  >>> from zope.interface import implements

  >>> class ISaludador(Interface):
  ...     def saludar(name):
  ...         "decir hola"

  >>> class Saludador(object):
  ...
  ...     implements(ISaludador)
  ...
  ...     def saludar(self, name):
  ...         print "Hola", name

  >>> from zope.component import getGlobalSiteManager
  >>> gsm = getGlobalSiteManager()

  >>> saludar = Saludador()
  >>> gsm.registerUtility(saludar, ISaludador)

  >>> from zope.component import getAllUtilitiesRegisteredFor

  >>> getAllUtilitiesRegisteredFor(ISaludador) #doctest: +ELLIPSIS
  [<Saludador object at ...>]


getFactoriesFor
~~~~~~~~~~~~~~~

Return a tuple (name, factory) of registered factories that create
objects which implement the given interface.

 - Ubicación: ``zope.component``

 - Firma: `getFactoriesFor(interface, context=None)`

Ejemplo::

  >>> from zope.interface import Attribute
  >>> from zope.interface import Interface
  >>> from zope.interface import implements

  >>> class IBaseDatos(Interface):
  ...
  ...     def getConexion():
  ...         """Devuelve el objecto conexion"""

  >>> class FakeDb(object):
  ...
  ...     implements(IBaseDatos)
  ...
  ...     def getConexion(self):
  ...         return "conexion"

  >>> from zope.component.factory import Factory

  >>> factory = Factory(FakeDb, 'FakeDb')

  >>> from zope.component import getGlobalSiteManager
  >>> gsm = getGlobalSiteManager()

  >>> from zope.component.interfaces import IFactory
  >>> gsm.registerUtility(factory, IFactory, 'fakedb')

  >>> from zope.component import getFactoriesFor

  >>> list(getFactoriesFor(IBaseDatos))
  [(u'fakedb', <Factory for <class 'FakeDb'>>)]


getFactoryInterfaces
~~~~~~~~~~~~~~~~~~~~

Get interfaces implemented by a factory.  Finds the factory of the
given name that is nearest to the context, and returns the interface
or interface tuple that object instances created by the named factory
will implement.

 - Ubicación: ``zope.component``

 - Firma: `getFactoryInterfaces(name, context=None)`

Ejemplo::

  >>> from zope.interface import Attribute
  >>> from zope.interface import Interface
  >>> from zope.interface import implements

  >>> class IBaseDatos(Interface):
  ...
  ...     def getConexion():
  ...         """Devuelve el objecto conexion"""

  >>> class FakeDb(object):
  ...
  ...     implements(IBaseDatos)
  ...
  ...     def getConexion(self):
  ...         return "conexion"

  >>> from zope.component.factory import Factory

  >>> factory = Factory(FakeDb, 'FakeDb')

  >>> from zope.component import getGlobalSiteManager
  >>> gsm = getGlobalSiteManager()

  >>> from zope.component.interfaces import IFactory
  >>> gsm.registerUtility(factory, IFactory, 'fakedb')

  >>> from zope.component import getFactoryInterfaces

  >>> getFactoryInterfaces('fakedb')
  <implementedBy __builtin__.FakeDb>


getGlobalSiteManager
~~~~~~~~~~~~~~~~~~~~

Return the global site manager.  This function should never fail and
always return an object that provides `IGlobalSiteManager`

 - Ubicación: ``zope.component``

 - Firma: `getGlobalSiteManager()`

Ejemplo::

  >>> from zope.component import getGlobalSiteManager
  >>> from zope.component import globalSiteManager
  >>> gsm = getGlobalSiteManager()
  >>> gsm is globalSiteManager
  True


getMultiAdapter
~~~~~~~~~~~~~~~

Look for a multi-adapter to an interface for an objects.  Returns a
multi-adapter that can adapt objects to interface.  If a matching
adapter cannot be found, raises ComponentLookupError.  The name
consisting of an empty string is reserved for unnamed adapters. The
unnamed adapter methods will often call the named adapter methods with
an empty string for a name.

 - Ubicación: ``zope.component``

 - Firma: `getMultiAdapter(objects, interface=Interface, name='',
   context=None)`

 - Ver también: `queryMultiAdapter`_

Ejemplo::

  >>> from zope.interface import Interface
  >>> from zope.interface import implements
  >>> from zope.component import adapts

  >>> class IAdaptadoUno(Interface):
  ...     pass

  >>> class IAdaptadoDos(Interface):
  ...     pass

  >>> class IFuncionalidad(Interface):
  ...     pass

  >>> class MiFuncionalidad(object):
  ...     implements(IFuncionalidad)
  ...     adapts(IAdaptadoUno, IAdaptadoDos)
  ...
  ...     def __init__(self, uno, dos):
  ...         self.uno = uno
  ...         self.dos = dos

  >>> from zope.component import getGlobalSiteManager
  >>> gsm = getGlobalSiteManager()

  >>> gsm.registerAdapter(MiFuncionalidad)

  >>> class Uno(object):
  ...     implements(IAdaptadoUno)

  >>> class Dos(object):
  ...     implements(IAdaptadoDos)

  >>> uno = Uno()
  >>> dos = Dos()

  >>> from zope.component import getMultiAdapter

  >>> getMultiAdapter((uno,dos), IFuncionalidad) #doctest: +ELLIPSIS
  <MiFuncionalidad object at ...>

  >>> mifuncionalidad = getMultiAdapter((uno,dos), IFuncionalidad)
  >>> mifuncionalidad.uno #doctest: +ELLIPSIS
  <Uno object at ...>
  >>> mifuncionalidad.dos #doctest: +ELLIPSIS
  <Dos object at ...>


getSiteManager
~~~~~~~~~~~~~~

Get the nearest site manager in the given context.  If `context` is
`None`, return the global site manager.  If the `context` is not
`None`, it is expected that an adapter from the `context` to
`IComponentLookup` can be found.  If no adapter is found, a
`ComponentLookupError` is raised.

 - Ubicación: ``zope.component``

 - Firma: `getSiteManager(context=None)`

Ejemplo 1::

  >>> from zope.component.globalregistry import BaseGlobalComponents
  >>> from zope.component import IComponentLookup
  >>> sm = BaseGlobalComponents()

  >>> class Context(object):
  ...     def __init__(self, sm):
  ...         self.sm = sm
  ...     def __conform__(self, interface):
  ...         if interface.isOrExtends(IComponentLookup):
  ...             return self.sm

  >>> context = Context(sm)

  >>> from zope.component import getSiteManager

  >>> lsm = getSiteManager(context)
  >>> lsm is sm
  True

Ejemplo 2::

  >>> from zope.component import getGlobalSiteManager
  >>> gsm = getGlobalSiteManager()

  >>> sm = getSiteManager()
  >>> gsm is sm
  True


getUtilitiesFor
~~~~~~~~~~~~~~~

Look up the registered utilities that provide an interface.  Returns
an iterable of name-utility pairs.

 - Ubicación: ``zope.component``

 - Firma: `getUtilitiesFor(interface)`

Ejemplo::

  >>> from zope.interface import Interface
  >>> from zope.interface import implements

  >>> class ISaludador(Interface):
  ...     def saludar(name):
  ...         "decir hola"

  >>> class Saludador(object):
  ...
  ...     implements(ISaludador)
  ...
  ...     def saludar(self, name):
  ...         print "Hola", name

  >>> from zope.component import getGlobalSiteManager
  >>> gsm = getGlobalSiteManager()

  >>> saludar = Saludador()
  >>> gsm.registerUtility(saludar, ISaludador)

  >>> from zope.component import getUtilitiesFor

  >>> list(getUtilitiesFor(ISaludador)) #doctest: +ELLIPSIS
  [(u'', <Saludador object at ...>)]


getUtility
~~~~~~~~~~

Get the utility that provides interface.  Returns the nearest utility
to the context that implements the specified interface.  If one is not
found, raises ``ComponentLookupError``.

 - Ubicación: ``zope.component``

 - Firma: `getUtility(interface, name='', context=None)`

Ejemplo::

  >>> from zope.interface import Interface
  >>> from zope.interface import implements

  >>> class ISaludador(Interface):
  ...     def saludar(name):
  ...         "decir hola"

  >>> class Saludador(object):
  ...
  ...     implements(ISaludador)
  ...
  ...     def saludar(self, name):
  ...         return "Hola" + name

  >>> from zope.component import getGlobalSiteManager
  >>> gsm = getGlobalSiteManager()

  >>> saludar = Saludador()
  >>> gsm.registerUtility(saludar, ISaludador)

  >>> from zope.component import getUtility

  >>> getUtility(ISaludador).saludar('Jack')
  'Hola Pepe'


handle
~~~~~~

Call all of the handlers for the given objects.  Handlers are
subscription adapter factories that don't produce anything.  They do
all of their work when called.  Handlers are typically used to handle
events.

 - Ubicación: ``zope.component``

 - Firma: `handle(*objects)`

Ejemplo::

  >>> import datetime

  >>> def documentoCreado(event):
  ...     event.doc.created = datetime.datetime.utcnow()

  >>> from zope.interface import Interface
  >>> from zope.interface import Attribute
  >>> from zope.interface import implements

  >>> class IDocumentoCreado(Interface):
  ...     doc = Attribute("El documento que fue creado")

  >>> class DocumentoCreado(object):
  ...     implements(IDocumentoCreado)
  ...
  ...     def __init__(self, doc):
  ...         self.doc = doc


  >>> def documentoCreado(event):
  ...     event.doc.created = datetime.datetime.utcnow()

  >>> from zope.component import adapter

  >>> @adapter(IDocumentoCreado)
  ... def documentoCreado(event):
  ...     event.doc.created = datetime.datetime.utcnow()


  >>> from zope.component import getGlobalSiteManager
  >>> gsm = getGlobalSiteManager()

  >>> gsm.registerHandler(documentoCreado)

  >>> from zope.component import handle

  >>> handle(DocumentCreated(doc))
  >>> doc.created.__class__.__name__
  'datetime'


implementedBy
~~~~~~~~~~~~~

Return the interfaces implemented for a class' instances.

 - Ubicación: ``zope.interface``

 - Firma: `implementedBy(class_)`

Ejemplo 1::

  >>> from zope.interface import Interface
  >>> from zope.interface import implements

  >>> class ISaludador(Interface):
  ...     def saludar(name):
  ...         "decir hola"

  >>> class Saludador(object):
  ...
  ...     implements(ISaludador)
  ...
  ...     def saludar(self, name):
  ...         print "Hola", name

  >>> from zope.interface import implementedBy
  >>> implementedBy(Saludador)
  <implementedBy __builtin__.Greeter>

Ejemplo 2::

  >>> from zope.interface import Attribute
  >>> from zope.interface import Interface
  >>> from zope.interface import implements

  >>> class IPersona(Interface):
  ...     nombre = Attribute("Nombre de persona")

  >>> class IEspecial(Interface):
  ...     pass

  >>> class Persona(object):
  ...     implements(IPersona)
  ...     nombre = u""

  >>> from zope.interface import classImplements
  >>> classImplements(Person, IEspecial)

  >>> from zope.interface import implementedBy

  To get a list of all interfaces implemented by that class::

  >>> [x.__name__ for x in implementedBy(Persona)]
  ['IPersona', 'IEspecial']


implementer
~~~~~~~~~~~

Create a decorator for declaring interfaces implemented by a factory.
A callable is returned that makes an implements declaration on objects
passed to it.

 - Ubicación: ``zope.interface``

 - Firma: `implementer(*interfaces)`

Ejemplo::

  >>> from zope.interface import implementer
  >>> class IPrueba(Interface):
  ...     pass
  >>> class Prueba(object):
  ...     implements(IPrueba)

  >>> @implementer(IPrueba)
  ... def creadorprueba():
  ...     prueba = Prueba()
  ...     return prueba
  >>> list(implementedBy(creadorprueba))
  [<InterfaceClass __builtin__.IPrueba>]


implements
~~~~~~~~~~

Declara interfaces implementadas por instancias de una clase. Esta función es llamada en una definicón de clase.  The arguments are one or more
interfaces.  The interfaces given are added to any interfaces
previously declared.  Previous declarations include declarations for
base classes unless implementsOnly was used.

 - Ubicación: ``zope.interface``

 - Firma: `implements(*interfaces)`

Ejemplo::

  >>> from zope.interface import Attribute
  >>> from zope.interface import Interface
  >>> from zope.interface import implements

  >>> class IPersona(Interface):
  ...
  ...     nombre = Attribute("Nombre de persona")

  >>> class Persona(object):
  ...
  ...     implements(IPersona)
  ...     nombre = u""

  >>> pepe = Persona()
  >>> pepe.nombre = "Pepe"

  Usted puede probar con esto: ::

  >>> from zope.interface import providedBy
  >>> IPersona in providedBy(pepe)
  True


implementsOnly
~~~~~~~~~~~~~~

Declara solamente interfaces implementadas por instancias de una clase.  This
function is called in a class definition.  The arguments are one or
more interfaces.  Previous declarations including declarations for
base classes are overridden.

 - Ubicación: ``zope.interface``

 - Firma: `implementsOnly(*interfaces)`

Ejemplo::

  >>> from zope.interface import Attribute
  >>> from zope.interface import Interface
  >>> from zope.interface import implements
  >>> from zope.interface import implementsOnly

  >>> class IPersona(Interface):
  ...
  ...     nombre = Attribute("Nombre de persona")

  >>> class IEstudiante(Interface):
  ...
  ...     colegio = Attribute("Nombre de colegio")

  >>> class Persona(object):
  ...
  ...     implements(IPersona)
  ...     nombre = u""

  >>> class NuevaPersona(Persona):
  ...     implementsOnly(IEstudiante)
  ...     colegio = u""

  >>> pepe = NuevaPersona()
  >>> pepe.colegio = "Nuevo Colegio"

  Usted puede probar con esto: ::

  >>> from zope.interface import providedBy
  >>> IPersona in providedBy(pepe)
  False
  >>> IEstudiante in providedBy(pepe)
  True


Interface
~~~~~~~~~

Usando esta clase, usted puede definir una interfaz.  To define an
interface, just inherit from ``Interface`` class.

 - Ubicación: ``zope.interface``

 - Firma: `Interface(name, doc='')`

Ejemplo 1::

  >>> from zope.interface import Attribute
  >>> from zope.interface import Interface

  >>> class IPersona(Interface):
  ...
  ...     nombre = Attribute("Nombre de persona")
  ...     email = Attribute("Direccion de email")


Ejemplo 2::

  >>> from zope.interface import Interface

  >>> class IAnfitrion(Interface):
  ...
  ...     def buenosdias(huesped):
  ...         """Le dice buenos dias al huesped"""


moduleProvides
~~~~~~~~~~~~~~

Declara interfaces proveidas por un módulo.  This function is used in a
module definition.  The arguments are one or more interfaces.  The
given interfaces are used to create the module's direct-object
interface specification.  An error will be raised if the module
already has an interface specification.  In other words, it is an
error to call this function more than once in a module definition.

This function is provided for convenience.  It provides a more
convenient way to call ``directlyProvides`` for a module.

 - Ubicación: ``zope.interface``

 - Firma: `moduleProvides(*interfaces)`

 - Ver también: `directlyProvides`_

You can see an example usage in `zope.component` source itself.  The
`__init__.py` file has a statement like this::

  moduleProvides(IComponentArchitecture,
                 IComponentRegistrationConvenience)

So, the `zope.component` provides two interfaces:
`IComponentArchitecture` and `IComponentRegistrationConvenience`.


noLongerProvides
~~~~~~~~~~~~~~~~

Remove an interface from the list of an object's directly provided
interfaces.

 - Ubicación: ``zope.interface``

 - Firma: `noLongerProvides(object, interface)`

Ejemplo::

  >>> from zope.interface import Attribute
  >>> from zope.interface import Interface
  >>> from zope.interface import implements
  >>> from zope.interface import classImplements

  >>> class IPersona(Interface):
  ...
  ...     nombre = Attribute("Nombre de persona")

  >>> class IEstudiante(Interface):
  ...
  ...     colegio = Attribute("Nombre de colegio")

  >>> class Persona(object):
  ...
  ...     implements(IPersona)
  ...     nombre = u""

  >>> pepe = Persona()
  >>> pepe.nombre = "Pepe"
  >>> pepe.colegio = "Nuevo Colegio"
  >>> directlyProvides(pepe, IEstudiante)

  Usted puede probar con esto: ::

  >>> from zope.interface import providedBy
  >>> IPersona in providedBy(pepe)
  True
  >>> IEstudiante in providedBy(pepe)
  True
  >>> from zope.interface import noLongerProvides
  >>> noLongerProvides(pepe, IEstudiante)
  >>> IPersona in providedBy(pepe)
  True
  >>> IEstudiante in providedBy(pepe)
  False


provideAdapter
~~~~~~~~~~~~~~

It is recommended to use `registerAdapter`_ .


provideHandler
~~~~~~~~~~~~~~

It is recommended to use `registerHandler`_ .


provideSubscriptionAdapter
~~~~~~~~~~~~~~~~~~~~~~~~~~

It is recommended to use `registerSubscriptionAdapter`_ .


provideUtility
~~~~~~~~~~~~~~

It is recommended to use `registerUtility`_ .


providedBy
~~~~~~~~~~

Test whether the interface is implemented by the object.  Return true
if the object asserts that it implements the interface, including
asserting that it implements an extended interface.

 - Ubicación: ``zope.interface``

 - Firma: `providedBy(object)`

Ejemplo 1::

  >>> from zope.interface import Attribute
  >>> from zope.interface import Interface
  >>> from zope.interface import implements

  >>> class IPersona(Interface):
  ...
  ...     nombre = Attribute("Nombre de persona")

  >>> class Persona(object):
  ...
  ...     implements(IPersona)
  ...     nombre = u""

  >>> pepe = Persona()
  >>> pepe.nombre = "Pepe"

  Usted puede probar con esto: ::

  >>> from zope.interface import providedBy
  >>> IPersona in providedBy(pepe)
  True

Ejemplo 2::

  >>> from zope.interface import Attribute
  >>> from zope.interface import Interface
  >>> from zope.interface import implements

  >>> class IPersona(Interface):
  ...     nombre = Attribute("Nombre de persona")

  >>> class IEspecial(Interface):
  ...     pass

  >>> class Persona(object):
  ...     implements(IPersona)
  ...     nombre = u""

  >>> from zope.interface import classImplements
  >>> classImplements(Person, IEspecial)
  >>> from zope.interface import providedBy
  >>> pepe = Persona()
  >>> pepe.nombre = "Pepe"

  To get a list of all interfaces provided by that object::

  >>> [x.__name__ for x in providedBy(pepe)]
  ['IPersona', 'IEspecial']


queryAdapter
~~~~~~~~~~~~

Look for a named adapter to an interface for an object.  Returns an
adapter that can adapt object to interface.  If a matching adapter
cannot be found, returns the default.

 - Ubicación: ``zope.component``

 - Firma: `queryAdapter(object, interface=Interface, name=u'',
   default=None, context=None)`

Ejemplo::

  >>> from zope.interface import Attribute
  >>> from zope.interface import Interface

  >>> class IRegistrador(Interface):
  ...     """Un registrador registrará los detalles de un objeto"""
  ...
  ...     def registrar():
  ...         """Registrar detalles de un objeto"""
  ...

  >>> from zope.interface import implements
  >>> from zope.component import adapts

  >>> class RegistradorHuespedNG(object):
  ...
  ...     implements(IRegistrar)
  ...     adapts(IHuesped)
  ...
  ...     def __init__(self, huesped):
  ...         self.huesped = huesped
  ...
  ...     def registrar(self):
  ...         huesped_id = proximo_id()
  ...         huespedes_db[huesped_id] = {
  ...         'nombre': huesped.nombre,
  ...         'lugar': huesped.lugar,
  ...         'telefono': huesped.telefono
  ...         }

  >>> class Huesped(object):
  ...
  ...     implements(IHuesped)
  ...
  ...     def __init__(self, nombre, lugar):
  ...         self.nombre = nombre
  ...         self.lugar = lugar

  >>> pepe = Huesped("Pepe", "España")
  >>> pepe_registradorhuesped = RegistradorHuespedNG(pepe)

  >>> IRegistrador.providedBy(pepe_registradorhuesped)
  True

  >>> from zope.component import getGlobalSiteManager
  >>> gsm = getGlobalSiteManager()
  >>> gsm.registerAdapter(RegistradorHuespedNG,
  ...                     (IHuesped,), IRegistrador, 'ng')

  >>> queryAdapter(pepe, IRegistrador, 'ng') #doctest: +ELLIPSIS
  <RegistradorHuespedNG object at ...>


queryAdapterInContext
~~~~~~~~~~~~~~~~~~~~~

Look for a special adapter to an interface for an object.

NOTE: This method should only be used if a custom context needs to be
provided to provide custom component lookup. Otherwise, call the
interface, as in::

  interface(object, default)

Returns an adapter that can adapt object to interface.  If a matching
adapter cannot be found, returns the default.

Context is adapted to IServiceService, and this adapter's 'Adapters'
service is used.

If the object has a __conform__ method, this method will be called
with the requested interface.  If the method returns a non-None value,
that value will be returned. Otherwise, if the object already
implements the interface, the object will be returned.

 - Ubicación: ``zope.component``

 - Firma: `queryAdapterInContext(object, interface, context,
   default=None)`

 - Ver también: `getAdapterInContext`_

Ejemplo::

  >>> from zope.component.globalregistry import BaseGlobalComponents
  >>> from zope.component import IComponentLookup
  >>> sm = BaseGlobalComponents()

  >>> class Context(object):
  ...     def __init__(self, sm):
  ...         self.sm = sm
  ...     def __conform__(self, interface):
  ...         if interface.isOrExtends(IComponentLookup):
  ...             return self.sm

  >>> context = Context(sm)

  >>> from zope.interface import Attribute
  >>> from zope.interface import Interface

  >>> class IRegistrador(Interface):
  ...     """Un registrador registrará los detalles de un objeto"""
  ...
  ...     def registrar():
  ...         """Registrar detalles de un objeto"""
  ...

  >>> from zope.interface import implements
  >>> from zope.component import adapts

  >>> class RegistradorHuespedNG(object):
  ...
  ...     implements(IRegistrar)
  ...     adapts(IHuesped)
  ...
  ...     def __init__(self, huesped):
  ...         self.huesped = huesped
  ...
  ...     def registrar(self):
  ...         huesped_id = proximo_id()
  ...         huespedes_db[huesped_id] = {
  ...         'nombre': huesped.nombre,
  ...         'lugar': huesped.lugar,
  ...         'telefono': huesped.telefono
  ...         }

  >>> class Huesped(object):
  ...
  ...     implements(IHuesped)
  ...
  ...     def __init__(self, nombre, lugar):
  ...         self.nombre = nombre
  ...         self.lugar = lugar

  >>> pepe = Huesped("Pepe", "España")
  >>> pepe_registradorhuesped = RegistradorHuespedNG(pepe)

  >>> IRegistrador.providedBy(pepe_registradorhuesped)
  True

  >>> from zope.component import getGlobalSiteManager
  >>> gsm = getGlobalSiteManager()
  >>> sm.registerAdapter(RegistradorHuespedNG,
  ...                     (IHuesped,), IRegistrador)

  >>> from zope.component import queryAdapterInContext

  >>> queryAdapterInContext(pepe, IRegistrador, sm) #doctest: +ELLIPSIS
  <RegistradorHuespedNG object at ...>


queryMultiAdapter
~~~~~~~~~~~~~~~~~

Look for a multi-adapter to an interface for objects.  Returns a
multi-adapter that can adapt objects to interface.  If a matching
adapter cannot be found, returns the default.  The name consisting of
an empty string is reserved for unnamed adapters.  The unnamed adapter
methods will often call the named adapter methods with an empty string
for a name.

 - Ubicación: ``zope.component``

 - Firma: `queryMultiAdapter(objects, interface=Interface,
   name=u'', default=None, context=None)`

 - Ver también: `getMultiAdapter`_

Ejemplo::

  >>> from zope.interface import Interface
  >>> from zope.interface import implements
  >>> from zope.component import adapts

  >>> class IAdaptadoUno(Interface):
  ...     pass

  >>> class IAdaptadoDos(Interface):
  ...     pass

  >>> class IFuncionalidad(Interface):
  ...     pass

  >>> class MiFuncionalidad(object):
  ...     implements(IFuncionalidad)
  ...     adapts(IAdaptadoUno, IAdaptadoDos)
  ...
  ...     def __init__(self, uno, dos):
  ...         self.uno = uno
  ...         self.dos = dos

  >>> from zope.component import getGlobalSiteManager
  >>> gsm = getGlobalSiteManager()

  >>> gsm.registerAdapter(MiFuncionalidad)

  >>> class Uno(object):
  ...     implements(IAdaptadoUno)

  >>> class Dos(object):
  ...     implements(IAdaptadoDos)

  >>> uno = Uno()
  >>> dos = Dos()

  >>> from zope.component import queryMultiAdapter

  >>> getMultiAdapter((uno,dos), IFuncionalidad) #doctest: +ELLIPSIS
  <MiFuncionalidad object at ...>

  >>> myfunctionality = queryMultiAdapter((uno,dos), IFuncionalidad)
  >>> mifuncionalidad.uno #doctest: +ELLIPSIS
  <Uno object at ...>
  >>> mifuncionalidad.dos #doctest: +ELLIPSIS
  <Dos object at ...>


queryUtility
~~~~~~~~~~~~

This function is used to look up a utility that provides an interface.
If one is not found, returns default.

 - Ubicación: ``zope.component``

 - Firma: `queryUtility(interface, name='', default=None)`

Ejemplo::

  >>> from zope.interface import Interface
  >>> from zope.interface import implements

  >>> class ISaludador(Interface):
  ...     def saludar(name):
  ...         "decir hola"

  >>> class Saludador(object):
  ...
  ...     implements(ISaludador)
  ...
  ...     def saludar(self, name):
  ...         return "Hola" + name

  >>> from zope.component import getGlobalSiteManager
  >>> gsm = getGlobalSiteManager()

  >>> saludar = Saludador()
  >>> gsm.registerUtility(saludar, ISaludador)

  >>> from zope.component import queryUtility

  >>> queryUtility(ISaludador).saludar('Pepe')
  'Hola Pepe'


registerAdapter
~~~~~~~~~~~~~~~

This function is used to register an adapter factory.

 - Ubicación: ``zope.component - IComponentRegistry``

 - Firma: `registerAdapter(factory, required=None, provided=None,
   name=u'', info=u'')`

 - Ver también: `unregisterAdapter`_

Ejemplo::

  >>> from zope.interface import Attribute
  >>> from zope.interface import Interface

  >>> class IRegistrador(Interface):
  ...     """Un registrador registrará los detalles de un objeto"""
  ...
  ...     def registrar():
  ...         """Registrar detalles de un objeto"""
  ...

  >>> from zope.interface import implements
  >>> from zope.component import adapts

  >>> class RegistradorHuespedNG(object):
  ...
  ...     implements(IRegistrar)
  ...     adapts(IHuesped)
  ...
  ...     def __init__(self, huesped):
  ...         self.huesped = huesped
  ...
  ...     def registrar(self):
  ...         huesped_id = proximo_id()
  ...         huespedes_db[huesped_id] = {
  ...         'nombre': huesped.nombre,
  ...         'lugar': huesped.lugar,
  ...         'telefono': huesped.telefono
  ...         }

  >>> class Huesped(object):
  ...
  ...     implements(IHuesped)
  ...
  ...     def __init__(self, nombre, lugar):
  ...         self.nombre = nombre
  ...         self.lugar = lugar

  >>> pepe = Huesped("Pepe", "España")
  >>> pepe_registradorhuesped = RegistradorHuespedNG(pepe)

  >>> IRegistrador.providedBy(pepe_registradorhuesped)
  True

  >>> from zope.component import getGlobalSiteManager
  >>> gsm = getGlobalSiteManager()
  >>> gsm.registerAdapter(RegistradorHuespedNG,
  ...                     (IHuesped,), IRegistrador, 'ng')

  Usted puede probar con esto: ::

  >>> queryAdapter(pepe, IRegistrador, 'ng') #doctest: +ELLIPSIS
  <RegistradorHuespedNG object at ...>


registeredAdapters
~~~~~~~~~~~~~~~~~~

Return an iterable of `IAdapterRegistrations`.  These registrations
describe the current adapter registrations in the object.

 - Ubicación: ``zope.component - IComponentRegistry``

 - Firma: `registeredAdapters()`

Ejemplo::

  >>> from zope.interface import Attribute
  >>> from zope.interface import Interface

  >>> class IRegistrador(Interface):
  ...     """Un registrador registrará los detalles de un objeto"""
  ...
  ...     def registrar():
  ...         """Registrar detalles de un objeto"""
  ...

  >>> from zope.interface import implements
  >>> from zope.component import adapts

  >>> class RegistradorHuespedNG(object):
  ...
  ...     implements(IRegistrar)
  ...     adapts(IHuesped)
  ...
  ...     def __init__(self, huesped):
  ...         self.huesped = huesped
  ...
  ...     def registrar(self):
  ...         huesped_id = proximo_id()
  ...         huespedes_db[huesped_id] = {
  ...         'nombre': huesped.nombre,
  ...         'lugar': huesped.lugar,
  ...         'telefono': huesped.telefono
  ...         }

  >>> class Huesped(object):
  ...
  ...     implements(IHuesped)
  ...
  ...     def __init__(self, nombre, lugar):
  ...         self.nombre = nombre
  ...         self.lugar = lugar

  >>> pepe = Huesped("Pepe", "España")
  >>> pepe_registradorhuesped = RegistradorHuespedNG(pepe)

  >>> IRegistrador.providedBy(pepe_registradorhuesped)
  True

  >>> from zope.component import getGlobalSiteManager
  >>> gsm = getGlobalSiteManager()
  >>> gsm.registerAdapter(RegistradorHuespedNG,
  ...                     (IHuesped,), IRegistrador, 'ng2')


  >>> reg_adapter = list(gsm.registeredAdapters())
  >>> 'ng2' in [x.name for x in reg_adapter]
  True


registeredHandlers
~~~~~~~~~~~~~~~~~~

Return an iterable of `IHandlerRegistrations`.  These registrations
describe the current handler registrations in the object.

 - Ubicación: ``zope.component - IComponentRegistry``

 - Firma: `registeredHandlers()`

Ejemplo::

  >>> import datetime

  >>> def documentoCreado(event):
  ...     event.doc.created = datetime.datetime.utcnow()

  >>> from zope.interface import Interface
  >>> from zope.interface import Attribute
  >>> from zope.interface import implements

  >>> class IDocumentoCreado(Interface):
  ...     doc = Attribute("El documento que fue creado")

  >>> class DocumentoCreado(object):
  ...     implements(IDocumentoCreado)
  ...
  ...     def __init__(self, doc):
  ...         self.doc = doc


  >>> def documentoCreado(event):
  ...     event.doc.created = datetime.datetime.utcnow()

  >>> from zope.component import adapter

  >>> @adapter(IDocumentoCreado)
  ... def documentoCreado(event):
  ...     event.doc.created = datetime.datetime.utcnow()


  >>> from zope.component import getGlobalSiteManager
  >>> gsm = getGlobalSiteManager()

  >>> gsm.registerHandler(documentoCreado, info='ng3')

  >>> reg_adapter = list(gsm.registeredHandlers())
  >>> 'ng3' in [x.info for x in reg_adapter]
  True

  >>> gsm.registerHandler(documentoCreado, name='ng4')
  Traceback (most recent call last):
  ...
  TypeError: Named handlers are not yet supported


registeredSubscriptionAdapters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Return an iterable of `ISubscriptionAdapterRegistrations`.  These
registrations describe the current subscription adapter registrations
in the object.

 - Ubicación: ``zope.component - IComponentRegistry``

 - Firma: `registeredSubscriptionAdapters()`

Ejemplo::

  >>> from zope.interface import Interface
  >>> from zope.interface import Attribute
  >>> from zope.interface import implements

  >>> class IValidar(Interface):
  ...     def validar(ob):
  ...         """Determine whether the object is valid
  ...
  ...         Return a string describing a validation problem.
  ...         An empty string is returned to indicate that the
  ...         object is valid.
  ...         """

  >>> class IDocumento(Interface):
  ...     resumen = Attribute("Resumen del Documento")
  ...     cuerpo = Attribute("Texto del Documento")

  >>> class Documento(object):
  ...     implements(IDocumento)
  ...     def __init__(self, resumen, cuerpo):
  ...         self.resumen, self.cuerpo = resumen, cuerpo

  >>> from zope.component import adapts

  >>> class LongitudAdecuada(object):
  ...
  ...     adapts(IDocumento)
  ...     implements(IValidar)
  ...
  ...     def __init__(self, doc):
  ...         self.doc = doc
  ...
  ...     def validar(self):
  ...         if len(self.doc.cuerpo) < 1000:
  ...             return 'too short'
  ...         else:
  ...             return ''

  >>> from zope.component import getGlobalSiteManager
  >>> gsm = getGlobalSiteManager()

  >>> gsm.registerSubscriptionAdapter(LongitudAdecuada, info='ng4')

  >>> reg_adapter = list(gsm.registeredSubscriptionAdapters())
  >>> 'ng4' in [x.info for x in reg_adapter]
  True


registeredUtilities
~~~~~~~~~~~~~~~~~~~

This function return an iterable of `IUtilityRegistrations`.  These
registrations describe the current utility registrations in the
object.

 - Ubicación: ``zope.component - IComponentRegistry``

 - Firma: `registeredUtilities()`

Ejemplo::

  >>> from zope.interface import Interface
  >>> from zope.interface import implements

  >>> class ISaludador(Interface):
  ...     def saludar(name):
  ...         "decir hola"

  >>> class Saludador(object):
  ...
  ...     implements(ISaludador)
  ...
  ...     def saludar(self, name):
  ...         print "Hola", name

  >>> from zope.component import getGlobalSiteManager
  >>> gsm = getGlobalSiteManager()

  >>> saludar = Saludador()
  >>> gsm.registerUtility(saludar, info='ng5')

  >>> reg_adapter = list(gsm.registeredUtilities())
  >>> 'ng5' in [x.info for x in reg_adapter]
  True


registerHandler
~~~~~~~~~~~~~~~

This function is used to register a handler.  A handler is a
subscriber that doesn't compute an adapter but performs some function
when called.

 - Ubicación: ``zope.component - IComponentRegistry``

 - Firma: `registerHandler(handler, required=None, name=u'', info='')`

 - Ver también: `unregisterHandler`_

Note: In the current implementation of ``zope.component`` doesn't
support `name` attribute.

Ejemplo::

  >>> import datetime

  >>> def documentoCreado(event):
  ...     event.doc.created = datetime.datetime.utcnow()

  >>> from zope.interface import Interface
  >>> from zope.interface import Attribute
  >>> from zope.interface import implements

  >>> class IDocumentoCreado(Interface):
  ...     doc = Attribute("El documento que fue creado")

  >>> class DocumentoCreado(object):
  ...     implements(IDocumentoCreado)
  ...
  ...     def __init__(self, doc):
  ...         self.doc = doc


  >>> def documentoCreado(event):
  ...     event.doc.created = datetime.datetime.utcnow()

  >>> from zope.component import adapter

  >>> @adapter(IDocumentoCreado)
  ... def documentoCreado(event):
  ...     event.doc.created = datetime.datetime.utcnow()


  >>> from zope.component import getGlobalSiteManager
  >>> gsm = getGlobalSiteManager()

  >>> gsm.registerHandler(documentoCreado)

  >>> from zope.component import handle

  >>> handle(DocumentCreated(doc))
  >>> doc.created.__class__.__name__
  'datetime'


registerSubscriptionAdapter
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This function is used to register a subscriber factory.

 - Ubicación: ``zope.component - IComponentRegistry``

 - Firma: `registerSubscriptionAdapter(factory, required=None,
   provides=None, name=u'', info='')`

 - Ver también: `unregisterSubscriptionAdapter`_

Ejemplo::

  >>> from zope.interface import Interface
  >>> from zope.interface import Attribute
  >>> from zope.interface import implements

  >>> class IValidar(Interface):
  ...     def validar(ob):
  ...         """Determine whether the object is valid
  ...
  ...         Return a string describing a validation problem.
  ...         An empty string is returned to indicate that the
  ...         object is valid.
  ...         """

  >>> class IDocumento(Interface):
  ...     resumen = Attribute("Resumen del Documento")
  ...     cuerpo = Attribute("Texto del Documento")

  >>> class Documento(object):
  ...     implements(IDocumento)
  ...     def __init__(self, resumen, cuerpo):
  ...         self.resumen, self.cuerpo = resumen, cuerpo

  >>> from zope.component import adapts

  >>> class LongitudAdecuada(object):
  ...
  ...     adapts(IDocumento)
  ...     implements(IValidar)
  ...
  ...     def __init__(self, doc):
  ...         self.doc = doc
  ...
  ...     def validar(self):
  ...         if len(self.doc.cuerpo) < 1000:
  ...             return 'too short'
  ...         else:
  ...             return ''

  >>> from zope.component import getGlobalSiteManager
  >>> gsm = getGlobalSiteManager()

  >>> gsm.registerSubscriptionAdapter(LongitudAdecuada)


registerUtility
~~~~~~~~~~~~~~~

This function is used to register a utility.

 - Ubicación: ``zope.component - IComponentRegistry``

 - Signature: `registerUtility(component, provided=None, name=u'',
   info=u'')`

 - Ver también: `unregisterUtility`_

Ejemplo::

  >>> from zope.interface import Interface
  >>> from zope.interface import implements

  >>> class ISaludador(Interface):
  ...     def saludar(name):
  ...         "decir hola"

  >>> class Saludador(object):
  ...
  ...     implements(ISaludador)
  ...
  ...     def saludar(self, name):
  ...         print "Hola", name

  >>> from zope.component import getGlobalSiteManager
  >>> gsm = getGlobalSiteManager()

  >>> saludar = Saludador()
  >>> gsm.registerUtility(saludar)


subscribers
~~~~~~~~~~~

This function is used to get subscribers.  Subscribers are returned
that provide the provided interface and that depend on and are
computed from the sequence of required objects.

 - Ubicación: ``zope.component - IComponentRegistry``

 - Firma: `subscribers(required, provided, context=None)`

Ejemplo::

  >>> from zope.interface import Interface
  >>> from zope.interface import Attribute
  >>> from zope.interface import implements

  >>> class IValidar(Interface):
  ...     def validar(ob):
  ...         """Determine whether the object is valid
  ...
  ...         Return a string describing a validation problem.
  ...         An empty string is returned to indicate that the
  ...         object is valid.
  ...         """

  >>> class IDocumento(Interface):
  ...     resumen = Attribute("Resumen del Documento")
  ...     cuerpo = Attribute("Texto del Documento")

  >>> class Documento(object):
  ...     implements(IDocumento)
  ...     def __init__(self, resumen, cuerpo):
  ...         self.resumen, self.cuerpo = resumen, cuerpo

  >>> from zope.component import adapts

  >>> class ResumenLineaSimple:
  ...     adapts(IDocumento)
  ...     implements(IValidar)
  ...
  ...     def __init__(self, doc):
  ...         self.doc = doc
  ...
  ...     def validar(self):
  ...         if '\n' in self.doc.resumen:
  ...             return 'Summary should only have one line'
  ...         else:
  ...             return ''

  >>> class LongitudAdecuada(object):
  ...     adapts(IDocumento)
  ...     implements(IValidar)
  ...
  ...     def __init__(self, doc):
  ...         self.doc = doc
  ...
  ...     def validar(self):
  ...         if len(self.doc.cuerpo) < 1000:
  ...             return 'too short'
  ...         else:
  ...             return ''

  >>> from zope.component import getGlobalSiteManager
  >>> gsm = getGlobalSiteManager()

  >>> gsm.registerSubscriptionAdapter(ResumenLineaSimple)
  >>> gsm.registerSubscriptionAdapter(LongitudAdecuada)

  >>> from zope.component import subscribers

  >>> doc = Document("A\nDocument", "blah")
  >>> [adapter.validate()
  ...  for adapter in subscribers([doc], IValidar)
  ...  if adapter.validate()]
  ['Summary should only have one line', 'too short']

  >>> doc = Document("A\nDocument", "blah" * 1000)
  >>> [adapter.validate()
  ...  for adapter in subscribers([doc], IValidar)
  ...  if adapter.validate()]
  ['Summary should only have one line']

  >>> doc = Document("A Document", "blah")
  >>> [adapter.validate()
  ...  for adapter in subscribers([doc], IValidar)
  ...  if adapter.validate()]
  ['too short']


unregisterAdapter
~~~~~~~~~~~~~~~~~

This function is used to unregister an adapter factory.  A boolean is
returned indicating whether the registry was changed.  If the given
component is None and there is no component registered, or if the
given component is not None and is not registered, then the function
returns False, otherwise it returns True.

 - Ubicación: ``zope.component - IComponentRegistry``

 - Firma: `unregisterAdapter(factory=None, required=None,
   provided=None, name=u'')`

 - Ver también: `registerAdapter`_

Ejemplo::

  >>> from zope.interface import Attribute
  >>> from zope.interface import Interface

  >>> class IRegistrador(Interface):
  ...     """Un registrador registrará los detalles de un objeto"""
  ...
  ...     def registrar():
  ...         """Registrar detalles de un objeto"""
  ...

  >>> from zope.interface import implements
  >>> from zope.component import adapts

  >>> class RegistradorHuespedNG(object):
  ...
  ...     implements(IRegistrar)
  ...     adapts(IHuesped)
  ...
  ...     def __init__(self, huesped):
  ...         self.huesped = huesped
  ...
  ...     def registrar(self):
  ...         huesped_id = proximo_id()
  ...         huespedes_db[huesped_id] = {
  ...         'nombre': huesped.nombre,
  ...         'lugar': huesped.lugar,
  ...         'telefono': huesped.telefono
  ...         }

  >>> class Huesped(object):
  ...
  ...     implements(IHuesped)
  ...
  ...     def __init__(self, nombre, lugar):
  ...         self.nombre = nombre
  ...         self.lugar = lugar

  >>> pepe = Huesped("Pepe", "España")
  >>> pepe_registradorhuesped = RegistradorHuespedNG(pepe)

  >>> IRegistrador.providedBy(pepe_registradorhuesped)
  True

  >>> from zope.component import getGlobalSiteManager
  >>> gsm = getGlobalSiteManager()
  >>> gsm.registerAdapter(RegistradorHuespedNG,
  ...                     (IHuesped,), IRegistrador, 'ng6')

  Usted puede probar con esto: ::

  >>> queryAdapter(pepe, IRegistrador, 'ng6') #doctest: +ELLIPSIS
  <RegistradorHuespedNG object at ...>

  Now unregister:

  >>> gsm.unregisterAdapter(RegistradorHuespedNG, name='ng6')
  True

  After unregistration:

  >>> print queryAdapter(pepe, IRegistrador, 'ng6')
  None


unregisterHandler
~~~~~~~~~~~~~~~~~

This function is used for unregistering a handler.  A handler is a
subscriber that doesn't compute an adapter but performs some function
when called.  A boolean is returned indicating whether the registry
was changed.

 - Ubicación: ``zope.component - IComponentRegistry``

 - Firma: `unregisterHandler(handler=None, required=None,
   name=u'')`

 - Ver también: `registerHandler`_

Ejemplo::

  >>> from zope.interface import Interface
  >>> from zope.interface import Attribute
  >>> from zope.interface import implements

  >>> class IDocumento(Interface):
  ...
  ...     resumen = Attribute("Resumen del Documento")
  ...     cuerpo = Attribute("Texto del Documento")

  >>> class Documento(object):
  ...
  ...     implements(IDocumento)
  ...     def __init__(self, resumen, cuerpo):
  ...         self.resumen, self.cuerpo = resumen, cuerpo

  >>> doc = Document("A\nDocument", "blah")

  >>> class IDocumentoConsultado(Interface):
  ...     doc = Attribute("The document that was accessed")

  >>> class DocumentoConsultado(object):
  ...     implements(IDocumentoConsultado)
  ...
  ...     def __init__(self, doc):
  ...         self.doc = doc
  ...         self.doc.count = 0

  >>> from zope.component import adapter

  >>> @adapter(IDocumentAccessed)
  ... def documentAccessed(event):
  ...     event.doc.count = event.doc.count + 1

  >>> from zope.component import getGlobalSiteManager
  >>> gsm = getGlobalSiteManager()

  >>> gsm.registerHandler(documentAccessed)

  >>> from zope.component import handle

  >>> handle(DocumentAccessed(doc))
  >>> doc.count
  1

  Now unregister:

  >>> gsm.unregisterHandler(documentAccessed)
  True

  After unregistration:

  >>> handle(DocumentAccessed(doc))
  >>> doc.count
  0


unregisterSubscriptionAdapter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This function is used to unregister a subscriber factory.  A boolean
is returned indicating whether the registry was changed.  If the given
component is None and there is no component registered, or if the
given component is not None and is not registered, then the function
returns False, otherwise it returns True.

 - Ubicación: ``zope.component - IComponentRegistry``

 - Firma: `unregisterSubscriptionAdapter(factory=None,
   required=None, provides=None, name=u'')`

 - Ver también: `registerSubscriptionAdapter`_

Ejemplo::

  >>> from zope.interface import Interface
  >>> from zope.interface import Attribute
  >>> from zope.interface import implements

  >>> class IValidar(Interface):
  ...     def validar(ob):
  ...         """Determine whether the object is valid
  ...
  ...         Return a string describing a validation problem.
  ...         An empty string is returned to indicate that the
  ...         object is valid.
  ...         """

  >>> class IDocumento(Interface):
  ...     resumen = Attribute("Resumen del Documento")
  ...     cuerpo = Attribute("Texto del Documento")

  >>> class Documento(object):
  ...     implements(IDocumento)
  ...     def __init__(self, resumen, cuerpo):
  ...         self.resumen, self.cuerpo = resumen, cuerpo

  >>> from zope.component import adapts

  >>> class LongitudAdecuada(object):
  ...
  ...     adapts(IDocumento)
  ...     implements(IValidar)
  ...
  ...     def __init__(self, doc):
  ...         self.doc = doc
  ...
  ...     def validar(self):
  ...         if len(self.doc.cuerpo) < 1000:
  ...             return 'too short'
  ...         else:
  ...             return ''

  >>> from zope.component import getGlobalSiteManager
  >>> gsm = getGlobalSiteManager()

  >>> gsm.registerSubscriptionAdapter(LongitudAdecuada)

  >>> from zope.component import subscribers

  >>> doc = Document("A\nDocument", "blah")
  >>> [adapter.validate()
  ...  for adapter in subscribers([doc], IValidar)
  ...  if adapter.validate()]
  ['too short']

  Now unregister:

  >>> gsm.unregisterSubscriptionAdapter(LongitudAdecuada)
  True

  After unregistration:

  >>> [adapter.validate()
  ...  for adapter in subscribers([doc], IValidar)
  ...  if adapter.validate()]
  []


unregisterUtility
~~~~~~~~~~~~~~~~~

This function is used for unregistering a utility.  A boolean is
returned indicating whether the registry was changed.  If the
given component is None and there is no component registered, or if
the given component is not None and is not registered, then the
function returns False, otherwise it returns True.

 - Ubicación: ``zope.component - IComponentRegistry``

 - Firma: `unregisterUtility(component=None, provided=None,
   name=u'')`

 - Ver también: `registerUtility`_

Ejemplo::

  >>> from zope.interface import Interface
  >>> from zope.interface import implements

  >>> class ISaludador(Interface):
  ...     def saludar(name):
  ...         "decir hola"

  >>> class Saludador(object):
  ...
  ...     implements(ISaludador)
  ...
  ...     def saludar(self, name):
  ...         return "Hola" + name

  >>> from zope.component import getGlobalSiteManager
  >>> gsm = getGlobalSiteManager()

  >>> saludar = Saludador()
  >>> gsm.registerUtility(saludar)

  >>> queryUtility(ISaludador).saludar('Pepe')
  'Hola Pepe'

  Now unregister:

  >>> gsm.unregisterUtility(greet)
  True

  After unregistration:

  >>> print queryUtility(ISaludador)
  None
