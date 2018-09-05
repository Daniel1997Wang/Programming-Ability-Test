msg = input("").split(" ")
N,C = int(msg[0]),msg[1]
n = int(N/2 + 0.5) - 2
print(C*N)
for i in range(n):
    print(C+" "*int(N-2)+C)
print(C*N,end="")