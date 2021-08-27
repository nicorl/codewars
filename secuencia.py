def max_sequence(arr):
    # https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/python
    negs = len(arr)
    check_negs = 0
    for num in arr:
        if num < 0:
            check_negs = check_negs + 1
    if check_negs == len(arr):
        return 0
    sumas = []
    for num in arr:
        if num < 0:
            pass
        else:
            for subnum in
    return sumas


print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
