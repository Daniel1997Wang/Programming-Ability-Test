def PAT(A,DA):
    PA = ""
    for i in range(len(A)):
        if (A[i] == DA):
            PA = PA + A[i]
    if PA == "":
        PA = 0
    return int(PA)

msg = input("").split(" ")
A,DA,B,DB = msg[0],msg[1],msg[2],msg[3]
print(PAT(A,DA)+PAT(B,DB),end="")
