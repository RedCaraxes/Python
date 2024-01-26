"""
/*
 * Crea un programa que comprueba si los paréntesis, llaves y corchetes
 * de una expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cieran
 *   en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios.
 *   No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
 */
"""
def is_balanced(expression):
    opening_symbols = {"{": "}", "[": "]", "(": ")"}
    stack = []

    for symbol in expression:
        if symbol in opening_symbols or symbol in opening_symbols.values():
            if symbol in opening_symbols:
                stack.append(symbol)
            else:
                if not stack or symbol != opening_symbols[stack.pop()]:
                    return False
    return not stack


print(is_balanced("{a + b [c] * (2x2)}}}}"))
print(is_balanced("{ [ a * ( c + d ) ] - 5 }"))
print(is_balanced("{ a * ( c + d ) ] - 5 }"))
print(is_balanced("{a^4 + (((ax4)}"))
print(is_balanced("{ ] a * ( c + d ) + ( 2 - 3 )[ - 5 }"))
print(is_balanced("{{{{{{(}}}}}}"))
print(is_balanced("(a"))
