import math

def cube(a):
	return a**3


def pyramid(b, h):
	return (1/3) * b**2 * h


def ellipsoid(r1, r2, r3):
	return (4/3) * math.pi * r1 * r2 * r3