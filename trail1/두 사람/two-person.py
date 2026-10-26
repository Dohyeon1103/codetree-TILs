a = input().split()
a_1, a_2 = int(a[0]), a[1]

b = input().split()
b_1, b_2 = int(b[0]), b[1]

if (a_1 >= 19 and a[1] == 'M') or (b_1 >= 19 and b[1] == 'M'):
    print(1)
else:
    print(0)