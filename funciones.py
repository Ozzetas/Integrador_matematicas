# Funciones auxiliares para el Trabajo Integrador 2
# Contiene las funciones para contar frecuencias, sumar números y verificar años bisiestos

# Función para contar la frecuencia de cada número en un DNI
def contar_frecuencias(dni):
    frecuencias = {}  # Diccionario para almacenar frecuencias
    for numero in dni:  # Iterar por cada número del DNI
        frecuencias[numero] = frecuencias.get(numero, 0) + 1  # Incrementar la cuenta
    # Devolver un diccionario ordenado por clave (número) de menor a mayor
    return dict(sorted(frecuencias.items()))

# Función para sumar los números de un DNI
def sumar_numeros(dni):
    total = 0  # Variable para acumular la suma
    for numero in dni:  # Iterar por cada número del DNI
        total += int(numero)  # Convertir a entero y sumar
    return total

# Función para verificar si un año es bisiesto
def es_bisiesto(anio):
    # Un año es bisiesto si es divisible por 4 y no por 100, o si es divisible por 400
    if anio % 4 == 0:  # Si es divisible por 4
        if anio % 100 == 0:  # Si también es divisible por 100
            return anio % 400 == 0  # Debe ser divisible por 400
        return True  # Si no es divisible por 100, es bisiesto
    return False  # Si no es divisible por 4, no es bisiesto