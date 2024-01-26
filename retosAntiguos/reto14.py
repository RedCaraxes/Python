"""
/*
 * Escribe una función que calcule y retorne el factorial de un número dado
 * de forma recursiva.
 */
"""
def factorial(number: int):
    if (number<0):
        return None 
    elif (number<=1):
        return 1 
    else:
        return number*factorial(number-1)
    
resultado = factorial(5)
print(resultado) 

resultado = factorial(-3)
print(resultado)  