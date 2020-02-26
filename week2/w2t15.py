'''Дано три числа. Упорядочите их в порядке неубывания. Программа
 должна считывать три числа a,b,c, затем программа должна менять
  их значения так, чтобы стали выполнены условия a≤b≤c, затем
   программа выводит тройку a,b,c.'''

a = int(input())
b = int(input())
c = int(input())

if a < c < b:
    a, b, c = a, c, b
elif b < a < c:
    a, b, c = b, a, c
elif b < c < a:
    a, b, c = b, c, a
elif c < a < b:
    a, b, c = c, a, b
elif c < b < a:
    a, b, c = c, b, a
print(a, b, c)
