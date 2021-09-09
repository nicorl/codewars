def alphabet_position(text):
    # https: // www.codewars.com/kata/546f922b54af40e1e90001da/train/python
    x = ''
    for letra in text:
        if letra.isalnum() and not letra.isnumeric():
            x += str(ord(letra.lower())-96) + ' '
    return x[:-1]
