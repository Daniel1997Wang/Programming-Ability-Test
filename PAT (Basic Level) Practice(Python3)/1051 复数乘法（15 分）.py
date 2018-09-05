import math
msg = input("").split(" ")
R1,P1,R2,P2 = float(msg[0]),float(msg[1]),float(msg[2]),float(msg[3])
A,B = R1*R2*math.cos(P1+P2),R1*R2*math.sin(P1+P2)

if A>-0.005 and A<0:
    print("0.00",end="")
else:
    print("{:.2f}".format(A),end="")

if B>-0.005 and B<0:
    print("+0.00i",end="")
elif B<=-0.005:
    print("{:.2f}i".format(B),end="")
else:
    print("+{:.2f}i".format(B), end="")