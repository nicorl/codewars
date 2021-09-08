import random
# https://www.codewars.com/kata/5864152183f7e6e834000160/train/python


def random_movie(movies):
    return movies[random.randint(0, len(movies)-1)]
