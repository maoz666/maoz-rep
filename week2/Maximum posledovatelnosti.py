'''Последовательность состоит из целых чисел и завершается числом 0.
Определите значение наибольшего элемента последовательности.'''

i = int(input())
m = 0
while i != 0:
    if i > m:
        m = i
        i = int(input())
    i = int(input())
print(m)
