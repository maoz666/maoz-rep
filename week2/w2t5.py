'''Шахматный король ходит по горизонтали, вертикали и диагонали,
но только на 1 клетку. Даны две различные клетки шахматной доски,
определите, может ли король попасть с первой клетки на вторую
одним ходом.'''

col1 = int(input())
lin1 = int(input())
col2 = int(input())
lin2 = int(input())

if col1 - col2 > 1 and lin2 - lin1 > 1:
    print('NO')
elif col1 == col2 and lin1 == lin2:
    print('NO')
else:
    print('YES')
