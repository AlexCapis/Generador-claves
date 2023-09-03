
import random
import string

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

# Solicita al usuario la longitud deseada para la contraseña y las preferencias de caracteres
longitud_deseada = int(input("Ingresa la longitud deseada para la contraseña: "))
usar_mayusculas = input("¿Usar letras mayúsculas? (S/n): ").strip().lower() != 'n'
usar_numeros = input("¿Usar números? (S/n): ").strip().lower() != 'n'
usar_especiales = input("¿Usar caracteres especiales? (S/n): ").strip().lower() != 'n'
excluye_ambiguos = input("¿Excluir caracteres ambiguos? (S/n): ").strip().lower() != 'n'

# Llama a la función generar_contrasena con las preferencias especificadas por el usuario
contrasena_generada = generar_contrasena(longitud_deseada, usar_mayusculas, usar_numeros, usar_especiales, excluye_ambiguos)

# Muestra la contraseña generada
print("Su contraseña generada es:", contrasena_generada)
