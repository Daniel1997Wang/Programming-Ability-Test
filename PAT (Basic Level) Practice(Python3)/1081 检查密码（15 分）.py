Number = "0123456789"
Str = "qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM"
All = Str + Number + "."


def is_legal(str):
    flag1, flag2 = 0, 0
    for i in range(len(str)):
        if str[i] not in All:
            return -1, -1  # 不合法
    for i in range(len(str)):
        if str[i] in Number :
            flag1 = 1  # 有数字

    for i in range(len(str)):
        if str[i] in Str:
            flag2 = 1  # 有字母

    return flag1, flag2


N = int(input(""))
Pass = []
for i in range(N):
    password = input("")
    Pass.append(password)


for i in range(len(Pass)):
    if(len(Pass[i])<=6):
        print("Your password is tai duan le.")
    else:
        flag1,flag2 = is_legal(Pass[i])
        if flag1==-1 and flag2 == -1:
            print("Your password is tai luan le.")
        elif flag1 == 0 and flag2 == 1:
            print("Your password needs shu zi.")
        elif flag1 == 1 and flag2 == 0:
            print("Your password needs zi mu.")
        elif flag1 == 1 and flag2 == 1:
            print("Your password is wan mei.")
