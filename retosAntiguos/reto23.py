"""
/*
 * Crea una función que reciba dos array, un booleano y retorne un array.
 * - Si el booleano es verdadero buscará y retornará los elementos comunes
 *   de los dos array.
 * - Si el booleano es falso buscará y retornará los elementos no comunes
 *   de los dos array.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
 */
"""
def func(lista1, lista2, bolean):
    lista=[]
    if bolean==True:
        for i in lista1:
            if i in lista2:
                yield i
    else:
        for i in lista1:
            if i not in lista2:
                yield i
        for i in lista2:
            if i not in lista1:
                yield i

test1=func([1,2,3,4,5,6],[2,4,6,8], True)
print(list(test1))
test2=func([1,2,3,4,5,6],[2,4,6,8], False)
print(list(test2))