'''Последовательность состоит из натуральных чисел и завершается числом 0.
Определите количество элементов этой последовательности, которые равны ее
наибольшему элементу.'''

i = int(input())
m = i
c = 0
while i != 0:
    if i > m:
        m = i
        c = 0
    if i == m:
        c += 1
    i = int(input())
print(c)
