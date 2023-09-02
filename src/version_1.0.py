import random
import string




def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    resultado = "Tu contraseña contiene {} caracteres y es la siguiente: {}".format(longitud, contrasena)
    return resultado

generar_contrasena(int(input("Introduce el número de caracteres que quieres que contenga tu contraseña ")))

import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    print("Su contraseña generada es:", contrasena_generada)
    return contrasena

longitud_deseada = int(input("Ingresa la longitud deseada para la contraseña: "))
contrasena_generada = generar_contrasena(longitud_deseada)
print("Contraseña generada:", contrasena_generada)
