    #https://www.codewars.com/kata/556c04c72ee1147ff20000c9/train/python
def valid(a):
    if tam(a):
        for x in a:
            if tam(x):
                pass
    for listadeldia in a:
        for equipo in listadeldia:
            for golfer in equipo:
                if norepiteenelmismodia(golfer, listadeldia):
                    pass
                if saletodoslosdias(golfer, a):
                    pass
    return True


def norepiteenelmismodia(golfer, listadeldia):
    valor = 0
    for equipo in listadeldia:
        for golf in equipo:
            if equipo.count(golf) > 1: 
                return False
            for i in range(0,len(listapytdeldia)):
                if golf in listadeldia[i]:
                    valor += 1
                    if valor > 1:
                        return False
            valor = 0
    return True

def saletodoslosdias(golfer, listacompleta):
    listas = []
    for listadeldia in listacompleta:
        lista = ''.join(listadeldia)
        listas.append(lista)

    for lista in listas:
        if golfer in lista:
            pass
        else:
            return False
    return True


def tam(lista):
    iterador1 = iter(lista)
    longitudlc = len(next(iterador1))
    lc = []
    for i in range(0,len(lista)):
        lc.append(len(lista[i]))
    if lc.count(lc[0]) == len(lc):
        return True
    else:
        return False


def contraquienjuega(golfer, listacompleta):
    contrincantes = ''
    for listadeldia in listacompleta:
        for equipo in listadeldia:
            if golfer in equipo:
                contrincantes += equipo
                contrincantes = contrincantes.replace(golfer, '')
    return contrincantes

def todos_los_del_dia(listadeldia):
    lista = ''.join(listadeldia)
    return lista



s = [
    ["AB", "CD"],
    ["AD", "BC"],
    ["BD", "AC"]]   

a = [
    ['ABCD', 'EFGH', 'IJKL', 'MNOP', 'QRST'],
    ['AEIM', 'BJOQ', 'CHNT', 'DGLS', 'FKPR'],
    ['AGKO', 'BIPT', 'CFMS', 'DHJR', 'ELNQ'],
    ['AHLP', 'BKNS', 'CEOR', 'DFIQ', 'GJMT'],
    ['AFJN', 'BLMR', 'CGPQ', 'DEKT', 'HIOS']]

t = ['ABCD', 'EFGH', 'IJKL', 'MNOP', 'QRST']



w = [
    ["AB", "CD", "EF", "GH"],
    ["AC", "BD", "EG", "FH"],
    ["AD", "CE"],
    ["AE", "BG", "CH", "FD"]]

z = [
    ["ABC", "DEF"],
    ["ADE", "CBF"]]

#print(norepiteenelmismodia('A', t))
#print(saletodoslosdias('A', z))
#print(tam(w))
#print(contraquienjuega('A',a))
#print(todos_los_del_dia(a[0]))
