'''Улитка ползет по вертикальному шесту высотой H метров,
поднимаясь за день на A метров, а за ночь спускаясь на B метров.
 На какой день улитка доползет до вершины шеста?'''

h = int(input())
a = int(input())
b = int(input())

if h <= a:
    print(1)
elif b == 0:
    print(h//a + 1)
else:
    print((h - a) // (a - b) + 1)
