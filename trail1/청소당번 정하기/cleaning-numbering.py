cnt_1 = 0
cnt_2 = 0
cnt_3 = 0

n = int(input())

for i in range(1,n+1):
    if i % 12 == 0:
        cnt_3 += 1
    elif i % 3 == 0:
        cnt_2 +=1
    elif i % 2 == 0:
        cnt_1 += 1

print(f'{cnt_1} {cnt_2} {cnt_3}')
