"""/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */"""

# Definición de variables
variable = "Python"
CONSTANTE = 42  

# Tipos de datos primitivos
cadena = "Hola, mundo!"
entero = 42
flotante = 3.14
booleano = True

# Imprimir por terminal
print(f"¡Hola, {variable}!")


# -------------------------------
# FUNCIONES EN PYTHON
# -------------------------------

# 1. Función sin parámetros ni retorno
def saludar():
    print("¡Hola desde una función sin parámetros!")

saludar()


# 2. Función con un parámetro
def saludo_personalizado(nombre):
    print(f"¡Hola, {nombre}!")

saludo_personalizado("Python")


# 3. Función con múltiples parámetros
def suma(a, b):
    print(f"La suma de {a} y {b} es {a + b}")

suma(5, 10)


# 4. Función con retorno de valor
def multiplica(x, y):
    return x * y

resultado = multiplica(3, 4)
print(f"El resultado de la multiplicación es {resultado}")


# 5. Función dentro de otra función (nested function)
def funcion_externa():
    mensaje = "Soy una función externa"

    def funcion_interna():
        print(f"{mensaje} y estoy dentro de otra función")

    funcion_interna()

funcion_externa()


# 6. Uso de funciones ya creadas en Python
lista = [1, 2, 3, 4, 5]
print(f"Longitud de la lista: {len(lista)}")
print(f"Valor máximo de la lista: {max(lista)}")
print(f"Valor mínimo de la lista: {min(lista)}")


# -------------------------------
# VARIABLES LOCALES Y GLOBALES
# -------------------------------

variable_global = "Soy una variable global"

def prueba_variables():
    variable_local = "Soy una variable local"
    print(variable_local)  # Se puede acceder dentro de la función
    print(variable_global)  # Se puede acceder a la variable global

prueba_variables()

# print(variable_local)  # Esto daría error porque la variable local no existe fuera de la función

# Modificación de una variable global dentro de una función
contador = 0

def incrementar_contador():
    global contador  # Declaramos que queremos modificar la variable global
    contador += 1
    print(f"Contador dentro de la función: {contador}")

incrementar_contador()
print(f"Contador fuera de la función: {contador}")

# DIFICULTAD EXTRA (OPCIONAL)

def func1(string1,string2):
    count = 0
    for i in range (1,101):
        if (i%3==0 and i%15!=0):
            print(string1)
        elif (i%5==0 and i%15!=0):
            print(string2)
        elif (i%15==0):
            print(string1+string2)
        else:
            print(i)
            count+=1
    return(count)

count=func1("fizz","buzz")
print(count)