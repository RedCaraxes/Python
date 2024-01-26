"""
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
"""

def esPrimo(numero):
    for i in range (2,numero):
        if numero%i==0:
            return False
    return True

for i in range (100):
    if esPrimo(i)==True:
        print(f"{i}, ",end="")