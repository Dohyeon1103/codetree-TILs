N = int(input())
n_list = list(map(int,input().split()))
new_list = [x**2 for x in n_list]
for x in new_list:
    print(x, end = " ")