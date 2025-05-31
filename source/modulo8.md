# 🔹 Sesión 8

## Publicar mapas interactivos en la web

En esta sesión vamos a aprender a **publicar mapas interactivos creados con Folium** en la web a través de `Github Pages`.

Tendremos dos tutoriales:

- Uno para personas que ya han trabajado con `Git` y `GitHub`.
- Otro para personas que **prefieren no usar la terminal** (_command prompt_) y quieren hacerlo solo desde el navegador.

Puedes revisar la documentación oficial de [GitHub Pages](https://pages.github.com/).

## ¿Qué necesitas?

- Tener una cuenta en [https://github.com](https://github.com)
- Tener un archivo `mapa.html` generado con `Folium`

  - Ejemplo en Python:

    ```python
    import folium

    m = folium.Map(location=[19.4326, -99.1332], zoom_start=12)
    m.save("mapa.html")
    ```

---

## Opción 1: Publicar usando solo el navegador (sin terminal)

### 1. Crear un repositorio

a. Ve a [github.com](https://github.com) e inicia sesión.

b. Haz clic en **+ (arriba a la derecha)** → **New**.

![](../source/images/1.png)

c. Ponle un nombre, por ejemplo: `my-map`.

```{admonition} github.io
:class: tip

En algunos foros se menciona que el nombre del repositorio debe seguir el formato `nombredeusuario.github.io`.
Sin embargo, en mi experiencia, **no fue necesario usar esa estructura**: el mapa se desplegó correctamente con un nombre de repositorio diferente.
```

![](../source/images/2.png)

d. Asegúrate de que:

- Sea **público**
- **No marques** "Add a README file"

e. Haz clic en **Create repository**

---

### 2. Subir el archivo `mapa.html`

a. En tu nuevo repositorio, haz clic en **Uploading an existing file**

![](../source/images/3.png)

b. Arrastra o selecciona tu archivo `mapa.html`
b. Haz clic en **Commit changes**

![](../source/images/4.png)

---

### 3. Activar GitHub Pages

a. En tu repositorio, ve a la pestaña **Settings**

![](../source/images/5.png)

b. En el menú lateral, haz clic en **Pages**

![](../source/images/6.png)

c. En "Source", selecciona:

- **Branch:** `main`
- **Folder:** `/ (root)`
  d. Haz clic en **Save**

![](../source/images/7.png)

GitHub te mostrará un enlace como este:

```bash
https://patymunoz.github.io/mi-mapa-darks/mymap.darks.html
```

**NOTA:** Si no te muestra el link, regresa a la página principal de tu repositorio y has lo siguiente:

![](../source/images/8.png)

¡Ese es tu mapa interactivo en línea!

---

## Opción 2: Publicar usando Git y la terminal

```{admonition} Git Bash
Si estás utilizando _Windows_, te recomiendo usar la terminal **Git Bash** para clonar repositorios desde GitHub, ya que ofrece una experiencia más fluida y compatible con comandos de Unix.

👉 [Descargar Git Bash](https://git-scm.com/downloads)
```

### 1. Sigue el paso número 1 de [Opción 1](#opcion-1-publicar-usando-solo-el-navegador-sin-terminal)

Desde tu computadora (requiere tener Git instalado):

```bash
# Clona el repositorio desde GitHub a tu computadora
git clone https://github.com/tuusuarix/mi-mapa-darks.git

# Entra a la carpeta del repositorio clonado
cd mi-mapa-darks

# (Asegúrate de que tu archivo mapa.html esté aquí; si no, muévelo o créalo aquí)

# Añade el archivo (o todos los cambios)
git add mapa.html

# Haz un commit con un mensaje
git commit -m "Subo el archivo mapa.html"

# Sube el cambio a GitHub
git push origin main
```

### 2. Sigue el paso 3 de la [Opción 1](#opcion-1-publicar-usando-solo-el-navegador-sin-terminal)

## Pro Tip 🔥🔥🔥

Ya publicamos un mapa de forma muy sencilla, ¡pero tenemos ciertas limitaciones!  
¿Qué pasa si además de nuestros mapas interactivos queremos compartir gráficos, texto, imágenes o explicaciones completas?

Te comparto una opción relativamente fácil que puedes aplicar de inmediato 😉

### Usando GitHub Pages + Jekyll

Puedes consulta esta documentación oficial de [Jekyll | GitHub Pages](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll).

...pero aquí te lo explico paso a paso 👇

1️⃣ En GitHub creamos un nuevo repositorio.

- Esta vez sí debe seguir la estructura `numbreusuario.github.io`, como en el siguiente ejemplo:

![](../source/images/octocat.png)

- Asegúrate de que el repositorio sea **público.**

- Marca la opción para generar un archivo `README.md`.

2️⃣ Clona tu repositorio localmente

- Puedes usar `Git Bash` y trabajar en tu editor favorito, como `Visual Studio Code` u otro IDE.

3️⃣ Después de clonar, probablemente solo tendrás `README.md`. Agrega la siguiente estructura:

```bash
MAPAI.GITHUB.IO/
├── assets/                     # Carpeta para tus mapas HTML, imágenes u otros recursos
│   ├── mymap_darks.html
│   └── tipos_culturales.html
│
├── _config.yml                 # Configuración de Jekyll (requerido por GitHub Pages)
├── index.md                   # Página principal (Markdown procesado por Jekyll)
└── README.md                  # (Opcional) Descripción del repositorio para GitHub

```

#### 📁 Carpeta assets

Aquí puedes colocar los archivos _html_ generados con `folium`, así como imágenes u otros recursos estáticos que desees mostrar en tu sitio.

#### ⚙️ Archivo `_config.yml`

Este archivo es **obligatorio** para que Jekyll procese correctamente tu sitio.

```bash
remote_theme: pages-themes/cayman@v0.2.0
plugins:
  - jekyll-remote-theme # puedes cambiar conforme el repositorio del tema de tu elección

title: Mapa interactivo
description: Este es un proyecto que muestra visualizaciones con mapitas.

include:
  - assets/mymap_darks.html
```

Puedes cambiar el tema según el que más te guste. Aquí usamos el tema `Cayman`.

Te comparto la [lista oficial de temas](https://pages.github.com/themes/).

#### ⚙️ Archivo `index.md`

Este será el contenido principal visible en tu sitio. Aquí tienes un ejemplo:

```bash
---
layout: default
title: Mapa Interactivo
---

# Bienvenido

Este proyecto muestra un **mapa de calor** interactivo de ciertos puntos geográficos en la ciudad de Guadalajara.
Fue generado con **Python** usando la librería `folium`, y desplegado con **GitHub Pages** usando `Jekyll`.

## ¿Qué representa este mapa?

Este mapa permite visualizar concentraciones de datos geográficos, el tema es:

- Centros culturales

La intensidad del color indica la densidad de puntos en esa zona.

Puedes visualizarlo aquí

<iframe src="/mapai.github.io/assets/mymap_darks.html"
        width="100%" height="800"
        style="border: none; max-width: 100%;">
</iframe>

## Gráfico: Sitios culturales por tipo

<iframe src="/mapai.github.io/assets/tipos_culturales.html"
        width="100%" height="600" style="border:none;"></iframe>

## Tecnologías utilizadas

- [Folium](https://python-visualization.github.io/folium/) para crear el mapa interactivo
- [Leaflet.js](https://leafletjs.com/) como motor de mapas
- [GitHub Pages](https://pages.github.com/) para hospedar este sitio
- Tema de Jekyll: `minimal`

```

```{admonition} Ojo
Los mapas se integran mediante **iframes**. Solo necesitas que los archivos `.html` estén dentro de la carpeta `assets/` y hacer referencia a ellos desde tu Markdown.
```

Este es un ejemplo muy simple, pero ideal si estás dando tus primeros pasos.
Te animo a experimentar, personalizar y descubrir todo lo que puedes hacer con estas herramientas.

Si quieres llevar tu sitio al siguiente nivel, aquí tienes la documentación oficial de [Jekyll](https://jekyllrb.com/docs/themes/) para explorar opciones más avanzadas y profesionales 🚀.
