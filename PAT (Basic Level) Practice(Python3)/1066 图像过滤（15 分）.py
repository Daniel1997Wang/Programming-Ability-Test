msg = input("").split(" ")
M,N,A,B,c = int(msg[0]),int(msg[1]),int(msg[2]),int(msg[3]),int(msg[4])
Color = []
for i in range(M):
    temp = input("").split(" ")
    for j in range(N):
        temp[j] = int(temp[j])
        if temp[j] >= A and temp[j] <= B:
            temp[j] = c
        print("{:>03d}".format(temp[j]), end="")
        if j != N-1:
            print(" ",end="")
    if i != M-1:
        print()