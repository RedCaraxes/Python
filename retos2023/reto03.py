#Estrucutra de datos
"""
/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
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
 */
"""
#Extra
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





