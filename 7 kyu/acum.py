def accum(s):
    # https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python
    # your code
    final = []
    final2 = ''
    alargar = 1
    for letra in s:
        final.append(letra * alargar)
        alargar += 1
    for elemento in final:
        final2 = final2 + '-' + \
            elemento.replace(elemento[0], elemento[0].upper(), 1)
    final2 = final2[1:]
    return final2


print(accum("RqaEzty"))
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
