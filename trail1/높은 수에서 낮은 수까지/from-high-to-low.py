num = input().split()

A, B = int(num[0]), int(num[1])

if A >= B:
    for i in range(A, B-1, -1):
        print(i, end = " ")

else:
    for i in range(B, A-1, -1):
        print(i, end = " ")