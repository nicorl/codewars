integers = [2,4,6,8,9]

def find_outlier(integers):
    pares, impares = [], []
    for num in integers:
        if (num % 2) == 0:
            pares.append(num)
        else:
            impares.append(num)
    if len(pares) == 1:
        return pares[0]
    else:
        return impares[0]
    


print(find_outlier(integers))
    