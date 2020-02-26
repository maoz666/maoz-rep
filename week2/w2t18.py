'''Есть две коробки, первая размером A₁×B₁×C₁, вторая размером
 A₂×B₂×C₂. Определите, можно ли разместить одну из этих коробок
  внутри другой, при условии, что поворачивать коробки можно только
   на 90 градусов вокруг ребер'''

a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())

if (a1 == a1 and b1 == b2 and c1 == c2) or (
        a1 == a2 and b1 == c2 and c1 == b2) or (
        a1 == b2 and b1 == a1 and c1 == c2) or (
        a1 == b2 and b1 == c2 and c1 == a1) or (
        a1 == c2 and b2 == a1 and c1 == b2) or (
        a1 == c2 and b1 == b2 and c1 == a2):
    print('Boxes are equal')
elif (a1 < a1 and b1 < b2 and c1 < c2) or (
        a1 < a2 and b1 < c2 and c1 < b2) or (
        a1 < b2 and b1 < a1 and c1 < c2) or (
        a1 < b2 and b1 < c2 and c1 < a1) or (
        a1 < c2 and b2 < a1 and c1 < b2) or (
        a1 < c2 and b1 < b2 and c1 < a2):
    print('The first box is smaller than the second one')
elif (a1 > a1 and b1 > b2 and c1 > c2) or (
        a1 > a2 and b1 > c2 and c1 > b2) or (
        a1 > b2 and b1 > a1 and c1 > c2) or (
        a1 > b2 and b1 > c2 and c1 > a1) or (
        a1 > c2 and b2 > a1 and c1 > b2) or (
        a1 > c2 and b1 > b2 and c1 > a2):
    print('The first box is larger than the second one')
else:
    print('Boxes are incomparable')
    