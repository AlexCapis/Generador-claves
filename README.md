
![Logo](/docs/passodi_logo.png)


</a>
<h1>PASSODI: ¡Tu Escudo Digital!</h1>

# Generador-claves





- **app/:** El contenido de dicha carpeta es la visualización de todas las distintas versiones del generador de contraseñas a través de la aplicación web de Streamlit.


- **notebooks/:** Esta carpeta alberga los notebooks de Jupyter utilizados para documentar y explicar el proyecto. Cada versión del generador de contraseñas tendrá su propio notebook correspondiente. El notebook `funcionamiento_generar_claves.ipynb` proporciona una descripción general y enlaces a las versiones específicas.

- **src/:** Esta carpeta contiene el código fuente de tu proyecto. Está dividido en los siguientes archivos:

  - `__init__.py`: Un archivo vacío que indica que esta carpeta es un paquete de Python.
  - `password_generator.py`: Contendrá funciones y clases relacionadas con la generación de contraseñas. Aquí definirás funciones generales que se utilizan en todas las versiones.
  - `version_1.py`, `version_2.py`, etc.: Cada archivo corresponde a una versión específica del generador de contraseñas y contiene las implementaciones específicas de cada versión.

- **docs/:** Esta carpeta se utiliza para almacenar datos adicionales que puedan ser necesarios para el proyecto, como diccionarios de palabras o archivos de configuración.

- **README.md:** Este archivo es la documentación principal del proyecto. Proporciona una descripción general, instrucciones para instalar y utilizar el generador de contraseñas, ejemplos de código y otra información relevante.

- **requirements.txt:** Lista las bibliotecas de Python necesarias para ejecutar tu proyecto.