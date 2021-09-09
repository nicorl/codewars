import re


def abbreviate(s):
    # https://www.codewars.com/kata/5375f921003bf62192000746/train/python
    # Split por guion y por espacio
    x = re.finditer('-', s)
    guiones = [match.start() for match in x]
    caracteresraros = []
    for l, m in enumerate(s):
        if (not m.isalnum()):
            caracteresraros.append(l)
    print(caracteresraros)
    print(guiones)
    s2 = re.split(' | |-', s)
    s3 = ''
    # ignore short words < 3
    for cadena in s2:
        if len(cadena) <= 3:
            s3 += cadena + ' '
        else:
            # checkear si tiene un caracter raro
            cadena2 = ''
            for i, c in enumerate(cadena):
                if (c.isalnum()):
                    cadena2 += cadena[i]
                    # luego habria que meter de nuevo el caracter raro!
            # acortar
            cadcort = ''
            for contar, letra in enumerate(cadena2):
                if contar == 0 or contar == len(cadena2)-1:
                    cadcort += letra
                else:
                    pass
            cadcort = cadcort[:1] + str(len(cadena2)-2) + cadcort[1:]
            s3 += cadcort + ' '
    return s3[:-1]


print(abbreviate("hola adi-osito! okay-makay"))
