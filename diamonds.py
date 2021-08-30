# https://www.codewars.com/kata/5503013e34137eeeaa001648/train/python
def diamond(n):
    space = ' '
    dz = ''
    # first line
    for i in range(0, n+1):
        if (i*2+1) > n:
            pass
        else:
            dz += (n/2-i) * space + '*' * (i*2+1) + '\n'
    return dz


print(diamond(7))

#          n=5
# ##x## i=0 (n/2-i) * space + '*' * (i*2+1) + '\n' ---> i =
# #xxx# i=1 (n/2-i) * space + '*' * (i*2+1) + '\n' --->
# xxxxx i=2 (n/2-i) * space + '*' * (i*2+1) + '\n' --->
# #xxx# i=3                 + '*' * (i*2+i)
# ##x## i=4
