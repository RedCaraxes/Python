"""
/*
 * Escribe una función que calcule si un número dado es un número de Armstrong
 * (o también llamado narcisista).
 * Si no conoces qué es un número de Armstrong, debes buscar información
 * al respecto.
 */
"""
def numberArmstrong(n:int):
    l=len(str(n))
    nl=list(str(n))
    calc=0
    for i in nl:
        calc+=int(i)**l
    if calc==n:
        print("es un numero Armstrong")
    else:
        print("no es Armstrong")

numberArmstrong(153)
numberArmstrong(370)
numberArmstrong(111)