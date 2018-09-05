n = int(input(""))
N,Jia,Yi = [],0,0
for i in range(n):
    number = input("").split()
    sum = int(number[0]) + int(number[2])
    if (int(number[1]) == sum and int(number[3]) != sum):
        Yi = Yi + 1
    if (int(number[1]) != sum and int(number[3]) == sum):
        Jia = Jia + 1
print(Jia, Yi)