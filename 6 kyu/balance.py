left = "!!!!"
right = "????"
def balance(left, right):
    #https://www.codewars.com/kata/57fb44a12b53146fe1000136/train/python
    for char in left:
        vl = 0
        if char == "!":
            vl += 2
        if char == "?":
            vl += 3
    for char in right:
        vr = 0
        if char == "!":
            vr += 2
        if char == "?":
            vr += 3
    if vl > vr: 
        return "Left"
    if vl == vr:
        return "Balance"
    if vl < vr:
        return "Right"

  