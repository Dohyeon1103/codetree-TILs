num = input().split()

a, b = int(num[0]), int(num[1])

prod = 1

for i in range(a, b+1):
    prod *= i

print(prod)