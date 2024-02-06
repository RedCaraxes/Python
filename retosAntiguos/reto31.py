"""
/*
 * Crea una función que reciba un texto y muestre cada palabra en una línea,
 * formando un marco rectangular de asteriscos.
 * - ¿Qué te parece el reto? Se vería así:
 *   **********
 *   * ¿Qué   *
 *   * te     *
 *   * parece *
 *   * el     *
 *   * reto?  *
 *   **********
 */
"""

def format_text(string):
    text=string.split(" ")
    lenmayor="a"
    for i in range (len(text)-1):
        if len(text[i])>len(lenmayor):
            mayor=len(text[i])
            lenmayor=text[i]
    
    print("*"*(2*mayor))
    for j in text:
        print(f"*{j.center(2*mayor-2)}*")
    
    print("*"*(2*mayor))

format_text("¿Qué te parece el reto?")
