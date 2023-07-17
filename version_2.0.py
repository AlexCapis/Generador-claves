
# VERSIÓN 2.0 he realizado que cada vez que se genere sea con el contenido de minúsculas, mayúsculas, números y caracteres especiales
# me faltaria un input() para el usuario introdujera la longitud que desee que tenga la contraseña

import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    contrasena = ''
    contrasena += random.choice(string.ascii_lowercase)  # Agregar una minúscula
    contrasena += random.choice(string.ascii_uppercase)  # Agregar una mayúscula
    contrasena += random.choice(string.digits)  # Agregar un número
    contrasena += random.choice(string.punctuation)  # Agregar un carácter especial

    # Generar el resto de la contraseña
    for _ in range(longitud - 4):
        contrasena += random.choice(caracteres)
    
    # Mezclar los caracteres de la contraseña
    contrasena_lista = list(contrasena)
    random.shuffle(contrasena_lista)
    contrasena = ''.join(contrasena_lista)
    
    print("Su contraseña generada es:", contrasena)
    return contrasena
