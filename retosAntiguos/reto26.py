"""
/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "R" (piedra), "P" (papel)
 *   o "S" (tijera).
 * - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
 */
"""
def gamewin(tupl):
    if "R" in tupl and "S" in tupl:
        if tupl[0]=="R":
            return "Player 1"
        else:
            return "Player 2"
    if "S" in tupl and "P" in tupl:
        if tupl[0]=="S":
            return "Player 1"
        else:
            return "Player 2"
    if "P" in tupl and "R" in tupl:
        if tupl[0]=="P":
            return "Player 1"
        else:
            return "Player 2"
    else:
        return "Tie"

def winner(list):
    p1,p2=0,0
    for i in list:
        if gamewin(i)=="Player 1":
            p1+=1
        elif gamewin(i)=="Player 2":
            p2+=1
    if p1>p2:
        return print("Player 1")
    elif p2>p1:
        return print("Player 2")
    else:
        return print("Tie")
    
    
Entrada=[("R","S"), ("S","R"), ("P","S"), ("S","S"),("S","P")]
winner(Entrada)

"""Mas corto"""
def calcular_ganador(partidas):
    # Contadores para los jugadores
    jugador1 = 0
    jugador2 = 0

    # Recorre cada par de jugadas
    for jugada1, jugada2 in partidas:
        # Determina el ganador de la partida
        if (jugada1, jugada2) in [("R", "S"), ("S", "P"), ("P", "R")]:
            jugador1 += 1
        elif (jugada1, jugada2) in [("S", "R"), ("P", "S"), ("R", "P")]:
            jugador2 += 1

    # Compara los contadores para determinar al ganador general
    if jugador1 > jugador2:
        return "Player 1"
    elif jugador2 > jugador1:
        return "Player 2"
    else:
        return "Tie"

# Ejemplo de uso
partidas = [("R","S"), ("S","R"), ("P","S")]
resultado = calcular_ganador(partidas)
print("El ganador es:", resultado)
