num = input().split()

a, b, c = int(num[0]), int(num[1]), int(num[2])

if a <= b and a <= c:
    print(1, end = " ")
else:
    print(0, end = " ")

if a == b == c:
    print(1, end = " ")
else:
    print(0, end = " ")
