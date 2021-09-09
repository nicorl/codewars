# https://www.codewars.com/kata/56dbe7f113c2f63570000b86/train/python
s = "abcd\nefgh\nijkl\nmnop"
t = "fijuoo\nCqYVct\nDrPmMJ\nerfpBA\nkWjFUG\nCVUfyL"
def rot(strng):
    tramos = strng.split("\n")
    strfinal = ''
    for tramo in reversed(tramos):
        strfinal += tramo[::-1] + '\n'
    return strfinal[:-1]
def selfie_and_rot(strng):
    tramos = strng.split("\n")
    strfinal = ''
    for tramo in tramos:
        strfinal += tramo + '.' * len(tramo) + '\n'
    for tramo in reversed(tramos):
        strfinal += '.' * len(tramo) + tramo[::-1] + '\n'
    return strfinal[:-1]
def oper(fct, s):
    return fct(s)

print(oper(rot,s))