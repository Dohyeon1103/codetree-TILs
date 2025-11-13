a, b = map(str, input().split())

A, B = len(a), len(b)

if A > B:
    print(f'{a} {A}')

elif A == B:
    print('same')

else:
    print(f'{b} {B}')