while True:
    rec = input().split()
    a, b, r = int(rec[0]), int(rec[1]), rec[2]
    print(a*b)
    if r == 'C':
        break