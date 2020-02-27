a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())

v1 = (a1 // a2) * (b1 // b2) * (c1 // c2)
v2 = (a1 // a2) * (b1 // c2) * (c1 // b2)
v3 = (a1 // b2) * (b1 // a2) * (c1 // c2)
v4 = (a1 // b2) * (b1 // c2) * (c1 // a2)
v5 = (a1 // c2) * (b1 // a2) * (c1 // b2)
v6 = (a1 // c2) * (b1 // b2) * (c1 // a2)

if ((a1 < a2) or (b1 < b2) or (c1 < c2)) and \
        ((a1 < a2) or (b1 < c2) or (c1 < b2)) and \
        ((a1 < b2) or (b1 < a2) or (c1 < c2)) and \
        ((a1 < b2) or (b1 < c2) or (c1 < a2)) and \
        ((a1 < c2) or (b1 < a2) or (c1 < b2)) and \
        ((a1 < c2) or (b1 < b2) or (c1 < a2)):
    print(0)
elif v1 > v2 and v1 > v3 and v1 > v4 and v1 > v5 and v1 > v6:
    print(v1)
elif v2 > v3 and v2 > v4 and v2 > v5 and v2 > v6:
    print(v2)
elif v3 > v4 and v3 > v5 and v3 > v6:
    print(v3)
elif v4 > v5 and v4 > v6:
    print(v4)
elif v5 > v6:
    print(v5)
else:
    print(v6)
