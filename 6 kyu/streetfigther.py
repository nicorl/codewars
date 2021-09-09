fighters = [
	["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
	["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
]
ip = (0,0)
opts = ["down", "up", "down", "down", "down", "up", "right", "right", "right", "right", "right", "right"]

def street_fighter_selection(fighters, initial_position, moves):
    #https://www.codewars.com/kata/5853213063adbd1b9b0000be/train/python
    ap = []
    ap.append([initial_position[0], initial_position[1]])

    for i, mov in enumerate(moves):
        if mov == "up":
            if ap[i][0] == 0:
                ap.append(ap[i])
            else:
                ap.append([0,ap[i][1]])
        if mov == "down":
            if ap[i][0] == 1:
                ap.append(ap[i])
            else:
                ap.append([1,ap[i][1]])
        if mov == "right":
            if ap[i][1] == len(fighters[0])-1:
                ap.append([ap[i][0],0])
            else:
                ap.append([ap[i][0],ap[i][1]+1])
        if mov == "left":
            if ap[i][1] == 0:
                ap.append([ap[i][0], len(fighters[0])-1])
            else:
                ap.append([ap[i][0], ap[i][1]-1])
    
    ap = ap[1::]
    solution = []
    for i, personaje in enumerate(ap):
        coordx = personaje[0]
        coordy = personaje[1]
        solution.append(fighters[coordx][coordy])

    return solution

print(street_fighter_selection(fighters, ip, opts))

