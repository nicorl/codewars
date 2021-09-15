def parse_molecule (formula):
    #https://www.codewars.com/kata/52f831fa9d332c6591000511/train/python
    for i, char in enumerate(formula):
        print(i, char)
    return "ok"


water = 'H2O'

print(parse_molecule(water))