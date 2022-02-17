'''Даны вещественные числа a, b, c, d, e, f. Известно, что система
 линейных уравнений:

ax + by = e

cx + dy = f

имеет ровно одно решение. Выведите два числа x и y, являющиеся решением
этой системы.'''

a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

if a != 0:
    y = (f - (c / a)) / (d - ((b * c) / a))
    x = (e - (b * y)) / a
    print(x, y)
