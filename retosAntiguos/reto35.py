"""
/*
 * Dado un array de enteros ordenado y sin repetidos,
 * crea una función que calcule y retorne todos los que faltan entre
 * el mayor y el menor.
 * - Lanza un error si el array de entrada no es correcto.
 */
"""
def fun(lista):
    lista2=[]
    lista3=[]
    if lista==sorted(lista) and len(lista)==len(set(lista)): #verifica que la lista este ordenada y tenga elementos unicos
        lista2=[x for x in range (lista[0],lista[-1]+1)]
        #forma resumida del bucle a continuación => lista3 = [x for x in lista2 if x not in lista]
        for i in lista2:
            if i not in lista:
                lista3.append(i)
        return lista3
    else:
        return "La entrada no es correcta, debe estar ordenado y no repetido"

#ejemplo
print(fun([2,3,4,5,6,10]))