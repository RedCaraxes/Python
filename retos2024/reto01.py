"""
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
"""
a = 10
b = 3

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
modulo = a % b
potencia = a ** b

print("Operadores Aritméticos:")
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("Módulo:", modulo)
print("Potencia:", potencia)

x = 5
y = 10

# Operadores de comparación
igual = x == y
diferente = x != y
mayor_que = x > y
menor_o_igual_que = x <= y

print("\nOperadores de Comparación:")
print("Igualdad:", igual)
print("Diferente:", diferente)
print("Mayor que:", mayor_que)
print("Menor o igual que:", menor_o_igual_que)

# Operadores lógicos
p = True
q = False

and_op = p and q
or_op = p or q
not_op = not p

print("\nOperadores Lógicos:")
print("AND lógico:", and_op)
print("OR lógico:", or_op)
print("NOT lógico:", not_op)


# Operadores de asignación
x = 5
x += 3  # Equivalente a x = x + 3

# Operadores de identidad
lista1 = [1, 2, 3]
lista2 = lista1
es_mismo_objeto = lista1 is lista2

# Operadores de pertenencia
elemento_en_lista = 2 in lista1

# Operadores de bits
bitwise_and = 5 & 3
bitwise_or = 5 | 3
bitwise_xor = 5 ^ 3
bitwise_not = ~5

print("\nOtros Operadores:")
print("Operador de Asignación:", x)
print("Operador de Identidad (es el mismo objeto):", es_mismo_objeto)
print("Operador de Pertenencia (elemento en lista):", elemento_en_lista)
print("Operadores de Bits:")
print("AND a nivel de bits:", bitwise_and)
print("OR a nivel de bits:", bitwise_or)
print("XOR a nivel de bits:", bitwise_xor)
print("NOT a nivel de bits:", bitwise_not)

# Estructura condicional (if-elif-else)
if x > 0:
    print("\nEstructuras Condicionales:")
    print("x es positivo")
elif x < 0:
    print("x es negativo")
else:
    print("x es cero")

# Estructuras iterativas (for y while)
print("\nEstructuras Iterativas:")
print("Bucle for:")
for i in range(10):
    print(i, end=" ")

print("\nBucle while:")
num = 10
while num > 0:
    print(num, end=" ")
    num -= 1

# Manejo de excepciones (try-except-finally)
print("\nManejo de Excepciones:")
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: División por cero")
finally:
    print("Bloque finally siempre se ejecuta")

print("\nNúmeros entre 10 y 55, pares, no 16 ni múltiplos de 3:")
for num in range(10, 56):
    if num % 2 == 0 and num != 16 and num % 3 != 0:
        print(num, end=" ")
