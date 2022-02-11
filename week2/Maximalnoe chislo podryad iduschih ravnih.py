'''Дана последовательность натуральных чисел, завершающаяся числом 0.
Определите, какое наибольшее число подряд идущих элементов этой
последовательности равны друг другу.'''

new = int(input())
old = 0
repeat = 1
repeatmax = 1

while new != 0:
    if new == old:
        repeat += 1
        if repeat > repeatmax:
            repeatmax = repeat
    else:
        repeat = 1
        old = new
    new = int(input())
print(repeatmax)
