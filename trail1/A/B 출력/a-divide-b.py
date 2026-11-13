n = input().split()

a, b = int(n[0]), int(n[1])
r = a // b
print(f'{r}.', end = "")
a = (a - r*b)*10

for i in range(20):
    r = a // b
    print(r, end = "")
    a = (a - r*b)*10





    
