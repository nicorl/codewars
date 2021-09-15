def rolldice_sum_prob(sum_, dice_amount):
    # https://www.codewars.com/kata/56f78a42f749ba513b00037f/train/python

    # sabiendo el numero de dados, ver cuantas combinaciones podemos conseguir para llegar a sum_
    # combinaciones de dados = combinaciones del 1 al 6

    # Iteramos por dice_amount 1 , 2 , 3 , ... y sacamos la cantidad de veces que obtenemos un resultado
    caras = [1,2,3,4,5,6]
    valores = []
    for n in range(1,dice_amount+1):                # de cada dado
        for cara in caras:
            pass
    return valores

caras = [1,2,3,4,5,6]
def veces(num):
    arr = []
    for i in range(1,len(caras)+1):
        for j in range(1,len(caras)+1):
            if i == j:
                pass
            else:
                arr.append(i+j)
                print(i,j)
    
    for cara in caras:                      # agregamos los 'diagonales' 1+1 , 2+2, 3+3, 4+4, 5+5
            arr.append(cara*num)
    return arr


print(rolldice_sum_prob(5, 2))
print(veces(2))
