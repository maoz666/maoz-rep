'''Напишите функцию, вычисляющую длину отрезка по координатам его концов. С
 помощью этой функции напишите программу, вычисляющую периметр треугольника
 по координатам трех его вершин.'''


def distance(n1, n2, n3, n4):
    res = ((n1 - n3) ** 2 + (n2 - n4) ** 2) ** 0.5
    return res


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())

per = distance(x1, y1, x2, y2) + distance(x2, y2, x3, y3) + \
      distance(x3, y3, x1, y1)
print('{0:.6f}'.format(per))
