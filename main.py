import cifrado_rotn
import cifrado_vigenere

def cifrado(mensaje,clave):
    cif1=cifrado_rotn.cod(mensaje,15)
    cif2=cifrado_vigenere.cifrar(clave,cif1)
    cif3=cifrado_rotn.cod(cif2,7)
    print('Mensaje cifrado: ',cif3)
    return(cif3)
def decifrado(mensaje,clave):
    cif1=cifrado_rotn.decod(mensaje,7)
    cif2=cifrado_vigenere.descifrar(clave,cif1)
    cif3=cifrado_rotn.decod(cif2,15)
    print('Mensaje descifrado: ',cif3)
    return(cif3)

#1
Clave='cvqnoteshrwnszhhksorbqcoas'
mensaje=input('Mensaje:')
print('El mensaje es: ',mensaje)
import requests

headers = {
    'Content-Type': 'text/plain',
}

data = '{"msg":"jjbnanrvv"}'

response = requests.post('http://finis.malba.cl/SendMsg', headers=headers, data=data)
print(response.text)

#2

Clave='aobkqolrzsrigpknkufezioer'
import requests
headers = {
    'Content-Type': 'text/plain',
}

response = requests.get('http://finis.malba.cl/GetMsg', headers=headers)

mensaje2= response
decodificado= decifrado(mensaje2,Clave)
