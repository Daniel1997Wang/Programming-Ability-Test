n = input("")
Num = "0123456789"
count = [0] * 10
for i in range(len(n)):
    index = Num.index(n[i])
    count[index] = count[index] + 1
for i in range(10):
    if count[i] != 0:
        print(str(i)+":"+str(count[i]))
