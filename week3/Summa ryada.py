'''По данному числу n вычислите сумму (1 / 1²)+(1 / 2²)+(1 / 3²)+...+(1 / n²).
'''
n = int(input())
s = 0
while n != 0:
    s += (1 / n ** 2)
    n -= 1
if s % 1 != 0:
    print('{0:.5f}'.format(s))
else:
    print(int(s))
