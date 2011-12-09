.. -*- coding: utf-8 -*-

================
Pruebas en Plone
================

En este tutorial se explica cómo escribir código mejor y más seguro para
darle un aspecto más profesional. Así es, es hora de escribir pruebas, para
todo lo que haga. No se preocupe, no es aburrido ni complicado, sólo tiene
que aprender cómo.

.. contents :: :local:


Introducción
============

¿Qué eso llamado pruebas?

"Yo se que tengo que escribir pruebas. pero...

-   ...estas toman tiempo en escribirse
-   ... soy un buen desarrollador
-   ... mi cliente/la comunidad hace las pruebas"

¿Le suena familiar? No importa lo bueno que usted cree que es, siempre
cometerá errores. Su código tendrá errores y alguien va a venir después a
exigirle una explicación. Sin alguna forma metódica de pruebas, usted estará
garantizando su código con nada más que conjeturas y arrogancia. Pasear un
poco por la interfaz de Plone durante algunos minutos antes de enviar el
código al cliente o usuario simplemente no es suficiente.

Hacer pruebas es un arte, tiene que estar integrado en su ciclo de desarrollo
desde el principio. No es algo que se hace sólo después de que haya hecho
todo el trabajo, es algo que tiene que hacer de forma continua.
Desgraciadamente hacer pruebas a menudo evoca emociones de temor en los
desarrolladores. Es lento, es aburrido, no es lo que acordaron hacer. Pero el
arte de hacer pruebas ha evolucionado más allá de eso. Existe una
considerable elegancia y diversión en el ambiente de buenas estrategias
planteadas para hacer pruebas.

Este tutorial apunta a darle las herramientas necesarias para escribir
pruebas y software comprobable en Plone. Si está escribiendo software para el
núcleo (core) de Plone como tal, ni siquiera piense en cometer cualquier
corrección de error o característica sin cobertura de pruebas. Si usted está
escribiendo un producto complementario o alguna personalización; manteniendo
los mismos altos estándares que el equipo core de Plone le dará una mejor
confianza en su software y probablemente le ahorrará dolor considerable a lo
largo del camino.


Ejemplos
--------

Este tutorial contiene varios ejemplos de los distintos tipos de pruebas.
Estas están disponibles en el paquete `example.tests`_, el cual puede
instalar como un huevo de desarrollo en su buildout de Plone 3. Los ejemplos
de pruebas de funcionamiento utilizan los comandos estándar para buildouts,
ya que esta es la única forma que funcione de forma fiable en Windows (es
decir zopectl test no funcionará en Windows).

Revise el `tutorial de buildout`_ para más información.


Un breve ejemplo
================

Sólo para que obtenga una idea de lo que estamos hablando.

Trate de encontrar el error en el siguiente fragmente de código:

.. code-block:: python

  class Employee(object):
      def __init__(self, name, position, employee_no=None):
          self.name = name
          self.position = position
          self.employee_no = employee_no

  salaries = {0: 12000,
              1: 4000,
              2: 8000,
              3: 4000}

  def print_salary(employee):
      if employee.employee_no:
         salary = salaries.get(employee.employee_no, 0)
         print "You make EUR %s." % salary
      else:
         print "You're not an employee currently."


¿Ya lo encontró? ¿tuvo que pasar más de unos segundos pensando en el error?
Cualquier desarrollador podría haber escrito ese código y no haber visto el
problema. Además, el error es un caso extremo que pudo no haber probado al
hacer pruebas manual/a-través-de-la-Web.

Escribamos una prueba (realmente una prueba doc/unit) para este código: No se
preocupe demasiado acerca de cómo esto está configurado y ejecutado por el
momento.

.. code-block:: python

  Employee w/o an employee number is ignored:

    >>> print_salary(Employee('Adam', 'Developer'))
    You\'re not an employee currently

  Employee w/o a known employee number earns nothing:

    >>> print_salary(Employee('Berta', 'Designer', 100))
    You make EUR 0.

  Employee w/ a valid employee number is found properly:

    >>> print_salary(Employee('Chris', 'CTO', 2))
    You make EUR 8000.

  Zero is a valid employee number:

    >>> print_salary(Employee('Devon', 'CEO', 0))
    You make EUR 12000


Durante el proceso, la última prueba fallará. Mostrará **You are not an
employee currently**. (Actualmente usted no es un empleado), a menos que
arreglemos el código:

.. code-block:: python

  class Employee(object):
      def __init__(self, name, position, employee_no=None):
          self.name = name
          self.position = position
          self.employee_no = employee_no

  salaries = {0: 12000,
              1: 4000,
              2: 8000,
              3: 4000}

  def print_salary(employee):
      if employee.employee_no is not None:
          salary = salaries.get(employee.employee_no, 0)
          print "You make EUR %s." % salary
      else:
          print "You're not an employee currently."


¿Cuál es la moraleja de la historia?

-   raramente se da cuenta de errores como este haciendo pruebas
    manualmente
-   pase el tiempo, que gasta en capturar errores tontos y errores de
    escritura, mejor escribiendo pruebas
-   con una decente cobertura de pruebas, usted termina ahorrándose
    grandes cantidades de tiempo cuando refactoriza


Tipos de pruebas
================
Un poco de terminología con la cual debería estar familiarizado

En términos generales, hay cuatro tipos principales de pruebas:

.. glossary::

  Pruebas unitarias
    Estas son escritas desde la perspectiva del programador. Una
    prueba unitaria debe probar un sólo método o función en aislamiento, para
    asegurar que funciona correctamente. Por ejemplo, probar que un cálculo
    determinado se realiza correctamente dado una variedad de entrada es una
    buena prueba unitaria para ese método.

  Pruebas de integración
    Mientras que las pruebas unitarias tratan de eliminar o abstraer 
    tantas dependencias como sea posible para asegurarse de que 
    realmente sólo se preocupen por el método a probar, las pruebas 
    de integración ejercitan los puntos de integración entre un método 
    o componente y los demás componentes en los que este se basa. Por
    ejemplo, probar que un método realiza un cálculo y luego almacena
    correctamente el resultado en la ZODB (Base de datos de objetos Zope) 
    es una prueba de integración, ya que prueba la integración entre el 
    componente y la ZODB.

  Pruebas funcionales
    Una prueba funcional suele demostrar un caso de uso, realizando una 
    "vertical" de la funcionalidad. Por ejemplo, probar que luego del llenado 
    de un formulario y hacer clic en "Guardar" haga que el objeto resultante 
    está disponible para su uso futuro, es una prueba funcional para
    el caso de uso de la utilización de ese formulario para crear objetos 
    de contenido.

  Pruebas de sistema
    Estas son escritas desde la perspectiva del usuario, y tratan el sistema
    como una caja negra. Una prueba de sistema puede probar el caso de un usuario 
    interactuando con el sistema de acuerdo con los patrones de uso esperados. 
    Por su naturaleza, generalmente son menos sistemáticas que los otros 
    tipos de pruebas.

Adicionalmente, las pruebas funcionales pueden ser **caja blanca**, en cuyo
caso pueden hacer afirmaciones sobre cosas como el almacenamiento de datos
subyacentes (pero sólo si se especifica claramente; los detalles de
implementación no deben afectar a las pruebas de funcionales). Estas pruebas
también se denominan **pruebas de integración funcional** (puede ver que los
limites comienzan a borrarse, pero no se preocupe demasiado por los nombres).
Alternativamente, las pruebas funcionales pueden ser **caja negra**, en cuyo
caso solo perciben el sistema desde el punto de vista de un actor (usualmente
el usuario final) y hace afirmaciones basadas sólo en lo que es presentado en
la interfaz de usuario para ese actor. Estas pruebas denominadas también
**pruebas de aceptación** no harán suposiciones sobre la arquitectura
subyacente en absoluto.


Pruebas y documentación
-----------------------

En un mensaje a la lista de correos Zope 3, Jim Fulton explica la importancia
de las pruebas y documentación, y la forma en que van mano a mano:

   Una cosa importante acerca de esto es que la mayoría de doctests
   debería escribirse como documentación. Cuando escribe nuevos
   componentes
   de software y necesita escribir pruebas para funcionalidad principal
   de su software usted necesita:

   - Ponga su mente en modo para escribir documentación
     Esto es extremadamente importante.

   - Usted necesita documentar cómo usar el software. Incluir ejemplos,
     which are tests


Más tarde aprenderemos más sobre doctests y como se usan para pruebas
unitarias y funcionamiento. Lo importante a destacar es que las buenas
pruebas a menudo sirven como documentación describiendo cómo su componente se
supone es utilizado. Pensar en la historia que cuentan es tan importante como
pensar en el número de estados de entrada y salida que cubren.


Contando historias con doctests
===============================

Los Doctests ponen el código y prueba junto, y hace más fácil describir que
hace una prueba, y por qué.

Por su naturaleza, la pruebas deberían ejercitar un API (Interfaz de
programación de aplicaciones) y demostrar cómo se usa. Por lo tanto, para
otros desarrolladores tratando de entender cómo un módulo o biblioteca
debería ser utilizado, las pruebas pueden ser la mejor forma de
documentación. Python soporta la noción de **doctests**, también conocida
como **documentación ejecutable**.

Los Doctests se asemejan a sesiones de Python interpreter. Ellos contienen
texto plano (normalmente en reStructedText, el cual puede ser renderizado a
HTML o PDF fácilmente) así como **ejemplos**. La idea es mostrar algo que
podría haber sido escrito en una sesión interpreter (de intérprete) y lo que
el resultado esperado debería ser. En el mundo de Zope 3, los doctests son
muy frecuentes y se utilizan para la mayoría de pruebas unitarias e de
integración.

Los doctests vienen principalmente en dos sabores: puede escribir un simple
archivo como ``README.txt``, explicando su código junto a ejemplos verificables,
o puede agregar doctests para un método o clase determinado dentro de la
docstring (cadena de documentación) de ese método o clase.

El enfoque de archivo-completo, también conocido como **desarrollo dirigido
por documentación (documentation-driven development)** es el más común. Este
tipo de prueba es muy apropiado para explicar cómo una API se debe utilizar y
al mismo tiempo asegurar que funciona como se espera. Sin embargo, note que
estas técnicamente no son pruebas unitarias como tal, porque no hay ninguna
garantía de aislamiento entre los steps del "script" que doctest describa. La
versión de cadena de documentación utiliza la misma sintaxis básica, pero
cada una se ejecuta como su propia prueba fixture, garantizando el
aislamiento total entre las pruebas.

Aquí hay un ejemplo trivial de un doctest. Aprenderemos cómo configurar tal
prueba en breve. 

.. code-block:: python

    Las interfaces se definen mediante sentencias de clases Python::

      >>> import zope.interface
      >>> class IFoo(zope.interface.Interface):
      ...    """Foo blah blah"""
      ...
      ...    x = zope.interface.Attribute("""X blah blah""")
      ...
      ...    def bar(q, r=None):
      ...        """bar blah blah"""

    En el ejemplo anterior, hemos creado una interfaz::

      >>> type(IFoo)
      <class 'zope.interface.interface.InterfaceClass'>

    Podemos pedir la documentación de la interfaz::

      >>> IFoo.__doc__
      'Foo blah blah'

    Se podría crear un objeto arbitrario; por supuesto esto no
    proporcionará la interfaz.

      >>> o = object()
      >>> o # doctest: +ELLIPSIS
      <object at ....>
      >>> IFoo.providedBy(o)
      False
      >>> o.bar() # doctest: +ELLIPSIS
      Traceback (most recent call last):
      ...
      AttributeError: 'object' object has no attribute 'bar'



Cada vez que el runner de doctest se ejecuta y encuentra un línea que
comienza con **>>>**, el indicador (línea de comandos) del Python interpreter
(esto es, lo que obtiene al ejecutar ``python`` sin argumentos en una terminal),
ejecutará entonces esa línea de código. Si esa sentencia es inmediatamente
seguida por una línea con el mismo nivel de sangría que **>>>** que no es una
línea en blanco y no comienza con **>>>**, esto se toma como el resultado
esperado de la sentencia. El runner de prueba comparará la salida que obtuvo
mediante la ejecución de la sentencia de Python con la salida especificada en
el doctest, e identificará un error si no coinciden.

Note que *no* escribir un valor de salida es equivalente a afirmar que el
método no posee salida. Por lo tanto, se trata de una falla:

.. code-block:: python

      >>> foo = 'hello'
      >>> foo
      >>> # do something else


La referencia a **foo** por sí misma imprimirá el valor de foo. El doctest
correcto será el siguiente:

.. code-block:: python

      >>> foo = 'hello'
      >>> foo
      'hello'
      >>> # do something else


Note también el elemento **...** (puntos suspensivos) en la salida esperada.
Estos significan "cualquier número de caracteres" (análogo a una sentencia **.***
en una expresión regular, si usted está familiarizado con ellas). Usualmente
es taquigrafía convenida, pero en ocasiones es necesaria. Por ejemplo:

.. code-block:: python

      >>> class Foo:
      ...     pass
      >>> Foo()
      <__main__.Foo instance at ...>


Aquí los **...** en la salida esperada remplaza una dirección de memoria
hexadecimal (**0x0x4523a0** en la computadora del autor al momento de escribir),
lo cual no se puede predecir de antemano. Cuando se escriben doctests en
particular (pero también cuando se escriben pruebas unitarias regulares),
usted necesita tener cuidado con los valores no puede predecir, como las
identificaciones auto-generadas basadas en la hora actual o un número al
azar. El operador ellipsis (de puntos suspensivos) le puede ayudar a trabajar
con esos.

No confunda el operador ellipsis en la salida esperada con la sintaxis de
usar **...** debajo de una línea **>>>**. Esta es la sintaxis estándar de Python
interpreter usada para designar sentencias que se ejecuten sobre líneas
múltiples, normalmente como el resultado de sangría. Usted puede por ejemplo
escribir:

.. code-block:: python

      >>> if a == b:
      ...     foo = bar


Si es necesario en su prueba.


Consejos y trucos para doctest
------------------------------

Así como lo es para el tema de pruebas, igualmente mejorará en el asunto de
doctests con la practica. A continuación se presentan algunos consejos que
pueden ayudarle a empezar.

.. glossary::

  Lea la documentación 
    los doctests han estado en Python desde hace mucho tiempo. 
    El `modulo de doctest`_ viene con más documentación sobre cómo funcionan. 

  ¿una prueba es sólo un montón de sentencias Python?
    Nunca olvide eso. Usted puede, por ejemplo, hacer referencia a métodos 
    de ayuda (helper methods) en su propio producto, por ejemplo imagine 
    que usted tiene un método en **Products.MyProduct.tests.utils** que a su 
    vez tiene un método **setUpSite()** para llenar previamente su sitio con 
    unos cuantos directorios y usuarios. Su doctest podría contener:

    .. code-block:: python

      >>> from Products.MyProduct.tests.utils import setUpSite
      >>> setUpSite()

  El conjunto de pruebas puede llevar a cabo inicialización adicional
    Un conjunto de pruebas puede tener controladores **setUp()** y/o **tearDown()**
    que realicen acciones adicionales de configuración o limpieza. Veremos
    ejemplos de esto más adelante. 

  PDB sigue siendo su amigo 
    Usted puede colocar en una línea en doctest el siguiente código Python:

    .. code-block:: python

      >>> import pdb
      >>> pdb.set_trace\(\)
    
    Lamentablemente, no se puede ir línea por línea a través de un doctest,
    pero puede imprimir variables y examinar el estado de la prueba fixture.
    Usted puede capturar las excepciones Si necesita depurar un doctest que
    está arrojando una excepción, esta sentencia es a menudo útil:

    .. code-block:: python

      >>> try:
      ...     someOperation()
      ... except:
      ...     import pdb;
      ...     pdb.set_trace\(\)
      >>> # continue as normal
