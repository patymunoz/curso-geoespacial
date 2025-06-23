# 🔹 Sesión 5

```{admonition} Antes de iniciar...

[Click aquí](https://docs.google.com/forms/d/e/1FAIpQLScycxos-GgWz2YWV18ciHjgLhNek5Fg-pA0dU957h0SRZFsDg/viewform?usp=dialog)
```

En esta sesión exploraremos el concepto de **reclasificación de datos**. Para esto, utilizaremos datos de uso del suelo y vegetación, así como imágenes satelitales.

## Reclasificación de datos

En el análisis SIG, la _reclasificación de datos_ consiste en transformar un conjunto de valores existentes para agruparlos, simplificarlos o asignarlos a nuevas categorías, de acuerdo con criterios específicos. Esta técnica permite facilitar la interpretación y el análisis de la información espacial.

```{admonition} Ejemplo práctico
:class: tip
Imagina que tienes un mapa de elevación con valores de altitud entre 0 y 3,000 metros. Puedes reclasificarlo así:
- 0-500 m --> categoría 1 (baja altitud)
- 501-1,500 m --> categoría 2 (media altitud)
- 1,501-3,000 m --> categoría 3 (alta altitud)

Esta reclasificación facilita el análisis espacial. Por ejemplo, te permite identificar rápidamente las zonas con mayor riesgo de inundación (más probables en áreas de baja altitud).
```

Además de simplificar la interpretación, la reclasificación también permite ajustar los datos según ciertos criterios de interés. Por ejemplo, si queremos identificar áreas que cumplan con los siguientes requisitos:

- **Zonas de elevación altas**
- **Zonas cercanas a parques**
- **Zonas alejadas de carreteras ruidosas**

Podemos reclasificar capas como elevación, uso del suelo y red vial, asignando categorías específicas a cada una. Luego, al combinar esas capas reclasificadas, es posible identificar las zonas que satisfacen todos los criterios establecidos.

#### `mapclassify` de PySAL

En mapas temáticos (como los mapas de coropletas), clasificamos datos numéricos en grupos o clases para visualizar mejor patrones geográficos (por ejemplo, niveles de ingreso por región). Cada clasificador define cómo se agrupan esos valores.

Aquí te comparto solo algunos de los clasificadores más usados y que, de hecho, puedes usar también en ArcGis Pro y QGIS, ya que vienen incluidos en sus herramientas de análisis:

📊 Clasificadores más usados en mapas temáticos

| Clasificador    | Descripción                                                                |
| --------------- | -------------------------------------------------------------------------- |
| Equal_Interval  | Divide el rango de datos en intervalos iguales. Fácil de interpretar.      |
| Quantiles       | Cada clase contiene el mismo número de observaciones.                      |
| Natural_Breaks  | También conocido como Fisher-Jenks. Minimiza la varianza dentro de clases. |
| Std_Mean        | Usa media y desviación estándar para agrupar datos.                        |
| Box_Plot        | Clasificación basada en cuartiles y valores atípicos.                      |
| HeadTail_Breaks | Ideal para datos muy sesgados o con distribución de Ley de Potencia.       |

Trabajar desde python, en este sentido, además de ofrecernos las mismas herramientas, puedes customizar los clasificadores y adaptarlos a tus necesidades de análisis. Es lo que veremos a continuación!!! 👁️‍🗨️👁️‍🗨️👁️‍🗨️

## Datos

Esta vez trabajaremos con los datos _"Conjunto de datos vectoriales de uso del suelo y vegetación escala 1:250 000"_ del [INEGI](https://www.inegi.org.mx/app/biblioteca/ficha.html?upc=702825570231), que se pueden descargar desde el siguiente enlace:

[![Descargar datos](https://img.shields.io/badge/descargar-datos-blue)](../source/data/uso_de_suelo.zip)

También te dejo por acá el [**diccionario de variables**](https://www.inegi.org.mx/contenidos/productos/prod_serv/contenidos/espanol/bvinegi/productos/nueva_estruc/702825063443.pdf) para que puedas consultar la información de cada variable, por si te interesa ahondar más al respecto de los datos.

### Ráster (archivos .tif)

Para el caso de los archivos .tif, los puedes descargar desde el siguiente enlace:

[![Descargar datos](https://img.shields.io/badge/descargar-datos-green)](../source/data/sentinel_jalisco_rgb_clean.tif)

[![Descargar datos](https://img.shields.io/badge/descargar-datos-orange)](../source/data/elev_jalisco.tif)

Ambos archivos fueron descargados a través de **Google Earth Engine**.

## Contenidos de esta sesión

En esta sesión estaremos trabajando con este cuaderno de trabajo:

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/patymunoz/curso-geoespacial/blob/main/notebooks/sesion5.ipynb)

#### Código compartido

Abre [este archivo](../source/codigo-sesion5.md) y copia el código cuando la profesora te lo indique 🙏🏾
