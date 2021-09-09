def move_zeros(array):
    i, k = 0, 0 
    nuevo = []
    for elemento in array:
        if elemento == 0:
            k = k +1
        else:
            nuevo.append(elemento)
        i = i +1 
    for n in range(0,k):
        nuevo.append(0)
    return nuevo

print(move_zeros([9, 0, 9, 1, 2, 1, 1, 3, 1, 9, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0]))