'''Дано действительное положительное число a и целоe число n. Вычислите aⁿ.
Решение оформите в виде функции power(a, n). Стандартной функцией возведения
в степерь пользоваться нельзя.'''


def power(x, y):
    if y == 0:
        return 1
    elif y > 0:
        return x * power(x, y - 1)
    else:
        return 1 / (x * power(x, abs(y) - 1)

print(power(2, 3))
