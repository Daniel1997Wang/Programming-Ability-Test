
msg = input("").split(" ")
N,L,H = int(msg[0]),int(msg[1]),int(msg[2])

first,second,third,forth = [],[],[],[]
count = 0
for i in range(N):
    msg = input("").split(" ")
    msg[0], msg[1], msg[2] = msg[0], int(msg[1]), int(msg[2])
    if msg[1]>=L and msg[2]>=L:
        count  += 1
        msg.append((int(msg[1])+int(msg[2])))
        if msg[1]>=H and msg[2]>=H:
            first.append(msg)
        elif msg[1]>msg[2] and msg[2]<H:
            second.append(msg)
        elif msg[1]<H and msg[2]<H and msg[1]>msg[2]:
            third.append(msg)
        else:
            forth.append(msg)


first = sorted(first,key=lambda first:(-first[3],-first[1],int(first[0])))
second = sorted(second,key=lambda second:(-second[3],-second[1],int(second[0])))
third = sorted(third,key=lambda third:(-third[3],-third[1],int(third[0])))
forth = sorted(forth,key=lambda forth:(-forth[3],-forth[1],int(forth[0])))
res = first + second + third + forth


print(count)
for i in range(len(res)):
    if i!= (len(res)-1):
        print(res[i][0],res[i][1],res[i][2])
    else:
        print(res[i][0], res[i][1], res[i][2],end="")
