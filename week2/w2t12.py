'''На доске стоит белая шашка. Требуется определить, может ли она
 попасть в заданную клетку, делая ходы по правилам и не пользуясь
  ходами дамки (т. е. не используя возможность перемещаться назад
  после превращения в дамку). Белые шашки могут ходить по клеткам
  одного цвета по диагонали вверх-влево или вверх-вправо. Ходов
  может быть несколько!'''

col1 = int(input())
line1 = int(input())
col2 = int(input())
line2 = int(input())

if line1 >= line2:
    print('NO')
elif (line2 - line1) < abs(col1 - col2) and (
        (col2 - (line2 - line1)) < col2 < (col2 + (line2 - line1))):
    print('NO')
elif (line2 - line1) % 2 != 0 and abs(col1 - col2) % 2 == 0:
    print('NO')
elif (line2 - line1) % 2 == 0 and abs(col1 - col2) % 2 != 0:
    print('NO')
else:
    print('YES')
