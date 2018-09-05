count = input("")
N = []
for i in range(int(count)):
    number = input("").split()
    N.append(number)


for i in range(len(N)):
    for j in range(len(N[i])):
        if(N[i][j][2] == 'T'):
            temp = N[i][j][0]
            if(temp == 'A'):
                print(1,end = "")
            if (temp == 'B'):
                print(2, end="")
            if (temp == 'C'):
                print(3, end="")
            if (temp == 'D'):
                print(4, end="")
