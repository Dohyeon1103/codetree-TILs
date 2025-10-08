a , b = map(int,input().split())

if a < b:
    r_1 = 1
else:
    r_1 = 0

if a == b:
    r_2 = 1
else:
    r_2 = 0
print(f"{r_1} {r_2}")