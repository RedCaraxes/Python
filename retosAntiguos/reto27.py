"""
/*
 * Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
 * - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
 * - EXTRA: ¿Eres capaz de dibujar más figuras?
 */
"""

def dibujar_cuadrado(lado):
    for i in range(lado):
        print("*" * lado)

def dibujar_triangulo(base):
    for i in range(1, base + 1):
        print("*" * i)

figura = input("¿Qué figura quieres dibujar? (cuadrado/triangulo): ")
if figura.lower() == "cuadrado":
    lado = int(input("Introduce el tamaño del lado: "))
    print("Dibujando cuadrado:")
    dibujar_cuadrado(lado)
elif figura.lower() == "triangulo":
    base = int(input("Introduce la longitud de la base del triángulo: "))
    print("Dibujando triángulo:")
    dibujar_triangulo(base)
else:
    print("Figura no válida. Inténtalo de nuevo.")