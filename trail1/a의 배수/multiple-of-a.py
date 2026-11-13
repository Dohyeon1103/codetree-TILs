num = input().split()

N, a = int(num[0]), int(num[1])

i = 1

while i < N+1:
    if i % a == 0:
        print("1")
    else:
        print("0")
    i += 1