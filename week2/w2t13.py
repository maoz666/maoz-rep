'''Даны три стороны треугольника a,b,c. Определите тип треугольника
 с заданными сторонами. Выведите одно из четырех слов: rectangular
 для прямоугольного треугольника, acute для остроугольного
 треугольника, obtuse для тупоугольного треугольника или
 impossible, если треугольника с такими сторонами не существует
 (считаем, что вырожденный треугольник тоже невозможен).'''

a = int(input())
b = int(input())
c = int(input())

if a > b and a > c:
    if a ** 2 == b ** 2 + c ** 2:
        print('rectangular')
    elif a ** 2 < b ** 2 + c ** 2:
        print('acute')
    elif a ** 2 > b ** 2 + c ** 2:
        print('obtuse')
    else:
        print('impossible')
elif b > a and b > c:
    if b ** 2 == a ** 2 + c ** 2:
        print('rectangular')
    elif b ** 2 < a ** 2 + c ** 2:
        print('acute')
    elif b ** 2 > a ** 2 + c ** 2:
        print('obtuse')
    else:
        print('impossible')
elif c > a and c > b:
    if c ** 2 == a ** 2 + b ** 2:
        print('rectangular')
    elif c ** 2 < a ** 2 + b ** 2:
        print('acute')
    elif c ** 2 > a ** 2 + b ** 2:
        print('obtuse')
    else:
        print('impossible')
