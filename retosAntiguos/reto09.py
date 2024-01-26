"""
/*
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
 */
"""
def decToBin(decimal):
    bin=[]
    divisor=decimal
    while True:
        cociente=divisor//2
        residuo=divisor%2
        bin.append(str(residuo))
        divisor=cociente
        if(cociente<2):
            bin.append(str(divisor))
            break
        bin.reverse()
    return print("".join(bin))
decToBin(10)