fighters = [
	["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
	["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
]
ip = (1,5)
opts = ["up","down","right","left"]

def street_fighter_selection(fighters, initial_position, moves):
    #https://www.codewars.com/kata/5853213063adbd1b9b0000be/train/python
    resp = []
    ap = list(initial_position)

    for i, posicion in enumerate(moves):
        if posicion == "up":
            if ap[i][0] == 0:
                ap.append(0, ap(1))# directamente estamos arriba, por lo que debemos agregar es la posicion actual (0)
            else:
                ap.append(1, ap(1))# de otra forma, asignamos el valor de abajo (1)
        if posicion == "down":
            if ap[i][0] == 1:
                ap.append(1, ap(1))# directamente estamos abajo, por lo que debemos agregar es la posicion actual (1)
            else:
                ap.append(0, ap(1))# de otra forma, asignamos el valor de arriba (0)
        if posicion == "right":
            if ap[i][0] == len(fighters[0]):
                ap.append(ap(0), 0)# entonces el ap(1) tiene que irse a valor 0
            else:
                ap.append(ap(0), ap(1)+1)# en otro caso, le sumamos 1 a ap(1)
        if posicion == "left":
            if ap[i][0] == 0:
                ap.append(ap(0), len(fighters[0]))# entonces el ap(1) tiene que irse a valor len(fighters[0])
            else:
                ap.append(ap(0), ap(1)-1)# en otro caso, le quitamos 1 a ap(1)
        ap.append(ap(0),ap(1))
    #resp.append(initial_position + movimiento)
    return ap


def street_fighter_selection2(fighters, initial_position, moves):
    #https://www.codewars.com/kata/5853213063adbd1b9b0000be/train/python
    resp = []
    ap = list([initial_position])
    print()
    for i, mov in enumerate(moves):
        if mov == "up":
            if ap[::-1][0] == 0:
                ap.append(ap)
            else:
                ap.append(1, ap[::-1][1])
        if mov == "down":
            if ap[::-1][0] == 1:
                ap.append(ap)
            else:
                ap.append(0, ap[::-1][1])            
    #resp.append(initial_position + movimiento)
    return ap

print(street_fighter_selection2(fighters, ip, opts))

