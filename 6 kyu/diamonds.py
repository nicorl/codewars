# https://www.codewars.com/kata/5503013e34137eeeaa001648/train/python
def diamond(n):
    space = ' '
    dz = ''
    j = 0
    for i in range(0, n+1):
        if (i*2+1) > n:
            j += 1
            dz += ((j) * space) + ('*' * (n-2*j)) + '\n'
        else:
            dz += (int((n/2-i)) * space) + \
                ('*' * (i*2+1)) + '\n'
    return dz


print(diamond(25))

#          n=5
# ##x## i=0 (n/2-i) * space + '*' * (i*2+1) + '\n' ---> i =
# #xxx# i=1 (n/2-i) * space + '*' * (i*2+1) + '\n' --->
# xxxxx i=2 (n/2-i) * space + '*' * (i*2+1) + '\n' --->
# #xxx# i=3 ()                + '*' * (i*2+i)
# ##x## i=4

#    n = 11
#             *  #  i   i*2+1   j
# *********** 11 0 i=5          0
# #*********# 9  1 i=6  13      1
# ##*******## 7  2 i=7  15      2
# ###*****### 5  3 i=8  17      3
# ####***#### 3  4 i=9  19      4
# #####*##### 1  5 i=10 21      5
#
