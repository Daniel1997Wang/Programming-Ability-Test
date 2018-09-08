def change(num):
    if len(num) == 3:
        num = num + "0"
    elif len(num) == 2:
        num = num + "00"
    elif len(num) == 1:
        num = num + "000"
    N,max,min = [],"",""
    for i in range(4):
        N.append(num[i])
    res = sorted(N)
    for i in range(4):
        min = min + res[i]
        max = max + res[3-i]
    return max,min

num = input("")

if (num[0]==num[1] and num[1]==num[2] and num[2]==num[3]):
    print(num+" - "+num+" = "+"0000")
else:
    while num!= "6174":
        max,min = change(num)
        num = int(max) - int(min)
        print(max + " - " + min + " = " + str(num))
        num = str(num)