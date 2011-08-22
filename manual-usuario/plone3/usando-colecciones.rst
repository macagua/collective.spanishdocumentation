5. Usando Colecciones
=====================

Las Colecciones se aprovechan de la inteligencia de Plone.


5.1. Introducción a Colecciones
===============================

Una Colección en Plone funciona como un reporte o una consulta en una base de
datos. Use Colecciones para clasificar y mostrar su contenido de una manera
dinámica.

Una **Colección** en Plone funciona como un reporte o una consulta en una
base de datos. La idea es que usted use una Colección para búsquedas en su
sitio web basado en un grupo de **Criterios** tales como: tipo de contenido
(Pagina, Noticia, Imagen), la fecha en que fue publicado, o palabras claves
contenidas en el titulo, descripción, o contenido.

Digamos que usted tiene una gran cantidad de fotografías y mapas en su sitio
web. Usted fácilmente las puede mostrar todas de una sola vez creando un
`hiperenlace`_ a la `carpeta`_ donde están guardadas.. Usted podría incluso
crear distintos enlaces a sub-carpetas si ha organizado los elementos de esa
manera. Sin embargo, si sus fotografías y mapas están repartidas por todo el
sitio, esto rápidamente se podría convertir en algo engorroso. Además no hay
manera que carpetas normales muestren distintos contenidos provenientes de
partes distintas del sitio basados en cosas como:

-   Palabras clave en el titulo
-   Fecha de creación
-   Autor
-   Tipo de contenido



La necesidad de mostrar contenido en formas dinámicas han dado auge a las
**Colecciones** (Formalmente conocidas conocidas como **Smart Folders
(Carpetas Inteligentes)**,o **Rich Topic (Contenido Enriquecido)** en
versiones anteriores a Plone). Las Colecciones no poseen elementos de
contenidos como tal, a diferencia de las carpetas. En lugar de esto es el
**Criterio** que usted establezca el que determine que contenido aparece en
cada pagina de Colección.

Las aplicaciones mas comunes para las Colecciones son:

-   Archivos nuevos
-   Archivos de eventos
-   Fotos mostradas por Date Range (Rango de Fechas)
-   Contenido mostrado por palabras clave


5.2. Agregando Colecciones
==========================

Las Colecciones (formalmente llamadas Smart Folders (Carpetas inteligentes))
son contenedores virtuales de listas de elementos que se encuentran haciendo
búsquedas especializadas.

Una Colección sirve para construir un tipo de contenedor virtual para
contenido -- en realidad el contenido existe donde quiera que este guardado
en el sitio web, pero la Colección encuentra contenido según las pautas
establecidas por un criterio de búsqueda y lo hace parecer como si los
elementos estuvieran almacenados en un acuerdo alternativo. Para las paginas
de mariposas descritas en la introducción de esta sección, el acuerdo de
almacenamiento existente es por grupos taxonómicos (Skippers, Monarchs,
Dustywings, etc.) pero con las Colecciones puede haber agrupaciones virtuales
de distintos criterios. Ej: el color. Las paginas de mariposas que concuerdan
con estos criterios se mostraran como si estuvieran "alojadas" en la
Colección que contiene las paginas de mariposas por color. Por supuesto tiene
que haber categorías (formalmente llamadas palabras claves) determinadas por
color en las paginas de mariposas para que esto funcione. Los criterios de
búsqueda hechos para encontrar textos en general puede ser configurada
también, para agrupar acuerdos significativos.

Aprender a pensar en contenidos donde sea que estén guardados, y en
colecciones por defecto para recolectar distintas "vistas" del contenido, es
un paso importante para utilizar Plone efectivamente, ya que es un sistema
inteligente.

Para agregar una colección, use el menú *Agregar elemento*, tal como los es
para agregar otros tipos de contenido:

.. image:: images/addnewmenu_002.png


Usted vera el panel de Agregar* Colección *:

.. image:: images/addcollection.png


Debajo de los campos de titulo y descripción hay un grupo de campos para
especificar el formato de los resultados arrojados por las búsqueda de
criterios en la nueva Colección. Los cuatro campos en el panel de arriba
están en pares. Los primeros campos le permiten limitar los resultados de
búsqueda a un numero especifico de elementos a mostrar. Los dos últimos
campos le dejan controlar el orden de los elementos en los resultados de
búsqueda.


Configurando el criterio de búsqueda
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Después de establecer la configuración mostrada en el panel de arriba, haga
clic en la pestaña Criterio para que se muestre el panel de configuración de
Criterios de búsqueda:

.. image:: images/collectionssearchcrit1.png


La parte superior del panel *Agregar Nuevos Criterios de Búsqueda*, le
permite configurar un campo de palabras claves y un campo de criterios que
coincidan. La parte baja *Establecer Tipo de Ordenación*, es un campo de
selección sencilla para ordenar:

.. image:: images/collectionssearchcrit2.png


Para que los tipos de criterios coincidan con los datos en los elementos de
contenido, dependerá del campo seleccionado.

Después de guardar la Colección, los criterios de búsqueda serán aplicados y
los resultados mostrados cuando se haga clic en la Colección. Usted puede
crear cualquier numero de Colecciones para tales vistas predeterminadas. Para
el ejemplo de las mariposas descrito arriba, además de una restricción de
fechas para encontrar elementos recientes, el campo de categorías podría
usarse para que coincida con el color de una serie de Colecciones "Mariposas
azules", "Mariposas blancas", etc.

Múltiples criterios pueden ser usados para una Colección. Por ejemplo, una
Colección llamada "Mariposas fotografiadas en el ultimo mes", podría usarse
para configurar un criterio de Fecha de Creación y en el Tipo de Contenido
como Imagen. Estas Colecciones basadas en fechas son realmente efectivas para
mostrar las ultimas vistas de contenido que no requieren trabajo manual
administrativo -- Una vez que estas Colecciones hayan sido creadas,
automáticamente se mantendrán al día.

Nota: una Colección no se comporta como una carpeta regular -- usted no puede
agregar elementos de contenido a través del menú de agregar elemento, tal
como lo podría hacer en una carpeta regular.

`.. image:: images/lights-camera-action_003.png
    :alt: lights-camera-action.png
`_Ver un vídeo sobre como `anadir una smart folder (ahora llamada
Colección).`_ en Plone 2


5.3. Ajustando las opciones de vista
====================================

Aprenda como las configuraciones de vista pueden cambiar el aspecto de una
pagina de Colección.

Mientras que el poder principal de las Colecciones yace en los Criterios, las
opciones de vista pueden hacer una gran diferencia en la forma en que su
Colección se muestra. Las tres opciones que apuntaremos en esta sección se
pueden encontrar haciendo clic en la **pestaña Editar **de una Colección.

**Herencia de Criterios**

Confirmando la opción **Herencia de Criterios** , la colección "heredara" los
Criterios de una Colección padre. Esto solo es útil cuando se utilizan Sub-
Colecciones. Si esta opción es activada, usted puede crear otra Colección que
sea mas especifica que la "Padre" igualmente conservando sus criterios
básicos. Un ejemplo simple podría ser una Colección padre que muestre todos
los Eventos en un sitio, y una Sub-Colección que también muestre los Eventos
(por medio de Herencia de Criterios) *pero solo *aquellos eventos con una
palabra clave en particular.

**Limitar Resultados de Búsqueda
**Se puede usar la opción Limitar Resultados de Búsqueda para (como su nombre
lo indica) limitar el numero de resultados que una Colección mostrara *por
pagina*. De esta manera si se tiene una Colección que muestra Noticias, se
pueden limitar los resultados a cinco o diez, en vez de mostrar todos los
elementos en una sola y larga lista.

**Mostrar como Tabla**

Mostrar como Tabla es una manera sencilla de mostrar los resultados de una
Colección. En lugar de que una Colección arroje los resultados en forma de
una lista, se puede **generar una tabla **con ellos, y establecer exactamente
que información acerca de los resultados se quiere mostrar. Se puede
personalizar la tabla seleccionando las **Columnas de la Tabla** de la lista
en la izquierda y haciendo clic en el botón de flechas que apuntan a la
derecha para moverlas a la derecha. En el ejemplo de arriba escogimos el
Titulo del objeto, su Creador y la Fecha de Efectividad. Puede usar
cualquiera de las columnas o si quiere todas ellas.

Cuando consideremos que seleccionar, tome en cuenta que no todos los objetos
tendrán la información para cada campo de columna. Por ejemplo, la **Fecha de
Inicio** y la **Fecha de Finalización** solo se aplican a Eventos. Por lo
tanto, si usted agrega estas columnas y su tabla incluye Paginas así como
Eventos, las filas para Paginas no tendrán los campos de Fecha de Inicio y
Fecha de Finalización llenos. La otra cosa a considerar es que entre mas
columnas muestre mas las tablas se congestionaran. La mejor regla general se
trata de solo mostrar aquello que absolutamente necesite ser mostrado.

Otras observaciones para seleccionar columnas: puede seleccionar mas de una a
la vez, manteniendo pulsada la tecla Control (Ctrl) mientras que hace clic.
Si quiere remover una columna, seleccionela en la lista de la derecha y haga
clic en las flechas que apuntan a la izquierda. También puede anadir y
remover columnas haciendo doble-clic en sus respectivos nombres.


5.4. Definición de Criterios
============================

Definición y ejemplos de los diferentes criterios disponibles

El poder de las Colecciones ciertamente yace en los campos de Criterios.
Dominando el uso de los diferentes Criterios le permitirá usar las
Colecciones de varias maneras útiles. En esta sección, usaremos ejemplos para
demostrar las distintas formas de usar los Criterios.


**Categorías**
~~~~~~~~~~~~~~

El criterio de Categoría le permite buscar los **campos categóricos** de los
elementos. Para que esto funcione usted debe especificar las Categorías para
los elementos de contenido antes de esta acción (esto se hace a través de la
pestaña de Categorización en elementos de contenido). Un ejemplo en donde
podría usar esto es; si quiere un Colección que mostrase todos los elementos
relacionados a la Categoría *Organización*. Como puede ver en la imagen
posterior, usted puede seleccionar el valor *Organización * para su criterio.
Luego guardando los criterios y viendo su Colección, los resultados serán
todos aquellos elementos de contenidos diseñados bajo la Categoría
*Organización*.

Una vez mas, los valores disponibles para usted dependerán completamente en
lo que se haya especificado en la pestaña Categorización de cada uno de los
elementos.

**Creador**
~~~~~~~~~~~

****

Cuando use el criterio Creador, se estarán **filtrando los elementos basados
en quien los creo**. Esto puede ser útil si usted quiere crear una sección de
autor destacado, donde quisiera mostrar solamente contenidos en su sitio que
hayan sido creados por ciertos autores.

Como puede ver tenemos varias opciones para este tipo de criterio. Estas nos
permiten restringir el creador a la persona que actualmente inicio sesión,
ingrese el nombre de otro usuario como texto, o seleccione usuarios de una
lista.

Si desea que se muestren resultados de distintos usuarios, usted necesitaría
usar la opción **Lista de Valores**. De lo contrario normalmente necesitaría
usar la opción de texto a menos que el creador que quiere seleccionar sea
usted mismo, en este caso usaría la opción Restringir al Usuario Actual.

**
**


**Descripción**
~~~~~~~~~~~~~~~

El campo de Descripción es esencialmente un criterio **tipo cuadro de
búsqueda **. Sin embargo, en vez de buscar el titulo y contenido de una
pagina **solo buscara por el texto en el campo de Descripción** de una pagina
de contenido. Este criterio es solo realmente útil si usted consistentemente
llena el campo de Descripción para todos sus elementos de contenido.

**

**
**Ubicación**
~~~~~~~~~~~~~

El usar el criterio de Ubicación se asemeja bastante a cuando especifica una
ubicación al buscar un documento en su disco duro. Al especificar un criterio
de Ubicación **los resultados mostrados en su Colección solo provendrán de
esa ubicación**, generalmente una Carpeta. Esto puede ser útil si usted solo
quiere mostrar contenido que esta en la sección "Acerca de" en su sitio.
También sirve para limitar los resultados de la Colección combinados con
otros criterios.

Para especificar una Ubicación, simplemente haga clic en el **botón
Agregar**, el cual mostrara una nueva ventana emergente mostrándole un
directorio de su sitio. Si continuamos nuestro ejemplo y quiere buscar la
sección "Acerca de" en su sitio, haga clic en el botón Insertar al lado de la
carpeta Acerca de.

Usted puede abrir carpetas para observar el contenido dentro de ellas, ya sea
haciendo el clic en el botón buscar o directamente en el titulo de la carpeta
que quiera abrir. También puede usar el cuadro de búsqueda para buscar por el
Titulo de un elemento.**

**


**Texto de Búsqueda**
~~~~~~~~~~~~~~~~~~~~~

El criterio Texto de Búsqueda es bastante útil. Es similar al cuadro de
búsqueda de su sitio o a los motores de búsqueda de internet. Toma el texto
que usted especifico y busca por el Titulo, Descripción y Contenido de todos
los elementos y muestra **cualquiera que tenga la palabra o frase que usted
especifico**. Esto es beneficioso cuando usted quiere encontrar elementos que
tienen que lidiar con cierta cosa, especialmente si la palabra o frase
aparece en muchos contenidos. Al utilizar LearnPlone.Org como ejemplo, si se
quiere crear una Colección que muestre todos los elementos que hagan
referencia a la palabra Colecciones, se usaría el criterio Texto de Búsqueda
y se especificaría *colecciones*. Todos los tutoriales, vídeos, elementos de
Glosario, etc. Con la palabra *colecciones* en el Titulo, Descripción, o
Contenido aparecerían en los resultados de la Colección.


**Relativo A**
~~~~~~~~~~~~~~

El campo Relativo A es otro campo mas, que como el de Categoría **tiene que
ser especificado en el contenido del elemento antes de ser usado por la
Colección.**. El campo Relativo A sobre un elemento, le permite especificar
que otros elementos en su sitio son similares o relevantes con el elemento
que usted creo. Al especificar este campo, cuando se crea un objeto usted
puede crear una red de contenido relacionados que se referenciaran unos a
otros (piense en esto como una función "Ver también") Cuando usted haga esto,
puede usar el criterio Relativo A en una colección para mostrar cualquier
cosa relacionada a un objeto especifico.****

En este caso hemos especificado que hay paginas relacionadas a Nuestro
Personal, Historia, y pagina de Inicio de "Acerca de". Seleccionando uno o
varios valores de esta lista, nuestra Colección mostrara las paginas
relacionadas a ese Valor.

Si seleccionamos Historia como el valor que queremos, nuestra Colección nos
mostrara todo aquello relacionado a la pagina de Historia.

Tenga en cuenta que la lista de Relativo A no funciona sobre la base de que
objetos están relacionados al contenido, sino que un objeto tiene otro objeto
relacionado **a el**. La Colección mostrara los resultados que estén
relacionados a ese valor.**

**

**Estado**
~~~~~~~~~~

Usar el criterio Estado es muy sencillo. Le permite ordenar los resultados
por los Estados **Publico o Privado**. Es una buena idea restringir
Colecciones públicamente disponibles **usando el filtrado Publico**, para que
ningún contenido privado aparezca en los resultados de la Colección. Filtrar
a través del Estado Privado también es útil. Por ejemplo, un administrador de
un sitio quisiera ver rápidamente el contenido privado, para determinar en
que se tiene que trabajar y que se podría eliminar.

**Fechas**
~~~~~~~~~~

Usted puede notar que hay **distintas fechas disponibles** a ser usadas como
criterios. Puesto que hay un gran numero de fechas, estas serán estudiadas en
su propia sección del manual.


5.5. Estableciendo el Tipo de Ordenación
========================================

Aprenda a usar la característica Tipo de Ordenación para personalizar en que
orden los resultados aparecen

El Tipo de Ordenación **determina el orden de los resultados mostrados por
una Colección**.  El Tipo de Ordenación le permite ordenar por tres
categorías principales: texto, propiedades del elemento y fechas. Cuando
ordena por texto, los elementos serán ordenados en orden alfabético. Cuando
ordene por una de las propiedades del elemento, estas efectivamente se
agrupan bajo propiedades especificadas. Cuando ordenamos por una fecha los
resultados serán mostrados empezando por el mas reciente (aunque hay muchas
fechas en Plone). Todos los Tipos de Ordenación están en orden ascendente, a
menos que se seleccione la casilla de confirmación Invertir. Al seleccionar
esto podemos invertir el orden de visualización, o la fecha mas reciente
primero, etc.


**Fechas******
~~~~~~~~~~

Existen numerosas opciones de Fechas que serán explicadas en la siguiente
sección del manual.




Propiedades del Objeto
~~~~~~~~~~~~~~~~~~~~~~

**Tipo de Elemento**

Cuando ordenamos por el Tipo de Elemento, obtenemos una Colección que arroja
resultados agrupados por el Tipo de Elemento. Esto se utiliza si se quiere
tener una Colección que muestre resultados con Tipos de Elementos diferentes.
De esta manera podemos hacer una Colección bastante sencilla de usar para el
visitante del sitio.

**Estado**

La Ordenación por Estado arrojara resultados agrupados por el Estado de
Publicación. Dado que solo hay solo dos tipos de Estado en la configuración
por defecto de Plone, solo habrá elementos Privados y Publicados. Se puede
usar esto para separar todas las paginas y simplemente ver que tenemos para
el publico (Publicado). Y a su vez que escondemos del ojo publico (Privado).

**Categoría**

La ordenación por Categoría es provechosa cuando se quiere mostrar elementos
agrupados por las Categorías en la que están localizados. Recuerde que, para
que la ordenación sea remotamente útil, usted debió haber especificado las
Categorías para los elementos. Si usted no especifico ninguna Categoría, la
ordenación hará absolutamente nada.

**Relativo A**

El orden por Relativo A se aplica realmente a un Criterio de su Colección.
Limita los resultados a aquellos que poseen una Información Relativo A
especificada en las propiedades.


Texto
~~~~~

**Nombre Corto**

La ordenación por Nombre Corto es lo mismo que poner los resultados en orden
alfabético. Por defecto Plone establece que el Nombre Corto de un elemento
sea el mismo que el Titulo. La diferencia entre estos dos en que el Nombre
Corto esta todo minúscula y con guiones en vez de espacios. Por ejemplo el
Nombre Corto para la pagina About Us (Acerca de) seria *about-us (acerca-
de)*. El Nombre Corto es lo que Plone utiliza en las direcciones URL para las
paginas (www.myplonesite.org/about-us). Usted puede establecer un Nombre
Corto distinto para un elemento usando el botón Renombrar en la pestaña de
Contenido.


**Creador**

La ordenación por Creador agrupara todos los resultados en orden alfabético
por autor. Por ejemplo, digamos que tenemos varios documentos publicados por
Bob Baker y otros publicados por Jane Smith. El orden por Creador arrojara
los resultados de todos los documentos creados por Bob Baker en primer lugar
y luego aquellos creados por Jane Smith.

**Titulo**

El ordenamiento por Titulo mostrara los resultados por el orden alfabético
de los Títulos.


A continuación estudiaremos las Fechas que hemos saltado en esta sección, así
como la sección de Criterios.


5.6. Uso y Comprensión de Fechas
================================

Explicación de Fechas asociadas con las Colecciones y sus respectivos usos.

Existen distintos tipos de Fechas disponibles entre las cuales podemos
escoger, muchas de ellas pueden parecer similares. Por esta razón es muy
fácil confundirse en relación a cual Fecha usar. Abajo, cada Fecha esta
definida.



Definición de Fechas
--------------------

**Fecha de Creación**
La Fecha de Creación es aquella cuando el documento fue hecho. Puede pensar
en ella como la fecha de cumpleaños o el día de nacimiento; esta fecha no se
puede cambiar.

**Fecha de Efectividad**
La Fecha de Efectividad es aquella cuando el elemento es publicado. Esta
fecha se puede cambiar a través de la **pestaña Editar** de los elementos
bajo la **pestaña Fechas **. Sin embargo ahí se encuentra referida como Fecha
de Publicación (una discrepancia menor en la nomenclatura de Plone).

La **Fecha de Creación** y la **Fecha de Efectividad** son muy similares, ya
que ambas representan el punto de inicio de un elemento. Un punto importante
que tiene recordar al escoger cual quiere usar, es que un elemento puede ser
creado mucho antes de ser publicado. Usted puede tener una pagina que haya
sido trabajada durante varias semanas antes de ser Publicada. De esta manera
se obtienen resultados distintos en una Colección dependiendo de que Fecha
quiera usar.

Se recomienda usar **Fecha de Efectividad** en vez de Fecha de Creación para
aquellas Colecciones orientadas a fechas. Así la Colección le muestra
resultados basados en cuando se volvieron disponibles para el publico, lo
cual es mas relevante para la audiencia de su Colección. Además manualmente
se puede cambiar la Fecha de Efectividad para controlar el orden de
ordenación, cosa que no se puede hacer con la Fecha de Creación.
**
Fecha de Caducidad**
La Fecha de Caducidad se refiere al día en que el elemento dejara de estar
disponible para el publico. Esta fecha también es personalizable a través de
la pestaña Editar (como se muestra arriba), al igual que la Fecha de
Efectividad. Por defecto los elementos no tienen Fecha de Caducidad.
**
Fecha de Modificación**
La Fecha de Modificación es la fecha en que el objeto fue editado por ultima
vez. Note que esta fecha es primero establecida de acuerdo al día en que fue
creado el elemento, y cambiara automáticamente cada vez que el elemento sea
editado. Esta fecha no se puede personalizar de ninguna manera. Usted podría,
por ejemplo, usarla como Tipo de Ordenación junto al Criterio Tipo de
Elemento configurada a una Pagina, para obtener todas las modificaciones
hechas en Paginas en la ultima semana. La lista de What's New (Que hay de
nuevo) en la pagina de inicio de LearnPlone.Org usa la Fecha de Modificación
como el Criterio de Fecha. De esta manera los nuevos documentos creados *y*
aquellos que han sido actualizados aparecerán listados.



**Fechas especificas de Eventos
**Las siguientes dos Fechas **solo **se aplican a aquellos elementos que
son** Eventos. **Estas dos Fechas son muy efectivas para crear Colecciones de
Eventos recientes y Eventos próximos que le permitirán a su audiencia saber
que esta haciendo su organización actualmente y que hará en el futuro.

**Fecha de Inicio**
La Fecha de Inicio es simplemente la fecha cuando el Evento empieza.

**Fecha de Finalización**
La Fecha de Finalización es simplemente la fecha cuando el Evento termina.


Configurando Fechas
-------------------

Algo que puede ser confuso en relación a las Fechas es como se establecen sus
Criterios, ellas tienen una configuración que no se parece a ninguno de los
otros paneles de Criterios. Primero tiene que escoger si desea usar un
Relative Date (Fecha Relativa) o un Date Range (Rango de Fechas).

La Fecha Relativa le permite construir una **sentencia condicional**. Tal
como: elementos modificados en los últimos de 5 días. Un Rango de Fechas le
permite **un rango de fechas exacto**, tal como: del 01/02/08 al 02/02/08. El
Rango de Fechas es útil cuando quiera crear un Colección con fechas estáticas
que no cambien. La Fecha Relativa es beneficiosa ya que le permitirá crear
Colecciones que se actualicen automáticamente, tales como: Colecciones de
Noticias recientes o una sección con Eventos próximos.


Relative Date (Fecha Relativa)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Al mirar la opción de Fecha Relativa usted puede ver que hay tres opciones
para llenar.

El primer menú se denomina **Que día**. Esto le permite seleccionar el numero
de días incluidos en nuestro Criterio. Una de las opciones en este menú se
denomina *Ahora*. Esta establecerá el rango de fechas al día actual. Si usa
la opción *Ahora* los otros dos menús no serán importantes.

El segundo menú tiene dos opciones **en el pasado o en el futuro**. Esto
permite saber si se tiene que mirar al pasado o al futuro.



El ultimo menú muestra **Mas que o Menor que**. De aquí podemos escoger entre
tres opciones. *Menor que* permite incluir todo aquello dentro de un periodo
de tiempo igual o menor a los días configurados en el menú **Que día **, ya
sea en el pasado o en el futuro. *Mas que* permite incluir todo aquello que
se encuentre igual o mas alla del numero especificado de días en el menú
**Que día**. Finalmente *En el día *solo incluye todo aquello que se
encuentre en el día especificado en el menú **Que día**. Si se toma el
ejemplo de la imagen de arriba y se hubiese seleccionado *En el día* en vez
de *Menor que* nuestra colección mostrara elementos que hayan sido
modificados exactamente 5 días antes (Se esta utilizando el Criterio de Fecha
de Modificación).

Si esto resulta confuso para usted, trate de leerlo de la siguiente manera;
substituyendo las opciones que usted escoja en los campos. "Quiero que los
resultados incluyan los elementos **Mas o Menor** que **Que día**, **En el
pasado o futuro**". El ejemplo en la imagen de arriba se transformaría en
esta frase "Quiero que los resultados incluyan los elementos **Menor que**
**5 días en el pasado**".



Date Range (Rango de Fechas)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El **Rango de Fechas** es mucho mas fácil de entender. Las Fechas de Inicio y
Finalización son requeridas (¡No confunda estos términos con las Fechas
especificas de Eventos!) El Rango de Fechas le permite entrar dentro de un
periodo con inicio y fin y mostrar todo el contenido dentro de este plazo.
Note que también le permite establecer horas especificas de los días.


