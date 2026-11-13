num = input().split()

A, B = int(num[0]), int(num[1])

if A > 0:
    for _ in range(B):
        print(A,end="")
    
else:
    print("0")