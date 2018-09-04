
N = int(input(""))
G,S = [],[]
for i in range(N):

    msg = input("").split(" ")
    if msg[0][0] == "B":
        grade = int(msg[1]) / 1.5
    elif msg[0][0] == "T":
        grade = int(msg[1]) * 1.5
    else:
        grade = int(msg[1])

    G.append(grade)
    school = msg[2].lower()
    S.append(school)





res = []
resG = []
count = []
for i in range(N):
    if S[i] not in res:
        res.append(S[i])
resG = [0] * len(res)
count = [0] * len(res)
for i in range(N):
    index = res.index(S[i])
    resG[index] = resG[index] + G[i]
    count[index] = count[index] + 1

for i in range(len(resG)):
    resG[i] = int(resG[i])

R = []
for i in range(len(resG)):
    temp = []
    temp.append(res[i])
    temp.append(int(resG[i]))
    temp.append(count[i])
    R.append(temp)


R = sorted(R,key=lambda R:(-R[1],R[2],R[0]))
print(len(R))
grade = -1
for i in range(len(R)):

    rank = i+1
    if(R[i][1] == grade):
        rank = rank - 1
    print(rank,R[i][0],R[i][1],R[i][2])
    grade = R[i][1]
