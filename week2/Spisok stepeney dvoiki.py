'''По данному числу N распечатайте все целые степени двойки, не
превосходящие N, в порядке возрастания.Операцией возведения в
степень пользоваться нельзя!'''

N = int(input())
i = 1
while i <= N:
    print(i)
    i = i * 2
