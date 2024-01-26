"""
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
"""
def isAnagrama(string1, string2):
    if string1==string2:
        return False
    return sorted(string1.lower())==sorted(string2.lower())

string1="amor"
string2="roma"

print(f" la palabra {string1} y {string2} son anagramas? : {isAnagrama(string1, string2)}" )
