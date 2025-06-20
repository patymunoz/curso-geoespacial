# 🔹 Sesión 2

En esta sesión trabajaremos con la biblioteca `shapely`, que nos permite realizar operaciones geométricas y espaciales en Python. Aprenderemos a crear, manipular y analizar geometrías, así como a realizar operaciones espaciales como la intersección, la unión y la diferencia entre geometrías.

## Introducción

En el capítulo anterior cubrimos los fundamentos de trabajar con Python. Ahora pasaremos al tema principal de este curso: _trabajar con datos geoespaciales_.

Los datos geoespaciales se pueden dividir en dos categorías principales:

- Capas de datos vectoriales
- Capas de datos ráster

En los próximos tres capítulos, abordaremos los fundamentos de trabajar con el primer tipo, las _capas vectoriales_, en Python. En esta sesión cubrimos el paquete `shapely`, que se utiliza para representar y trabajar con _geometrías vectoriales individuales_.

Las _geometrías individuales_ (_Simple Features_) dentro de una capa vectorial se almacenan como geometrías de `shapely`. Así que es importante familiarizarse con este paquete antes de pasar a trabajar con _capas vectoriales_ completas.

!['Tipos de geometrías'](images/simple_feature_types.svg)

**Figura 1.** Recuperado de: Dorman, M. (2025). _Geometries (Shapely)._ En _Spatial Data Programming with Python._

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

Un estándar para representar estas geometrías es mediante el formato **WKT (Well-Known Text)**, es un formato de texto plano estructurado, usado para describir objetos geométricos de forma estandarizada y legible por humanos y máquinas conforme al estándar _Simple Features._

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

> 🛈 **WKT es ampliamente utilizado** en bibliotecas como `shapely` y bases de datos espaciales como PostGIS, porque es un estándar abierto, legible y fácil de intercambiar entre sistemas.

También es utilizado en otros entornos como:

- GeoServer (para WFS)

- GDAL/OGR

- QGIS (al exportar geometrías)

- APIs REST geoespaciales

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

![](../source/images/geoms.png)

**Figura 2.** Relación entre el modelo de geometrías espaciales del OGC (Simple Features), su representación visual, y las distintas formas de codificación interoperable (WKT, WKB, GeoJSON)

### Otras formas de codificar geometrías según _Simple features_

Además de WKT, existen otros formatos estandarizados que permiten codificar geometrías para su uso e intercambio entre sistemas:

#### WKB (Well-Known Binary)

Formato binario definido por el OGC para representar geometrías de forma compacta y eficiente. Es útil cuando se necesita reducir el tamaño de almacenamiento o transmitir datos por red.

![](../source/images/wkb.png)

#### GeoJSON

Formato basado en JSON ampliamente usado en aplicaciones web y APIs. Permite representar geometrías junto con propiedades (atributos) y, en algunos casos, especificar un CRS. GeoJSON es legible por humanos y fácilmente integrable con bibliotecas como Leaflet, Mapbox o GeoPandas.

![](../source/images/geosjon1.png)

## Shapely

`shapely` es una biblioteca de Python para trabajar con geometrías vectoriales, es decir, el _componente geométrico_ de las capas vectoriales (el otro componente son los atributos no espaciales).

`shapely` es una interfaz de Python para la biblioteca de geometría `GEOS` (Geometry Engine - Open Source), que es una biblioteca de C++. `GEOS` es la biblioteca de geometría subyacente utilizada por muchos sistemas de información geográfica (SIG) de código abierto y bibliotecas de análisis espacial, como `PostGIS`, `GDAL`, `GeoPandas`, `QGIS`, entre otros.

La [documentación](https://shapely.readthedocs.io/en/stable/manual.html) de `shapely` es muy completa y contiene ejemplos de uso.

### Atributos vs. métodos en `shapely`

Al trabajar con objetos geométricos en `shapely`, es importante entender la diferencia entre **atributos** y **métodos**, ya que ambos son formas de interactuar con las geometrías, pero funcionan de manera distinta.

| Tipo         | ¿Qué es?                         | ¿Cómo se usa?       | ¿Ejemplo?                      |
| ------------ | -------------------------------- | ------------------- | ------------------------------ |
| **Atributo** | Una propiedad del objeto         | Sin paréntesis      | `.area`, `.bounds`, `.length`  |
| **Método**   | Una acción que realiza el objeto | Con paréntesis `()` | `.intersects()`, `.contains()` |

Los `atributos` permiten acceder a información descriptiva de la geometría, como su área o sus límites.

Los `métodos` permiten realizar operaciones espaciales como calcular distancias, verificar relaciones topológicas o modificar la geometría.

## Contenidos de esta sesión

En esta sesión estaremos trabajando con este cuaderno de trabajo:

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/patymunoz/curso-geoespacial/blob/main/notebooks/sesion2.ipynb)

Al finalizar el taller, tienes disponible un cuaderno para practicar lo aprendido:

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/patymunoz/curso-geoespacial/blob/main/notebooks/sesion2_practica.ipynb)
