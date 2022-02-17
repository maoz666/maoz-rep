'''Даны длины сторон треугольника. Вычислите площадь треугольника.'''
a = float(input())
b = float(input())
c = float(input())

p = (a + b + c) / 2
s = ((p * (p - a) * (p - b) * (p - c)) ** 0.5)
if s % 1 != 0:
    print('{0:.6f}'.format(s))
else:
    print(int(s))
