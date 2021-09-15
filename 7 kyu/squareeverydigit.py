def square(x):
    return int(x)**2

def square_digits(num):
    #https://www.codewars.com/kata/546e2562b03326a88e000020/train/python
    x = map(square, list(str(num)))
    k = ''
    for i in x:
        k += str(i)
    return k

print(square_digits(9119))