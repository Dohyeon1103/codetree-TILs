N = int(input())

for i in range(1,50):
    N = N // i
    if N <= 1:
        print(i)
        break

