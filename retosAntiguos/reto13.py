"""
/*
 * Escribe una función que reciba un texto y retorne verdadero o
 * falso (Boolean) según sean o no palíndromos.
 * Un Palíndromo es una palabra o expresión que es igual si se lee
  * de izquierda a derecha que de derecha a izquierda.
 * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
 * Ejemplo: Ana lleva al oso la avellana.
 */
"""
def isPalidrome(str):
    str=list(str.lower())
    while " " in str:
            str.remove(" ")
    str_i=list(reversed(str))
    if str==str_i:
          return True
    else:
          return False
    
print(isPalidrome("Ana lleva al oso la avellana"))
print(isPalidrome("Oso Baboso"))

