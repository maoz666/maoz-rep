'''Для данного числа n<100 закончите фразу “На лугу пасется...”
одним из возможных продолжений: “n коров”, “n корова”, “n коровы”,
 правильно склоняя слово “корова”.'''

n = int(input())

if n == 1 or (n > 1 and n != 11 and (n - 1) % 10 == 0):
    print(str(n) + ' korova')
elif n == 2 or (n > 2 and n != 12 and (n - 2) % 10 == 0):
    print(str(n) + ' korovy')
elif n == 3 or (n > 3 and n != 13 and (n - 3) % 10 == 0):
    print(str(n) + ' korovy')
elif n == 4 or (n > 4 and n != 14 and (n - 4) % 10 == 0):
    print(str(n) + ' korovy')
else:
    print(str(n) + ' korov')
