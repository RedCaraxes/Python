"""
/*
 * Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra
 * que calcule el mínimo común múltiplo (mcm) de dos números enteros.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
 */
"""
def mcm(num1, num2):
    try:
        div=1
        num1=int(num1)
        num2=int(num2)
        if num2>=num1:
            num1,num2=num2,num1
        for i in range(2,num1+1):
            while num1%i==0 or num2%i==0:
                if num1%i==0 and num2%i==0:
                    div*=i
                    num1=num1/i
                    num2=num2/i
                elif num2%i==0:
                    div*=i
                    num2=num2/i
                elif num1%i==0:
                    div*=i
                    num1=num1/i
        return print(str(div))
    except:
        print("valores invalidos")

def mcd(num1, num2):
    try:
        div=1
        num1=int(num1)
        num2=int(num2)
        if num2>=num1:
            num1,num2=num2,num1
        for i in range(2,num2+1):
            if num1==1 or num2==1:
                break
            while num1%i==0 or num2%i==0:
                if num1==1 or num2==1:
                    break
                elif num1%i==0 and num2%i==0:
                    div*=i
                    num1=num1/i
                    num2=num2/i
                elif num2%i==0:
                    div*=i
                    num2=num2/i
                elif num1%i==0:
                    div*=i
                    num1=num1/i
        return print(str(div))
    except:
        print("valores invalidos")

mcm(2,8)
mcm(21,24)
mcd(2,8)
mcd(1,8)
mcd(5,35)

"""SOLUCION MEJORADA: Esto sale en 2 patadas si conoces a euclides"""
def resumida_mcd(a, b):
    while b:
        a, b = b, a % b
    return a

def resumida_mcm(a, b):
    return abs(a*b) // resumida_mcd(a, b)
print(resumida_mcm(2,8))
print(resumida_mcm(21,24))
print(resumida_mcd(2,8))
print(resumida_mcd(1,8))
print(resumida_mcd(5,35))
