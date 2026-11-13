n = input().split()
A, N = int(n[0]), int(n[1])
r = A + N
print(r)
for _ in range(N-1):
    r += N
    print(r)
    