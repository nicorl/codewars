def row_sum_odd_numbers(n):
    x = 0
    for numero in range(1,n):
        x = x + numero
    first = 2*x+1 
    elementos = []
    elementos.append(first)
    for i in range(1,n):
        elementos.append(2*x+1+2*i)
    return sum(elementos)

print(row_sum_odd_numbers(2))