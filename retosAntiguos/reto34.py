"""
/*
 * Crea un función, que dado un año, indique el elemento 
 * y animal correspondiente en el ciclo sexagenario del zodíaco chino.
 * - Info: https://www.travelchinaguide.com/intro/astrology/60year-cycle.htm
 * - El ciclo sexagenario se corresponde con la combinación de los elementos
 *   madera, fuego, tierra, metal, agua y los animales rata, buey, tigre,
 *   conejo, dragón, serpiente, caballo, oveja, mono, gallo, perro, cerdo
 *   (en este orden).
 * - Cada elemento se repite dos años seguidos.
 * - El último ciclo sexagenario comenzó en 1984 (Madera Rata).
 */
"""
def calendario_chino(year):
    elementos = ["Madera", "Fuego", "Tierra", "Metal", "Agua"]
    animales = ["Rata", "Buey", "Tigre", "Conejo", "Dragón", "Serpiente",
                "Caballo", "Oveja", "Mono", "Gallo", "Perro", "Cerdo"]
    año_base = 1984
    diferencia = year - año_base

    # Calcular la posición en el ciclo 
    posicion = diferencia % 60

    # Calcular el elemento y el animal 
    indice_elemento = posicion // 2 % 5
    indice_animal = posicion % 12

    elemento = elementos[indice_elemento]
    animal = animales[indice_animal]

    return elemento, animal

year=2024
elemento, animal=calendario_chino(year)
print(f"El año {year} es el año del animal {animal} y elemento {elemento}")