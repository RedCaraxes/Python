"""
/*
 * Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su
 * resultado e imprímelo.
 * - El .txt se corresponde con las entradas de una calculadora.
 * - Cada línea tendrá un número o una operación representada por un
 *   símbolo (alternando ambos).
 * - Soporta números enteros y decimales.
 * - Soporta las operaciones suma "+", resta "-", multiplicación "*"
 *   y división "/".
 * - El resultado se muestra al finalizar la lectura de la última
 *   línea (si el .txt es correcto).
 * - Si el formato del .txt no es correcto, se indicará que no se han
 *   podido resolver las operaciones.
 */
"""
def calcular_resultado(entrada):
    resultado = 0
    operacion_pendiente = None

    for linea in entrada:
        linea = linea.strip()
        if not linea:
            continue  # Ignorar líneas vacías

        try:
            valor = float(linea)
            if operacion_pendiente is None:
                resultado = valor
            else:
                if operacion_pendiente == '+':
                    resultado += valor
                elif operacion_pendiente == '-':
                    resultado -= valor
                elif operacion_pendiente == '*':
                    resultado *= valor
                elif operacion_pendiente == '/':
                    resultado /= valor
                else:
                    raise ValueError("Operación no válida")
                operacion_pendiente = None
        except ValueError:
            # Si no es un número, asumimos que es una operación
            if linea in ['+', '-', '*', '/']:
                operacion_pendiente = linea
            else:
                raise ValueError("Símbolo no válido")

    if operacion_pendiente is not None:
        raise ValueError("Operación incompleta")

    return resultado



try:
    with open("retosAntiguos/challenge21.txt", "r") as archivo:
        resultado = calcular_resultado(archivo)
        print("El resultado es:", resultado)
except FileNotFoundError:
    print("No se pudo encontrar el archivo.")
except ValueError as e:
    print("No se pudieron resolver las operaciones:", e)