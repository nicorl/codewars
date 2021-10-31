def valid(a):
    #https://www.codewars.com/kata/556c04c72ee1147ff20000c9/train/python
    for i, equipo in enumerate(a):
        print(equipo)
    return True



s = [ ["AB"] ]

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

s = [
    ["AB", "CD", "EF", "GH"],
    ["AC", "BD", "EG", "FH"],
    ["AD", "CE"],
    ["AE", "BG", "CH", "FD"]]

s = [
    ["ABC", "DEF"],
    ["ADE", "CBF"]]

print(valid(a))