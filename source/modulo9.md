# 🔹 Sesión 9

## ¿Qué es OpenStreetMap?

![](../source/images/OpenStreetMap-Mexico.png)

En esta sesión aprenderemos cómo descargar y visulizar un _red de calles_ y datos adicionales provenientes de _OpenStreetMap_.

**OpenStreetMap (OSM)** es un proyecto colaborativo que ofrece un **mapa del mundo gratuito y editable**, construido enteramente por personas voluntarias. A menudo se le describe como la [_“Wikipedia de los mapas”_](https://wiki.openstreetmap.org), ya que cualquier persona puede contribuir con datos geográficos, como carreteras, senderos, edificios y elementos naturales, utilizando dispositivos GPS, imágenes aéreas o conocimiento local.

[Mapa OpenStreetMap](https://www.openstreetmap.org/#map=5/23.95/-94.88)

---

## Características Clave de OpenStreetMap

- **Basado en la comunidad _(crowd-sourced)_:** La comunidad de _OpenStreetMap_ es diversa, apasionada y crece cada día. Nuestros colaboradores incluyen mapeadores entusiastas, profesionales de los SIG, ingenieros asegurando el funcionamiento de los servidores de OSM, personal humanitario que mapean las zonas afectadas por desastres, y muchos más.

- **Libre de uso:** Los datos de OSM son abiertos y gratuitos bajo la **Licencia de Base de Datos Abierta (ODbL)**, lo que significa que puedes usarlos para casi cualquier propósito, incluso comercialmente, siempre que se dé la atribución correspondiente. Consulta la página de [derechos de autor y licencia](https://www.openstreetmap.org/copyright) para más detalles.

- **Detalles geográficos ricos:** Incluye calles, ciclovías, edificios, transporte público, parques, tipos de uso del suelo, entre muchos otros.

- **Editable:** Cualquiera puede registrarse en [www.openstreetmap.org](https://www.openstreetmap.org) para comenzar a editar y contribuir.

- **Cobertura global:** Desde senderos rurales hasta redes urbanas complejas, su objetivo es proporcionar datos cartográficos completos a nivel mundial.

- **Apoyado por herramientas y comunidad:** Existe un gran ecosistema de herramientas y una comunidad global apasionada que contribuye y mantiene los datos.

---

## ¿Quién utiliza OpenStreetMap?

- **Desarrolladores de aplicaciones** (por ejemplo, de navegación, fitness, entregas)
- **Gobiernos y organizaciones humanitarias** (por ejemplo, para respuesta ante desastres)
- **Investigadores y planificadores urbanos**
- **Empresas y startups** (por ejemplo, servicios basados en ubicación)

---

## OSMnx y NetworkX

- **OSMnx**: Módulo de Python que permite **descargar y analizar datos de OpenStreetMap**, especialmente redes de calles. Facilita tareas como obtener mapas urbanos, calcular rutas, analizar pendientes y visualizar estructuras urbanas.

- **NetworkX**: Paquete de Python especializado en el **análisis de grafos y redes**. Se utiliza para representar, manipular y estudiar la topología de redes (por ejemplo, calles como nodos y conexiones como aristas).

> 🔗 **OSMnx utiliza NetworkX internamente** para representar las redes de calles descargadas desde OpenStreetMap como grafos, lo que permite aplicar algoritmos de análisis y cálculo sobre estas redes.

### Funcionalidades principales:

1. Descargar límites administrativos y huellas de edificios.
2. Automatizar la descarga y construcción de redes viales de OSM en cualquier parte del mundo con múltiples tipos de red (conducción, caminata, etc.).
3. Corrección algorítmica y simplificación de la topología de la red.
4. Descargar datos de elevación y calcular pendientes de calles.
5. Análisis: calcular rutas, proyectar y visualizar, calcular medidas métricas y topológicas.

Boeing, G. 2017. “[OSMnx: New Methods for Acquiring, Constructing, Analyzing, and Visualizing Complex Street Networks.](https://www.researchgate.net/publication/309738462_OSMNX_New_Methods_for_Acquiring_Constructing_Analyzing_and_Visualizing_Complex_Street_Networks)” Computers, Environment and Urban Systems 65, 126-139.

## Datos

Trabajaremos con dos geometrías.

Formato: `GeoJson`

[![Descargar datos](https://img.shields.io/badge/descargar-datos-blue)](../source/data/map.geojson)

[![Descargar datos](https://img.shields.io/badge/descargar-datos-purple)](../source/data/col_americana.geojson)

## Contenidos de esta sesión

En esta sesión estaremos trabajando con este cuaderno de trabajo:

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/patymunoz/curso-geoespacial/blob/main/notebooks/sesion9.ipynb)
