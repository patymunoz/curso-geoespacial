## Codigo primero

```python
# 2. Función para enmascarar nubes usando la banda QA60
def maskS2clouds(image):
    qa = image.select('QA60')
    cloudBitMask = 1 << 10
    cirrusBitMask = 1 << 11
    mask = qa.bitwiseAnd(cloudBitMask).eq(0).And(qa.bitwiseAnd(cirrusBitMask).eq(0))
    return image.updateMask(mask).copyProperties(image, ["system:time_start"])

# 3. Filtrar colección Sentinel-2 y aplicar máscara de nubes
s2_clean = ee.ImageCollection("COPERNICUS/S2_SR") \
    .filterBounds(aoi) \
    .filterDate('2023-01-01', '2023-12-31') \
    .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20)) \
    .map(maskS2clouds)

# 4. Obtener la primera imagen limpia
image = s2_clean.first().select(['B4', 'B3', 'B2'])  # RGB

# 5. Exportar a mii Google Drive
task = ee.batch.Export.image.toDrive(
    image=image.clip(aoi),
    description='sentinel_rgb_sin_nubes_jalisco',
    folder='EarthEngine',
    fileNamePrefix='sentinel_jalisco_rgb_clean',
    region=aoi,
    scale=10,
    fileFormat='GeoTIFF'
)

task.start()

print("Tarea de exportación iniciada.")
```

## Código segundo

```python
fig, ax = plt.subplots(figsize=(10, 10))

roads.plot(ax=ax, color='gray', linewidth=1, label='Carreteras')
parks.plot(ax=ax, color='green', alpha=0.5, label='Parques')

ax.set_title('Carreteras y parques', fontsize=14)
ax.legend()
ax.axis('off')
plt.show()
```

## Código tercero

```python
fig, ax = plt.subplots(figsize=(10, 10))

# Cuadrícula
grid.plot(ax=ax, facecolor='none', edgecolor='lightgray', linewidth=0.5, label='Cuadrícula')

# Carreteras
roads_clip.plot(ax=ax, color='black', linewidth=1, label='Carreteras')

# Parques
parks_clip.plot(ax=ax, color='green', alpha=0.5, label='Parques')

ax.set_title("Capas recortadas al área de la cuadrícula", fontsize=14)
ax.legend()
ax.axis('off')
plt.show()
```

## Código cuarto

```python
# Mapa de colores y normalización para valores binarios
cmap = colors.ListedColormap(['lightcoral', 'forestgreen'])
bounds = [-0.5, 0.5, 1.5]
norm = colors.BoundaryNorm(bounds, cmap.N)

# Figura
fig, ax = plt.subplots(figsize=(15, 20))

grid_proj.to_crs(epsg=3857).plot(
    column='area_interes',
    cmap=cmap,
    norm=norm,
    ax=ax,
    edgecolor='none',
    alpha=0.6
)

# Mapa base
cx.add_basemap(ax, source=cx.providers.CartoDB.Positron)

ax.set_title("Zonas de interés", fontsize=14)
ax.axis('off')
plt.show()
```
