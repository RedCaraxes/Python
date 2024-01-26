"""
/*
 * Crea una función que reciba dos cadenas como parámetro (str1, str2)
 * e imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO
 *   estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO
 *   estén presentes en str1.
 */
"""

def fun(str1,str2):
    str1=list(str1)
    str2=list(str2)
    out2=str2.copy()
    out1=[]
    for i in str1:
        if i not in str2:
            out1.append(i)
        elif i in out2:
            out2.remove(i)
    return print(out1,out2)

fun("pala","coca")
