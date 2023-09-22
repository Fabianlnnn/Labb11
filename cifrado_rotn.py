def cod(mensaje, rotaciones):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    n_alfabeto = 26
    mensajeTemp = ""
    for caracter in mensaje:
        if not caracter.isalpha() or caracter.lower() == 'ñ':
            mensajeTemp += caracter
        elif caracter.isupper():
            letraEnOrd = ord(caracter)
            inicioEnOrd = 65 
            posicion = (letraEnOrd - inicioEnOrd + rotaciones) % n_alfabeto
            mensajeTemp += alfabeto[posicion].upper()
        else:
            letraEnOrd = ord(caracter)
            inicioEnOrd = 97
            posicion = (letraEnOrd - inicioEnOrd + rotaciones) % n_alfabeto
            mensajeTemp += alfabeto[posicion]

    return mensajeTemp

def decod(mensaje, rotaciones):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    n_alfabeto = 26
    mensajeTemp = ""
    for caracter in mensaje:
        if not caracter.isalpha() or caracter.lower() == 'ñ':
            mensajeTemp += caracter
        elif caracter.isupper():
            letraEnOrd = ord(caracter)
            inicioEnOrd = 65
            posicion = (letraEnOrd - inicioEnOrd - rotaciones) % n_alfabeto
            mensajeTemp += alfabeto[posicion].upper()
        else:
            letraEnOrd = ord(caracter)
            inicioEnOrd = 97
            posicion = (letraEnOrd - inicioEnOrd - rotaciones) % n_alfabeto
            mensajeTemp += alfabeto[posicion]

    return mensajeTemp