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

if (a1, b1, c1, a2, b2, c2) <= (0, 0, 0, 0, 0, 0):
    print('Boxes are incomparable')
elif (a1 == a2 and b1 == b2 and c1 == c2) or (
        a1 == a2 and b1 == c2 and c1 == b2) or (
        a1 == b2 and b1 == a2 and c1 == c2) or (
        a1 == b2 and b1 == c2 and c1 == a2) or (
        a1 == c2 and b2 == a2 and c1 == b2) or (
        a1 == c2 and b1 == b2 and c1 == a2):
    print('Boxes are equal')
elif (a1 <= a2 and b1 <= b2 and c1 <= c2) or (
        a1 <= a2 and b1 <= c2 and c1 <= b2) or (
        a1 <= b2 and b1 <= a2 and c1 <= c2) or (
        a1 <= b2 and b1 <= c2 and c1 <= a2) or (
        a1 <= c2 and b2 <= a2 and c1 <= b2) or (
        a1 <= c2 and b1 <= b2 and c1 <= a2):
    print('The first box is smaller than the second one')
else:
    print('The first box is larger than the second one')
