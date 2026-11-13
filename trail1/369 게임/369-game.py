N = int(input())

for i in range(1, N+1):
    if i <= 12:
        if i % 3 == 0:
            print("0", end = " ")
        else:
            print(i, end = " ")
    
    else:
        if i % 3 == 0:
            print("0", end = " ")
        elif str(i)[0] == "3" or str(i)[0]== "6" or str(i)[0]=="9":
            print("0", end = " ")
        elif str(i)[1] == "3" or str(i)[1] == "6" or str(i)[1] == "9":
            print("0", end = " ")
        else:
            print(i, end = " ")

