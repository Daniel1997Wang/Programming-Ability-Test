msg = input("").split(" ")
T,K = int(msg[0]),int(msg[1])
Msg = []
for i in range(K):
    msg = input("").split(" ")
    Msg.append(msg)

for i in range(K):
    n1,b,t,n2 = int(Msg[i][0]),int(Msg[i][1]),int(Msg[i][2]),int(Msg[i][3])
    if T<=0:
        print("Game Over.",end="")
        break
    else:
        if T<t:
            print("Not enough tokens.  Total = {}.".format(T))
        else:
            if (n2 < n1 and b == 0) or (n2 > n1 and b == 1):
                T = T + t
                print("Win {}!  Total = {}.".format(t,T))
            else:
                T = T - t
                print("Lose {}.  Total = {}.".format(t, T))