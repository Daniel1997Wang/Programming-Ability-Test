number = input("").split()
N = []
for i in range(1,len(number)):
    N.append(int(number[i]))

sum = 0
for i in range(len(N)):
    for j in range(len(N)):
        if(i != j):
            number = N[i] * 10 + N[j]
            sum = sum + number
print(sum)