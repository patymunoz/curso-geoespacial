# 🔹 Ambiente virtual local

Para trabajar de forma ordenada y reproducible en tus proyectos con Python y datos geoespaciales, es importante crear un ambiente virtual que contenga solamente las bibliotecas necesarias.

A continuación, te mostramos cómo hacerlo paso a paso.

---

## 1. ¿Por qué usar un ambiente virtual?

Un ambiente virtual te permite:

- Evitar conflictos entre versiones de paquetes
- Reproducir tus análisis en otros equipos o entornos
- Mantener tu instalación de Python base limpia

---

## 2. Crear un ambiente con Conda

Si estás utilizando **Anaconda** o **Miniconda**, puedes crear un ambiente con:

```bash
conda create -n geo_env python=3.13
```

Luego actívalo:

```bash
conda activate geo_env
```

---

## 3. Instalar bibliotecas geoespaciales

Dentro del ambiente puedes instalar bibliotecas esenciales como:

```bash
conda install geopandas jupyter notebook matplotlib contextily
```

También puedes usar `pip` para algunas que no estén en conda:

```bash
pip install folium osmnx pyproj
```

---

## 4. Crear un archivo `environment.yml` (opcional)

Esto te permitirá guardar y compartir tu ambiente. Ejecuta:

```bash
conda env export > environment.yml
```

Y para reconstruirlo en otro equipo:

```bash
conda env create -f environment.yml
```

---

## 5. Verifica tu instalación

Abre un Jupyter Notebook y prueba importar:

```python
import geopandas as gpd
import folium
import osmnx as ox
```

Si no hay errores, ¡estás listo para comenzar! 🚀

---

## ¿Por qué recomendamos Anaconda o Miniconda?

Trabajar con bibliotecas geoespaciales en Python como `geopandas`, `gdal`, `fiona`, `pyproj` o `shapely` puede ser complicado si se instalan con `pip`, ya que muchas de ellas dependen de librerías del sistema, compiladores o extensiones externas.

Usar **Anaconda** o **Miniconda** te permite:

- Evitar errores por compilación o conflictos entre paquetes
- Contar con un ecosistema científico preinstalado (en Anaconda)
- Tener control total sobre tus entornos con `conda`

**Por eso, este curso recomienda fuertemente usar Conda desde el inicio.**  
Te evitarás muchas frustraciones técnicas, especialmente al trabajar con archivos espaciales, proyecciones, geometrías y datos ráster o vectoriales.

```{admonition} ¡Recuerda!

Mantén tu ambiente virtual activo solo mientras trabajas en tu proyecto. Usa `conda deactivate` para salir cuando termines.
```

Si necesitas más documentarte más, consulta la [documentación oficial de Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).
