"""По данному натуральному n вычислите сумму 1²+2²+3²+...+n²."""

n = int(input())
summ = 0
while n != 0:
    summ += n ** 2
    n -= 1
print(summ)
