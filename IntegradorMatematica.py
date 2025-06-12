# Trabajo Integrador 2: Matemática y Programación
# Integrantes: Gabriel y Milagros
# Este programa permite ingresar nombres, DNIs y años de nacimiento,
# genera conjuntos de números únicos, realiza operaciones de conjuntos,
# calcula frecuencias (ordenadas), sumas, evalúa expresiones lógicas,
# y realiza operaciones con años de nacimiento.
# Los conjuntos y frecuencias se muestran ordenados de menor a mayor.
# Las funciones auxiliares están en funciones.py.

from datetime import datetime
from funciones import contar_frecuencias, sumar_numeros, es_bisiesto

# --- Parte 2A: Validación y procesamiento de DNIs ---
# Pedir al usuario los nombres para los DNIs
nombre1 = input("Ingrese el nombre para el primer DNI: ")
nombre2 = input("Ingrese el nombre para el segundo DNI: ")

# Pedir al usuario que ingrese los DNIs
dni1 = input(f"Ingrese el DNI de {nombre1} (8 números): ")
dni2 = input(f"Ingrese el DNI de {nombre2} (8 números): ")

# Validar que el primer DNI tenga 8 números y sea solo numérico
while not (dni1.isdigit() and len(dni1) == 8):
    print(f"Error: El DNI de {nombre1} debe tener exactamente 8 números.")
    dni1 = input(f"Ingrese el DNI de {nombre1} (8 números): ")

# Validar que el segundo DNI tenga 8 números y sea solo numérico
while not (dni2.isdigit() and len(dni2) == 8):
    print(f"Error: El DNI de {nombre2} debe tener exactamente 8 números.")
    dni2 = input(f"Ingrese el DNI de {nombre2} (8 números): ")

# Crear conjuntos con los números únicos de cada DNI
conjunto_1 = set(dni1)  # Conjunto del primer DNI
conjunto_2 = set(dni2)  # Conjunto del segundo DNI

# Realizar operaciones con conjuntos
union = conjunto_1 | conjunto_2  # Unión: todos los números de ambos conjuntos
interseccion = conjunto_1 & conjunto_2  # Intersección: números comunes
diferencia_1_2 = conjunto_1 - conjunto_2  # Diferencia 1-2
diferencia_2_1 = conjunto_2 - conjunto_1  # Diferencia 2-1
diferencia_simetrica = conjunto_1 ^ conjunto_2  # Diferencia simétrica

# Mostrar los conjuntos y resultados, ordenados de menor a mayor
print(f"\nConjunto de {nombre1}: {sorted(conjunto_1)}")
print(f"Conjunto de {nombre2}: {sorted(conjunto_2)}")
print(f"Unión: {sorted(union)}")
print(f"Intersección: {sorted(interseccion)}")
print(f"Diferencia ({nombre1} - {nombre2}): {sorted(diferencia_1_2)}")
print(f"Diferencia ({nombre2} - {nombre1}): {sorted(diferencia_2_1)}")
print(f"Diferencia simétrica: {sorted(diferencia_simetrica)}")

# Calcular frecuencias (ordenadas) y sumas para cada DNI
frec_1 = contar_frecuencias(dni1)  # Frecuencias del primer DNI
frec_2 = contar_frecuencias(dni2)  # Frecuencias del segundo DNI
suma_1 = sumar_numeros(dni1)  # Suma del primer DNI
suma_2 = sumar_numeros(dni2)  # Suma del segundo DNI

# Mostrar frecuencias y sumas
print(f"\nFrecuencias de {nombre1}: {frec_1}")
print(f"Frecuencias de {nombre2}: {frec_2}")
print(f"Suma de números de {nombre1}: {suma_1}")
print(f"Suma de números de {nombre2}: {suma_2}")

# Evaluación de las expresiones lógicas
print("\nEvaluación de expresiones lógicas:")
# Expresión 1: Ambos conjuntos tienen al menos 5 números
if len(conjunto_1) >= 5 and len(conjunto_2) >= 5:
    print("Expresión 1: Verifica si ambos conjuntos tienen al menos 5 elementos.\nSe considera alta diversidad numérica.")
else:
    print("Expresión 1: Verifica si ambos conjuntos tienen al menos 5 elementos.\nNo se considera alta diversidad numérica.")

# Expresión 2: La intersección tiene más de 3 números
if len(interseccion) > 3:
    print("Expresión 2: Evalúa si la intersección tiene más de 3 elementos.\nHay un número común significativo.")
else:
    print("Expresión 2: Evalúa si la intersección tiene más de 3 elementos.\nNo hay un número común significativo.")

# Expresión 3: Algún conjunto no contiene el número 0
if '0' not in conjunto_1 or '0' not in conjunto_2:
    print("Expresión 3: Comprueba si al menos un conjunto no contiene el dígito 0.\nSe considera un grupo sin ceros.")
else:
    print("Expresión 3: Comprueba si al menos un conjunto no contiene el dígito 0.\nNo se considera un grupo sin ceros.")

# Expresión 4: La diferencia simétrica tiene más números que la intersección
if len(diferencia_simetrica) > len(interseccion):
    print("Expresión 4: Compara la cantidad de elementos en la diferencia simétrica y la intersección.\nHay mayor diversidad exclusiva.")
else:
    print("Expresión 4: Compara la cantidad de elementos en la diferencia simétrica y la intersección.\nVaya, no hay mayor diversidad exclusiva.")

# Expresión 5: La unión contiene todos los números del 0 al 9
if len(union) == 10:
    print("Expresión 5: Verifica si la unión contiene todos los dígitos del 0 al 9.\nSe considera un grupo completo.")
else:
    print("Expresión 5: Verifica si la unión contiene todos los dígitos del 0 al 9.\nNo se considera un grupo completo, faltan números.")

# --- Parte 2B: Validación y procesamiento de años de nacimiento ---
# Pedir al usuario los nombres para los años de nacimiento
print("\nAhora vamos con los años de nacimiento.")
nombre_anio1 = input("Ingrese el nombre para el primer año de nacimiento: ")
nombre_anio2 = input("Ingrese el nombre para el segundo año de nacimiento: ")

# Pedir y validar el primer año de nacimiento
anio1 = input(f"Ingrese el año de nacimiento de {nombre_anio1} (por ejemplo, 2000): ")
while not (anio1.isdigit() and 1900 <= int(anio1) <= datetime.now().year):
    print(f"Error: El año de {nombre_anio1} debe ser un número entre 1900 y {datetime.now().year}.")
    anio1 = input(f"Ingrese el año de nacimiento de {nombre_anio1} (por ejemplo, 2000): ")
anio1 = int(anio1)

# Pedir y validar el segundo año de nacimiento
anio2 = input(f"Ingrese el año de nacimiento de {nombre_anio2} (por ejemplo, 2002): ")
while not (anio2.isdigit() and 1900 <= int(anio2) <= datetime.now().year):
    print(f"Error: El año de {nombre_anio2} must be a number between 1900 and {datetime.now().year}.")
    anio2 = input(f"Ingrese el año de nacimiento de {nombre_anio2} (por ejemplo, 2002): ")
anio2 = int(anio2)

# Crear una lista con los años de nacimiento
anios = [anio1, anio2]

# Contar años pares e impares
pares = 0  # Contador para años pares
impares = 0  # Contador para años impares
for anio in anios:  # Iterar por cada año
    if anio % 2 == 0:  # Si el año es divisible por 2, es par
        pares += 1
    else:  # Si no, es impar
        impares += 1
print(f"\nAños pares: {pares}")
print(f"Años impares: {impares}")

# Verificar si ambos nacieron después del 2000 ("Grupo Z")
es_grupo_z = True  # Suponer que todos son después del 2000
for anio in anios:  # Verificar cada año
    if anio <= 2000:  # Si algún año es 2000 o anterior
        es_grupo_z = False
        break
if es_grupo_z:
    print("Grupo Z: Todos nacieron después del 2000.")
else:
    print("No todos nacieron después del 2000.")

# Verificar años bisiestos
for anio, nombre in zip(anios, [nombre_anio1, nombre_anio2]):  # Iterar por años y nombres
    if es_bisiesto(anio):
        print(f"Año {anio} de {nombre} es bisiesto: ¡Tenemos un año especial!")
    else:
        print(f"Año {anio} de {nombre} no es bisiesto.")

# Calcular edades y producto cartesiano
anio_actual = datetime.now().year  # Año actual (2025)
edades = [anio_actual - anio for anio in anios]  # Calcular edades
producto_cartesiano = [(anio, edad) for anio in anios for edad in edades]  # Producto cartesiano
print(f"Producto cartesiano (años, edades): {producto_cartesiano}")