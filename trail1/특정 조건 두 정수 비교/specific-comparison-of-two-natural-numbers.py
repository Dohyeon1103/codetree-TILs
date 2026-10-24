n = input().split()
a, b = int(n[0]), int(n[1])

if a < b:
    r1 = 1
else:
    r1 = 0

if a == b:
    r2 = 1
else:
    r2 = 0

print(f'{r1} {r2}')