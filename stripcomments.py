string= "apples, pears # and bananas\ngrapes\nbananas !apples"
markers = ["#", "!"]

def solution(string,markers):
    #https://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python
    x = string.split('\n')
    indices_markers = []
    y = ''
    for frase in x:                                         # para cada frase vamos a mirar
        for marker in markers:                              # para cada marcador vamos a mirar
            if marker in frase:               # si marcador está en frase
                indices_markers[enumerate(frase)].append(frase.index(marker))
            else: 
                indices_markers[enumerate(frase)].append(False)

    return indices_markers
print(solution(string,markers))