"""
/*
 * Crea una función que evalúe si un/a atleta ha superado correctamente una
 * carrera de obstáculos.
 * - La función recibirá dos parámetros:
 *      - Un array que sólo puede contener String con las palabras
 *        "run" o "jump"
 *      - Un String que represente la pista y sólo puede contener "_" (suelo)
 *        o "|" (valla)
 * - La función imprimirá cómo ha finalizado la carrera:
 *      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
 *        será correcto y no variará el símbolo de esa parte de la pista.
 *      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
 *      - Si hace "run" en "|" (valla), se variará la pista por "/".
 * - La función retornará un Boolean que indique si ha superado la carrera.
 * Para ello tiene que realizar la opción correcta en cada tramo de la pista.
 */
"""
def goal(actions:[],obstacle:str):
    result=""
    for act,pista in zip(actions, obstacle):
        if act=="run" and pista=="_" or act=="jump" and pista=="|":
            result+=pista
        elif act=="jump" and pista=="_":
            result+="x"
        elif act=="run" and pista=="|":
            result+="/"
    print(result)
    return obstacle==result

actions1=["run","run","jump","run","jump"]
pista1="__|_|"
actions2=["jump","run","jump","jump","jump"]
pista2="|_|||"

print(goal(actions1,pista1))
print(goal(actions2,pista2))
print(goal(actions1,pista2))
print(goal(actions2,pista1))



