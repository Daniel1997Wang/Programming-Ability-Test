K = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
M = ["1","0","X","9","8","7","6","5","4","3","2"]
Num = ["0","1","2","3","4","5","6","7","8","9"]
N  = int(input(""))
flag = True
for k in range(N):
    invalid = True
    ID = input("")
    #判定合法性
    for i in range(17):
        if ID[i] not in Num:
            invalid = False
            print(ID)
            break
    #判定校验码
    if invalid:
        sum = 0
        for i in range(17):
            sum = sum + int(ID[i])*K[i]
        index = sum % 11
        if ID[17] != M[index]:
            print(ID)
            flag = False


if flag and invalid:
    print("All passed")

