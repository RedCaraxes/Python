"""
/*
 * Crea una función que ordene y retorne una matriz de números.
 * - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro
 *   adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor
 *   o de mayor a menor.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan
 *   automáticamente.
 */
"""

def order_matrix(list1, param):
    for i in range (len(list1)-1):
        for j in range (len(list1)-1-i):
            if list1[j]>list1[j+1]:
                list1[j], list1[j+1]=list1[j+1], list1[j]
    if param=="Asc":
        return list1
    elif param=="Desc":
        inverted=[x for x in list1[::-1]]
        return inverted
    
n=order_matrix([2, 4, 1, 8, 0], "Asc")
print(n)
m=order_matrix([2, 4, 1, 8, 0], "Desc")
print(m)
