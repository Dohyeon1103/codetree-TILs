num = input().split()

a, b = int(num[0]), int(num[1])

prod = 1
for _ in range(b):
    prod *= a

print(prod)