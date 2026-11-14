num = input().split()
if int(num[0]) >= int(num[1]):
    A = int(num[1])
    B = int(num[0])
else:
    A = int(num[0])
    B = int(num[1])

sum_val = 0

for i in range(A,B+1):
    if i % 5 == 0:
        sum_val += i

print(sum_val)