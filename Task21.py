'''Улитка ползет по вертикальному шесту высотой H метров,
поднимаясь за день на A метров, а за ночь спускаясь на B метров.
 На какой день улитка доползет до вершины шеста?'''

h = int(input())
a = int(input())
b = int(input())

print(h // a + (h // a * b - 1))
