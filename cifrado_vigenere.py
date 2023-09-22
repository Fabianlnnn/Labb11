LETRAS = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
def cifrar(clave,mensaje):
    return traductor_mensaje(clave,mensaje,'encriptar')

def descifrar(clave,mensaje):
    return traductor_mensaje(clave,mensaje,'descifrar')

def traductor_mensaje(clave,mensaje,accion):
    traducido=[]
    indice_clave=0
    clave=clave.upper()

    for symbol in mensaje:
        num=LETRAS.find(symbol.upper())
        if num!=-1:
            if accion=='encriptar':
                num+=LETRAS.find(clave[indice_clave])
            elif accion=='descifrar':
                num-=LETRAS.find(clave[indice_clave])
            num%=len(LETRAS)
            if symbol.isupper():
                traducido.append(LETRAS[num])
            elif symbol.islower():
                traducido.append(LETRAS[num].lower())
            indice_clave+=1
            if indice_clave==len(clave):
                indice_clave=0

        else:
            traducido.append(symbol)
    return ('').join(traducido)
