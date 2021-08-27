# https://www.codewars.com/kata/5592e3bd57b64d00f3000047/train/python
import math


def find_nb(m):
    entero = math.sqrt(m)
    print(entero)
    if entero.is_integer():
        x = 1
        k = 2
        while x <= entero:  # 1 < 450010
            x = x + k  # x = 1 + 2
            k = k + 1  # k = 2 + 1
            print(x, k, entero)
            if x == entero:
                return k - 1
        if x > entero:
            return -1
        return -1
    else:
        return -1


print(find_nb(202509000100))


# Visto:
# Cada escalon de la piramide suma un numero mas que el anterior.
# x + k
# 1 + 2 = 3     # it 1
# 3 + 3 = 6     # it 2
# 6 + 4 = 10    # it 3
# 10 + 5 = 15   # it 4
# 15 + 6 = 21   # it 5

# Y luego al cuadrado cada numero, ojo.
# []                --> 1   ---> 1      m3  --> 1
# [][]              --> 3   ---> 9      m3  --> 2
# [][][]            --> 6   ---> 36     m3  --> 3
# [][][][]          --> 10  ---> 100    m3  --> 4
# [][][][][]        --> 15  ---> 225    m3  --> 5
# [][][][][][]      --> 21  ---> 441    m3  --> 6


# Dado N^3 como volumen, hay una estructura sum N a 1 = N

# Entra N^3 como volumen y le hacemos raiz cuadrada.
# El valor resultante de la raiz cuadrada debe ser entero --> Verificar
# El valor resultante de la raiz cuadrada debe ser suma del 1 al entero, mediante los saltos,
