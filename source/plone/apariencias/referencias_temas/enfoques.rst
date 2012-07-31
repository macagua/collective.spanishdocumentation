.. -*- coding: utf-8 -*-

.. _3_seccion:

Enfoques
========

Hay diferentes maneras de abordar temas de Plone. Aquí está la información
para ayudarle a tomar una decisión sobre su enfoque; ya sea para basar su
tema en estructuras existentes, o para trabajar a través de la web o en el
sistema de archivos, si todavía necesita este manual para ejecutar estas
acciones.


¿Empezar desde cero o basarse en Plone Default?
-----------------------------------------------

Es perfectamente posible crear su propio tema Plone desde cero, pero es
probable que no quiera hacer esto.


¿Basarse en Plone Default?
..........................

En particular, las características avanzadas de la interfaz de edición de
Plone están empaquetadas como parte del tema por defecto: Plone Default, y es
probable que desee mantenerlos.

La buena noticia es que puede **basar** su propio tema en Plone Default y
entrelazar sus pedacitos de plantillas, estilos, scripts y componentes, con
los que ya existen. Hay tres maneras de hacerlo:

-   con el bloque Skin para construcción **personalice** los detalles de
    Plone Default (hay una manera elegante de hacer esto, la cual deja el
    tema Plone Default completamente intacto)

-   con el bloque Components para construcción **construya el suyo
    propio**, pero también puede **reusar** partes de componentes de Plone
    Default en el proceso

-   con la Configuración, simplemente **agregue nuevas** pautas


Hay otras buenas noticias: los elementos de un tema Plone se dividen en
partes muy pequeñas. Cada uno puede tratarse de manera independiente con
respecto a los demás, por lo que puede enfocarse tan sólo en las partes que
desea cambiar. El costo de toda esta flexibilidad es que a veces es difícil
localizar exactamente que parte desea, y las cosas podrían comenzar a parecer
complicadas. Este manual puede ayudarle con eso.

Puede cambiar bastante la apariencia sólo con sobrescribir los estilos CSS
existentes, o reescribiendo algunas de las hojas de estilo existentes. Sin
embargo, si usted quiere empezar a mover elementos de la página o reescribir
algo del XHTML, entonces usted necesita profundizar en las plantillas,
componentes y configuración con más detalle.

Al final de todo puede que surja con un tema basado en Plone Default (basado
estructuralmente, más no visualmente). Esto probablemente incluirá

-   su propia hoja de estilo, o los rescritos de algunas partes de la CSS de Plone

-   un reordenamiento de los elementos de la página

-   algunos rescritos de algunos elementos de la página

-   unos elementos "nuevos" de la página


¿A través de la Web o en el Sistema de archivos?
------------------------------------------------

¿Cómo decidir si se debe construir su tema a través de la web o en el sistema
de archivos?

Tarde o temprano se enfrentará con una decisión. Plone es lo suficientemente
flexible para que regularmente haya más una manera de hacer esto, y la
interrogante por lo general no es *cómo* hacerlo, sino a través de *cuál
camino*.

Se puede personalizar Plone Default a través de la web muy fácilmente,
especialmente el skin y los bloques de configuración para construcción. En
secciones posteriores de este manual le señalaremos las dirección de los
lugares relevantes en la Interfaz de Administración de Zope para hacer esto.
Sin embargo, si desea mover estas personalizaciones a un nuevo sitio,
encargarse de personalizaciones bastante extensas, o construir un tema
completamente nuevo, pues entonces es recomendable mover su trabajo al
sistema de archivos.

En este caso necesitará crear un modulo instalable (también conocido como
producto de tema o huevo) Esta puede ser una perspectiva atemorizante, pero
se cuenta con herramientas para simplificar el proceso. Mediante un paquete
listo para usarse en el que se colocan todos los elementos de sus bloques
para construcción de temas. Explicaremos estas herramientas en las siguientes
páginas.

Si apenas está comenzando, es una buena idea familiarizarse con los bloques
para construcción y las técnicas para trabajar a través de la web. No hay
ninguna dificultad en mover después lo que ha hecho al sistema de archivo.
Una vez que comience a reestructurar o mover componentes de un lado a otro
descubrirá que el sistema de archivos es una forma más cómoda para trabajar.


A través de la Web
..................

+---------------------------------------+-----------------------------------------+
| Pros                                  |  Contras                                |
+=======================================+=========================================+
| Rápido y sencillo                     | Dificultad para replicar o mover de un  |
|                                       | sitio a otro                            |
+---------------------------------------+-----------------------------------------+
| Resultados inmediatamente visibles    | Personalizaciones de gran escala pueden |
|                                       | complicarse                             |
+---------------------------------------+-----------------------------------------+
|                                       | Algunas personalizaciones no son        |
|                                       | posibles (ej.: no puede mover viewlets  |
|                                       | entre administradores de viewlets)      |
+---------------------------------------+-----------------------------------------+


En el Sistema de archivos
.........................

+---------------------------------------+-----------------------------------------+
| Pros                                  |  Contras                                |
+=======================================+=========================================+
| Portatil y reutilizable               | Curva de aprendizaje más abrupta cuando |
|                                       | comience por primera vez                |
+---------------------------------------+-----------------------------------------+
| Completa flexibilidad, puede escribir | Necesita acceso al sistema de archivos  |
| sus propios viewlets y portlets       |                                         |
+---------------------------------------+-----------------------------------------+
| Agrupa sus propios cambios dentro de  | A menudo necesitará reiniciar para ver  |
| sus propio tema / skin                | los cambios                             |
+---------------------------------------+-----------------------------------------+

Direcciones futuras
-------------------

Este manual de referencia describe el enfoque actual de temas en Plone. Pero
de igual manera puede estar al tanto de que hay otros caminos en el
horizonte, quizás mucho más simples.

La tematización de Plone se está complicando un poco. Así que la comunidad
Plone, a su manera inimitable y llena de energía, está explorando diferentes
soluciones para el asunto de temas.

Las cosas se mueven rápidamente Al momento de diseñar, algunas de las
soluciones presentadas a continuación quizás ya no están lo suficientemente
desarrolladas para ser usadas muy seriamente, particularmente si usted está
empezando. No obstante, debería investigarlas para ver cómo están
progresando:


Temas listos
............

Un proyecto veloz y en curso para generar temas que se incluirán con el Plone
de caja, y aportes mediante lluvias de ideas para mejorar las historia de
temas en Plone:

-   `http://www.coactivate.org/projects/ootb-plone-themes/summary`_


Deliverance
...........

Deliverance es un programa ligero que aplica un tema a contenido de acuerdo a
un conjunto de reglas.

-   `http://www.coactivate.org/projects/deliverance/summary`_

-   `http://blog.repoze.org/setting-up-deliverance-screencast-20071025.html`_


.. _http://www.coactivate.org/projects/ootb-plone-themes/summary: http://www.coactivate.org/projects/ootb-plone-themes/summary
.. _http://www.coactivate.org/projects/deliverance/summary : http://www.coactivate.org/projects/deliverance/summary
.. _http://blog.repoze.org/setting-up-deliverance-screencast-20071025.html: http://blog.repoze.org/setting-up-deliverance-screencast-20071025.html
