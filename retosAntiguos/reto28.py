"""
/*
 * Crea un programa que determine si dos vectores son ortogonales.
 * - Los dos array deben tener la misma longitud.
 * - Cada vector se podría representar como un array. Ejemplo: [1, -2]
 */
"""
def isOrtogonal(list1, list2):
    try:
        if len(list1)==2 and len(list2)==2 and type(list1)==list and type(list2)==list:
            if list1[0]*list2[0]+list1[1]*list2[1]==0:
                return print("Son ortogonales")
        else:
            raise AttributeError
    except AttributeError:
        return print("valores incorrectos")

isOrtogonal([1, -2],[6, 3])
isOrtogonal([1, -2,0],[6, 3])

