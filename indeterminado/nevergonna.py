# https://www.codewars.com/kata/5f000483f71133002359b897/train/python
chorus = {
    0: 'give you up',
    1: 'let you down',
    2: 'run around and desert you',
    3: 'make you cry',
    4: 'say goodbye',
    5: 'tell a lie and hurt you'
}


def music(numbers):
    arr = []
    for i, number in enumerate(numbers):
        if i % 2 == 0:
            arr.append('Never gonna ' + chorus[number])
        else:
            arr.append('NEVER GONNA ' + chorus[number])
    return arr


print(music(chorus))
