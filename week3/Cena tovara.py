'''Цена товара обозначена в рублях с точностью до копеек, то есть
действительным числом с двумя цифрами после десятичной точки. Запишите в две
 целочисленные переменные стоимость товара в виде целого числа рублей и целого
  числа копеек и выведите их на экран. При решении этой задачи нельзя
   пользоваться условными инструкциями и циклами.'''

import math

a = float(input())

rub = math.trunc(a)
kop = round((a - math.trunc(a)) * 100)
print(rub, kop)
