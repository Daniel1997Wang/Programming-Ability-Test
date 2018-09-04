msg = input("").split(" ")
d,N = msg[0],int(msg[1])

if N == 1:
    print(1,end="")
else:
    for i in range(N-1):
        d = d + "#"
        index = [0]
        for i in range(len(d)-1):
            if d[i] != d[i+1]:
                index.append(i+1)

        count = []
        for i in range(len(index)-1):
            temp = index[i+1]-index[i]
            count.append(temp)

        res = ""
        for i in range(len(count)):
            res = res + str(d[index[i]]) + str(count[i])
        d = res + "#"


    print(res,end="")