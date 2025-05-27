# 🔹 Sesión 4

En esta sesión exploraremos el concepto de **geocodificación** _(geocoding)_, que consiste en transformar nombres de lugares o direcciones específicas en coordenadas geográficas (latitud y longitud). Este proceso es fundamental para vincular datos espaciales con ubicaciones reales en un mapa.

Cabe mencionar que también estaremos trabajando dos temas en paralelo: _Spatial joins_ y _Análisis de vecinos más cercanos_.

## Geocodificación en Python 🐍

En el ecosistema Python, algunas de las bibliotecas más utilizadas para realizar geocodificación son **GeoPy** y **Geocoder**. Ambas permiten convertir direcciones, ciudades o países en coordenadas geográficas mediante servicios web conocidos como **geocoders.**

Entre los geocoders más conocidos se encuentran:

```{admonition} Geocoders
:class: tip

- [Google Geocoding API](https://developers.google.com/maps/documentation/geocoding/overview?hl=es-419)
- [Nominatim](https://nominatim.openstreetmap.org/ui/search.html)
- [HERE Geocoder REST API](https://www.here.com/platform/geocoding)
- [Mapbox Geocoding API](https://docs.mapbox.com/api/search/geocoding/)
- [ArcGIS World Geocoding Service](https://www.arcgis.com/home/item.html?id=305f2e55e67f4389bef269669fc2e284)
- [Bing Maps Locations API](https://learn.microsoft.com/en-us/bingmaps/rest-services/locations/)
- [Carto](https://carto.com/geocoding)

```

![Geocoders](../source/images/geocoders.png)

**Figura 1.** Ejemplos de servicios que proveen servicios de geocodificación. Elaboración propia.

Actualmente existe una amplia variedad de servicios de geocodificación. Las principales diferencias entre ellos —además del modelo de precios— radican en la calidad y cobertura de sus datos. Por ejemplo, una dirección puede estar correctamente registrada en Google Maps pero no en Bing o Carto, y viceversa.

#### Consideraciones técnicas

La mayoría de estos servicios requieren una API key para su uso, lo que implica que debes registrarte en sus plataformas para obtener acceso. Además, suelen establecer límites de uso, como un número máximo de peticiones por segundo o por día, lo cual es importante tener en cuenta para evitar errores o bloqueos al procesar grandes volúmenes de datos.

Para más información sobre el uso de geopy con pandas, puedes consultar su [documentación oficial](https://geopy.readthedocs.io/en/stable/#usage-with-pandas).

## Uso de Nominatim (OpenStreetMaps)

En esta sesión utilizaremos el servicio _Nominatim_, proporcionado por OpenStreetMap. Este geocodificador es gratuito y no requiere de una API key, aunque sí impone restricciones en la frecuencia de peticiones: **solo se permite una petición por segundo.** Puedes revisar las políticas de uso en [este enlace](https://operations.osmfoundation.org/policies/nominatim/).

```{admonition} Batch Geocoding

Ten en cuenta que el envío masivo de solicitudes o la repetición frecuente de la misma consulta puede considerarse uso indebido, lo que podría conllevar al bloqueo del acceso al servicio.
```

Una consideración importante al utilizar _Nominatim_ es el uso del parámetro `user_agent`. Este parámetro es **obligatorio** y se utiliza para identificarnos ante el servicio, indicando quién está realizando las peticiones.

![](../source/images/nominatim.png)

**Figura 2.** Documentación de _Nominatim_ vía [GeoPy](https://geopy.readthedocs.io/en/stable/#nominatim).

## Spatial Joins (Uniones espaciales)

Un _spatial join_ es una operación espacial fundamental en análisis geoespacial. Consiste en combinar atributos de dos capas espaciales en función de su relación espacial, como si un objeto de una capa _"intersecta"_, _"está dentro de"_ o _"contiene"_ a un objeto de otra capa. Esta operación es muy útil cuando necesitamos enriquecer una capa con información proveniente de otra, basándonos en su ubicación geográfica.

Por ejemplo, podríamos querer unir una capa de puntos (como estaciones meteorológicas) con una capa de polígonos (como regiones administrativas), para asignar a cada punto los atributos del polígono en el que se encuentra.

[**GeoPandas**](https://geopandas.org/en/stable/docs/reference/api/geopandas.sjoin.html) facilita este proceso mediante la función `gpd.sjoin()`, que permite realizar un spatial join. Esta función admite diferentes tipos de relaciones espaciales definidas mediante el parámetro `predicate`:

```{admonition} Tipos de relaciones espaciales
:class_tip
- **intersects**: selecciona elementos que se cruzan o tocan espacialmente.
- **within**: selecciona elementos que están completamente contenidos dentro del otro.
- **contains**: selecciona elementos que contienen completamente al otro.

- **touches**: selecciona elementos que tocan el borde del otro.
- **crosses**: selecciona elementos que cruzan el otro, es decir, comparten parte de su geometría pero no están completamente contenidos.
- **overlaps**: selecciona elementos que se superponen parcialmente, es decir, comparten parte de su geometría pero no están completamente contenidos ni contienen al otro.
```

![](../source/images/spatial-joins.png)

![](../source/images/spatial-joins2.png)

**Figura 3.** Tipos de relaciones espaciales. Imágenes extraídas de [PyGIS](https://pygis.io/docs/e_spatial_joins.html#spatial-join-relationships), bajo licencia CC BY-NC-SA 4.0.

Además, puedes especificar el tipo de unión que deseas mediante el parámetro `how`:

```{admonition} Tipos de uniones
:class: tip
- **left**:  conserva todos los elementos de la capa izquierda (primera).
- **right**: conserva todos los elementos de la capa derecha (segunda).
- **inner**: conserva solo los elementos que tienen coincidencias en ambas capas.
```

![](../source/images/join_types.jpg)

**Figura 4.** Tipos de uniones. Imágenes extraídas de [PyGIS](https://pygis.io/docs/e_spatial_joins.html#spatial-join-types), bajo licencia CC BY-NC-SA 4.0.

Este es un ejemplo de uso tanto del parámetro `how` como del parámetro `predicate`:

```python
gpd.sjoin(puntos, regiones, how="left", predicate="within")
```

## Análisis de vecinos más cercanos

Una tarea común el análisis espacial consiste en identificar el objeto más cercano a otro dentro de un conjunto de datos. Por ejemplo, podrías tener un punto que representa tu casa, y una colección de ubicaciones que representan _restaurantes_. En ese caso, una pregunta frecuente sería: “¿Cuál es el restaurante más cercano a mi casa?”. Este tipo de análisis se conoce como _búsqueda del vecino más próximo_, y su objetivo es encontrar la geometría más cercana a una geometría dada.

En Python, este análisis puede realizarse utilizando la función `nearest_points()` de la biblioteca Shapely, la cual devuelve una tupla con los puntos más cercanos entre las geometrías proporcionadas.

## Datos

Para esta sesión, utilizaremos un conjunto de datos en formato `.txt`.

[![Descargar datos](https://img.shields.io/badge/descargar-datos-purple)](../source/data/direcciones.txt)

ambién utilizaremos un conjunto de datos del Instituto Nacional de Estadística y Geografía (INEGI) de México, que contiene información geoespacial sobre el [Marco Geoestadístico de México](https://www.inegi.org.mx/temas/mg/). Se ha filtrado solamente a Jalisco y los municipios correspondientes al Área Metropolitana de Guadalajara (AMG): Este conjunto de datos está disponible en formato `shapefile`:

[![Descargar datos](https://img.shields.io/badge/descargar-datos-blue)](../source/data/metropolitana.zip)

Y, finalmente capa de Colonias de Jalisco proveniente del [Instituto de Información Estadística y Geográfica de Jalisco (IIEG)](https://iieg.gob.mx/ns/?page_id=881):

[![Descargar datos](https://img.shields.io/badge/descargar-datos-yellow)](../source/data/colonias_iieg.zip)

## Contenidos de esta sesión

En esta sesión estaremos trabajando con este cuaderno de trabajo:

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/patymunoz/curso-geoespacial/blob/main/notebooks/sesion4.ipynb)

#### Código compartido

Abre [este archivo](../source/codigo-sesion4.md) y copia el código cuando la profesora te lo indique 🙏🏾

## Extra: Google Maps' trick

![](../source/images/alfiler.png)

[Google My Maps](https://www.google.com/intl/es/maps/about/mymaps/)
