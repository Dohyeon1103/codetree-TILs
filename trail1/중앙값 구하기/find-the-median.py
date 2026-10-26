n = input().split()
a, b, c = int(n[0]), int(n[1]), int(n[2])

if (b > a and a > c) or (c > a and a > b):
    print(a)

elif (a > b and b > c) or (c > b and b > a):
    print(b)

else:
    print(c)