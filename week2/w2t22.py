'''На сковородку одновременно можно положить k котлет. Каждую
котлету нужно с каждой стороны обжаривать m минут непрерывно. За
какое наименьшее время удастся поджарить с обеих сторон n котлет?

Формат ввода
Программа получает на вход три числа: k,m,n.'''

k = int(input())
m = int(input())
n = int(input())

x = n // k
y = n % k
if y != 0:
    x = x + 1
print(x * 2 * m)