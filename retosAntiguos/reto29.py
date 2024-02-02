"""
/*
 * Simula el funcionamiento de una máquina expendedora creando una operación
 * que reciba dinero (array de monedas) y un número que indique la selección
 * del producto.
 * - El programa retornará el nombre del producto y un array con el dinero
 *   de vuelta (con el menor número de monedas).
 * - Si el dinero es insuficiente o el número de producto no existe,
 *   deberá indicarse con un mensaje y retornar todas las monedas.
 * - Si no hay dinero de vuelta, el array se retornará vacío.
 * - Para que resulte más simple, trabajaremos en céntimos con monedas
 *   de 5, 10, 50, 100 y 200.
 * - Debemos controlar que las monedas enviadas estén dentro de las soportadas.
 */
"""
def productValue(item,op):
    products={1:(25,"papas"),2:(50,"refresco"),3:(80,"coca"),4:(110,"choco"),5:(150,"helado"),6:(200,"milkshake")}
    if op=="cost":
        return products.get(item)[0]
    elif op=="product":
        return products.get(item)[1]


def machine(list1, product):
    monedas=[5, 10, 50, 100, 200]
    presupuesto=sum(list1)
    try:
        if presupuesto>=productValue(product,"cost"):
            presupuesto=presupuesto-productValue(product,"cost")
            if presupuesto==0:
                return None
            else:
                vuelto=[]
                for elem in monedas[::-1]:
                    while presupuesto>=elem:
                        vuelto.append(elem)
                        presupuesto-=elem
                return productValue(product,"product"),vuelto
        else:
            return "No puede comprar este producto", presupuesto
    except:
        return f"el producto {product} no existe"

a=machine([5,5,100,100],1)
print(a)
b=machine([5,5,100,100],7)
print(b)
c=machine([5,5,100],6)
print(c)