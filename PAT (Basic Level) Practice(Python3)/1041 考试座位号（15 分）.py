N = int(input(""))
stu = []
for i in range(N):
    msg = input("").split(" ")
    stu.append(msg)
n = int(input(""))
search = input("").split(" ")

for i in range(n):
    for j in range(N):
        if stu[j][1] == search[i]:
            print(stu[j][0],stu[j][2])
