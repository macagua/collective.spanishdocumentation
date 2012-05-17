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
-   ... mi cliente/la comunidad hace las pruebas "

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
    Usted puede colocar **import pdb; pdb.set_trace()** en una línea en doctest.
    Lamentablemente, no se puede ir línea por línea a través de un doctest,
    pero puede imprimir variables y examinar el estado de la prueba fixture.
    Usted puede capturar las excepciones Si necesita depurar un doctest que
    está arrojando una excepción, esta sentencia es a menudo útil:

    .. code-block:: python

      >>> try:
      ...     someOperation()
      ... except:
      ...     import pdb; pdb.set_trace()
      >>> # continue as normal


Ejecutando pruebas
==================

No sirve de mucho escribir una prueba o confiar en las pruebas de otra
persona si no sabe cómo ejecutarlas.

La forma más fácil de ejecutar pruebas en Zope es el uso de ``zopectl`` o el
script de control equivalente.

.. code-block:: sh

  $ ./bin/zopectl test -s Products.RichDocument


Este ejecutará todas las pruebas en el módulo **Products.RichDocument**. Si usted
está usando `buildout`_ con un script de control de instancia llamado
``instance``, esto será:

.. code-block:: sh

  $ ./bin/instance test -s Products.RichDocument

Usar buildout es probablemente una buena idea (vea `el tutorial de buildout`_) para empezar porque es la única forma que funcione de forma
fiable en Windows. Usaremos esta sintaxis de ahora en adelante.

Para ejecutar una sola prueba o un conjunto de pruebas acompañada de
expresiones regulares, puede utilizar:

.. code-block:: sh

  $ ./bin/instance test -s Products.RichDocument -t setup


Esto puede ejecutar pruebas en archivos como ``test_setup.py``. Para ejecutar
todos los doctests en ``README.txt`` (asumiendo que hay un conjunto de pruebas
para este archivo) tendría que escribir:

.. code-block:: sh

  $ ./bin/instance test -s Products.RichDocument -t README.txt

El nuevo runner de pruebas también incluye algunas opciones para depuración.
Por ejemplo:

.. code-block:: sh

  $ ./bin/instance test -m Products.RichDocument -D


Esto detendrá la ejecución en la primera prueba fallida y lo situará dentro
de un PDB post-mortem.

Para ver las otras opciones que están disponibles, ejecute:

.. code-block:: sh

  $ ./bin/instance test --help


Cuando las pruebas que considere relevante pasaron, es el momento de ejecutar
todas las pruebas y asegurarse de que nada más esté dañado. (No, no nos
importa si usted está escribiendo su código en un módulo de Python totalmente
distinto que el aquel de esas otras pruebas se supone que prueben, y que
todas estaban bien, y lo único que cambié fue una docstring (cadena de
documentación). Ejecute la prueba cuando piense que este listo).

Cuando las pruebas terminen de ejecutarse, usted verá un reporte como este:

.. code-block:: sh

        ...
        Ran 18 tests in 6.463s
        
        OK


(puede lucir un poco diferente, dependiendo de cual runner de prueba está
usted utilizando)

Practique un suspiro de satisfacción para cuando lea la línea "OK", en lugar
de ver un recuento de pruebas fallidas. Con el tiempo, este será el pequeño
notificador que le permite ir a la cama, ver a sus amigos una vez más o en
general volver a la vida real con un ``svn commit``.

Si no tiene tanta suerte, puede que vea:

.. code-block:: sh

        ...
        Ran 18 tests in 7.009s
        
        FAILED (failures=1, errors=1)


(de igual manera la salida puede ser algo diferente dependiendo del runner de
prueba, pero la información será esencialmente la misma)

Esto significa que hubo 1 error y 1 prueba fallida durante la ejecución de la
prueba.

Un error de Python significa que algo de su prueba de código, o un código que
fue llamado por una prueba, arrojé una excepción. Esto no es algo bueno, y
debería arreglarlo inmediatamente.

Una prueba fallida significa que su prueba estaba tratando de afirmar algo
que resultó no ser verdadero. Esto podría estar bien. Podría significar que
no ha escrito el código que la prueba está probando (bien hecho, ¡escribió la
prueba primero!), o que no sabe todavía por qué está fallando. A veces puede
que está radicalmente refactorizando o reescribiendo partes de su código, y
las pruebas seguirán fallando hasta que haya terminado. Por cierto, esto es
parte de la razón por la cual las pruebas unitarias son tan buenos; usted
puede hacer ese tipo de cosas.

A veces es (no siempre, no intente hacer esto en el core de Plone a menos que
se le haya dicho que está bien por el administrador) aceptable ir a la cama y
reportar una prueba fallida si no está en la posición de saber cómo
solucionarla. Al menos otros desarrolladores estarán al tanto del problema y
podrían estar en la capacidad de solucionarlo.


Escribiendo una prueba unitaria
===============================

Ahora que usted entiende el principio de las pruebas y la forma de
ejecutarlas, es momento de escribir algunas. Empezaremos con simples pruebas
unitarias usando sintaxis de doctest.

Vamos a empezar por cómo crear una simple prueba unitaria con una sintaxis
doctest. No hay nada específico de Zope o Plone relacionado a esta prueba.
Este tipo de prueba es ideal para métodos y clases que realizan algún tipo de
operación bien definida en primitivas o objetos simples. La sintaxis doctest
es muy adecuada para explicar las entradas y salidas. Ya que las pruebas son
relativamente pocas y/o descriptivas, mantener las documentación, pruebas y
código juntos tiene sentido.

Las pruebas generalmente se encuentran en un sub-paquete ``tests/``. En el
paquete ``example.tests``, hemos creado un archivo llamado
``tests/test_simple_doctest.py``. Esto establece un conjunto de pruebas para
ejecutar doctests en las cadenas de documentación en el módulo
``example.tests.context``. Primero echemos un vistazo a la configuración de la
prueba:

.. code-block:: python

    """Esta es la configuración de un doctest donde los ejemplos de pruebas 
    se mantienen en docstrings en un módulo.

    En este caso, no estamos usando nada Zope-específico en absoluto. Por
    supuesto que podríamos utilizar la arquitectura de componentes de Zope 3
    en la configuración si quisiéramos. para esto,
    revise test_zope3_doctest.py.

    Sin embargo *si* usamos el paquete zope.testing, el cual proporciona
    un versión mejorada de DocTestSuite estándar de Python, DocFileSuite
    entre otros. Si usted
    no quiere esta dependencia, simplemente use doctest.DocTestSuite.
    """

    import unittest
    import zope.testing

    import example.tests.context

    def setUp(test):
        """Podemos usar esta opción para configurar todo lo que tiene
        que estar disponible para
        cada prueba. Se ejecuta para cada prueba, es decir, para
        docstring que
        contiene doctests.

        Revise la documentación de Python para pruebas unitarias y
        módulos doctest para aprender
        más sobre cómo preparar el estado y pasarlo en varias
        pruebas.
        """

    def tearDown(test):
        """Este es el compañero del setUP; se puede utilizar para 
        limpiar el entorno de prueba después de cada prueba.
        """

    def test_suite():
        return unittest.TestSuite((

            # Aquí. le decimos al runner de prueba que ejecute la prueba en tal
            # módulo. Los métodos setUP y tearDown pueden usarse para llevar a cabo
            # configuración de prueba-especifica y desmontaje.

            zope.testing.doctest.DocTestSuite(example.tests.context,
                         setUp=setUp,          # setUp y tearDown son opcionales!
                         tearDown=tearDown),
            ))


Hay un montón de comentarios aquí, y mostramos cómo usar los métodos **setUp()**
y **tearDown()** inicialización adicional y limpieza, en caso de que sea
necesario. El runner de prueba llamará el método **test_suite()** y esperará un
objeto **TestSuite** como respuesta. Si se desea, podríamos haber puesto varios
conjuntos de pruebas que se refieran a múltiples módulos dentro del **TestSuite**
que esté respondiendo.

Aquí está el código tras la prueba, en ``context.py``:

.. code-block:: python

    from zope.interface import implements
    from example.tests.interfaces import IContext

    class Context(object):
        """Un objeto usado para hacer pruebas. Vamos a registrar un
        adaptador de esta
        interfaz para IUpperCaser en la configuración de la prueba.

        Aquí está cómo usarla. Primero, importe la clase

            >>> de Contexto de importación example.tests.context

        Luego haga una instanciación (¿sigue conmigo?):

            >>> my_context = Context()

        Bueno, aquí está el truco...ahora tenemos que definir el
        título:

            >>> my_context.title = u"¡alguna cadena!"

        uf...¿funcionó eso?

            >>> my_context.title
            u'¡alguna cadena!'

        ¡Así es!
        """

        implements(IContext)

        def __init__(self, title=u""):
            self.title = title


Así es como puede ejecutar las pruebas desde un buildout:

.. code-block:: sh

    ./bin/instance test -s example.tests -t context
    Running unit tests:
      Running:
    ....
      Ran 4 tests with 0 failures and 0 errors in 0.071 seconds.



Probando un componente Zope 3 con un archivo separado doctest
=============================================================

A veces, puede ser necesario realizar configuración adicional para que
nuestras pruebas se ejecuten correctamente.

En el ejemplo previo, escribimos un doctest en un docstring. Como las pruebas
se hacen más complejos o que requieren una configuración más profunda. por lo
general es mejor separar la prueba como tal en un archivo de texto. Algunas
veces, este puede ser el archivo ``README.txt`` de un paquete. Este es el enfoque
preferido por los componentes de Zope 3.

En este ejemplo, vamos a registrar un adaptador que se utiliza en un doctest.
Este doctest también sirve para ilustrar cómo este adaptador en particular
debe ser utilizado. Este estilo de prueba es genial cuando se hace hincapié
en la documentación así como en la prueba. Tenga en cuenta que no cargamos el
paquete ZCML en su totalidad. En su lugar, registramos los componentes
necesarios de forma explícita. Esto significa que poseemos el control sobre
lo que es ejecutado en la prueba. Nosotros usamos el método
``zope.component.testing.tearDown`` para asegurarnos que nuestro entorno de
prueba esta debidamente limpio.

En el paquete ``example.tests``, tenemos la siguiente configuración de prueba en
``tests/test_zope3_doctest.py``:

.. code-block:: python

    """Esta es la configuración para un doctest que prueba un componente de Zope 3.

    Realmente no hay nada muy diferente a una prueba "plain Python".
    Nosotros no estamos analizando ZCML, por ejemplo: Sin embargo, usamos algunos de los
    helpers de Zope 3 para asegurar que la Component Architecture (Arquitectura de
    Componente) este debidamente creada y desmontada.
    """

    import unittest

    import zope.testing
    import zope.component

    def setUp(test):
        """Este método se utiliza para configurar el entorno de
        prueba. Lo pasamos al
        DocFileSuite initialiser. También pasamos un tear-down
        (desmontaje), pero en este caso,
        usamos un tear-down desde zope.component.testing, el cual se
        encarga de
        limpiar los registros de Component Architecture.
        """

        # Registre el adaptador. Vea zope.component.interfaces para más información
        from example.tests.context import UpperCaser
        zope.component.provideAdapter(UpperCaser)

    def test_suite():
        return unittest.TestSuite((

            # Aquí. le decimos al runner de prueba que ejecute la prueba en tal
            # archivo. Los métodos setUp y tearDown empleados hacen uso de Zope 3
            # Component Architecture, pero realmente no hay nada Zope-específico
            # acerca de esto. Si quiere probar "plain-Python" de esta manera,
            # la configuración es la misma.

            zope.testing.doctest.DocFileSuite('tests/zope3.txt',
                         package='example.tests',
                         setUp=setUp,
                         tearDown=zope.component.testing.tearDown),
            ))


Observe cómo se utiliza un método personalizado **setUp()** para registrar el
adaptador personalizado, y después hacer referencia a
``zope.component.testing.tearDown`` para el método de desmontaje.

Esto se refiere al archivo ``zope3.txt``, que luce como este:

.. code-block:: rst

    ===============================
    Un doctest de componente Zope 3
    ===============================

    Este es el tipo de prueba que se encuentran más comúnmente en Zope 3.
    Tenemos un método de configuración personalizado (in
    test_zope3_doctest.py) el cual registra los componentes que necesitamos
    para la prueba. A continuación podemos utilizar esos aquí. El ZCML no es
    procesado directamente,
    tampoco tenemos un entorno completo Zope 2/Plone disponible. Esto
    hace que la prueba esté
    más asilada (¡y más rápida!). A menudo, se puede optar por utilizar
    las implementaciones simuladas de ciertos componentes a fin de hacer la
    prueba correctamente aislada.

    Por supuesto, igual deberíamos contar una historia con esta
    documentación.

    Digamos que teníamos uno de nuestros objetos de contexto realmente
    emocionantes:

        >>> de Contexto de importación example.tests.context
        >>> context = Context()
        >>> context.title = u"cualquier título"

    Por supuesto eso está bien, pero y que si ¿quisiéramos hacer un poco
    más de un impacto?
    Podemos utilizar nuestro útil adaptador upper-caser!

        >>> from example.tests.interfaces import IUpperCaser
        >>> shout = IUpperCaser(context)
        >>> shout.title
        u'CUALQUIER TÍTULO'

    ¡Vaya!


Para ejecutar sólo esta prueba, podemos hacer:

.. code-block:: sh

    ./bin/instance test -s example.tests -t zope3.txt
    Running unit tests:
      Running:
    ..
      Ran 2 tests with 0 failures and 0 errors in 0.010 seconds.



Escribiendo una prueba unitaria/integración PloneTestCase
==========================================================

A veces, tenemos que tener acceso a una instancia Plone en todas sus facetas
con el fin de escribir efectivamente las pruebas

``PloneTestCase``, que a su vez utiliza ``ZopeTestCase``, se utiliza para configurar
un entorno de Zope completo, incluyendo una instancia de Plone, para hacer
pruebas. Este tipo de prueba es muy conveniente y a menudo necesario debido a
los tipos de contenido, herramientas y otras partes de Plone tienen
dependencias estrictas en distintos subyacentes Zope, CMF y componentes de
Plone. En general es mejor para escribir pruebas más sencillas, sin embargo,
tanto debido a que proporcionan un mejor aislamiento (lo que prueba el
componente más directamente y en mejores condiciones controladas) y se
ejecutan más rápidamente.

PloneTestCase-tests regularmente se refieren a "pruebas unitarias", pero en
realidad son pruebas de *integración*, ya que dependen de una instancia
"viva" de Zope y así probar la integración entre su código y el framework
subyacente. Podemos usar el setup de PloneTestCase para ejecutar doctests,
como veremos en la próxima sección.

No obstante aquí demostraremos cómo usar clases ``unittest.TestCase``, donde cada
prueba es un método en una clase (con un nombre que comienza con ``test``) Este
tipo de prueba no es muy buena documentación, pero puede ser muy útil para la
ejecución sistemática de muchas variaciones en la misma prueba. Algunos
desarrolladores también encuentran este tipo de prueba más fácil de depurar,
ya que es código normal de Python que se puede recorrer utilizando un
depurador.

En el paquete ``example.tests``, tenemos ``tests/base.py``. Este no contiene ninguna
prueba, sino que realiza la configuración necesaria para definir la prueba
fixture:

.. code-block:: python

    """Configuración de pruebas funcionales y de integración

    Cuando importamos PloneTestCase y luego llamamos setupPloneSite(),
    todos los productos de Plone son cargados, y un sitio Plone será creado.
    Esto ocurre a nivel de módulo, lo que hace que sea más rápido para 
    ejecutar cada prueba, pero ralentiza el arranque del runner de prueba.
    """

    from Products.Five import zcml
    from Products.Five import fiveconfigure

    from Testing import ZopeTestCase as ztc

    from Products.PloneTestCase import PloneTestCase as ptc
    from Products.PloneTestCase.layer import onsetup

    #
    # Cuando ZopeTestCase configura Zope, este *no* auto-cargará productos en
    # Products/. En su lugar, tenemos que usar una sentencia como:
    #
    #   ztc.installProduct('SimpleAttachment')
    #
    # Esto *no* aplica a productos en huevos ni al namespace (espacio de
    # nombre) de paquetes Python (es decir, no en los Productss.*)
    # para esto, vea a continuación
    #
    # Todos los productos de Plone están ya establecidos por PloneTestCase.
    #

    @onsetup
    def setup_product():
        """Configure el paquete y sus dependencias.

        El decorador @onsetup provoca que la ejecución de este cuerpo sea aplazada
        hasta la configuración de la capa de pruebas del sitio Plone.
        Pudimos haber creado nuestra propia capa, pero esta es la manera más 
        fácil para pruebas de integración Plone.
        """

        # Ejecute la configuración ZCML para el paquete example.tests
        # Esto obviamente puede usar <include /> para incluir otros paquetes.

        fiveconfigure.debug_mode = True
        import example.tests
        zcml.load_config('configure.zcml', example.tests)
        fiveconfigure.debug_mode = False

        # Hay que decirle al framework de pruebas de que estos productos
        # deberían estar disponibles. Esto no puede ocurrir hasta después de haber cargado
        # el ZCML. Por lo tanto, lo hacemos aquí. observe el uso de installPackage() en vez
        # de installProduct().
        #
        # Esto es necesario *sólo* para paquetes fuera del espacio de nombres de Productos .*
        # los cuales también son declarados como productos Zope 2, usando
        # <five:registerPackage /> in ZCML.

        # También puede ser necesario cargar dependencias, por ejemplo:
        #
        #   ztc.installPackage('borg.localrole')
        #

        ztc.installPackage('example.tests')

    # # El orden aquí es importante: En primer lugar llama la función (diferida) que
    # instala los productos que necesita para este producto. Luego dejamos PloneTestCase
    # configure este producto en la instalación.

    setup_product()
    ptc.setupPloneSite(products=['example.tests'])

    class ExampleTestCase(ptc.PloneTestCase):
        """Usamos esta clase base para todas las pruebas en este paquete. Si es necesario,
        podemos poner utilidad común o el código del setup aquí. Esto se aplica a casos de
        prueba unitaria
        """

    class ExampleFunctionalTestCase(ptc.FunctionalTestCase):
        """Usamos esta clase para pruebas de integración funcional que usan 
        sintaxis doctest. Una vez más podemos poner utilidad común o el
        código del setup aquí.
        """


Observe cómo podemos instalar de forma explícita productos de terceros (y
paquetes base-huevo que utilizan la semántica del producto) y luego decirle a
PloneTestCase hacer una rápida instalación de estos en el sitio de prueba
fixture. El runner de prueba *no* cargará automáticamente todos los productos
en el namespace de **Products.***, y tampoco ejecutará el ZCML para paquetes
fuera de **Products.*** automáticamente.

La clase de prueba que usa el entorno se puede encontrar en
``tests/test_integration_unit.py``:

.. code-block:: python

    """Esta es una prueba "unitaria" de integración. Usa PloneTestCase, 
    pero no usa la sintaxis doctest.

    Encontrará varios ejemplos de este tipo en CMFPlone/tests, por
    ejemplo.
    """

    import unittest
    from example.tests.tests.base import ExampleTestCase

    from Products.CMFCore.utils import getToolByName

    class TestSetup(ExampleTestCase):
        """El nombre de la clase debería significar algo. Esto puede
        ser una clase que pruebe la instalación de un producto en particular.
        """

        def afterSetUp(self):
            """Este método es llamado antes de cada prueba individual. Puede ser 
            utilizado para establecer el estado común. Configuración que sea
            específica para una determinada prueba debería hacerse con ese método.
            """
            self.workflow = getToolByName(self.portal,
            'portal_workflow')

        def beforeTearDown(self):
            """Este método es llamado después de cada prueba individual. 
            Puede ser utilizado para limpieza, si usted lo necesita. 
            Tenga en cuenta que el framework deshará la transacción Zope 
            al final de cada prueba, así que las pruebas son en general
            independiente de unas a otras. Sin embargo, si usted
            está modificando recursos externos (digamos una base de datos) 
            o globales (tal como registrar u nuevo adaptador en 
            la Component Architecture durante una prueba), tal vez quiera
            usar un tear-down (desmontaje) aquí.
            """

        def test_portal_title(self):

            # Esta es una prueba sencilla. El método tiene que empezar con el nombre
            # 'test'.

            #Revise la documentación de Python para pruebas unitarias para aprender más sobre los
            # tipos de métodos de afirmaciones disponibles.

            # PloneTestCase tiene algunos métodos y atributos para ayudar con Plone.
            # Observe la documentación PloneTestCase, pero en pocas palabras:
            #
            #   - self.portal es el root de portal
            #   - self.folder es la carpeta del usuario actual
            #   - self.logout() "cierra sesión" y el usuario entonces es Anónimo.
            #   - self.setRoles(['Manager', 'Member']) ajusta los role del usuario actual

            self.assertEquals("Plone site",
            self.portal.getProperty('title'))

        def test_able_to_add_document(self):
            new_id = self.folder.invokeFactory('Document', 'my-page')
            self.assertEquals('my-page', new_id)

        # Mantenga la adición de métodos aquí, o divida en varias clases o
        # archivos múltiples, según corresponda. Tener pruebas en múltiples archivos hace
        # hace posible la ejecución de pruebas desde un solo paquete:
        #
        #   ./bin/instance test -s example.tests -t
        test_integration_unit


    def test_suite():
        """Esto establece un conjunto de pruebas que ejecuta las 
        pruebas en la clase anterior
        """
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(TestSetup))
        return suite


Aquí tenemos un conjunto de pruebas con una clase de prueba; pudimos haber
añadido más clases si es necesario. Los métodos **afterSetUp()** y
**beforeTearDown()**, si están presentes, son llamados inmediatamente antes y
después de cada prueba. Después de que una prueba se ejecuta, la transacción
se regresa, causando que pruebas se ejecuten de forma aislada. Sólo se
necesita realmente un teardown (desmontaje) explícito si sus pruebas hacen
cambios permanentes que no están cubiertos por el mecanismo de transacción de
la ZODB.

Usted es libre de añadir cualquiera de los métodos de ayuda que desee para su
clase de prueba unitaria, pero cualquier método con un nombre que comience
con **test** se ejecutará como una prueba. Las pruebas suelen ser escritas para
ser lo más conciso (no confundir con "ofuscado") posible.

Vea las llamadas a los métodos como **self.assertEqual()** o **self.failUnless()**.
Estos son los métodos de afirmación que hace realmente la prueba. Si alguno
de ellos falla, esa prueba se cuenta como una falla, y obtendrá un horrible F
la salida de su prueba.

Para ejecutar la prueba, haríamos:

.. code-block:: sh

    ./bin/instance test -s example.tests -t test_integration_unit
      Running:
    ..
      Ran 2 tests with 0 failures and 0 errors in 0.178 seconds.


En realidad, hay más salida que ésta, ya que PloneTestCase instala una serie
de productos y procesos ZCML.


Reglas generales
----------------

Hay algunas reglas básicas para escribir las pruebas unitarias con
PloneTestCase que debería tener en cuenta :

-   Escriba la prueba primero; no sea perezoso y no aplace esto (¿ya no
    lo hemos dicho lo suficiente?)
-   Escriba una prueba (esto es, un método) para cada cosa que desea
    probar
-   Mantenga las pruebas que se asemejen juntas (es decir, en la misma
    clase de caso de prueba)
-   Sea pragmático. Si desea probar cada combinación de entradas y
    salidas probablemente su cara se tornará morada, y las pruebas
    adicionales son poco probables que sean de mucho valor. Del mismo modo,
    si un método es complicado, no pruebe solamente el caso básico. Esto
    viene con la experiencia, pero en general, debe probar los casos más
    comunes, los casos extremos y preferiblemente los casos en que se espera
    que el método o componente falle (es decir, prueba que falle como es
    esperado; aun así ¡no debería conseguir ninguna F en la salida de su
    prueba!).
-   Haga las pruebas sencillas. No trate de ser demasiado astuto, y no
    generalice. Cuando falla una prueba, es necesario determinar con
    facilidad si se debe a que la prueba en sí está mala, o si aquello que
    está analizando tiene un error.



Métodos de utilidad y afirmación en el framework de pruebas unitarias
-----------------------------------------------------------------------

Hay un considerable número de métodos de afirmación, y la mayoría hacen
básicamente lo mismo. Comprobar si es algo es verdadero o falso. Tener una
variedad de nombres le permite hacer sus pruebas de lectura de la manera que
desee. La lista de métodos de afirmación se puede encontrar en la
documentación de Python para ``unittest.TestCase``. Los más comunes son:

.. glossary::

  failUnless(expr)
    Asegura que expr es verdadero

  assertEqual(expr1, expr2)
    Asegura que expr1 sea igual a expr2

  assertRaises(exception, callable, ...)
    Asegura que la excepction (excepción) es levantada por callable. Tenga en cuenta que callable aquí debe ser el nombre de un método o un objeto callable (que se puede llamar), no una llamada como tal, por lo que se escribe por ejemplo, ``self.assertRaises(AttributeError, myObject.myMethod, someParameter)``. Note la falta de () después de myMethod. Si lo incluye, obtendría la excepción arrojada en su método de prueba, que probablemente no es lo que usted quiere. En vez de eso, la sentencia anterior causará que el framework de pruebas unitarias llame ``myMethod(someParameter)`` (puede pasar a lo largo de cualquier parámetro que desee después del callable) y revise por un ``AttributeError``.

  fail() 
    Falla simple. Esto es útil si una prueba aún no se ha completado, o en una sentencia "if" dentro de una prueba donde sabe que la prueba ha fallado.

Además de los métodos de afirmación para el framework de pruebas unitarias,
ZopeTestCase y PloneTestCase incluyen algunos métodos de ayuda y variables
que le ayudarán a interactuar con Zope. Es instructivo leer el código fuente
de estos dos productos, pero brevemente, las principales variables que puede
utilizar en las pruebas unitarias son:

.. glossary::

  self.portal
    El portal de Plone que la prueba está ejecutando

  self.folder
    La carpeta de miembro del miembro que usted está ejecutando

Y los métodos claves son:

.. glossary::

  self.logout()
    Cerrar sesión, es decir, convertirse en usuario anónimo

  self.login()
    Iniciar sesión nuevamente. Pasar un nombre de usuario para acceder al sistema como un usuario diferente. 

  self.setRoles(roles)
    Aprobar una lista de funciones que desee tener. Por ejemplo, self.setRoles(('Manager',)) le permite ser el administrador por un tiempo. Genial!!!

  self.setPermissions(permissions)
    Igualmente, garantizar un serie de permisos al usuario actual en ``self.folder``. 

  self.setGroups(groups)
    Establece en que grupos está el usuario de prueba

Consejos y trucos
-----------------

Buena pruebas unitarias vienen con la experiencia. Siempre es útil leer las
pruebas unitarias de código con las que usted está más familiarizado, para
ver cómo otras personas hacen pruebas unitarias. Vamos a cubrir algunas
pistas aquí para empezar a pensar acerca de cómo enfocar sus propias pruebas:

-   ¡No sea tímido! Python, al ser un lenguaje de programación dinámico,
    le permite hacer todo tipo de locuras. Usted puede sacar una función
    fuera del core de Plone y reemplazarla con su propia implementación en
    afterSetUp() o una prueba si eso cumple con sus propósitos de prueba.
-   Igualmente remplazar cosas como el **MailHost** con dummy implementations
    (implementaciones simuladas) tal vez sea la única forma de probar ciertas
    características. Observe ``CMFPlone/tests/dummy.py`` para algunos ejemplos de
    objetos dummy.
-   Utilice pruebas para probar las cosas. Se tratan de un entorno
    seguro. Si usted necesita probar algo un poco fuera de lo común,
    escribirlos en una prueba a menudo es la manera más fácil de ver cómo
    funciona algo.
-   Durante la depuración, puede insertar impresión de sentencias en las
    pruebas para obtener rastros en su terminal al ejecutar las pruebas. Sin
    embargo, no compruebe el código con impresión de sentencias. :)
-   Del mismo modo, el depurador de Python es muy valioso dentro de
    pruebas. Colocar ``import pdb; pdb.set_trace()`` dentro de los métodos de
    prueba le permite desplazarse por el código de prueba y entrar en el
    código que este llama. Si usted no está familiarizado con el depurador de
    Python, su vida está incompleta. `más sobre el uso de pdb con Plone`_.



Doctests de integración usando PloneTestCase
=============================================

El setup de prueba de integración PloneTestCase también puede usarse en
doctests

La elección de clases de caso de prueba sobre doctest es puramente de
preferencias sintácticas. Podemos utilizar el setup de prueba de la sección
anterior (en ``base.py``) también en un doctest. Este tipo de prueba es más útil
para la documentar la integración de su código con Zope/Plone en una
narrativa elegante.

No hay ningún cambio a ``tests/base.py`` para este tipo de setup (configuración)
Sin embargo, debemos tener cuidado de utilizar una clase de prueba que se
deriva de ``FunctionalTestCase``, ya que realiza la inicialización necesaria para
doctests. El setup de prueba se encuentra en ``tests/test_integration_doctest.py``:

.. code-block:: python

    """Esta es una prueba de doctest de integración. Se usa PloneTestCase y sintaxis doctest.
    """

    import unittest
    import doctest

    from zope.testing import doctestunit
    from Testing import ZopeTestCase as ztc

    from example.tests.tests import base

    def test_suite():
        """Esto establece un conjunto de pruebas que ejecuta las
        pruebas en la clase anterior
        """
        return unittest.TestSuite([

            # Aquí creamos un conjunto de pruebas que pasa el nombre de un pariente archivo
            # A la casa del paquete, el nombre del paquete, y la clase de base de prueba
            # a usar. Aquí la clase de base es un completo PloneTestCase, lo cual
            # significa que obtenemos una configuración de sitio Plone completa.

            # La prueba como tal está en integration.txt

            ztc.ZopeDocFileSuite(
                'tests/integration.txt',
                package='example.tests',
                test_class=base.ExampleFunctionalTestCase,
                optionflags=doctest.REPORT_ONLY_FIRST_FAILURE
                | doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS),

            # Podríamos añadir más archivos doctest aquí también, mediante la copia del archivo
            # de bloque anterior.

            ])


Aquí definimos ``ExampleFunctionalTestCase`` desde ``base.py`` como la **test_class**, lo
que significa que el **self** será el mismo que el **self** en la clase de prueba que
observamos en la sección anterior. En particular, podemos acceder a variables
tales como ``self.portal`` y ``self.folder``. También establecemos algunas banderas
(flags) de opciones de doctest; reportando sólo la primera falla (para evitar
la salida de error demasiado larga cuando un ejemplo previo en el ``doctest``
falla), normalizando espacios en blanco (para que podamos utilizar libremente
nuevas líneas) y permitiendo el operador de puntos suspensivos en todas
partes (en lugar de tener que activarlo cada vez que queramos usarlo). Revise
la documentación del módulo doctest para más información.

La prueba en sí que se encuentra en ``tests/integration.txt``, está escrita muy
parecida a los otros doctest que hemos visto:

.. code-block:: rst

    =========================
    Un doctest de integración
    =========================

    Esta es una prueba de doctest de integración que usa PloneTestCase.
    En este caso 'self' es la clase de prueba, para poder 
    usar 'self.folder', 'self.portal', etc. El setup se hace en
    teststest_integration_doctest.py

    Al ser un doctest, podemos contar una historia aquí.

    Por ejemplo, supongamos que un usuario tiene una última voluntad:
    añadir una noticia. Lo haremos usando API estándar de Plone

        >>> self.folder.invokeFactory('News Item', 'news-item')
        'news-item'

    Eso está muy bien, pero en realidad, él quería añadirla al root del portal:

        >>> self.portal.invokeFactory('News Item', 'news-item')
        Traceback (most recent call last):
        ...
        Unauthorized: Cannot create News Item

    ¡Ooops! ¡Que mal!

    Al menos demostramos el operador (ellipsis) de puntos suspensivos,
    que combina texto arbitrario. Esto lo habilitamos en
    test_integration_doctest.py. También
    es posible habilitar (o deshabilitar) esta bandera en una sola
    sentencia.

    Consulte la documentación de doctest de Python para más información.


Para ejecutar esta prueba por sí misma, haríamos:

.. code-block:: sh

    ./bin/instance test -s example.tests -t integration.txt
     Running:
    ..
     Ran 2 tests with 0 failures and 0 errors in 0.384 seconds.


Una vez más, hemos cortado parte de la salida de PloneTestCase.


Pruebas funcionales y de sistema con zope.testbrowser
=====================================================

Mientras que las pruebas unitarias y doctests verifican la exactitud de
métodos individuales y módulos, las pruebas funcionales prueban porciones de
aplicación como un todo, a menudo desde el punto de vista del usuario, y por
lo general en consonancia con los casos de uso. Las pruebas de sistema, en
comparación, prueban toda la aplicación como una caja negra.

A ningún desarrollador le gusta hacer clic por el explorador para comprobar
si ese botón que se suponía iba a aparecer sólo en algunos casos realmente se
apareció. Desgraciadamente estos son también los tipos de problemas que con
mayor frecuencia sufren regresiones, porque las plantillas son difíciles (y
lentas) para poner a prueba.

Zope 3 tiene una librería elegante llamada ``zope.testbrowser`` que le permite
escribir doctests que se comporten como un navegador Web real (casi...pues no
se puede manejar JavaScript, lo que significa que pruebas de interfaz de
usuario dinámica que depende de JavaScript no es posible, sin embargo 
`Selenium`_  podría ser una alternativa valida aquí). Usted puede abrir
direcciones URL, hacer clics en enlaces, rellenar campos de formulario y
hacer pruebas de las cabeceras HTTP, URL y contenidos de página que son
devueltos desde Plone. De hecho, usted podría poner a prueba cualquier sitio
web, no sólo los de Zope o Plone.

Las pruebas funcionales no son reemplazos de las pruebas unitarias. Estas
prueban un trozo de la funcionalidad, por lo general como el usuario la ve.
Por lo tanto, no pueden incluir sistemáticamente todos los aspectos de la
aplicación. Por ejemplo, una prueba funcional puede comprobar si un botón
"Eliminar" está presente, e incluso si funciona como es esperado, pero no
debe ser utilizado para probar de forma exhaustiva si la operación de
eliminación funciona en todos los casos posibles. Donde se destacan, sin
embargo, es en las pruebas de cosas como que opciones aparecen a que usuarios
en función de roles y permisos, o simplemente ejercitar todas las plantillas
diversas utilizadas en un determinado producto para asegurarse de que no
fallen.

Aquí hay un ejemplo del paquete ``example.tests``. El setup de prueba está en
``tests/test_functional_doctest.py``:

.. code-block:: python

    """Esta es una prueba de doctest funcional Se usa PloneTestCase y sintaxis doctest. 
    En la prueba como tal, usamos zope.testbrowser para probar funcionalidades de extremo
    a extremo, incluyendo la UI (interfaz de usuario)

    Una cosa importante a tener en cuenta: zope.testbrowser no es
    percibe JavaScript! Para eso, necesita un explorador real. 
    Revise zope.testbrowser.real y Selenium si requiere hacer 
    pruebas reales con un explorador.
    """

    import unittest
    import doctest


    from Testing import ZopeTestCase as ztc

    from example.tests.tests import base

    def test_suite():
        """Esto establece un conjunto de pruebas que ejecuta las
        pruebas en la clase anterior
        """
        return unittest.TestSuite([

            # Aquí creamos un conjunto de pruebas que pasa el nombre de un pariente archivo
            # A la casa del paquete, el nombre del paquete, y la clase de base de prueba
            # a usar. Aquí la clase de base es un completo PloneTestCase, lo cual
            # significa que obtenemos una configuración de sitio Plone completa.

            # La prueba como tal esta en functional.txt

            ztc.ZopeDocFileSuite(
                'tests/functional.txt',
                package='example.tests',
                test_class=base.ExampleFunctionalTestCase,
                optionflags=doctest.REPORT_ONLY_FIRST_FAILURE
                | doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS),

            # Podríamos añadir más archivos doctest aquí también, mediante la copia del archivo
            # de bloque anterior.

            ])


Este código es en realidad idéntico al setup de prueba para la doctest de
integración en la sección anterior. Las diferencias se encuentran en la
prueba misma, que usa ``Products.Five.testbrowser.Browser``, una compatibilidad
Zope 2 empaquetado alrededor de ``zope.testbrowser.Browser``:

.. code-block:: rst

    ====================
    Un doctest funcional
    ====================

    Esta es una prueba funcional completa Aquí el énfasis se encuentra 
    en probar lo que el usuario puede introducir y ver, y el sistema 
    es en gran parte a probado como una caja negra.
    Utilizamos PloneTestCase para comprobar esta prueba, y así tener 
    un sitio completo de Plone para jugar con él. Nosotros *podemos* 
    inspeccionar el estado del portal por ejemplo usando self.portal 
    y self.folder, pero generalmente no es bien visto ya que
    usted no está tratando el sistema como una caja negra. Además si usted 
    por ejemplo inicia sesión o define roles usando llamadas como 
    self.setRoles(), estas no se reflejan en la navegador
    de prueba, el cual se ejecuta como una sesión independiente.

    Al ser un doctest, podemos contar una historia aquí.

    En primer lugar, hay que realizar alguna configuración. Usamos el
    testbrowser que se suministra con Five, ya que este proporciona 
    adecuada integración de Zope 2. Sin embargo, la mayoría de la
    documentación,  se encuentra en el paquete subyacente
    zope.testbrower.

        >>> from Products.Five.testbrowser import Browser
        >>> browser = Browser()
        >>> portal_url = self.portal.absolute_url()

    Lo siguiente es útil para escribir y depurar las pruebas testbrowser.
    Nos permite usar todos los mensajes de errores en el error_log.

        >>> self.portal.error_log._ignored_exceptions = ()

    Con eso en su lugar, podemos ir a la página principal del portal y
    entrar (iniciar sesión) Haremos esto utilizando el usuario por 
    defecto de PloneTestCase:

        >>> from Products.PloneTestCase.setup import portal_owner,
        default_password

        >>> browser.open(portal_url)

    Tenemos el portlet de inicio de sesión, así vamos a usarlo.

        >>> browser.getControl(name='__ac_name').value = portal_owner
        >>> browser.getControl(name='__ac_password').value =
        default_password
        >>> browser.getControl(name='submit').click()

    Aquí establecemos el valor de los campos en el formulario de inicio
    sesión y luego simular un clic de un supuesto envío.

    Luego probamos si seguimos en la página principal del portal:

        >>> browser.url == portal_url
        True

    Y nos aseguramos que obtenemos el mensaje amistoso para inicio de
    sesión.

        >>> "You are now logged in" in browser.contents
        True

    Para aprender más, observe la documentación del paquete zope.testbrowser y sus interfaces.
    También hay algunos ejemplos de pruebas de testbrowser en Plone como tal.


Toda la acción ocurre con el objeto ``browser``. Este simula un navegador Web
(aunque como se ha dicho, uno que no soporta JavaScript), y tiene una API
agradable para encontrar los controles de formulario y enlaces y acciones por
clic sobre ellos. Las variables ``browser.url`` y ``browser.contents`` representan lo
que habría estado en la barra URL y la vista renderizada de la página
respectivamente, y pueden ser examinadas como cualquier otra variable.

``zope.testbrowser`` tiene documentación bastante completa en su archivo
`README.txt de zope.testbrowser`_ - que es, por supuesto, una doctest ejecutable. En resumen, los
métodos más importantes del `IBrowser interface`_ (y por lo tanto de la clase
``Browser``) son:

.. glossary::

  open(url)
    Abrir una URL determinada.

  reload()
    Actualizar la página actual, tanto como en el botón de Actualizar o Recargar en el navegador haría.

  goBack(count=1)
    Simular la acción del número de ``veces`` por el botón Atrás o Retroceder. 

  getLink(text=None, url=None, id=None) 
    Obtener un ILink (el cual puede luego llamar para un ``click()``), ya sea por el texto dentro de la <a> etiqueta, por el URL en el atributo ``href``, o la id del enlace.

  getControl(label=None, name=None, index=None) 
    Obtener un ``IControl``, representando un control de formulario, mediante una etiqueta (ya sea el valor de un botón de envío o el contenido de etiqueta ``<label>`` asociada) o nombre del formulario. El argumento index (índice) se utiliza para eliminar la ambigüedad de si hay más de un control (ejemplo ``index=0`` obtiene el primero.). Una vez más, usted puede llamar un ``click()`` en el objeto de control para simular las acciones por clic en él.

La interfaz iBrowser también proporciona algunas propiedades que se pueden
utilizar para examinar el estado de la página actual. Las más importantes
son:

.. glossary::

  url
    La dirección URL completa de la página actual. contents Los contenidos completos de la página actual, como una cadena (por lo general contienen etiquetas HTML) headers Un diccionario de los cabeceras HTTP

Por favor revise `interfaces`_ y el `archivo README`_ para más detalles sobre
los otros métodos y atributos, las interfaces para distintos tipos de enlaces
y controles, y más ejemplos.


Depurando pruebas funcionales
-----------------------------

A veces obtendrá errores de Zope provenientes de un comando ejecutado
utilizando el testbrowser. En este caso, a veces puede ser difácil saber cuál
es la causa subyacente. Dos ayudas de depuración existentes para hacer esto
un poco más fácil.

En primer lugar Asegúrese de ver todos los errores:

.. code-block:: python

      >>> browser.handleErrors = False


Si ``handleErrors`` es True (Verdadero, por defecto) obtendrá errores como
``HTTPError: HTTP Error 404: Not Found`` o ``HTTPError: HTTP Error 500: Internal
Server Error``. Probablemente esos no son muy útiles para usted. Ajustando
``handleErrors`` a False (falso) mostrará el Zope con las excepciones completa (o
posiblemente el HTML renderizando de la página de error, dependiendo del tipo
de error).

En segundo lugar si está usando PloneTestCase, puede utilizar registro de
error de Plone. En la parte superior del ejemplo, podemos hacer:

.. code-block:: python

      >>> self.portal.error_log._ignored_exceptions = ()


Esto significa que errores como NotFound (no encontrado) y Unauthorized (no
autorizado) se mostrarán en el registro de errores. También puede ser útil
activar la Seguridad Verbosa en ``zope.conf`` (vea los comentarios en ese archivo
para más detalles). Ahora cuando aparezca una línea que está lanzando un
error que no se puede depurar, puede hacer lo siguiente:

.. code-block:: python

        >>> try:
        ...     browser.getControl('Save').click()
        ... except:
        ...     print
        self.portal.error_log.getLogEntries()[0]['tb_text']
        ...     import pdb; pdb.set_trace()
        >>> # continue as normal


Esto imprimirá la entrada más reciente en el registro de errores, y establece
un punto de ruptura PDB.


Usando un navegador real para renderizar los resultados de sus pruebas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A veces le gustaría ver la salida de ``browser.contents`` en un navegador
para depurar fácilmente lo que está sucediendo en las pruebas funcionales.
Para ello coloque un punto de ruptura PDB en las pruebas como se describió
anteriormente (``import pdb; pdb.set_trace()``) y escriba lo siguiente cuando
llegue a la parte PDB durante la ejecución de pruebas:

.. code-block:: python

    >>> from Testing.ZopeTestCase.utils import startZServer
    >>> startZServer()


Esto imprimirá una tupla como:

.. code-block:: python

    ('127.0.0.1', 55143)

que contiene una dirección IP y el puerto donde se puede acceder al sitio con
el que testbrowser está trabajando, en un navegador real.


Pruebas funcionales vs. Pruebas de sistema
------------------------------------------

A system test is one which treats the entire system as a black box,
interacting with it as a user would. Una prueba funcional se centra más en
una sola "vertical" de funcionalidad, por lo general vinculada a un caso de
uso en particular.

Para una prueba funcional *puede* que sea aceptable examinar el estado
interno del portal (usando ``self.portal`` y la clase
``PloneTestCase.FunctionalTestCase`` para construir un conjunto de pruebas) para
proporcionar afirmaciones. En contraste, una prueba de sistema no hace tales
afirmaciones. Idealmente, debería estar en la capacidad de apuntar a la
prueba ``zope.testbrowser`` en un sitio remoto ejecutando una instalación nueva
de su sistema, y pasar la pruebas.

más allá de eso, las herramientas utilizadas para escribir una prueba de
sistema son los mismas. Es sólo el enfoque de la prueba lo que cambia. Ya sea
que necesite una o la otra, o ambas, dependerá del nivel de rigor que
necesita en sus pruebas, y cómo su sistema está construido. Sin embargo en
general, las pruebas reales de sistema son más raras que las funcionales (de
integración) y unitarias.


Usando zope.testrecorder para grabar pruebas funcionales
========================================================

El producto ``zope.testrecorder`` nos trae el círculo completo: las pruebas
funcionales se graban desde el navegador, y se guardan en una prueba
ejecutable.

Las pruebas funcionales que utilizan ``zope.testbrowser`` nos salvan de hacer
clic por todo el navegador para la interfaz de usuario de pruebas de
regresión, pero incluso la escritura de ellas puede ser más fácil. Con
plantillas complejas, a veces puede ser difícil saber qué enlaces y campos de
formulario de la prueba testbrowser debería estar buscando, y que texto
debería utilizar en las afirmaciones.

Aquí es donde entra ``zope.testrecorder``. La teoría es que navegue por la
interfaz de usuario sólo una vez, y luego renderizar la historia de lo que
hizo para una prueba de testbrowser ejecutable. ``zope.testrecorder`` puede
incluso crear `pruebas Selenium`_ una forma alternativa de pruebas
funcionales que se ejecutan en el navegador (es decir, que automatiza el
navegador frente a sus ojos) y por lo tanto compatibles con JavaScript, pero
no se pueden ejecutar como parte de una prueba automatizada ejecutándose sin
un navegador.

instalar ``zope.testrecorder`` es simple. Primero obtenga una copia desde el repositorio de subversión de Zope:

.. code-block:: sh

  svn co svn://svn.zope.org/repos/main/zope.testrecorder/trunk zope.testrecorder

Vea ``INSTALL.txt`` para obtener más instrucciones, pero la manera más fácil de
instalarla en una instancia Zope 2 es simplemente ponerla en su directorio
Products: Copie ``zope.testrecorder/src/zope/testrecorder`` como un producto
dentro de ``Products/testrecorder`` y reinicie Zope. Luego vaya a la ZMI y
agregue un objeto ``Test Recorderen`` el root de su instancia Zope. Colóquele un
nombre como: ``test-recorder``.

Asumiendo que está corriendo su Zope en localhost:8080, ahora debería ser
capaz de ir a ``http://localhost:8080/test-recorder/index.html``. Usted debería
ver en la página algo como esto:

.. image:: ./blank-testrecorder.png
  :alt: Screenshot of blank test recorder
  :align: center

.. note::

  Como la mayoría de las cosas, ``zope.testrecorder`` pareciera trabajar mejor en Firefox que en otros navegadores.

Ahora introduzca la dirección de su sitio Plone (o de hecho cualquier sitio
web), ejemplo: ``http://localhost:8080/Plone`` y haga clic en ``Go``. Usted puede
realizar cualquier número de operaciones, por ejemplo, el iniciar sesión y
hacer clic por la interfaz de usuario. Si desea agregar un comentario a la
ejecución de su prueba, tal como agregaría texto libre dentro de un doctest,
haga clic en el botón ``Add comment`` (añadir comentario). Si usted desea
verificar si un texto aparece en la página, seleccione el texto, haga un
shift-clic sobre él y seleccione "Check text appears on page" ("revisar si un
texto aparece en la página"):

.. image:: ./verify-testrecorder.png
  :alt: Screenshot of text verification
  :align: center


Cuando finalice haga clic en ``Stop recording`` (detener la grabación). A
continuación, puede optar por renderizar la prueba como un ``doctest de Python``

.. code-block:: python

      Crear el objeto de navegador que vamos a utilizar.

          >>> from zope.testbrowser import Browser
          >>> browser = Browser()
          >>> browser.open('http://localhost/test')

      Un comentario de prueba.

          >>> 'start writing' in browser.contents
          True


A continuación, puede pegar esto en un archivo doctest, y realizar cualquier
procesamiento posterior o hacer cambios que sean necesarios para hacer la
prueba más valida desde un punto de vista general.


Consejos al usar zope.testrecorder
----------------------------------

.. glossary::

  Plan, plan, plan
    Es mejor si tiene un guión así sea un borrador, delante de usted antes de empezar las pruebas de grabación, o puede perderse después. Haga un buen uso del botón para ``Añadir comentarios`` para indicar lo que usted probará antes de probarlo, para que el doctest resultante tenga sentido.

  Cuidado donde hace clic
    Algunas partes de la interfaz de usuario de Plone son más efímeras que otras. Puede que no sea buena idea contar con enlaces en el portlet ``Recientes``, por ejemplo. Piense en que operaciones proporcionarán la prueba más general y válida. Esto le ahorrará tiempo a largo plazo. 

  Configure su sitio de antemano
    Recordemos la sección sobre ``zope.testbrowser`` donde definimos usuarios y estructura básica del sitio, con llamadas a los API de Python en lugar de usar testbrowser para manipular las pantallas de "Configuración de sitio". Cuando usa ``zope.testrecorder`` es posible que desee para definir los mismos usuarios con los mismos nombres de usuario y contraseñas, y la misma estructura del sitio antes de iniciar la grabación para pruebas. De lo contrario, puede que tenga que cambiar algunos de los valores de la prueba. 

  Revisar el doctest
    ``zope.testrecorder`` es una herramienta para ahorrar tiempo. A veces, puede terminar haciendo referencia a partes de la página que no se puede garantizar que sean consistentes (por ejemplo, generación aleatoria de identificadores para objetos de contenido), y a veces puede haber tomado un desvío y terminado con una prueba que contiene secciones duplicada o irrelevante. Siempre arregle su prueba ¡y ejecútela! después, para asegurarse de que la prueba sigue siendo válida para el futuro, de lo contrario, terminará haciendo clics con rabia por la interfaz de usuario nuevamente.


Determinando la cobertura del código de su conjunto de pruebas.
===============================================================

Explicación de cómo utilizar el Zope test runner\'s (runner de prueba Zope)
construido en cobertura de código para probar la calidad de su conjunto de
prueba

Entre mejor sea la cobertura de su conjunto de pruebas, menor será la
probabilidad de que algunas modificaciones a su código dañen otra parte de la
funcionalidad en alguna manera inesperada. Pero, ¿cómo se **conoce la
calidad** de la cobertura de su prueba? el Zope\'s test runner viene con
varias características que le ayudarán a hacer precisamente eso.

Pero primero, vamos a decir que ha escrito un poco de código con un
condicional Python como el siguiente:

.. code-block:: python

  if value % 2 == 0:
      print "This is an even number"
  else:
      # tenemos que hacer cómputos
      # mas complejos para manejar números impares
      _someComplexCodeDealingWithOddNumbers(value)


Los comentarios y llamada de función en la cláusula "else" son simbólicos de
algunas codificaciones avanzadas que son requeridas en el manejo de todos los
números impares.

Ahora, como sin duda ha aprendido al leer este tutorial, es que las pruebas
son importante. Pero que pasa si por una u otra razón, todos los casos de
prueba con los que ha surgido durante las pruebas llegan a números pares
cuando obtiene el bloque de códigos ya mencionado. Si este fuera el caso
tendría un gran riesgo de ruptura de código no anticipada para la manera en
que maneja números impares. Esto es algo que realmente tiene que cubrir en su
conjunto de pruebas.

Descubriendo las secciones no probadas de su código
---------------------------------------------------

Usted ha aprendido a cómo ejecutar su conjunto de pruebas en este tutorial.
Zope\'s test runner acepta un parámetro opcional llamado ``--coverage``. Cuando se
le pasa una ruta a un directorio, Zope generará una salida de alto nivel y
producirá un archivo de cobertura para cada uno de los módulos de Python en
su producto o paquete.

En total, ejecutar el conjunto de pruebas con la opción de cobertura activada
se vería así:

.. code-block:: sh

  ./bin/instance test -s Products.productname --coverage=$HOME/coverage

.. note::

  La ejecución de pruebas con la opción de cobertura activada toma mucho más tiempo (aproximadamente 10 veces o más) que si no estuviera activada, así que esto es algo que se hace de vez en cuando para calibrar su trabajo, en lugar hacerlo cada vez que ejecute sus pruebas.

Al final de la ejecución de su conjunto de pruebas, obtendrá un resultado
inmediato como el siguiente, que incluye líneas de código y su porcentaje de
cobertura

.. code-block:: sh

  lines   cov%   module   (path)
    104   100%   $INSTANCE_HOME.parts.salesforce-integration-products.salesforcepfgadapter.Extensions.Install
                 ($INSTANCE_HOME/parts/salesforce-integration-products/salesforcepfgadapter/Extensions/Install.py)
     39    41%   $INSTANCE_HOME.parts.salesforce-integration- products.salesforcepfgadapter.__init__
                 ($INSTANCE_HOME/parts/salesforce-integration-products/salesforcepfgadapter/__init__.py)
      2   100%   $INSTANCE_HOME.parts.salesforce-integration-products.salesforcepfgadapter.content.__init__
                 ($INSTANCE_HOME/parts/salesforce-integration-products/salesforcepfgadapter/content/__init__.py)
    168    91%   $INSTANCE_HOME.parts.salesforce-integration-products.salesforcepfgadapter.content.salesforcepfgadapter
                 ($INSTANCE_HOME/parts/salesforce-integration-products/salesforcepfgadapter/content/salesforcepfgadapter.py)
     21   100%   $INSTANCE_HOME.parts.salesforce-integration-products.salesforcepfgadapter.migrations.migrateUpTo10rc1
                 ($INSTANCE_HOME/parts/salesforce-integration-products/salesforcepfgadapter/migrations/migrateUpTo10rc1.py)


Si todo lo que está buscando es un informe rápido sobre la situación, esto debería ser suficiente.

Sin embargo si desea nadar más profundo, vaya al directorio que listo en la
opción ``--coverage``.

.. note::

  Los archivos pueden ser precedidos por puntos, lo que requiere un ``ls -a`` con el fin de llegar a los archivos de cobertura.

Un ejemplo de archivo puede lucir de la siguiente manera:

.. code-block:: python

       1:     def initializeArchetype(self, **kwargs):
                   """Initialize Private instance
                   variables
                   """
       15:         FormActionAdapter.initializeArchetype(self, **kwargs)

       15:         self._fieldsForSFObjectType = {}


        1:     security.declareProtected(View, 'onSuccess')
        1:     def onSuccess(self, fields, REQUEST=None):
                   """ The essential method of a PloneFormGen Adapter
                   """
    >>>>>>         logger.debug('Calling onSuccess()')
    >>>>>>         sObject = self._buildSObjectFromForm(fields, REQUEST)
    >>>>>>         if len(sObject.keys()) > 1:


Esto es realmente sólo su archivo con algunos datos significativos procediendo cada línea. Cualquier cosa con un ``1:`` significa que su código fue por lo menos tanteado durante la ejecución del conjunto de pruebas. Cuanto mayor sea el número, más a menudo su código fue tanteado. Tal vez esto sea intencional y represente una cobertura muy buena en otros casos, puede que sea inevitable e incluso podría significar que el alto nivel de cobertura en realidad no será necesario. La ``>>>>>>`` significa que se ha pasado una línea y debería considerar un escenario de prueba o más para revisar esta línea de código en cuestión. El número de líneas no probadas dividido por el total de líneas le da el porcentaje de cobertura.

Si lo que quiere es algo vistoso
--------------------------------

Si desea gráficos bonitos para darle a su jefe incluidos en un informe o para
que un cliente se sienta mejor con respecto a la calidad del código que está
recibiendo, ``z3c.coverage`` toma el contenido de los archivos de salida y crea
resúmenes vistosos. Obtenga z3c.coverage desde subversión a través de lo
siguiente:

.. code-block:: sh

  svn co  svn://svn.zope.org/repos/main/z3c.coverage/trunk z3c.coverage

Cree un directorio en el directorio de cobertura previamente creado. Nosotros
lo llamamos reports. (informes). Ejecute el módulo coveragereport.py con la
fuente siendo su salida de cobertura y el destino, del directorio reports
reción creado. Vea lo siguiente:

.. code-block:: sh

  mkdir $HOME/coverage/reports
  python z3c.coverage/src/z3c/coverage/coveragereport.py $HOME/coverage $HOME/coverage/reports

Ahora debería pode abrir ``$HOME/coverage/reports/all.html`` dentro de su navegador para obtener una salida muy similar a la siguiente.

.. image:: ./coverage.png
  :alt: z3c.coverage test coverage screenshot
  :align: center

Con esta información disponible, puede comenzar a sacar conclusiones acerca
de cómo puede trabajar su camino hacia una mejor cobertura para su producto.


Ejemplos de pruebas
===================

Aquí listamos algunos paquetes y proyectos que demuestren una buena cobertura
de pruebas

La ejecución de pruebas se aprender mejor mediante ejemplos. Puede ser muy
instructivo leer a través de las pruebas escritas por otros desarrolladores y
aprender lo que prueban, lo que no y cómo escriben sus pruebas.

-   `example.tests`_, que ya hemos mencionado, contiene un ejemplo para
    cada uno de los diferentes tipos de pruebas estudiadas en este tutorial.
    El código de setup (configuración) de la prueba está bien comentado, con
    la intención de que este paquete proporcione un buen documento para los
    desarrolladores en la creación de un nuevo proyecto.
-   `Plone per se`_ cuenta con más de 1.600 pruebas al momento de la
    escritura. La mayoría de estas son pruebas de integración utilizando
    sintaxis prueba-unitaria con PloneTestCase.
-   `RichDocument`_ tiene una básica ``test_setup.py`` prueba de integración.
    Este es un buen ejemplo de la clase de prueba que es posible que desee
    hacer para asegurar que su paquete instale limpiamente.
-   `borg.project`_ contiene un archivo `README.txt`_ con un doctest de
    integración demostrando como usarle. Tiene un sólo modulo de prueba
    `tests.py`_, el cual realiza el mismo setup que ``base.py`` y
    ``test_integration_doctest.py`` de ``example.tests``.
-   La mayoría de pruebas en el paquete `plone.app.controlpanel`_
    utilizan pruebas test-browser (prueba-navegador) funcionales para
    verificar que los paneles de control en Plone funcionen correctamente.


Sientase en plena libertad de editar o comentar en esta página si ¡posee más
ejemplos para agregar!


Referencias
===========

- `Testing in Plone`_.
- `unittest — Unit testing framework`_.

.. _example.tests: http://dev.plone.org/collective/browser/examples/example.tests/trunk
.. _tutorial de buildout: http://plone.org/documentation/kb/buildout
.. _el tutorial de buildout: http://plone.org/documentation/kb/buildout
.. _buildout: http://plone.org/documentation/kb/buildout
.. _modulo de doctest: http://docs.python.org/lib/module-doctest.html
.. _más sobre el uso de pdb con Plone: http://plone.org/documentation/how-to/using-pdb/
.. _Selenium: http://www.openqa.org/selenium/
.. _README.txt de zope.testbrowser: http://svn.zope.org/zope.testbrowser/trunk/src/zope/testbrowser/README.txt?view=auto
.. _archivo README: http://svn.zope.org/zope.testbrowser/trunk/src/zope/testbrowser/README.txt?view=auto
.. _IBrowser interface: http://svn.zope.org/zope.testbrowser/trunk/src/zope/testbrowser/interfaces.py?view=auto
.. _interfaces: http://svn.zope.org/zope.testbrowser/trunk/src/zope/testbrowser/interfaces.py?view=auto
.. _pruebas Selenium: http://plone.org/documentation/kb/testing/zope.org/Members/tseaver/Zelenium
.. _Plone per se: http://dev.plone.org/plone/browser/Plone/trunk/Products/CMFPlone/tests
.. _RichDocument: http://dev.plone.org/collective/browser/RichDocument/trunk/tests/testSetup.py
.. _borg.project: http://dev.plone.org/collective/browser/borg/components/borg.project/trunk
.. _README.txt: http://dev.plone.org/collective/browser/borg/components/borg.project/trunk/borg/project/README.txt
.. _tests.py: http://dev.plone.org/collective/browser/borg/components/borg.project/trunk/borg/project/tests.py
.. _plone.app.controlpanel: http://dev.plone.org/plone/browser/plone.app.controlpanel/trunk/plone/app/controlpanel/tests
.. _Latest changes: http://dev.plone.org/plone/timeline
.. _Testing in Plone: http://plone.org/documentation/kb/testing
.. _unittest — Unit testing framework: http://docs.python.org/library/unittest.html
