"""/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como
 * variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime
 *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
 *   su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */"""

"""signación de Variables "Por Valor" y "Por Referencia" en Python
En Python, el comportamiento de las variables depende del tipo de dato:
🔹 Tipos inmutables (se pasan por valor): int, float, str, tuple, bool
🔹 Tipos mutables (se pasan por referencia): list, dict, set"""

def modificar_valor(numero):
    numero += 10  # Se crea una nueva variable local, no modifica la original
    print(f"Dentro de la función: {numero}")

num = 5
modificar_valor(num)
print(f"Fuera de la función: {num}")  # Sigue siendo 5 (no se modificó)

def modificar_lista(lista):
    lista.append(99)  # Se modifica la lista original
    print(f"Dentro de la función: {lista}")

mi_lista = [1, 2, 3]
modificar_lista(mi_lista)
print(f"Fuera de la función: {mi_lista}")  # Se modificó la lista original

# Como evitar modificaciones

def modificar_lista(lista):
    lista = lista.copy()  # Crea una copia, sin afectar la original
    lista.append(99)
    print(f"Dentro de la función: {lista}")

mi_lista = [1, 2, 3]
modificar_lista(mi_lista)
print(f"Fuera de la función: {mi_lista}")  # No se modificó la lista original

# DIFICULTAD EXTRA

def saludo(mensaje, usuarios):
    mensaje = mensaje.upper()
    usuarios[0] = usuarios[0].upper()
    resultado = ""
    for usuario in usuarios:
        resultado += f"{mensaje} {usuario} "
    return resultado

nombres = ["pedro","juan"]
mensaje = "Hola"

texto_final = saludo(mensaje, nombres)
print(texto_final)
print(mensaje)
print(nombres)

