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
