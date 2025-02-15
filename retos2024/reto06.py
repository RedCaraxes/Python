"""/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 */"""

def cuenta_regresiva(numero):
    if numero < 0:
        return
    print(numero)
    cuenta_regresiva(numero-1)

numero = 100
cuenta_regresiva(100)

# DIFICULTAD EXTRA

"""Ejemplo: Calcular el factorial de un número (n! = n × (n-1)!).

Subproblema: 5! = 5 × 4!, 4! = 4 × 3!, etc.
Caso base: 1! = 1 (cuando n = 1)."""

def factorial(n):
    if n == 0 or n == 1:  
        return 1
    return n * factorial(n - 1)  


def fibonacci(n):
    if n <= 0:
        return "La posición debe ser mayor a 0"
    elif n == 1:
        return 0  # Primer número de Fibonacci es 0
    elif n == 2:
        return 1  # Segundo número de Fibonacci es 1
    return fibonacci(n - 1) + fibonacci(n - 2)  # Llamada recursiva

# Ejemplo: Obtener el 10º número de Fibonacci
posicion = 10
resultado = fibonacci(posicion)
print(f"El término {posicion} de Fibonacci es: {resultado}")