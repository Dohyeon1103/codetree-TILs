N = int(input())

sum_val = 0

for _ in range(N):
    num = int(input())
    sum_val += num

print(f'{sum_val} {sum_val/N:.1f}')