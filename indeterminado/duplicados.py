def duplicate_count(text):
    textlow = text.lower()
    dupe = []
    for letra in textlow:
        if (textlow.count(letra) > 1):
            dupe.append(letra)
    return len(list(dict.fromkeys(dupe)))


duplicate_count("holaa")
