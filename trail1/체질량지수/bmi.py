num = input().split()
h, w = int(num[0]), int(num[1])

b = (10000*w)//(h*h)

print(b)

if b>= 25:
    print("Obesity")