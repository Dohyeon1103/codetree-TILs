na = input().split()
am , ae = int(na[0]), int(na[1])

nb = input().split()
bm, be = int(nb[0]), int(nb[1])

if am > bm and ae > be:
    print(1)
else:
    print(0)