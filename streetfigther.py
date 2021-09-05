fighters = [
	["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
	["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
]
ip = (1,5)
opts = ["up","down","right","left"]

def street_fighter_selection(fighters, initial_position, moves):
    #https://www.codewars.com/kata/5853213063adbd1b9b0000be/train/python
    resp = []
    if ip[0] == 0:
        resp.append(fighters[0][ip[1]])
    else:
        resp.append(fighters[1][ip[1]])

    return resp

print(street_fighter_selection(fighters, ip, opts))