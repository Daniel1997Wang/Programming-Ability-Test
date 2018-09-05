N = int(input(""))
for X  in range(N):
    msg = input("").split(" ")
    A,B,C = int(msg[0]),int(msg[1]),int(msg[2])
    if A+B > C:
        print("Case #" + str(X+1) + ": true")
    else:
        print("Case #" + str(X+1) + ": false")