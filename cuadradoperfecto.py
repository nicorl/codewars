import math


def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    # https://www.codewars.com/kata/56269eb78ad2e4ced1000013/train/python
    if math.sqrt(sq).is_integer():
        return (math.sqrt(sq) + 1) ** 2
    else:
        return -1


print(find_next_square(121))
