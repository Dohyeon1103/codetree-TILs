n = input().split()

a, b, c = int(n[0]), int(n[1]), int(n[2])

if a >= b:
    if a >= c:
        print(f'{a}')
    else:
        print(f'{c}')

else:
    if b >= c:
        print(f'{b}')
    else:
        print(f'{c}')