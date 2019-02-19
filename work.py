import math

def rad (n):
    radius = math.pow(n, 3)
    return radius

def vol (n):
    vols = 4/3*math.pi
    volle = (rad(n))*vols
    return volle
