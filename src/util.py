import math

from context import PI

def get_fractional(i):
    _, fractional = math.fmod(i)
    return fractional

def sin(x):
    return math.sin(x * PI / 180)

def cos(x):
    return math.cos(x * PI / 180)
