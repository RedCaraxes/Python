"""
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
"""
print("0, 1, ", end="")
a,b=0,1
for i in range(0,49):
    c=a+b
    print(f"{c}, ", end="")
    a,b=b,c

