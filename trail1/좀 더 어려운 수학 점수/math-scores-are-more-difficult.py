A = input().split()
B = input().split()

am, ae = int(A[0]), int(A[1])
bm, be = int(B[0]), int(B[1])

if am > bm:
    print('A')
elif bm > am:
    print('B')
else:
    if ae > be:
        print('A')
    else:
        print('B')