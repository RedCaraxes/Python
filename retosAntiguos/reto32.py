"""
/*
 * Crea una función que imprima los 30 próximos años bisiestos
 * siguientes a uno dado.
 * - Utiliza el menor número de líneas para resolver el ejercicio.
 */
"""
def bisiesto(año):
    for a in range (año,(año+30)):
        if (not a % 4 and (a % 100 or not a % 400)):
            print(a)
    return "terminado"
n=bisiesto(1840)
print(n)