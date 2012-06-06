.. -*- coding: utf-8 -*-

.. highlight:: rest

.. _deliverance_configuracion:

=============
Configuración
=============

Para aplicar las reglas con ``Deliverance`` debemos hacerlo en el archivo ``rules.xml`` 
y esto consiste en configurar el puerto que servirá como fuente de contenido, y el puerto 
donde se verán los cambios y el efecto de las reglas de Deliverance. Para aplicar las reglas 
hay que seleccionar la ruta y crear una clase.
  
.. code-block:: xml

    <proxy path="/" class="plone">

    <!--Luego llamar a la clase, indicarle la ruta del tema y aplicar las reglas-->

    <rule class="plone" suppress-standard="1">

    <!-- Tema -->

    <theme href="/static/index.html" />


.. tip::
    Por defecto el servicio ``Deliverance`` viene configurado para salir por el 
    puerto ``5000`` pero puede ser cambiado por cualquiera de su preferencia.


Bajo este formato se configuran los proxys, para indicar donde esta la fuente de contenido 
y en que puerto serán visualizados los cambios con deliverance.

.. code-block:: xml

    <proxy path="/" class="plone">

    <dest href="http://localhost:8080/VirtualHostBase/http/localhost:5000/Plone/VirtualHostRoot/" />

    </proxy>

Esta configuración previa indica que la fuente de contenido ``Plone`` se publica por 
el puerto ``8080`` http://localhost:8080 y los cambios en el ``Deliverance`` serán 
vistos por el puerto ``5000`` http://localhost:5000

.. tip::
    Para más información sobre configuración de los Proxy revisar esta documentación:
    http://plone.org/documentation/kb/plone-apache/vhm


Para configurar Deliverance con Plone 
=====================================

El archivo de reglas debe ir así:

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <ruleset>

    <server-settings>
    <server>localhost:5000</server>
    <execute-pyref>true</execute-pyref>
    <dev-allow>localhost</dev-allow>
    <dev-user username="guest" password="guest" />
    </server-settings>

    <proxy path="/static" class="static" editable="1">
    <dest href="{here}/static/" />
    </proxy>
  
    <proxy path="/banjo" class="banjo">
      <dest href="{here}/src/banjo/" />
    </proxy>
  
    <proxy path="/" class="plone">
    <dest href="http://localhost:8080/VirtualHostBase/http/localhost:5000/Plone/VirtualHostRoot/" />
    </proxy>
  
    <rule class="static" />
      
    <rule class="banjo" />
  
    <rule class="plone" suppress-standard="1">
    
    
    <!-- Theme -->
    <theme href="/static/index.html" />

    <!-- Rules -->
    
    <replace content='/html/head/title' theme='/html/head/title' />
    <append content='/html/head/base' theme='children:/html/head' />
    
    <append content="link[href *= 'authoring']" theme='children:/html/head' />
    <append content="link[href *= 'portlets']" theme='children:/html/head' />
        
    <!-- Add in the Plone-created CSS and JS in addition to the static ones -->
    <append content='/html/head/script' theme='/html/head' />
    <!--><append  content='/html/head/style' theme='/html/head' /> -->

    <!-- Append the id/class attributes from the body tag, this is important for Kupu and per-section styling -->
    <append content="attributes(id,class):/html/body" theme="attributes:/html/body" />

    <!-- Copy the logo -->
    <replace content='#portal-logo img' theme='#logo h1' />

    <!-- Copy the breadcrumbs -->
    <!-- <replace content='#portal-breadcrumbs' theme='#pathbar' />
    <replace content='#portal-personaltools' theme='#personaltools' /> -->
 
    
    <!-- Copy the main navigation -->
    <replace content='children:#portal-globalnav' theme='children:#links ul' /> 


    <!-- <prepend content='dl.portletLogin' theme='children:#rightbar' /> -->

    <!-- <replace content='children:#parent-fieldname-title' theme='children:#leftbar h2' /> -->
    <!-- Get rid of the user icon and copy the user link -->
    <drop content='#user-name img' /> 
    <replace content='#user-name' theme='#user a' />

    <!-- Copy the edit bar -->
    <replace content='#content-views' theme='children:#edit-menu' />
    <replace content='div.contentActions' theme='children:#action-menu' />
    
    <!-- …but get rid of the content type icons. -->
    <drop content='#plone-contentmenu-factories dd ul li a img' /> 

    <!-- <drop content='#link-presentation' />
    <drop content='div.documentActions' />
    <drop content='div.documentByLine' />
    <drop content='span.documentByLine' />
    <drop content='#review-history' />
    <drop content="attributes(class):a.external-link" />
    <drop content="attributes(class):a.plain-link" /> -->
    
    <!-- Copy over the contents of the page body -->
    <!-- <replace content='children:#content' theme='children:#leftbar' /> -->

    <!-- put the title of the page as the heading -->
    <replace content='children:#parent-fieldname-title' theme='children:#heading' />

    <!-- remove the history dropdown -->
    <drop content='dl#history' />
    
    <!-- put the documentDescription in the first paragraph -->
    <replace content='children:#parent-fieldname-description' theme='children:#description' />
    <!-- we keep the documentDescription class so we can do some styling later -->
    
    <!-- put the body text in the second paragraph -->
    <replace content='children:#parent-fieldname-text' theme='children:#bodytext' />
    
    <!-- drop the more link at the bottom -->
     <drop theme='/html/body/div/div/div[3]/div/a' />
    
    <!-- for news listing page -->
    <drop content='div.documentByLine' />
    <drop content='attributes(class):h2.tileHeadline a' />
    <drop content='attributes(class):h2.tileHeadline' />
    <replace content='children:div.tileItem' theme='//*[@id="leftbar"]/p[2]' />
    
    <!-- for event listing page -->
    <!-- <replace content='/html/body/div/table/tbody/tr/td/div/div[2]/div[2]/div/dl/dt/span/a' theme='//*[@id="leftbar"]/p[2]' /> -->
    <!-- <replace content='span.contenttype-event' theme='//*[@id="leftbar"]/p[2]' /> -->

    <!-- <replace content='/html/body/div/table/tbody/tr/td/div/div[2]/div[2]/div/dl' theme='//*[@id="leftbar"]/p[2]' /> -->
    
    <!-- stuff to remove from portlet -->
    <drop content='dd.portletItem a img' /> 
    <drop content='span.portletItemDetails' /> 

    <!-- <replace content='children:.portletNews span.portletItemDetails' theme='children:span.orangetext' /> -->

    <!-- <replace ifcontent='body.section-events' content='children:dl.portletNews dt.portletHeader a' theme='children:#rightbar h2' />
    <replace ifcontent='body.section-events' content='children:dl.portletNews dd.portletItem' theme='children:#rightbar p' />    

    <replace ifcontent='body.section-news' content='children:dl.portletEvents dt.portletHeader a' theme='children:#rightbar h2' />
    <replace ifcontent='body.section-news' content='children:dl.portletEvents dd.portletItem' theme='children:#rightbar p' />     -->
        
    <!-- Bring the portlet columns inside the sidebar -->
    <!-- <append content='#portal-column-one'  theme='#rightbar' />
    <append content='#portal-column-two'  theme='#rightbar' /> -->

    </rule>
    </ruleset>


Configurar Deliverance con archivos HTML locales 
================================================

Ideal para cuando no se cuenta con conexión a Internet o no se tiene 
acceso directo a la fuente de contenido, con esta configuración 
la fuente de contenido será una pagina ``HTML`` previamente guardada y 
colocada dentro de la carpeta correspondiente.

Para este caso se crea un Proxy con una clase y se le indica la dirección 
donde se encontrara el ``HTML``, para este ejemplo dentro del directorio raíz 
del proyecto se creo una carpeta llamada ``local``:

.. code-block:: xml

    <proxy path="/" class="plone" rewrite-links="1">
    <dest href="{here}/local/" />
    </proxy>

El archivo de reglas por consiguiente queda de esta manera

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <ruleset>
    <server-settings>
    <server>localhost:5000</server>
    <execute-pyref>true</execute-pyref>
    <dev-allow>localhost</dev-allow>
    <dev-user username="guest" password="guest" />
    </server-settings>

    <proxy path="/static" class="static" editable="1">
    <dest href="{here}/static/" />
    </proxy>

    <proxy path="/" class="plone" rewrite-links="1">
    <dest href="{here}/local/" />
    </proxy>

    <rule class="static" />
    <rule class="plone" suppress-standard="1">

    <!-- Tema -->

    <theme href="/static/local_pagina_inicio/index.html" />

    <!--Reglas-->
    
    </rule>
    </ruleset>

