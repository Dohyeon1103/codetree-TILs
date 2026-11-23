N = int(input())
cnt = 0
answer = 0
for i in range(1, 101):
    cnt += i
    answer = i
    if cnt >= N:
        break

print(answer)


