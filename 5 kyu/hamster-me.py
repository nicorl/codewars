# https://www.codewars.com/kata/595ddfe2fc339d8a7d000089/python

def hamsterMe(code, message):
    letrasordenadas = sorted(code) # ordenamos hola --> ahlo
    letrasnumeros = []
    for letra in letrasordenadas:
        letrasnumeros.append(ord(letra)) # convertimos la letras a numeros 
    posiciones = []
    for i, numero in enumerate(letrasnumeros):
        if i+1 == len(letrasnumeros):           #cuando estemos en la ultima letra de la cadena
            while numero+1 <= 122:              #mientras llegamos a la 'z' - dejamos el principio del bucle sin rellenar
                numero+=1
                posiciones.append([i, chr(numero)])
        else:                                   #para cualquier otra letra de la cadena agregamos elementos en su rango
            while numero+1 < letrasnumeros[i+1]:
                numero+=1
                posiciones.append([i, chr(numero)])
    lavuelta = 97                               #la vuelta de la ultima letra hasta la primera letra de la cadena
    while lavuelta < letrasnumeros[0]:
        posiciones.append([len(letrasnumeros)-1, chr(lavuelta)])
        lavuelta+=1
    return posiciones


'''     print("Lo de acontinuacion nada")
    x = []
    for i, numero in enumerate(letrasnumeros):
        if i+1 == len(letrasnumeros):
            num_ini = numero+1
            if num_ini >= 122: #si la letra es la Z, a ver que hacemos
                num_ini = 97
            num_fin = letrasnumeros[0]-1
            x.append([num_ini,num_fin])
        else:
            num_ini = numero+1
            num_fin = letrasnumeros[i+1]-1
            x.append([num_ini,num_fin])
    return x '''

print(hamsterMe("hola", 'xx'))
#print(ord('z')) #122
#print(ord('a')) #97

# ahora mismo las letras que van consecutivas no tienen presencia, su rango al ser nulo no aparecen
# abcdefgh... solo devuelve el rango de la ultima