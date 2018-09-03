def translat(strtime):
    msg = strtime.split("/")
    yyyy    = int(msg[0])
    mm      = int(msg[1])
    dd      = int(msg[2])
    time = yyyy*10000 + mm*100 + dd
    return time



early_time = translat("1814/09/06")
late_time = translat("2014/09/06")



N = int(input(""))
PAT_Print = []
count = 0
for i in range(N):
    msg = input("").split(" ")
    name,time = msg[0],msg[1]
    new_time = translat(time)
    if (new_time >= early_time) and (new_time <= late_time):
        temp = []
        temp.append(name)
        temp.append(new_time)
        PAT_Print.append(temp)
        count += 1

if count == 0:
    print(0, end="")
elif count == 1:
    print(1, PAT_Print[0][0], PAT_Print[0][0], end="")
elif count == 2:
    PAT_Print = sorted(PAT_Print, key=lambda PAT_Print: PAT_Print[1])
    print(2, PAT_Print[0][0], PAT_Print[1][0], end="")
else:
    PAT_Print = sorted(PAT_Print,key=lambda PAT_Print:PAT_Print[1])
    print(count,PAT_Print[0][0],PAT_Print[count-1][0],end="")