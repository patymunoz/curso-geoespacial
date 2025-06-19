# 🔹 Sesión 2

En esta sesión trabajaremos con la biblioteca `shapely`, que nos permite realizar operaciones geométricas y espaciales en Python. Aprenderemos a crear, manipular y analizar geometrías, así como a realizar operaciones espaciales como la intersección, la unión y la diferencia entre geometrías.

## Introducción

En el capítulo anterior cubrimos los fundamentos de trabajar con Python. Ahora pasaremos al tema principal de este curso: _trabajar con datos geoespaciales_.

Los datos geoespaciales se pueden dividir en dos categorías principales:

- Capas de datos vectoriales
- Capas de datos ráster

En los próximos tres capítulos, abordaremos los fundamentos de trabajar con el primer tipo, las _capas vectoriales_, en Python. En esta sesión cubrimos el paquete `shapely`, que se utiliza para representar y trabajar con _geometrías vectoriales individuales_.

Las _geometrías individuales_ dentro de una capa vectorial se almacenan como geometrías de `shapely`. Así que es importante familiarizarse con este paquete antes de pasar a trabajar con _capas vectoriales_ completas.

!['Tipos de geometrías'](images/simple_feature_types.svg)

Recuperado de: Dorman, M. (2025). _Geometries (Shapely)._ En _Spatial Data Programming with Python._

```{admonition} ¿Qué es una geometría individual?

Una **geometría individual** es una representación única de una forma geométrica, definida según los [tipos establecidos en la especificación *Simple Features*](https://en.wikipedia.org/wiki/Simple_Features). Esta especificación contempla al menos 17 tipos de geometrías, aunque en la práctica se utilizan comúnmente solo 7. Estas son:

- `Point`: un punto en el espacio (bidimensional o tridimensional).
- `LineString`: una línea compuesta por una secuencia de puntos conectados.
- `Polygon`: un área cerrada delimitada por una secuencia de puntos (puede incluir huecos).
- `MultiPoint`: un conjunto de puntos.
- `MultiLineString`: un conjunto de líneas (`LineString`).
- `MultiPolygon`: un conjunto de polígonos.
- `GeometryCollection`: una colección que puede incluir cualquier combinación de los tipos anteriores.
```

Una forma común de representar estas geometrías es mediante el formato **WKT (Well-Known Text)**, un lenguaje de marcado en texto plano que describe el tipo de geometría y sus coordenadas.

Por ejemplo:

| Tipo                   | Ejemplo WKT                                                                                                                |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `'Point'`              | `POINT (30 10)`                                                                                                            |
| `'LineString'`         | `LINESTRING (30 10, 10 30, 40 40)`                                                                                         |
| `'Polygon'`            | `POLYGON ((35 10, 45 45, 15 40, 10 20, 35 10), (20 30, 35 35, 30 20, 20 30))`                                              |
| `'MultiPoint'`         | `MULTIPOINT (10 40, 40 30, 20 20, 30 10)`                                                                                  |
| `'MultiLineString'`    | `MULTILINESTRING ((10 10, 20 20, 10 40), (40 40, 30 30, 40 20, 30 10))`                                                    |
| `'MultiPolygon'`       | `MULTIPOLYGON (((40 40, 20 45, 45 30, 40 40)), ((20 35, 10 30, 10 10, 30 5, 45 20, 20 35), (30 20, 20 15, 20 25, 30 20)))` |
| `'GeometryCollection'` | `GEOMETRYCOLLECTION (POINT (40 10), LINESTRING (10 10, 20 20, 10 40), POLYGON ((40 40, 20 45, 45 30, 40 40)))`             |

Recuperado de: Wikipedia. (2025). _Well-known text representation of geometry objects._ En [Wikipedia](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry).

> 🛈 **WKT es ampliamente utilizado** en bibliotecas como `shapely` y bases de datos espaciales como PostGIS, pero **no es la única forma** de representar geometrías.

```{admonition} 🎯 ¿Qué representa un WKT?
:class: note

Cuando ves un WKT como:

`POLYGON((0 0, 0 2, 2 2, 2 0, 0 0))`

puede parecer que son solo **números enteros** o una simple lista de puntos. Pero en realidad, este texto **describe un dibujo geométrico**: un polígono cerrado con esquinas en esos puntos (0,0), (0,2), etc.

En *Shapely*, al cargar este WKT con `shapely.wkt.loads()`, estás creando *una figura matemática*, que puedes visualizar, medir (área, perímetro), y analizar (intersecciones, uniones, etc.).

💡 **La clave**: esos números no tienen aún un significado geográfico. Son solo coordenadas *en un espacio abstracto*. Para convertirlos en *coordenadas reales sobre el planeta*, necesitas asociarlos a un **sistema de referencia (CRS)** —como decir “estos puntos están en lat/lon” o “en metros UTM”.

Así, un simple `POLYGON((500000 2100000, ...))` puede convertirse en una ubicación en Sudamérica... si sabes en qué CRS estás trabajando.
```

```{admonition} WKT: el plano del objeto geométrico
:class: tip

Puedes pensar en un **WKT** como el **plano arquitectónico** de una geometría: es un texto que describe cómo debe “verse” una figura (punto, línea, polígono) en el espacio.

📐 **Shapely** toma ese plano (WKT) y lo convierte en un **objeto matemático real** con el que puedes hacer cálculos, análisis o visualizaciones.
```

## Shapely

`shapely` es una biblioteca de Python para trabajar con geometrías vectoriales, es decir, el _componente geométrico_ de las capas vectoriales (el otro componente son los atributos no espaciales).

`shapely` es una interfaz de Python para la biblioteca de geometría `GEOS` (Geometry Engine - Open Source), que es una biblioteca de C++. `GEOS` es la biblioteca de geometría subyacente utilizada por muchos sistemas de información geográfica (SIG) de código abierto y bibliotecas de análisis espacial, como `PostGIS`, `GDAL`, `GeoPandas`, `QGIS`, entre otros.

La [documentación](https://shapely.readthedocs.io/en/stable/manual.html) de `shapely` es muy completa y contiene ejemplos de uso.

## Contenidos de esta sesión

En esta sesión estaremos trabajando con este cuaderno de trabajo:

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/patymunoz/curso-geoespacial/blob/main/notebooks/sesion2.ipynb)

Al finalizar el taller, tienes disponible un cuaderno para practicar lo aprendido:

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/patymunoz/curso-geoespacial/blob/main/notebooks/sesion2_practica.ipynb)
