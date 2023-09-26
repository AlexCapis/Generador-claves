
# PASSODI: ¡Tu Escudo Digital!

![Logo](/docs/passodi_logo.png)

#### Autor: [Alex Marzá Manuel](https://github.com/AlexCapis)

## ÍNDICE

1. [Introducción](#1-introducción)
2. [Desarrollo](#2-desarrollo)


3. [Estructura de carpetas](#3-estructura-de-carpetas)



4. [Breve explicación de las diversas versiones](#4-breve-explicación-de-las-diversas-versiones)

5. [Demostración en video](#5-demostración-en-video)
    

6. [Agradecimientos](#agradecimientos)

---

## 1. Introducción

### Descripción del proyecto

PASSODI es un proyecto que busca proporcionar a los usuarios una forma segura y conveniente de generar contraseñas sólidas para proteger sus cuentas en línea. En el mundo digital actual, la seguridad es de suma importancia, y las contraseñas seguras son esenciales para garantizar esa seguridad. Este proyecto aborda esta necesidad ofreciendo un generador de contraseñas robusto y fácil de usar.

## 2. Desarrollo

### ¿Qué dificultades podemos encontrar?

Durante el desarrollo de PASSODI, podríamos enfrentar desafíos como la optimización del algoritmo de generación de contraseñas, asegurando la eficiencia y seguridad en todas las versiones, y también la implementación exitosa de la inteligencia artificial para futuras versiones.

## 3. Estructura de carpetas

- [app](): El contenido de dicha carpeta es la visualización de todas las distintas versiones del generador de contraseñas a través de la aplicación web de Streamlit.


- [notebooks](): Esta carpeta alberga los notebooks de Jupyter utilizados para documentar y explicar el proyecto. Cada versión del generador de contraseñas tendrá su propio notebook correspondiente. El notebook `funcionamiento_generar_claves.ipynb` proporciona una descripción general y enlaces a las versiones específicas.

- [src](): Esta carpeta contiene el código fuente de tu proyecto. Está dividido en los siguientes archivos:

  - `__init__.py`: Un archivo vacío que indica que esta carpeta es un paquete de Python.
  - `password_generator.py`: Contendrá funciones y clases relacionadas con la generación de contraseñas. Aquí definirás funciones generales que se utilizan en todas las versiones.
  - `version_1.py`, `version_2.py`, etc.: Cada archivo corresponde a una versión específica del generador de contraseñas y contiene las implementaciones específicas de cada versión.

- [docs](): Esta carpeta se utiliza para almacenar datos adicionales que puedan ser necesarios para el proyecto..

- [requirements.txt](): Lista las bibliotecas de Python necesarias para ejecutar tu proyecto.

## 4. Breve explicación de las diversas versiones

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



## 5. Demostración en video

A continuación podrás observar como se han implementado las diversas versiones a través de Streamlit con el fin de poder visualizar el trabajo de una forma dinámica, rápida y sencilla. 

![Demostración en Video](docs/generador_contraseñas.gif)

## Demostración en Video

A continuación, puedes observar cómo se han implementado las diversas versiones del generador de contraseñas a través de Streamlit. Esta demostración te permitirá visualizar el proyecto de manera dinámica y comprender su funcionamiento de forma rápida y sencilla.

[![Demostración en Video](docs/generador_contraseñas.gif)](https://link_to_your_video) 


Siéntete libre de explorar las características de cada versión y cómo ha evolucionado el generador de contraseñas. Cada versión aporta mejoras significativas para garantizar contraseñas seguras y fáciles de usar.

¿Tienes alguna pregunta o sugerencia sobre el funcionamiento de las versiones? ¡No dudes en comentar y compartir tus ideas!

## 6. Agradecimientos

Espero que este proyecto te resulte útil y te sirva de ayuda. ¡Explora el contenido y siéntete libre de utilizar esta información para tomar decisiones informadas!

---
