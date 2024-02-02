"""
/*
 * Crea una función que reciba días, horas, minutos y segundos (como enteros)
 * y retorne su resultado en milisegundos.
 */
"""
def converterMili(dias,horas,min,seg):
    try:
 #       if (type(dias)==int and type(horas)==int and type(min)==int and type(seg)==int):
        if all(isinstance(valor, int) for valor in (dias, horas, min, seg)):
            milisegundos=dias*3600000*24+horas*3600000+min*60000+seg*1000
            return milisegundos
        else:
            raise Exception
    except:
        return ("se debe ingresar valores enteros en el orden dias, horas, minutos y segundos")
        

print(converterMili(1,1,5,1))
print(converterMili(0,0,2,5))
print(converterMili("nn","0",5,1))