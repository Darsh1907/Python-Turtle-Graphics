from random import randint


def random_color():
    r = randint(0,255)
    b = randint(0,255)
    g = randint(0,255)
    random_color = (r, b, g)
    return random_color

