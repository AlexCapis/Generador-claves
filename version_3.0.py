

#VERSIÓN 3.0: en esta versión se trataría de que no aparezca ningun caracter repetido
# me faltaria un input() para el usuario introdujera la longitud que desee que tenga la contraseña


import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    contrasena = []

    # Agregar un número, una minúscula, una mayúscula y un carácter especial
    contrasena.append(random.choice(string.digits))  # Agregar un número
    contrasena.append(random.choice(string.ascii_lowercase))  # Agregar una minúscula
    contrasena.append(random.choice(string.ascii_uppercase))  # Agregar una mayúscula
    contrasena.append(random.choice(string.punctuation))  # Agregar un carácter especial

    # Generar el resto de la contraseña sin caracteres repetidos
    while len(contrasena) < longitud:
        nuevo_caracter = random.choice(caracteres)
        if nuevo_caracter not in contrasena:
            contrasena.append(nuevo_caracter)

    # Mezclar los caracteres de la contraseña
    random.shuffle(contrasena)

    contrasena = ''.join(contrasena)
    print("Su contraseña generada es:", contrasena)
    return contrasena