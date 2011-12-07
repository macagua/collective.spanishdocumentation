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
