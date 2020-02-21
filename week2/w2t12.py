'''На доске стоит белая шашка. Требуется определить, может ли она
 попасть в заданную клетку, делая ходы по правилам и не пользуясь
  ходами дамки (т. е. не используя возможность перемещаться назад
  после превращения в дамку). Белые шашки могут ходить по клеткам
  одного цвета по диагонали вверх-влево или вверх-вправо. Ходов
  может быть несколько!'''

line1 = int(input())
col1 = int(input())
line2 = int(input())
col2 = int(input())

if line1 >= line2:
    print('NO')
elif (line2 - line1) < abs(col1 - col2):
    print('NO')


elif abs(line1 - line2) % 2 == 0:
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
