"""
/*
 * Crea una función que analice una matriz 3x3 compuesta por "X" y "O"
 * y retorne lo siguiente:
 * - "X" si han ganado las "X"
 * - "O" si han ganado los "O"
 * - "Empate" si ha habido un empate
 * - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta.
 *   O si han ganado los 2.
 * Nota: La matriz puede no estar totalmente cubierta.
 * Se podría representar con un vacío "", por ejemplo.
 */
"""
def rev(matriz):
    tmatriz=list(zip(*matriz))
    if (fila.count("o") for fila in matriz)==(fila.count("x") for fila in matriz) or abs(sum([fila.count("o") - fila.count("x") for fila in matriz]))<2:
        if (["o","o","o"] in matriz)==1 or (["o","o","o"] in tmatriz)==1 or matriz[0][0]==matriz[1][1]==matriz[2][2]=="o":
            if (["x","x","x"] in matriz)==1 or (["x","x","x"] in matriz)==1 or matriz[0][0]==matriz[1][1]==matriz[2][2]=="x":
                print("Empate")
            else:
                print("ha ganado O")

        elif (["x","x","x"] in matriz)==1 or (["x","x","x"] in matriz)==1 or matriz[0][0]==matriz[1][1]==matriz[2][2]=="x":
            if (["o","o","o"] in matriz)==1 or (["o","o","o"] in tmatriz)==1 or matriz[0][0]==matriz[1][1]==matriz[2][2]=="o":
                print("Empate")
            else:
                print("ha ganado X")
        else:
            print("empate")
    else:
        return print("invalid!!!")
a=[["x","x","x"],["o","x","o"],["o","o","x"]]
b=[["x","o","x"],["o","o","o"],["o","o","x"]]  
c=[["x","x","x"],["o","o","o"],["o","o","x"]]
d=[["x","x","x"],["o",None,"o"],["o",None,"x"]]
rev(a)
rev(b)
rev(c)
rev(d)



