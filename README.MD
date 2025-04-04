# Proyecto ML - Documentación

Este proyecto utiliza [Miniconda](https://docs.conda.io/en/latest/miniconda.html) para la gestión de entornos y [Jupyter Book](https://jupyterbook.org/) para la generación de documentación.

## Instalación y Configuración

### 0. Ubicación en la Carpeta del Proyecto
Antes de comenzar, asegúrate de estar ubicado en la carpeta raíz del proyecto. Puedes hacerlo ejecutando:

**Ejemplo:**
```bash
cd /c:/Users/jesus/OneDrive/Escritorio/proyecto_ml/proyect_book
```

### 1. Instalación de Miniconda
Descarga e instala Miniconda desde su [página oficial](https://docs.conda.io/en/latest/miniconda.html). Sigue las instrucciones según tu sistema operativo.

### 2. Creación del Entorno
Ejecuta los siguientes comandos en tu terminal para crear y activar un entorno virtual:

```bash
conda create -n proyecto_ml python=3.8.20 -y
conda activate proyecto_ml
```

### 3. Instalación de Requerimientos
Instala las dependencias necesarias ejecutando:

```bash
pip install -r requirements.txt
```

Asegúrate de que el archivo `requirements.txt` contiene todas las dependencias necesarias para tu proyecto.

## Generación de la Documentación

### 1. Construcción del Jupyter Book
Antes de construir la documentación, asegúrate de estar dentro de la carpeta de trabajo correcta y de tener el entorno virtual activado. Luego, ejecuta:

```bash
jupyter-book build .
```

Esto generará los archivos HTML en la carpeta `_build/html`.

### 2. Publicación en GitHub Pages
Asegúrate de que tu repositorio ya contenga todos los archivos necesarios y actualizados. Para publicar la documentación en GitHub Pages, utiliza el siguiente comando:
## Notas
- Asegúrate de tener configurado correctamente tu repositorio de GitHub.
- Verifica que `ghp-import` esté instalado. Si no lo está, puedes instalarlo con:

```bash
pip install ghp-import
```

```bash
ghp-import -n -p -f _build/html
```

Este comando subirá los archivos generados a la rama `gh-pages` de tu repositorio.



¡Listo! Ahora tu proyecto está configurado y la documentación publicada.