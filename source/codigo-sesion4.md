# Primer código

```python
# ----------- Código Mapa interactivo para visualizar los resultados ----------- #

m = am.explore(color="gray", edgecolor="black", name="Municipios", tooltip="NOMGEO")

# + within
contenidos.explore(m=m, color="green", marker_kwds={'radius': 5}, name="Within", tooltip=True)
madius': 5}, name="Within", tooltip=True)
m
```

# Segundo código

```python
#---- ver centroides y poligonos ----#
fig, ax = plt.subplots(figsize=(10, 10))
colonias_am.plot(ax=ax, color='lightgray', edgecolor='black', alpha=0.5)
colonias_am.centroid.plot(ax=ax, color='blue', markersize=5, label='Centroides')
plt.title("Centroides de Colonias en el Área Metropolitana")
plt.legend()
plt.show()
```

# Tercer código

```python
from shapely.ops import nearest_points

def obtener_vals_cercanos(fila, gdf_referencia, columna_geom='geometry', columna_valor='NOMCOL1'):
    """Encuentra el valor del objeto más cercano desde una geometría de entrada."""

    if fila[columna_geom].is_empty:
        return None

    # crear unión de geometrías objetivo
    other_union = gdf_referencia.geometry.unary_union

    # encontrar punto más cercano
    _, nearest_geom = nearest_points(fila[columna_geom], other_union)

    # buscar el índice del objeto cuya geometría coincide con la más cercana
    distancias = gdf_referencia.geometry.distance(nearest_geom)
    idx = distancias.idxmin()

    if columna_valor in gdf_referencia.columns:
        return gdf_referencia.loc[idx, columna_valor]
    else:
        return None
```

# Cuarto código

```python
import folium

# 1. Mapa base con colonias (polígonos)
m = c.explore(
    color="gray",
    edgecolor="white",
    name="Colonias",
    tooltip="NOMCOL1"
)

# 2. Centroides de colonias
c_centroids = c.copy()
c_centroids["centroid"] = c_centroids.geometry.centroid
c_centroids = c_centroids.set_geometry("centroid")

m = c_centroids.explore(
    m=m,
    color="#CD5C5C",
    marker_kwds={"radius": 2},
    tooltip=["NOMCOL1", "CP", "POBTOT"],
    name="Centroides"
)

# 3. Puntos de interés
m = geoc.explore(
    m=m,
    color="blue",
    marker_kwds={"radius": 4},
    tooltip="colonia_mas_cercana",
    name="Puntos de interés"
)

# 4. Añadir control de capas
folium.LayerControl().add_to(m)

# 5. Mostrar mapa
m
```
