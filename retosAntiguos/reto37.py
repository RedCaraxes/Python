"""
/*
 * ¡La Tierra Media está en guerra! En ella lucharán razas leales
 * a Sauron contra otras bondadosas que no quieren que el mal reine
 * sobre sus tierras.
 * Cada raza tiene asociado un "valor" entre 1 y 5:
 * - Razas bondadosas: Pelosos (1), Sureños buenos (2), Enanos (3),
 *   Númenóreanos (4), Elfos (5)
 * - Razas malvadas: Sureños malos (2), Orcos (2), Goblins (2),
 *   Huargos (3), Trolls (5)
 * Crea un programa que calcule el resultado de la batalla entre
 * los 2 tipos de ejércitos:
 * - El resultado puede ser que gane el bien, el mal, o exista un empate.
 *   Dependiendo de la suma del valor del ejército y el número de integrantes.
 * - Cada ejército puede estar compuesto por un número de integrantes variable
 *   de cada raza.
 * - Tienes total libertad para modelar los datos del ejercicio.
 * Ej: 1 Peloso pierde contra 1 Orco
 *     2 Pelosos empatan contra 1 Orco
 *     3 Pelosos ganan a 1 Orco
 */
"""

class KindArmy:
    valor_raza_1={"Pelosos" :1, "Sureños buenos" :2, "Enanos" :3,"Númenóreanos" :4, "Elfos" :5}

    def __init__(self, raza):
        self.raza=raza

    def Avalue(self):
        return KindArmy.valor_raza_1[self.raza]
    
class EvilArmy:
    valor_raza_2={"Orcos" :2, "Sureños malos" :2, "Goblins" :2,"Huargos" :3, "Trolls" :5}

    def __init__(self, raza):
        self.raza=raza

    def Avalue(self):
        return EvilArmy.valor_raza_2[self.raza]
    
def battle_for_the_middle_earth(good_army,evil_army):
    good_army_points=sum(KindArmy(army[0]).Avalue()*army[1] for army in good_army)
    evil_army_points=sum(EvilArmy(army[0]).Avalue()*army[1] for army in evil_army)

    if good_army_points>evil_army_points:
        print("Gana el bien")
    elif evil_army_points > good_army_points:
        print("Gana el mal")
    else:
        print("Empate")




battle_for_the_middle_earth(
    [("Elfos", 1)],
    [("Trolls", 1)]
)

battle_for_the_middle_earth(
    [("Elfos", 1), ("Enanos", 1)],
    [("Trolls", 1)]
)

battle_for_the_middle_earth(
    [("Elfos", 1), ("Enanos", 1)],
    [("Trolls", 1), ("Orcos", 1)]
)

battle_for_the_middle_earth(
    [("Elfos", 56), ("Enanos", 80), ("Númenóreanos", 5)],
    [("Trolls", 200), ("Orcos", 51), ("Huargos", 10), ("Sureños malos", 2)]
)