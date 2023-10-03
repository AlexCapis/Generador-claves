import streamlit as st
import string
import random

st.set_page_config(page_title="PASSODI", page_icon=":key:", layout="wide")

# Ponemos un titulo a nuestra aplicación
st.title("Descubre PASSODI: Tu Escudo Digital:shield:")

# Texto de explicación
texto = """

"""
st.write(texto)

menu = st.sidebar.selectbox("Selecciona la Página", ['HOME', 'VERSIÓN 1.0', 'VERSIÓN 2.0', 'VERSIÓN 3.0'])

# Variable de control para ocultar o mostrar el contenido de HOME
mostrar_home = True

# Contenido de la versión 1.0
if menu == 'VERSIÓN 1.0':
    mostrar_home = False
    st.header(":globe_with_meridians: Versión 1.0: El Fundamento")

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
    longitud_deseada = st.number_input(":key: Ingresa la longitud deseada para la contraseña (mínimo 5 caracteres):", min_value=5, value=15)

    # Botón para generar la contraseña
    if st.button("Generar Contraseña Sencilla"):
        contrasena_generada = generar_contrasena(longitud_deseada)
        st.success("La contraseña generada contiene {} caracteres y es la siguiente: {}:".format(longitud_deseada, contrasena_generada))



# Contenido de la versión 1.0
if menu == 'VERSIÓN 2.0': 
    mostrar_home = False
    st.header(":lock: Versión 2.0: Potenciando la Versatilidad")

    texto_version_2= '''
En esta versión, hemos realizado mejoras significativas en el generador de contraseñas. Las principales características de la "Versión 2.0" incluyen:

- **Caracteres Obligatorios:** Ahora, cada contraseña generada contendrá al menos una letra minúscula, una mayúscula, un número y un carácter especial. Esto garantiza que las contraseñas sean aún más seguras y resistentes a los ataques.

- **Longitud Personalizada:** Hemos escuchado a nuestros usuarios y les ofrecemos la posibilidad de especificar la longitud exacta que desean para sus contraseñas. ¡Tú tienes el control total!

- **Generación Eficiente:** Hemos optimizado el proceso de generación para que obtengas contraseñas seguras en menos tiempo.

    '''
    st.markdown(texto_version_2)

    # Función para generar contraseñas seguras
    def generar_contrasena(longitud):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        contrasena = ''

        # Permitimos al usuario especificar la longitud total deseada de la contraseña
        longitud -= 4  # Restamos 4 para tener en cuenta las categorías obligatorias
        if longitud < 1:
            st.warning(":warning: La longitud deseada es demasiado corta para generar una contraseña segura. Mínimo debe contener 5 caracteres.")
            return None

        contrasena += random.choice(string.ascii_lowercase)  # Agregar una minúscula
        contrasena += random.choice(string.ascii_uppercase)  # Agregar una mayúscula
        contrasena += random.choice(string.digits)  # Agregar un número
        contrasena += random.choice(string.punctuation)  # Agregar un carácter especial

        # Generar el resto de la contraseña
        for _ in range(longitud):
            contrasena += random.choice(caracteres)
        
        # Mezclar los caracteres de la contraseña
        contrasena_lista = list(contrasena)
        random.shuffle(contrasena_lista)
        contrasena = ''.join(contrasena_lista)
        
        return contrasena

    # Interacción con el usuario para ingresar la longitud deseada de la contraseña
    longitud_deseada = st.number_input(":key: Ingresa la longitud deseada para la contraseña (mínimo 5 caracteres):", min_value=5, value=12)

    # Botón para generar la contraseña
    if st.button("Generar Contraseña Versatil"):
        contrasena_generada = generar_contrasena(longitud_deseada)
        if contrasena_generada:
            st.success("La contraseña generada contiene {} caracteres y es la siguiente: {}:".format(longitud_deseada, contrasena_generada))

    # Nota explicativa
    st.markdown(":bulb: **Recuerda** que una contraseña segura debe contener una combinación de letras mayúsculas y minúsculas, números y caracteres especiales.")


# Contenido de la versión 3.0
if menu == 'VERSIÓN 3.0':
    mostrar_home = False
    st.header(":gear: Versión 3.0: Personalización Avanzada")

    texto_version_3 = '''
    En esta nueva versión, hemos realizado mejoras significativas en el generador de contraseñas. Las principales características de la "Versión 3.0" incluyen:

    - **Personaliza la Longitud:** Ahora puedes decidir exactamente cuántos caracteres deseas en tus contraseñas. ¡Tú tienes el control total de su longitud!

    - **Selecciona los Tipos de Caracteres:** Elige entre varios tipos de caracteres para incluir en tu contraseña, como letras minúsculas, mayúsculas, números y caracteres especiales. ¡Adáptala a tus necesidades!

    - **Excluye Caracteres Ambiguos:** Evita la confusión al excluir caracteres ambiguos como 'l', 'I', '1', '0', 'O' y 'o' de tus contraseñas. ¡Mantén la claridad!

    '''
    
    st.markdown(texto_version_3)


    def generar_contrasena(longitud, usar_mayusculas=True, usar_numeros=True, usar_especiales=True, excluye_ambiguos=True):
        # Define los conjuntos de caracteres disponibles
        caracteres = string.ascii_lowercase  # Inicialmente, solo incluye letras minúsculas
        
        # Agrega letras mayúsculas, números y caracteres especiales según las preferencias del usuario
        if usar_mayusculas:
            caracteres += string.ascii_uppercase
        if usar_numeros:
            caracteres += string.digits
        if usar_especiales:
            caracteres += string.punctuation
        
        # Excluye caracteres ambiguos si se selecciona esta opción
        if excluye_ambiguos:
            caracteres = ''.join(c for c in caracteres if c not in 'lI10Oo')
        
        # Verifica si la longitud especificada es suficiente
        if longitud < 4:
            print("La longitud deseada es demasiado corta para generar una contraseña segura. Mínimo debe ser 4.")
            return None
        
        contrasena = []
        
        # Asegura que haya al menos un carácter de cada tipo seleccionado
        if usar_mayusculas:
            contrasena.append(random.choice(string.ascii_uppercase))
        if usar_numeros:
            contrasena.append(random.choice(string.digits))
        if usar_especiales:
            contrasena.append(random.choice(string.punctuation))
        
        # Genera el resto de la contraseña
        while len(contrasena) < longitud:
            contrasena.append(random.choice(caracteres))
        
        # Mezcla los caracteres de la contraseña para mayor seguridad
        random.shuffle(contrasena)
        
        contrasena = ''.join(contrasena)
        return contrasena


        # Interacción con el usuario para configurar las preferencias de contraseña
    st.markdown("<h3 style='color: blue;'>Configura las preferencias de tu contraseña:</h3>", unsafe_allow_html=True)
    longitud_personalizada = st.number_input(" :key: Ingresa la longitud deseada para la contraseña (mínimo 5 caracteres):", min_value=5, value=12)
    usar_mayusculas = st.checkbox(":ab: Incluir letras mayúsculas")
    usar_numeros = st.checkbox(":1234: Incluir números")
    usar_especiales = st.checkbox(":heavy_plus_sign: Incluir caracteres especiales")
    excluye_ambiguos = st.checkbox(":warning: Excluir caracteres ambiguos (l, I, 1, 0, O)")

        # Botón para generar la contraseña personalizada
    if st.button("Generar Contraseña Personalizada"):
        contrasena_generada = generar_contrasena(longitud_personalizada, usar_mayusculas, usar_numeros, usar_especiales, excluye_ambiguos)
        st.success("La contraseña generada contiene {} caracteres y es la siguiente: {}:".format(longitud_personalizada, contrasena_generada))





# Contenido de HOME
if mostrar_home:
    # Ponemos una imagen
    imagen = "docs/passodi_logo.png"
    imagen_cargada = st.image(imagen)

    texto_home = '''
    Esta es la página de inicio de PASSODI, una aplicación para generar contraseñas seguras. Puedes seleccionar una de las versiones disponibles en el menú lateral para conocer más sobre cada versión y su funcionalidad.

    :mag: ¡Explora las distintas versiones y descubre cómo PASSODI puede ayudarte a proteger tus contraseñas!

    
    '''
    st.write(texto_home)

