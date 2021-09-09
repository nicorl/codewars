# https://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/python
s1 = 'ab'
s2 = 'aabb'


def permutations(string):
    s = list(string)
    for i, letra in enumerate(s):
        s[i] = [s+i]
    return s


print(permutations(s2))
