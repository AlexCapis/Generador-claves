import streamlit as st
import string
import random

st.set_page_config(page_title="PASSODI", page_icon=":key:", layout="wide")

# Ponemos un titulo a nuestra aplicación
st.title("Descubre PASSODI: Tu Escudo Digital")

# Texto de explicación
texto = """

"""
st.write(texto)

menu = st.sidebar.selectbox("Selecciona la Página", ['HOME', 'VERSIÓN 1.0', 'VERSIÓN 2.0', 'VERSIÓN 3.0', 'VERSIÓN 4.0'])

# Variable de control para ocultar o mostrar el contenido de HOME
mostrar_home = True

# Contenido de la versión 1.0
if menu == 'VERSIÓN 1.0':
    mostrar_home = False
    st.header(":shield: Versión 1.0: El Fundamento")

    texto_version_1 = '''
    Esta es la primera versión de PASSODI, un generador de contraseñas básico que consta de:

    - **Longitud de Contraseña Personalizada:** El usuario inicia el proceso ingresando la longitud deseada para la contraseña.

    - **Generación Aleatoria:** Nuestro generador selecciona aleatoriamente caracteres de entre letras minúsculas, mayúsculas, dígitos y caracteres especiales. Estos caracteres se combinan para crear la contraseña.

    - **Contraseña Generada:** La contraseña generada se muestra al usuario.
    '''
    st.markdown(texto_version_1)

    # Función para generar contraseñas
    def generar_contrasena(longitud):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
        return contrasena

    # Interacción con el usuario para ingresar la longitud deseada de la contraseña
    longitud_deseada = st.number_input(":key: Ingresa la longitud deseada para la contraseña, el mínimo permitido es 4 y el máximo 15:", min_value=4, value=15)

    # Botón para generar la contraseña
    if st.button("Generar Contraseña"):
        contrasena_generada = generar_contrasena(longitud_deseada)
        st.success("La contraseña generada contiene {} caracteres y es la siguiente: {}:".format(longitud_deseada, contrasena_generada))

# Contenido de HOME
if mostrar_home:
    # Ponemos una imagen
    imagen = "../docs/passodi_logo.png"
    imagen_cargada = st.image(imagen)

    texto_home = '''
    Esta es la página de inicio de PASSODI, una aplicación para generar contraseñas seguras. Puedes seleccionar una de las versiones disponibles en el menú lateral para conocer más sobre cada versión y su funcionalidad.

    ¡Explora las versiones y descubre cómo PASSODI puede ayudarte a proteger tus contraseñas!
    '''
    st.write(texto_home)








