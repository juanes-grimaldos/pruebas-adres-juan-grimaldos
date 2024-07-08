# Proyecto de Prueba Técnica en R

Este proyecto consiste en la carga de bases de datos a SQLite y el análisis subsiguiente de los datos utilizando R Markdown (.Rmd). Se ha incluido `renv` para garantizar la reproducibilidad del entorno de desarrollo y análisis.

## Estructura del Proyecto

- `/src`: Código fuente del proyecto.
  - `scripts/backend_creacion_db_sqlite.Rmd`: Script para cargar los datos en SQLite.
  - `scripts/reporte.Rmd`: Documento R Markdown con el análisis de los datos.
- `/data`: Directorio para las bases de datos originales y de SQLite.
- `renv.lock`: Archivo de bloqueo para `renv`.
- `/plots`: gráficos generados para visualización de datos. 

## Requisitos

Para ejecutar este proyecto, necesitarás R instalado en tu sistema. Además, se recomienda utilizar RStudio para una mejor integración con `renv` y R Markdown.

## Uso

1. Clona este repositorio en tu máquina local.
2. Abre el proyecto en RStudio.
3. Ejecuta `renv::restore()` para instalar las dependencias. Si no tienes iniciado un proyecto de renv te pedirá activarlo primero. Luego de activarlo debes correr el mismo comando y darle a sí para installar las dependencias
5. Ejecuta el script `scripts/backend_creacion_db_sqlite.Rmd` para cargar las bases de datos en SQLite.
6. Abre y ejecuta `scripts/reporte.Rmd` para ver el análisis. Utiliza el directorio de trabajo como el del documento. 

