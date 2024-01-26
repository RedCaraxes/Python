"""
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
"""
def areaPol(poligono):
    poligono=poligono.lower()
    if poligono=="triangulo":
        h=int(input("Ingrese la altura del triangulo: "))
        b=int(input("Ingrese la base del triangulo: "))
        return ((h*b)/2)
    elif poligono=="cuadrado":
        l=int(input("Ingrese el lado del cuadrado: "))
        return (l*l)
    elif poligono=="rectangulo":
        h=int(input("Ingrese la altura del rectangulo: "))
        b=int(input("Ingrese la base del rectangulo: "))
        return ((h*b))
    else:
        print("no ha introducido un poligono valido")

print(areaPol("triangulo"))
print(areaPol("Rectangulo"))
print(areaPol("Cuadrado"))