N = input().split()

a, b = int(N[0]), int(N[1])

if a >= 90:
    if b >= 95:
        print(100000)
    elif b >= 90:
        print(50000)
    else:
        print(0)

else:
    print(0)