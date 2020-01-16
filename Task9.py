i = int(input())
if i < 10:
    print(i)
elif 10 <= i < 100:
    print((i % 10) + (i // 10))
elif 100 <= i <1000:
    print((i % 10) + ((i // 10) % 10) + (i // 100))
