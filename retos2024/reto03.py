"""/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 */"""

# -------------------------------
# ESTRUCTURAS DE DATOS EN PYTHON
# -------------------------------

# 1. LISTAS (listas mutables)
mi_lista = [3, 1, 4, 1, 5, 9, 2]
print("Lista original:", mi_lista)

# Inserción
mi_lista.append(6)  # Agrega un elemento al final
mi_lista.insert(2, 7)  # Inserta el 7 en la posición 2
print("Lista después de inserciones:", mi_lista)

# Eliminación
mi_lista.remove(1)  # Elimina la primera ocurrencia del 1
del mi_lista[3]  # Elimina el elemento en el índice 3
print("Lista después de eliminaciones:", mi_lista)

# Actualización
mi_lista[0] = 8  # Modifica el primer elemento
print("Lista después de actualización:", mi_lista)

# Ordenación
mi_lista.sort()
print("Lista ordenada:", mi_lista)

# 2. TUPLAS (listas inmutables)
mi_tupla = (10, 20, 30, 40)
print("Tupla original:", mi_tupla)

# No se pueden modificar, pero podemos convertirla a lista y operar sobre ella
lista_desde_tupla = list(mi_tupla)
lista_desde_tupla.append(50)
mi_tupla = tuple(lista_desde_tupla)
print("Tupla modificada:", mi_tupla)

# 3. CONJUNTOS (sets, sin elementos duplicados)
mi_conjunto = {3, 1, 4, 1, 5, 9, 2}
print("Conjunto original:", mi_conjunto)

# Inserción
mi_conjunto.add(6)
print("Conjunto después de inserción:", mi_conjunto)

# Eliminación
mi_conjunto.discard(1)  # Elimina el 1 si existe
print("Conjunto después de eliminación:", mi_conjunto)

# No es posible ordenar un conjunto directamente, pero podemos convertirlo a lista y ordenarlo
conjunto_ordenado = sorted(mi_conjunto)
print("Conjunto ordenado:", conjunto_ordenado)

# 4. DICCIONARIOS (almacenamiento clave-valor)
mi_diccionario = {
    "nombre": "Python",
    "versión": 3.11,
    "tipado": "dinámico"
}
print("Diccionario original:", mi_diccionario)

# Inserción
mi_diccionario["creador"] = "Guido van Rossum"
print("Diccionario después de inserción:", mi_diccionario)

# Eliminación
del mi_diccionario["tipado"]
print("Diccionario después de eliminación:", mi_diccionario)

# Actualización
mi_diccionario["versión"] = 3.12
print("Diccionario después de actualización:", mi_diccionario)

# Ordenación (solo podemos ordenar claves y devolver un diccionario ordenado)
diccionario_ordenado = dict(sorted(mi_diccionario.items()))
print("Diccionario ordenado por claves:", diccionario_ordenado)

# DIFICULTAD EXTRA (OPCIONAL)
agenda= {"messi":10, "cr7":17}
while True:
    print("====AGENDA===")
    print("****Menú****")
    print("1-Busqueda de contacto")
    print("2-Inserción de contacto")
    print("3-Actualización de contacto")
    print("4-Eliminación de contacto")
    print("5-Salir")
    opcion=int(input("elija una opción: "))
    if opcion==1:
        contacto=input("introduzca el contacto que desea buscar: ")
        if contacto in agenda:
            print("el contacto se encuentra en la agenda y su numero telefonico es: "+ str(agenda[contacto]))
            
    elif opcion==2:
        contacto=input("introduzca el contacto que desea insertar: ")
        while True:
            telefono=int(input("introduzca el numero de telefono del contacto: "))
            if len(str(telefono))==2 and type(telefono)==int:
                agenda[contacto]=telefono
                break
            print("numero no correcto")
        
    elif opcion==3:
        contacto=input("introduzca el contacto que desea actualizar: ")
        if contacto in agenda:
            telefono=int(input("el contacto se encuentra en la agenda, introduzca su numero: "))
            agenda[contacto]=telefono
        else:
            print("no se encontro registro del contacto")
    elif opcion==4:
        contacto=input("introduzca el contacto que desea eliminar: ")
        if contacto in agenda:
            print("el contacto se encuentra en la agenda, se procede a eliminar: ")
            del agenda[contacto]
        else:
            print("no se encontro registro del contacto")
    elif opcion==5:
        print("saliendo del programa")
        break
    else:
        print("entrada no valida \n\n")