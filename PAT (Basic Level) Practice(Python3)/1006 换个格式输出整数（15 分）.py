n = int(input(""))
B = int(n / 100)
S = int((n-B*100) / 10)
G = int(n % 10)
print("B"*B,end="")
print("S"*S,end="")
for i in range(G):
    print(i+1,end="")