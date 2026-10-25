n = input().split()

a, b, c = int(n[0]), int(n[1]), int(n[2])

if a <= b:
    if a <= c:
        print(a)
    else:
        print(c)

else:
    if b <= c:
        print(b)
    else:
        print(c)