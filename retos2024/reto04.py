"""/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */"""

# -------------------------------
# OPERACIONES CON CADENAS EN PYTHON
# -------------------------------

texto = "Hola, Python!"

# 1. Acceso a caracteres específicos
print("Primer carácter:", texto[0])   # 'H'
print("Último carácter:", texto[-1])  # '!'

# 2. Subcadenas (slicing)
print("Primeros 4 caracteres:", texto[:4])  # 'Hola'
print("Últimos 6 caracteres:", texto[-6:])  # 'Python'
print("Cada segundo carácter:", texto[::2])  # 'Hl,Pto!'

# 3. Longitud de la cadena
print("Longitud del texto:", len(texto))

# 4. Concatenación
saludo = "¡Bienvenido a "
frase_completa = saludo + texto
print("Concatenación:", frase_completa)

# 5. Repetición de cadenas
print("Repetición:", "Python! " * 3)

# 6. Recorrido de una cadena (iteración)
print("Recorrido de la cadena:")
for letra in texto:
    print(letra, end=" ")  # H o l a ,   P y t h o n !

print()  # Salto de línea

# 7. Conversión a mayúsculas y minúsculas
print("Mayúsculas:", texto.upper())
print("Minúsculas:", texto.lower())
print("Capitalizado:", texto.capitalize())  # Solo primera letra en mayúscula
print("Cada palabra en mayúscula:", texto.title())

# 8. Reemplazo de texto
nuevo_texto = texto.replace("Python", "Mundo")
print("Reemplazo de palabra:", nuevo_texto)

# 9. División de cadenas
palabras = texto.split(", ")  # Divide en lista separada por ', '
print("División:", palabras)

# 10. Unión de cadenas
nueva_frase = " - ".join(palabras)
print("Unión:", nueva_frase)

# 11. Verificación dentro de cadenas
print("¿'Python' está en el texto?", "Python" in texto)
print("¿'Java' no está en el texto?", "Java" not in texto)

# 12. Interpolación de cadenas (f-strings)
nombre = "Carlos"
edad = 25
print(f"Mi nombre es {nombre} y tengo {edad} años.")  # f-string

# 13. Eliminación de espacios en blanco al inicio o final del string
texto_con_espacios = "   Python   "
print("Texto sin espacios:", texto_con_espacios.strip())  # 'Python'
print("Solo eliminar espacios a la izquierda:", texto_con_espacios.lstrip())
print("Solo eliminar espacios a la derecha:", texto_con_espacios.rstrip())

# 14. Verificación de inicio y fin de una cadena
print("¿Empieza con 'Hola'?", texto.startswith("Hola"))
print("¿Termina con 'Python!'?", texto.endswith("Python!"))

# 15. Contar ocurrencias de una subcadena
print("Número de veces que aparece 'o':", texto.count("o"))

# 16. Encontrar la posición de una subcadena
print("Posición de 'Python':", texto.find("Python"))  # Devuelve el índice
print("Posición de 'Java' (no existe):", texto.find("Java"))  # Devuelve -1

# 17. Comprobaciones de tipo
print("¿Es alfabético?", texto.isalpha())  # Falso porque tiene ',' y '!'
print("¿Es numérico?", "12345".isdigit())  # Verdadero
print("¿Es alfanumérico?", "Python3".isalnum())  # Verdadero

# 18. Inversión de la cadena
print("Texto invertido:", texto[::-1])  # '!nohtyP ,aloH'

# 19. Conversión entre caracteres y código ASCII
print("Código ASCII de 'H':", ord('H'))  # 72
print("Carácter del código ASCII 72:", chr(72))  # 'H'

# 20. Formateo de cadenas con format()
print("Mi lenguaje favorito es {}".format("Python"))
print("Hola, {}. Tienes {} años.".format(nombre, edad))
print("Valor con decimales: {:.2f}".format(3.14159))  # Redondear a 2 decimales


def isAnagrama(string1, string2):
    if string1==string2:
        return False
    return sorted(string1.lower())==sorted(string2.lower())

def isPalindromo(string1):
    string1 = string1.replace(" ","")
    string1inv = string1[::-1]
    return string1 == string1inv

def isIsograma(string1):
    string1 = string1.lower()
    return len(string1) == len(set(string1))

string1="amor"
string2="roma"

print(f" la palabra {string1} y {string2} son anagramas? : {isAnagrama(string1, string2)}" )

string3 = "anita lava la tina"
string4 = "murcielago"

print(isPalindromo(string3))
print(isIsograma(string4))  # True
print(isIsograma("oso"))        # False

