# 🔹 Sesión 7

En esta sesión trabajaremos con la _visualización de datos espaciales interactivos_ utilizando la biblioteca **Folium**. Aprenderás a crear mapas dinámicos con capacidades de interacción, y a personalizar su estilo y contenido visual.

Los mapas interactivos son ideales cuando se desea:

- Explorar información geoespacial de forma intuitiva.

- Permitir a la persona usuaria desplazarse, acercar/alejar, hacer clic en objetos.

- Compartir resultados fácilmente en web o notebooks.

#### ¿Por qué mapas interactivos?

A diferencia de los mapas estáticos (como los que creamos con `matplotlib` o `geopandas.plot()`), los mapas interactivos permiten:

- Ver informacion adicional al hacer clic _(pop ups)_
- Encender y apagar capas
- Explorar diferentes niveles de zoom
- Integrarse fácilmente en notebooks o páginas web.

```{admonition} Otras bibliotecas para mapas interactivos
:class: tip

Además de **Folium**, existen otras bibliotecas en Python para crear mapas dinámicos:

- 🌍 [Leaflet.js](https://leafletjs.com/): base en JavaScript, utilizada internamente por Folium.
- 🧭 [OpenLayers](https://openlayers.org/): potente y flexible, ideal para desarrollos web avanzados.
- 📊 [Plotly Express](https://plotly.com/python/maps/): mapas integrados en visualizaciones estadísticas.
- 📈 [Bokeh](https://docs.bokeh.org/en/latest/): mapas como parte de dashboards y gráficos interactivos.
- 🌐 [Geoviews](https://geoviews.org/): integración con HoloViews, excelente para análisis exploratorio.
```

## ¿Qué es Folium?

![](../source/images/folium.png)

Folium es una biblioteca de **Python** que permite crear mapas interactivos basados en [Leaflet.js](https://leafletjs.com/). Tiene una sintaxis sencilla y permite integrar fácilmente datos espaciales con estilo personalizado, marcadores, capas y controles interactivos.

Puedes checar la documentación oficial de [Folium](https://python-visualization.github.io/folium/latest/getting_started.html)

## Datos

Trabajaremos con los datos que anteriormente habíamos corregido en la sesión de `geocodificación` [(Sesión 4)](../source/modulo4.md).

Formato: `KML`

[![Descargar datos](https://img.shields.io/badge/descargar-datos-blue)](../source/data/direcciones-corregidas.kml)

También utilizaremos el conjunto de datos de Información Sociodemográfica por colonia, Jalisco 2020. Colonias INE 2024 (Colonias Enteras) proveniente del [Instituto de Información Estadística y Geográfica de Jalisco (IIEG)](https://iieg.gob.mx/ns/?page_id=881).

Formato: `GeoJson`

[![Descargar datos](https://img.shields.io/badge/descargar-datos-purple)](../source/data/colonias.geojson)

Finalmente, trabajaremos con datos provenientes de [GPWv4 (Gridded Population of the World)](https://daac.ornl.gov/cgi-bin/dsviewer.pl?ds_id=975) y un recorte de una capa proveniente de [Natural Earth](https://www.naturalearthdata.com/downloads/110m-cultural-vectors/). Sin embargo, este archivo que te comparto trabajado y listo para descargarlo directamente:

Formato: `TIF`

[![Descargar datos](https://img.shields.io/badge/descargar-datos-orange)](../source/data/poblacion_mexico_1995.tif)

## Contenidos de esta sesión

En esta sesión estaremos trabajando con este cuaderno de trabajo:

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/patymunoz/curso-geoespacial/blob/main/notebooks/sesion7.ipynb)

## Ejercicio práctico

```{admonition} Manos a la obra
i. Entra al portal [GEMA](https://gema.conahcyt.mx/visualizador?capas=#map=4/23.6254/-89.1034).

ii. Explora el porta y descarga un conjunto de datos de tu interés en formato `.geojson`.

iii. Este conjunto de datos debe contar con variables que en geometría de puntos, líneas o polígonos.

iv. Genera un mapa interactivo y preséntalo a la clase 🤓.
```
