'''По данному числу N распечатайте все целые степени двойки, не
превосходящие N, в порядке возрастания.Операцией возведения в
степень пользоваться нельзя!'''

N = int(input())

if N == 1:
    print(N)
elif N == 2 or N == 3:
    print(int(1), int(2), sep=" ")
else:
    print(int(1), int(2), sep=" ", end=' ')
    i = 4
    while i <= N:
        print(i, end=' ')
        i = i * 2

# i = 1
# while i <= N:
#     print(i, end=' ')
#     i = i * 2
