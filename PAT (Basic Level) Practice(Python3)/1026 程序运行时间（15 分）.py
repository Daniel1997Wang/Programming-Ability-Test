msg = input("").split(" ")
C = (int(msg[1]) - int(msg[0])) / 100
mm = int(C / 60)
ss = C - mm * 60 + 0.5
print("{:0>2d}:{:0>2d}:{:0>2d}".format(int(mm/60),int(mm%60),int(ss)),end="")