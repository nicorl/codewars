def decipher_this(string):
    # https://www.codewars.com/kata/581e014b55f2c52bb00000f8/train/python
    descifrado = ''
    s = string.split()
    for p in s:
        numerito, palabrita, palabra = '', '', ''
        for letra in p:
            k = 0
            if letra.isnumeric():
                if k == 0:
                    numerito += letra
            else:
                palabrita += letra
                k = 1
        palabra += chr(int(numerito))

        # + palabrita + ' ' # esto, luego de tratar palabrita

        if len(palabrita) == 0:
            descifrado += palabra + ' '
        else:
            prime = palabrita[0]
            final = palabrita[-1]
            list1 = list(palabrita)
            list1[0] = final
            list1[-1] = prime
            str1 = ''.join(list1)
            descifrado += palabra + str1 + ' '
        numerito, palabrita, palabra = '', '', ''
    return descifrado[:-1]


print(decipher_this("65 119esi 111dl 111lw 108dvei 105n 97n 111ka"))
