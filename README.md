Trabajo Practico - Integrador 2
Alumnos: Roqué, Gabriel Osvaldo / Comision 5 - Airalde, Milagros Abril / Comision 1
Link al video: https://youtu.be/xpUfarlD2zI
Responsabilidades de los integrantes

Gabriel:
-Cálculo de la unión y la intersección de los conjuntos.
-Elaboración de los diagramas de Venn para unión e intersección (dibujados a mano e insertados como imágenes).
-Definición y evaluación de las expresiones lógicas 1 ("Alta diversidad numérica") y 3 ("Grupo sin ceros").
-Creación y prueba del código Python en Visual Studio Code, incluyendo el ingreso dinámico de nombres, DNIs y años de nacimiento, y la modularización en dos archivos.
Milagros:
-Cálculo de las diferencias (1-2, 2-1) y la diferencia simétrica.
-Elaboración de los diagramas de Venn para diferencias y diferencia simétrica (dibujados a mano e insertados como imágenes).
-Implementación y verificación del conteo de frecuencias (ordenadas) y suma de números en el código Python.
-Definición y evaluación de las expresiones lógicas 2 ("Número común significativo") y 4 ("Mayor diversidad exclusiva").
Ambos:
-Definición y evaluación de la expresión lógica 5 ("Grupo completo").
-Inserción de las imágenes de los diagramas de Venn en Google Docs.
-Colaboración en la redacción del documento, la implementación de la Parte 2B y la preparación del programa Python.

Relación entre expresiones lógicas y código  
- Expresión 1: Implementada con `if len(conjunto_1) >= 5 and len(conjunto_2) >= 5`. Verifica si ambos conjuntos tienen al menos 5 números.  
- Expresión 2: Implementada con `if len(interseccion) > 3`. Evalúa si la intersección tiene más de 3 números.  
- Expresión 3: Implementada con `if '0' not in conjunto_1 or '0' not in conjunto_2`. Comprueba si al menos un conjunto no contiene el número 0.  
- Expresión 4: Implementada con `if len(diferencia_simetrica) > len(interseccion)`. Compara la cantidad de números en la diferencia simétrica y la intersección.  
- Expresión 5: Implementada con `if len(union) == 10`. Verifica si la unión contiene todos los números del 0 al 9.
