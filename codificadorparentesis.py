def duplicate_encode(word):
    # https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python
    word = word.lower()
    coded = ''
    for letra in word:
        if word.count(letra) == 1:
            coded += "("
        else:
            coded += ")"
    return coded