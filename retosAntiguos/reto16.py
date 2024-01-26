"""
/*
 * Crea una función que calcule y retorne cuántos días hay entre dos cadenas
 * de texto que representen fechas.
 * - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
 * - La función recibirá dos String y retornará un Int.
 * - La diferencia en días será absoluta (no importa el orden de las fechas).
 * - Si una de las dos cadenas de texto no representa una fecha correcta se
 *   lanzará una excepción.
 */
"""
import datetime

def diffDate(date1,date2):
    
    try:
        #date1=list(map(int, date1.split("/")))
        #date2=list(map(int, date2.split("/")))
        date1=datetime.datetime.strptime(date1,'%d/%m/%Y')
        date2=datetime.datetime.strptime(date2,'%d/%m/%Y')
        return print(f"la diferencia de dias es: {abs(date1-date2)}")
    except:
        print("La fecha no es la correcta, formato dd/MM/yyyy")

diffDate("01/05/2023","10/11/2023")
