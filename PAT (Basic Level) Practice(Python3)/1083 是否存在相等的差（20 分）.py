N = int(input(""))
Number = input("").split(" ")
absN = []
for i in range(N):
    absN.append(abs(int(Number[i]) - (i+1)))


Result  = []
for i in range(N):
    Result.append(0)

for i in range(N):
    index = absN[i]
    Result[index] = Result[index]+1


for i in range(N-1,-1,-1):
    if(Result[i]>1):
        print(i,Result[i])

