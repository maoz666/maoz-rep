'''Напишите функцию min4(a, b, c, d), вычисляющую минимум четырех чисел,
 которая не содержит инструкции if, а использует стандартную функцию min
 от двух чисел. Считайте четыре целых числа и выведите их минимум.'''


def min4(a, b, c, d):
    res = min(min(min(a, b), c), d)
    return res


a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(min4(a, b, c, d))
