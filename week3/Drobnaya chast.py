'''Дано положительное действительное число X. Выведите его дробную часть.'''
import math
a = float(input())

print(a - math.trunc(a))
