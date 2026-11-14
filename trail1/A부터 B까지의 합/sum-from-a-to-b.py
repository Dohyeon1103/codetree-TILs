n = input().split()
a, b = int(n[0]), int(n[1])
num_sum = 0

for i in range(a, b+1):
    num_sum += i

print(num_sum)