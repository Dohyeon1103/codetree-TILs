num_list = list(map(int,input().split()))

for x in range(8):
    num_list.append((num_list[-1]+num_list[-2]) % 10)

for k in num_list:
    print(k, end = " ")