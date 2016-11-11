Visualizando los tweets durante el fin de semana de las elecciones
==================================================================

:date: 2015-12-10 09:30
:modified: 2015-12-15 18:04
:slug: visualizing-tweets
:tags: data, tweets, twitter, elections, visualize, folium, python, matplotlib, pylab
:author: Luis Alberto Santana
:status: draft
:lang: es


El domingo 6 de diciembre se realizaron las elecciones parlamentarias en Venezuela. Utilicé esta oportunidad para obtener algunos datos del stream público de Twitter y usar gráficos para mostrar qué estaba pasando en las "`redes sociales`' ese día. Para esto, usé Python como lenguaje de programación.


`Los datos`_
-------------

Decidí enfocarme en los tweets georeferenciados de mi ciudad (Caracas) durante un periodo de cinco días, dos días antes de las elecciones, el día de las elecciones, y dos días después.

Para obtener los datos, utilicé `Twython`_, una biblioteca con la que ya tenía experiencia, por lo tanto sería sencillo escribir un script que permitiera obtener los datos y guardarlos en un archivo de texto.

Una vez que se han configurado las claves de `API` y `OAUTH` siguiendo la `documentación de Twython`_, el próximo paso es obtener los datos que se originan en cierta ubicación, pasándole las coordenadas de la ubicación al API de streaming. Twitter usa un conjunto de límites para delimintar la ubicación de un tweet, sólo envía tweets dentro de esos límites.


.. code:: python

    import json, os
    from twython import TwythonStreamer

    caracas_location = "-67.017225,10.419554,-66.778716,10.52006"

    class MyStreamer(TwythonStreamer):
        def on_success(self, data):
            if data['coordinates'] is not None:
                with open('tweets.txt', 'a') as f:
                    f.write(json.dumps(data))
                    f.write('\n')

        def on_error(self, status_code, data):
            with open('errors.txt', 'a') as f:
                f.write('error: {0}: {1}'.format(status_code, data))



    stream = MyStreamer(os.environ['APP_KEY'], os.environ['APP_SECRET'],
                            os.environ['OAUTH_TOKEN'], os.environ['OAUTH_TOKEN_SECRET'])

    stream.statuses.filter(locations=caracas_location)



Como solamente quería obtener tweets georeferenciados, verifiqué cada tweet buscando la existencia del atributo `coordinates`, y sólo almacené tweets con datos de geolocalización (lat/long). Luego de ejecutar el script durante algunos días, contaba con ~50.000 tweets para empezar a jugar.



`Visualizando los Datos`_
--------------------------

`¿Dónde estaban ubicados esos tweets?`_
+++++++++++++++++++++++++++++++++++++++

Lo primero que quería hacer con los datos era ver dónde se originaban los tweets durante ese periodo. Decidí usar un `heatmap`_ sobre un mapa de la ciudad. Utilicé la versión en desarrollo de `Folium`_, que implementa mapas en Python basados en `Leafleat.js` y sus plugins.

.. image:: {filename}/images/heatmap.jpeg
    :height: 450px
    :width: 750 px
    :alt: Heatmap
    :align: center

Haz click aquí para ver la `versión completa <{filename}/files/heatmap.html>`_ e interactiva del heatmap (**advertencia** archivo pesado!)
    
El código usado para generar el mapa, una vez se cargaron los datos en una lista llamada `data` es tan simple como:

- Crear un mapa centrado en Caracas (`10.497084, -66.8854171`).
- Agregar cada punto de dato en el mapa usando el método `add_children`.
- Escribir el archivo HTML.


.. code:: python
    
    import folium
    from folium import plugins

    # Create a heatmap with the data.
    heatmap_map = folium.Map(location=[10.497084, -66.8854171], zoom_start=12)
    heatmap_map.add_children(plugins.HeatMap([[t[1], t[0]] for t in [tweet["coordinates"]["coordinates"] for tweet in data]]))
    heatmap_map.save("heatmap.html")


**NOTE**: Las coordenadas de Twitter vienen en formato `geoJSON`, esto es: longitud primero, y luego latitud. El código las intercambia para agregar puntos de `(lat, long`) al mapa.


En el `heatmap`, se pueden ver los parques y áreas protegidas en Caracas, las cuales no tuvieron ningún tipo de actividad. De igual manera, se puede ver que hay mucha menos actividad en `Caricuao`_ que en el resto de la ciudad. Esto es interesante, dado que Caricuao una zona residencial bastante extensa.


`¿Cómo se ve la actividad?`_
++++++++++++++++++++++++++++

So, there's a heatmap of the location of the tweets, but how can we represent the activity over the five days?

I thought that a calendar type chart, such as the one that shows the contributions activity on `Github's`_ profiles, was an interesting way to represent the data visually. Grouping the tweets by day and hours in cells, and increasing the intensity of the cell depending on the total amount of tweets during that moment.

To achieve this, I decided to use `matplotlib`_ as the plotting library, insted of using a Javascript based library such as `D3.js`.


.. code:: python
    
    import matplotlib
    import matplotlib.pyplot as plt
    from matplotlib.ticker import FuncFormatter, MaxNLocator

    import numpy as np

    #
    # Load the dataset into a nested list with the `Date` and the `hour` data
    # 

    fig, ax = plt.subplots(figsize=(10, 4))
    image = np.array(data_array)
    cax = ax.imshow(image, cmap=plt.cm.magma, interpolation='nearest')

    #
    # Add some parameters for the ticks
    #

    # Add colorbar/legend
    cbar = fig.colorbar(cax, orientation='horizontal')

    plt.subplots_adjust(wspace=5, hspace=5)
    plt.savefig("tweet_frequency_heatmap.png")


With some visual adjustments such as adding labels to the ticks, I've got the graphic I wanted.


.. image:: {filename}/images/tweet_frequency_heatmap.png
    :height: 320px
    :width: 800px
    :alt: Tweets by hour
    :align: center

**NOTE**: The lack of tweets during the morning of December 4, is due the absence of data in that period.


As expected, after midnight, when most people are sleeping, the amount of tweets is very close to zero in normal days (Dec 04, Dec 05, Dec 08). On the election day, the graph shows above "normal" activity, and we can see the exact moment when the results of the election were announced on national TV. Between 12 a.m and 2 a.m. of Dec. 07 the amount of tweets in Caracas duplicated.



**Pronto publicaré nuevos gráficos**


`Herramientas`_
----------------

Usé este pequeño proyecto para investigar y aprender lo básico de las herramientas disponibles para representar datos visualmente (gráficos, mapas, etc.) algunas de las herramientas que probé fueron:


- `Matplotlib`_
- `Folium`_
- `mplleaflet`_
- `Plotly`_
- `leaflet.js`_

En el wiki de Python se puede conseguir una `lista muy completa`_ de bibliotecas y recursos para visualizar datos.


.. _`Twython`: https://pypi.python.org/pypi/twython/ 
.. _`documentación de Twython`: http://twython.readthedocs.org/en/latest/usage/starting_out.html
.. _`heatmap`: https://en.wikipedia.org/wiki/Heat_map

.. _`Caricuao`: https://en.wikipedia.org/wiki/Caricuao


.. _`D3.js`: http://d3js.org

.. _`Plotly`: https://plot.ly/
.. _`mplleaflet`: https://pypi.python.org/pypi/mplleaflet/0.0.5
.. _`Matplotlib`: http://matplotlib.org
.. _`Folium`: http://folium.readthedocs.org/en/latest/
.. _`leaflet.js`: http://leafletjs.com
.. _`lista muy completa`: https://wiki.python.org/moin/NumericAndScientific/Plotting

.. _`Github's`: https://github.com
