"""
/*
 * Crea un programa que sea capaz de transformar texto natural a código
 * morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar
 *   la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
 *   o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en
 *   https://es.wikipedia.org/wiki/Código_morse.
 */
"""
morseToLetter = {
    "A": ".—",
    "N": "—.",
    "0": "—————",
    "B": "—...",
    "Ñ": "——.——",
    "1": ".————",
    "C": "—.—.",
    "O": "———",
    "2": "..———",
    "CH": "————",
    "P": ".——.",
    "3": "...——",
    "D": "—..",
    "Q": "——.—",
    "4": "....—",
    "E": ".",
    "R": ".—.",
    "5": ".....",
    "F": "..—.",
    "S": "...",
    "6": "—....",
    "G": "——.",
    "T": "—",
    "7": "——...",
    "H": "....",
    "U": "..—",
    "8": "———..",
    "I": "..",
    "V": "...—",
    "9": "————.",
    "J": ".———",
    "W": ".——",
    ".": ".—.—.—",
    "K": "—.—",
    "X": "—..—",
    ",": "——..——",
    "L": ".—..",
    "Y": "—.——",
    "?": "..——..",
    "M": "——",
    "Z": "——..",
    "\"": ".—..—.",
    "/": "—..—."
}

letterToMorse= {value:key for key,value in morseToLetter.items()}

def convertToMorse(texto):
    texto=texto.split(" ")
    count=0
    new=""
    for item in texto:
        for codigo in item:
            new+=(morseToLetter[codigo])
            if count<len(texto)-1:
                new +=" " 
        count+=1
        if count<len(texto):
            new +=" "           
    return new

def convertToTexto(morse):
    morse=morse.split("  ")
    cache=""
    converted=""
    for item in morse:
        cache=item.split(" ")
        for code in cache:
            converted+=letterToMorse[code]
        converted+=" "
    return converted


            
texto="AB BC C"
morse=convertToMorse(texto)
print(convertToMorse(texto))
print(convertToTexto(morse))


