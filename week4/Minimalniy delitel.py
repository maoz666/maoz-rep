'''Дано натуральное число n>1. Выведите его наименьший делитель, отличный от 1.
 Решение оформите в виде функции MinDivisor(n). Алгоритм должен иметь сложность
  порядка корня квадратного из n.

Указание. Если у числа n нет делителя не превосходящего корня из n, то число n
— простое и ответом будет само число n. А у всех составных чисел обязательно
 есть делители, отличные от единицы и не превосходящие корня из n.'''


def MinDivisor(n):
    i = 2
    while i <= n ** 0.5:
        if n % i != 0:
            i += 1
        else:
            return i
    return n


n = int(input())

print(MinDivisor(n))
