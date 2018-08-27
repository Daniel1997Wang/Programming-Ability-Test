
str = input("")
str = str[str.index("P"):]
A_index = []
for i in range(len(str)):
    if(str[i] == "A"):
       A_index.append(i)


P_count,T_count = [],[]
p,t = 0,0
for i in range(len(str)):
    if str[i] == "P":
        p+=1
    elif str[i] == "T":
        t+=1
    elif str[i] == "A":
        P_count.append(p)
        T_count.append(t)
        p,t = 0,0
P_count.append(p)
T_count.append(t)

sum = 0
for i in range(len(A_index)):
    sum_P,sum_T = 0,0
    for j in range(0,i+1):
        sum_P = sum_P + P_count[j]
    for j in range(i+1,len(T_count)):
        sum_T = sum_T + T_count[j]
    sum = sum + sum_P * sum_T


print(sum,end="")