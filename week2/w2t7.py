'''Заданы две клетки шахматной доски. Если они покрашены в один
цвет, то выведите слово YES, а если в разные цвета – то NO.'''

line1 = int(input())
col1 = int(input())
line2 = int(input())
col2 = int(input())

if line1 == line2:
    if col1 == col2:
        print("YES")
    elif abs(col1 - col2) % 2 == 0:
        print("YES")
    else:
        print("NO")
else:
    if abs(line1 - line2) % 2 == 0:
        if col1 == col2:
            print("YES")
        elif abs(col1 - col2) % 2 == 0:
            print("YES")
        else:
            print("NO")
    else:
        if col1 == col2:
            print("NO")
        elif abs(col1 - col2) % 2 == 0:
            print("NO")
        else:
            print("YES")
