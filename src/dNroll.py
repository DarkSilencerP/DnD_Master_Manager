__author__ = 'Papo'
__project__ = 'dNroll'

import random

"""
sd = rnd.SystemRandom()
a = sd.randint(1,10)
"""


def rolld2():
    global d2
    d2 = random.randint(1, 2)
    return d2


def rolld4():
    global d4
    d4 = random.randint(1, 4)
    return d4


def rolld6():
    global d6
    d6 = random.randint(1, 6)
    return d6


def rolld8():
    global d8
    d8 = random.randint(1, 8)
    return d8


def rolld10():
    global d10
    d10 = random.randint(1, 10)
    return d10


def rolld12():
    global d12
    d12 = random.randint(1, 12)
    return d12


def rolld20():
    global d20
    d20 = random.randint(1, 20)
    return d20


def rolld100():
    global d100
    d100 = random.randint(1, 100)
    return d100