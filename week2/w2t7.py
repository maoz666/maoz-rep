'''Заданы две клетки шахматной доски. Если они покрашены в один
цвет, то выведите слово YES, а если в разные цвета – то NO.'''

line1 = int(input())
row1 = int(input())
line2 = int(input())
row2 = int(input())

if line1 == line2:
    if row1 == row2:
        print("YES")
    elif abs(row1 - row2) % 2 == 0:
        print("YES")
    else:
        print("NO")
else:
    if abs(line1 - line2) % 2 == 0:
        if row1 == row2:
            print("YES")
        elif abs(row1 - row2) % 2 == 0:
            print("YES")
        else:
            print("NO")
    else:
        if row1 == row2:
            print("NO")
        elif abs(row1 - row2) % 2 == 0:
            print("NO")
        else:
            print("YES")
