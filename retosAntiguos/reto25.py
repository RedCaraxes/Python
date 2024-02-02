"""
/*
 * Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno).
 * ¿De cuántas maneras eres capaz de hacerlo?
 * Crea el código para cada una de ellas.
 */
"""
"*****1*****"
for i in range (1,101):
    print(f"{i} ",end="")

"*****2*****"
j=0
while j<101:
    print(f"{j} ",end="")
    j+=1

"*****3*****"
print([x for x in range(1,101)])

"*****4*****"
def print100(n):
    if (n<=100):
        print(n,end=" ")
        print100(n+1)
print100(1)