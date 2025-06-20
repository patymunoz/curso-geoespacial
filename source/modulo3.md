# 🔹 Sesión 3

En esta sesión trabajaremos con la biblioteca `geopandas`, que nos permite trabajar con datos geoespaciales en Python. Aprenderemos a leer, escribir y manipular datos geoespaciales, así como a realizar análisis espaciales y visualizaciones.

```{admonition} Descarga de datos
:class: important

Para poder continuar con los ejercicios de esta sesión, asegúrate de descargar los archivos de datos que encontrarás al final de esta página.

Por favor, hazlo ahora, para no perder mucho tiempo cuando comencemos con el cuaderno de trabajo 🙂.
```

## Introducción

En la sesión anterior cubrimos los fundamentos de trabajar con geometrías individuales. Ahora pasaremos al tema principal de este curso: _trabajar con capas vectoriales_.

[Geopandas](http://geopandas.org/) es la biblioteca específica para trabajar con datos geoespaciales en Python. Geopandas combina las capacidades de `pandas` para el manejo de _datos tabulares_ con las capacidades de `shapely` para el manejo de _geometrías_. Esto nos permite trabajar con datos geoespaciales de manera similar a como lo haríamos con un `DataFrame` de `pandas`.

![go](images/geom-of.png)

**Figura 3.1.** Estructura de un GeoDataFrame (Fuente: [Geopandas](https://geopandas.org/en/stable/getting_started/introduction.html))

Las estrucutras de datos de `geopandas` son:

- `GeoSeries`: una serie de geometrías, similar a una columna de un `DataFrame` de `pandas`.

- `GeoDataFrame`: un `DataFrame` de `pandas` que contiene una columna de _geometry_. Es la estructura principal para trabajar con datos geoespaciales en `geopandas`.

![gg](images/geopandas.jpg)

**Figura 3.2.** Estructura de un GeoDataFrame en un entorno de Jupyter Notebook (Fuente: Elaboración propia.)

## Sistema de Coordenadas de Referencia (CRS)

El **Sistema de Coordenadas de Referencia** (_CRS_) es fundamental para ubicar correctamente los datos geoespaciales. Sin un CRS definido, los objetos _no tienen una posición significativa en el espacio_, lo que los hace arbitrarios.

Un CRS especifica:

- Cómo se representa la _forma_ de la Tierra (a través de un datum, como WGS84)
- Y opcionalmente, cómo se _proyectan esas coordenadas_ sobre un plano bidimensional (si es proyectado)

Una **proyección de mapa** es el proceso mediante el cual las coordenadas esféricas de latitud y longitud se transforman en coordenadas planas (x, y), utilizando unidades como `metros` o `grados`, dependiendo del tipo de CRS.

Los CRS se dividen en dos grupos principales:

- **CRS geográficos**: trabajan directamente con _latitud y longitud_ en unidades de **grados** (por ejemplo, [WGS84](https://epsg.io/4326))

- **CRS proyectados**: representan la Tierra sobre un plano usando unidades de distancia real (como **metros**) y aplican una proyección cartográfica (por ejemplo, [UTM Zona 14N](https://epsg.io/32614), [ITRF2008 / UTM zone 13N](https://epsg.io/6368))

En México, uno de los sistemas más comunes para trabajos cartográficos es el sistema **UTM**, dividido en zonas como la 13N y 14N, basadas en el datum `WGS84`. Para aplicaciones geodésicas de alta precisión, también puede usarse el sistema `ITRF` (por ejemplo, ITRF2008).

La forma más sencilla y común de especificar un CRS es a través del código **EPSG**, que es un identificador estándar. A continuación se presentan algunos CRS relevantes para México:

**Tabla: Sistemas de Coordenadas de Referencia (CRS) comunes en México**

| Nombre                                        | Tipo       | Unidades             | Código EPSG |
| --------------------------------------------- | ---------- | -------------------- | ----------- |
| [WGS84](https://epsg.io/4326)                 | Geográfico | Grados decimales (°) | 4326        |
| [UTM zona 11N (WGS84)](https://epsg.io/32611) | Proyectado | Metros (m)           | 32611       |
| [UTM zona 12N (WGS84)](https://epsg.io/32612) | Proyectado | Metros (m)           | 32612       |
| [UTM zona 13N (WGS84)](https://epsg.io/6368)  | Proyectado | Metros (m)           | 32613       |
| [UTM zona 14N (WGS84)](https://epsg.io/32614) | Proyectado | Metros (m)           | 32614       |
| [UTM zona 15N (WGS84)](https://epsg.io/32615) | Proyectado | Metros (m)           | 32615       |
| [UTM zona 16N (WGS84)](https://epsg.io/32616) | Proyectado | Metros (m)           | 32616       |

Los **CRS geográficos** abarcan toda la superficie terrestre y utilizan coordenadas angulares (grados), mientras que los **CRS proyectados** representan áreas más pequeñas con coordenadas en unidades lineales (metros), lo que permite realizar cálculos geométricos como distancias y áreas.

### Ejemplo reales de CRS en herramientas geoespaciales

Los Sistemas de Coordenadas de Referencia (_CRS_) no son solo una teoría: están en plataformas que usamos todos los días, desde tu GPS hasta Google Maps. Aquí te mostramos cómo se aplican en la práctica:

#### 🛰️ GPS

- **CRS:** `EPSG:4326` (WGS84)
- Coordenadas en _grados decimales_ (latitud, longitud)
- Usado por: dispositivos GPS, teléfonos móviles, drones

📍 **Ejemplo:**  
`20.6235, -103.4376` (latitud, longitud)

#### Google Maps

- **CRS:** `EPSG:3857` (Web Mercator)
- Coordenadas proyectadas en _metros_
- Proyección basada en WGS84, ideal para navegación web

📍 **Transformación interna:**  
Un punto como `20.6235, -103.4376` se transforma a coordenadas planas (x, y) para ser mostrado sobre un mapa interactivo.

#### OpenStreetMap (OSM)

- **CRS:** `EPSG:3857` (igual que Google Maps)
- Usado por: aplicaciones como Leaflet, Mapbox, QGIS base layers
- Muy utilizado para mapas web interactivos

#### Mapas Web (Leaflet, Mapbox, etc.)

- **CRS:** `EPSG:3857`
- Compatible con servicios de teselas (_tile servers_)
- Traducen automáticamente las coordenadas para las personas usuarias

````{admonition} ¡Atención al orden de coordenadas!
:class: warning

Cuando copies coordenadas desde Google Maps u otras fuentes, recuerda que el _orden_ es `latitud, longitud` (Y, X).

Sin embargo, al crear geometrías con `shapely`, debes invertir ese orden y usar `Point(X, Y)` → es decir:

```python
from shapely.geometry import Point

# Coordenadas de Google Maps:
# lat = 20.62435
# lon = -103.42748

punto = Point(-103.42748, 20.62435)  # Point(longitud, latitud)
````

## Datos

### Descarga para Geopandas

Para esta sesión utilizaremos un conjunto de datos de Información Sociodemográfica por colonia, Jalisco 2020. Colonias INE 2024 (Colonias Enteras) proveniente del [Instituto de Información Estadística y Geográfica de Jalisco (IIEG)](https://iieg.gob.mx/ns/?page_id=881).

Los datos están disponibles para su descarga en el siguiente enlace:

Formato: `shapefile` (zip)

[![Descargar datos](https://img.shields.io/badge/descargar-datos-blue)](../source/data/colonias_iieg.zip)

### Descarga para CRS

Para este ejercicio utilizaremos un conjunto de datos de países del mundo en formato `shapefile` proveniente de [Natural Earth](https://www.naturalearthdata.com/). Este conjunto de datos contiene información geoespacial sobre los límites políticos de los países.

Formato: `shapefile` (zip)

[![Descargar datos](https://img.shields.io/badge/descargar-datos-blue)](../source/data/ne_110m_admin_0_countries.zip)

También utilizaremos un conjunto de datos del Instituto Nacional de Estadística y Geografía (INEGI) de México, que contiene información geoespacial sobre el [Marco Geoestadístico de México](https://www.inegi.org.mx/temas/mg/). Este conjunto de datos contiene información sobre los límites políticos y geográficos de México.

Formato: `shapefile`

[![Descargar datos](https://img.shields.io/badge/descargar-datos-purple)](https://www.inegi.org.mx/app/biblioteca/ficha.html?upc=794551132173)

> ¡OJO! --> Sólo descarga el `SHP` llamado `Marco Geoestadístico Integrado 2024` (al final del listado de SHPs).

## Contenidos de esta sesión

En esta sesión estaremos trabajando con este cuaderno para trabajar con _GeoPandas_:

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/patymunoz/curso-geoespacial/blob/main/notebooks/sesion3.ipynb)

También veremos algunos ejemplos para trabajar el **Sistema de Coordenadas de Referencia (CRS)**

![Mapa de transición animado](_static/map.gif)

Créditos de la visualización: [@jasondavies](https://www.jasondavies.com/)

En este cuaderno trabajaremos con el _CRS_ de datos geoespaciales:

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/patymunoz/curso-geoespacial/blob/main/notebooks/sesion3-1.ipynb)

Recursos adicionales en los que te puedes apoyar para aprender más sobre el tema de _CRS_:

- [Spatial Reference](https://spatialreference.org/)
- [EPSG](https://epsg.io/)
- [Proj4](https://proj4.org/en/stable/operations/projections/)
- [EPSG Geodetic Parameter Dataset](https://epsg.org/home.html)
