def multiplication_table(size):
    # https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08/train/python
    tabla = []
    tablafinal = []
    for j in range(0, size):
        for i in range(0, size):
            tabla.append((i+1)*(j+1))
        tablafinal.append(tabla)
        tabla = []
    return tablafinal


print(multiplication_table(4))
