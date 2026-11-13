num = input().split()
A, B = int(num[0]), int(num[1])

while A <= B:
    print(A, end = " ")
    if A % 2 == 0:
        A += 3
    else:
        A *= 2
