cnt = 0
age = 0

while True:
    A = int(input())

    if 20 <= A and A <= 29:
        cnt += 1
        age += A
    
    else:
        print(f'{age/cnt:.2f}')
        break