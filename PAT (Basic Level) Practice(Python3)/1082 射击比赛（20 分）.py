N = int(input(""))
Result = []
for i in range(N):
    temp = []
    msg = input("").split(" ")
    ID,x,y = msg[0],int(msg[1]),int(msg[2])
    distance = x*x + y*y
    temp.append(ID)
    temp.append(distance)
    Result.append(temp)

r = sorted(Result,key=lambda Result:Result[1])

print(r[0][0],r[N-1][0],end="")