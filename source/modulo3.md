# 🔹 Sesión 3

En esta sesión trabajaremos con la biblioteca `geopandas`, que nos permite trabajar con datos geoespaciales en Python. Aprenderemos a leer, escribir y manipular datos geoespaciales, así como a realizar análisis espaciales y visualizaciones.

## Introducción

En la sesión anterior cubrimos los fundamentos de trabajar con geometrías individuales. Ahora pasaremos al tema principal de este curso: _trabajar con capas vectoriales_.

[Geopandas](http://geopandas.org/) es la biblioteca específica para trabajar con datos geoespaciales en Python. Geopandas combina las capacidades de `pandas` para el manejo de datos tabulares con las capacidades de `shapely` para el manejo de geometrías. Esto nos permite trabajar con datos geoespaciales de manera similar a como lo haríamos con un `DataFrame` de `pandas`.

![go](images/geom-of.png)

**Figura 1.** Estructura de un GeoDataFrame (Fuente: [Geopandas](https://geopandas.org/en/stable/getting_started/introduction.html))

Las estrucutras de datos de `geopandas` son:

- `GeoSeries`: una serie de geometrías, similar a una columna de un `DataFrame` de `pandas`.

- `GeoDataFrame`: un `DataFrame` de `pandas` que contiene una columna de geometrías. Es la estructura principal para trabajar con datos geoespaciales en `geopandas`.

![gg](images/geopandas.jpg)

**Figura 2.** Estructura de un GeoDataFrame en un entorno de Jupyter Notebook (Fuente: Elaboración propia.)

## Sistema de Coordenadas de Referencia (CRS)

El **Sistema de Coordenadas de Referencia** _(CRS)_ es fundamental para ubicar correctamente los datos geoespaciales. Sin un CRS definido, los objetos no tienen una posición significativa en el espacio, lo que los hace arbitrarios. Este sistema determina cómo se proyectan las coordenadas geográficas sobre un plano bidimensional.

Una proyección de mapa es el proceso mediante el cual las coordenadas de latitud y longitud se transforman en un plano, utilizando unidades que suelen ser metros o grados, según el tipo de proyección empleada.

Los CRS se dividen en dos grupos principales:

- **CRS geográficos**, donde las unidades son grados (por ejemplo, [WGS84](https://epsg.io/4326))
- **CRS proyectados**, donde las unidades son distancias reales, típicamente metros (por ejemplo, [UTM Zona 14N](https://epsg.io/32614), [ITRF2008 / UTM zone 13N](https://epsg.io/6368))

En México, uno de los sistemas más utilizados para trabajos precisos es el **ITRF** o el sistema **UTM** adaptado a distintas zonas del país, como la Zona 13N o 14N.

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

## Datos

#### Descarga para Geopandas

Para esta sesión utilizaremos un conjunto de datos de Información Sociodemográfica por colonia, Jalisco 2020. Colonias INE 2024 (Colonias Enteras) proveniente del [Instituto de Información Estadística y Geográfica de Jalisco (IIEG)](https://iieg.gob.mx/ns/?page_id=881).

Los datos se encuentran en formato `shapefile` y están disponibles para su descarga en el siguiente enlace:

[![Descargar datos](https://img.shields.io/badge/descargar-datos-blue)](../source/data/colonias_iieg.zip)

#### Descarga para CRS

Para este ejercicio utilizaremos un conjunto de datos de países del mundo en formato `shapefile` proveniente de [Natural Earth](https://www.naturalearthdata.com/). Este conjunto de datos contiene información geoespacial sobre los límites políticos de los países.

[![Descargar datos](https://img.shields.io/badge/descargar-datos-blue)](../source/data/ne_110m_admin_0_countries.zip)

También utilizaremos un conjunto de datos del Instituto Nacional de Estadística y Geografía (INEGI) de México, que contiene información geoespacial sobre el [Marco Geoestadístico de México](https://www.inegi.org.mx/temas/mg/). Este conjunto de datos está disponible en formato `shapefile` y contiene información sobre los límites políticos y geográficos de México.

[![Descargar datos](https://img.shields.io/badge/descargar-datos-blue)](../source/data/mg_2024_integrado.zip)

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
