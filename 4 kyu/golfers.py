    #https://www.codewars.com/kata/556c04c72ee1147ff20000c9/train/python
def valid(a):
    if tamaniosOK(a):
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
            for i in range(0,len(listadeldia)):
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

def tamaniosOK(listacompleta):
    it1 = iter(listacompleta)
    the_len1 = len(next(it1))
    if not all(len(d) == the_len1 for d in it1):
        return False
    for listadeldia in listacompleta:
        it = iter(listadeldia)
        the_len = len(next(it))
        if not all(len(l) == the_len for l in it):
            return False
    return True


def contraquienjuega(golfer, listacompleta):
    contrincantes = ''
    for listadeldia in listacompleta:
        for equipo in listadeldia:
            if golfer in equipo:
                contrincantes += equipo
                contrincantes = contrincantes.replace(golfer, '')
    return contrincantes

def todos_los_del_dia(listadeldia):
    for equipo in listadeldia:
        lista = ''.join(equipo)
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



s = [
    ["AB", "CD", "EF", "GH"],
    ["AC", "BD", "EG", "FH"],
    ["AD", "CE"],
    ["AE", "BG", "CH", "FD"]]

z = [
    ["ABC", "DEF"],
    ["ADE", "CBF"]]

#print(norepiteenelmismodia('A', t))
#print(saletodoslosdias('A', z))
#print(tamaniosOK(a))
#print(contraquienjuega('A',a))
print(todos_los_del_dia(a))
