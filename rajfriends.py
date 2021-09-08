# https://www.codewars.com/kata/5866d90edbca9ae420000145/train/python
wholeGroup = {'Leonard': 'Married',
              'Penny': 'Married',
              'Howard': 'Married',
              'Bernadette': 'Married',
              'Sheldon': 'In a relationship',
              'Amy': 'In a relationship',
              'Raj': 'Single'}


def mission_impossible(obj):
    # Your code here ;)
    obj['Raj'] = 'In a relationship'
    return obj


print(mission_impossible(wholeGroup))
