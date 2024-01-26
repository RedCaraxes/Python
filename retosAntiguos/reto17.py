"""
/*
 * Crea una función que reciba un String de cualquier tipo y se encargue de
 * poner en mayúscula la primera letra de cada palabra.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
 */
"""
def cap(str):
    nstr=""
    flag=1
    for i in str:
        if i==" ":
            flag=1
            nstr+=" "
        elif flag==1:
            nstr+=i.upper()
            flag=0
        else:
            nstr+=i
    return print(nstr)

cap("hola mundo cruel")
