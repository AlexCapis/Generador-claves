# PASSODI: ¡Tu Escudo Digital!

![Logo](/docs/passodi_logo.png)

#### Autor: [Alex Marzá Manuel](https://github.com/AlexCapis)

## ÍNDICE

1. [Acceso a la Aplicación](#1-acceso-a-la-aplicación)
2. [Introducción](#2-introducción)
3. [Desarrollo](#3-desarrollo)
4. [Estructura de carpetas](#4-estructura-de-carpetas)
5. [Breve explicación de las diversas versiones](#5-breve-explicación-de-las-diversas-versiones)
6. [Demostración en video](#6-demostración-en-video)
7. [Agradecimientos](#7-agradecimientos)


## 1. Acceso a la Aplicación

Puedes acceder a la aplicación del Generador de Contraseñas a través del siguiente enlace: [Generador de Contraseñas PASSODI](https://generador-claves.streamlit.app/). ¡Explora y experimenta la generación de contraseñas de forma interactiva y sencilla.


## 2. Introducción

### Descripción del proyecto

PASSODI es un proyecto que busca proporcionar a los usuarios una forma segura y conveniente de generar contraseñas sólidas para proteger sus cuentas en línea. En el mundo digital actual, la seguridad es de suma importancia, y las contraseñas seguras son esenciales para garantizar esa seguridad. Este proyecto aborda esta necesidad ofreciendo un generador de contraseñas robusto y fácil de usar.

## 3. Desarrollo

### ¿Qué dificultades podemos encontrar?

Durante el desarrollo de PASSODI, podríamos enfrentar desafíos como la optimización del algoritmo de generación de contraseñas, asegurando la eficiencia y seguridad en todas las versiones, y también la implementación exitosa de la inteligencia artificial para futuras versiones.

## 4. Estructura de carpetas

- [docs](https://github.com/AlexCapis/Generador-claves/tree/main/docs): Esta carpeta se utiliza para almacenar datos adicionales que puedan ser necesarios para el proyecto como  `generador_contraseñas.gif` y  `passodi_logo.png`

- [notebooks](https://github.com/AlexCapis/Generador-claves/tree/main/notebooks): Esta carpeta alberga los notebooks de Jupyter utilizados para documentar y explicar el proyecto. Cada versión del generador de contraseñas tendrá su propio notebook correspondiente. El notebook `funcionamiento_generar_claves.ipynb` proporciona una descripción general y enlaces a las versiones específicas.

- [src](https://github.com/AlexCapis/Generador-claves/tree/main/src): Esta carpeta contiene el código fuente de tu proyecto. Está dividido en los siguientes archivos:

  - `__init__.py`: Un archivo vacío que indica que esta carpeta es un paquete de Python.
  - `password_generator.py`: Contendrá funciones y clases relacionadas con la generación de contraseñas. Aquí definirás funciones generales que se utilizan en todas las versiones.
  - `version_1.py`, `version_2.py`, etc.: Cada archivo corresponde a una versión específica del generador de contraseñas y contiene las implementaciones específicas de cada versión.

- [.gitignore](https://github.com/AlexCapis/Generador-claves/blob/main/.gitignore): En el se muestran todos los archivos ignorados.

-  [`visualizacion_negocio.py`](https://github.com/AlexCapis/Generador-claves/blob/main/visualizacion_negocio.py): Aquí podemos observar el código perteniente a Streamlit a través del cual realizamos la visualización de las distintas versiones del generados de contraseñas PASSODI.

## 5. Breve explicación de las diversas versiones

### Versión 1.0 - "El Fundamento"

Esta versión establece las bases del generador de contraseñas. Permite a los usuarios especificar la longitud deseada para la contraseña y genera contraseñas aleatorias seguras que incluyen una combinación de letras (mayúsculas y minúsculas), dígitos y caracteres especiales.

[Ver explicación detallada](notebooks/version_1.0.ipynb)

### Versión 2.0 - "Potenciando la Versatilidad"

En la Versión 2.0, se mejoran las contraseñas generadas al garantizar la inclusión de al menos una letra minúscula, una mayúscula, un número y un carácter especial. Los usuarios también pueden personalizar la longitud exacta que desean para sus contraseñas.

[Ver explicación detallada](notebooks/version_2.0.ipynb)

### Versión 3.0 - "Personalización Avanzada"

La Versión 3.0 introduce opciones avanzadas que permiten a los usuarios personalizar la longitud y los tipos de caracteres en sus contraseñas, incluyendo la posibilidad de excluir caracteres ambiguos para una mayor claridad y seguridad.

[Ver explicación detallada](notebooks/version_3.0.ipynb)

### Versión en Desarrollo: Versión 4.0 con Inteligencia Artificial

En la Versión 4.0, estamos trabajando en la implementación de inteligencia artificial para optimizar la generación de contraseñas y mejorar la fortaleza y seguridad de las contraseñas generadas. Además, planeamos incorporar contraseñas desechables ideales para situaciones de un solo uso o temporales.

## 6. Demostración en video

A continuación, puedes observar cómo se han implementado las diversas versiones del generador de contraseñas a través de Streamlit. Esta demostración te permitirá visualizar el proyecto de manera dinámica y comprender su funcionamiento de forma rápida y sencilla.

![Demostración en Video](docs/generador_contraseñas.gif) 

Siéntete libre de explorar las características de cada versión y cómo ha evolucionado el generador de contraseñas. Cada versión aporta mejoras significativas para garantizar contraseñas seguras y fáciles de usar.

## 7. Agradecimientos

Espero que este proyecto te resulte útil y te sirva de ayuda. ¡Explora el contenido y siéntete libre de utilizar esta información para tomar decisiones informadas!
