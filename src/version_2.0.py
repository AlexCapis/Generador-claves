import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    contrasena = ''

    # Permitimos al usuario especificar la longitud total deseada de la contraseña
    longitud -= 4  # Restamos 4 para tener en cuenta las categorías obligatorias
    if longitud < 1:
        print("La longitud deseada es demasiado corta para generar una contraseña segura. Mínimo debe contener 5 caracteres.")
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
    
    # print("Su contraseña generada es:", contrasena)
    return contrasena

# Solicita al usuario la longitud deseada para la contraseña
longitud_deseada = int(input("Ingresa la longitud deseada para la contraseña: "))

# Llama a la función generar_contrasena con la longitud especificada
contrasena_generada = generar_contrasena(longitud_deseada)
print("Contraseña generada:", contrasena_generada)
