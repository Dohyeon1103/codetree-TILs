a = input().split()
b = input().split()
c = input().split()

a1, a2 = a[0], int(a[1])
b1, b2 = b[0], int(b[1])
c1, c2 = c[0], int(c[1])

d = 0

if a1 == 'Y' and a2 >= 37:
    d += 1
if b1 == 'Y' and b2 >= 37:
    d+=1
if c1 == 'Y' and c2 >= 37:
    d+=1

if d >= 2:
    print('E')
else:
    print("N")