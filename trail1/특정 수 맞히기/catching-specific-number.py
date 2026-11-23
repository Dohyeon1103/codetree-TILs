N = 25

while True:
    num = int(input())

    if num < N:
        print("Higher")
    elif num > N:
        print("Lower")
    else:
        print("Good")
        break