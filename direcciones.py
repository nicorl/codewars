def dirReduc(arr):
    # https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python
    noReducs = True
    while (noReducs == True):
        i = 0
        reducs = []
        # Comprobamos que se puedan quitar a pares
        # print(len(arr))
        # print(arr)
        # print(len(reducs))
        if len(arr) == 0:
            pass
        else:
            for direc in range(0, len(arr)-2):
                if (arr[i] == "NORTH") and (arr[i+1] == "SOUTH"):
                    reducs.append(i)
                    reducs.append(i+1)
                if (arr[i] == "SOUTH") and (arr[i+1] == "NORTH"):
                    reducs.append(i)
                    reducs.append(i+1)
                if (arr[i] == "WEST") and (arr[i+1] == "EAST"):
                    reducs.append(i)
                    reducs.append(i+1)
                if (arr[i] == "EAST") and (arr[i+1] == "WEST"):
                    reducs.append(i)
                    reducs.append(i+1)

                if (arr[i] == "SOUTH") and (arr[i+1] == "NORTH"):
                    reducs.append(i)
                    reducs.append(i+1)
                if (arr[i] == "NORTH") and (arr[i+1] == "SOUTH"):
                    reducs.append(i)
                    reducs.append(i+1)
                if (arr[i] == "EAST") and (arr[i+1] == "WEST"):
                    reducs.append(i)
                    reducs.append(i+1)
                if (arr[i] == "WEST") and (arr[i+1] == "EAST"):
                    reducs.append(i)
                    reducs.append(i+1)
                i = i + 1
            if len(reducs) > 0:
                # Damos la vuelta a los indices y borramos los que faltan
                redinv = list(set(reducs))
                redinv = redinv[::-1]
                for elemento in redinv:
                    arr.pop(elemento)
                # print("#################")
                # print("#### VUELTA #####")
                # print("#################")
            else:
                #print("Cerramos bucle")
                noReducs = False

    return arr


print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
