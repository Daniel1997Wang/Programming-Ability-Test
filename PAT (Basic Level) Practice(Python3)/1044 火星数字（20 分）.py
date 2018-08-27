
L = ["tret","jan", "feb", "mar", "apr", "may", "jun", "jly", "aug", "sep", "oct", "nov", "dec"]
H = ["tret","tam", "hel", "maa", "huh", "tou", "kes", "hei", "elo", "syy", "lok", "mer", "jou"]
N = int(input(""))
Num = []
for i in range(170):
    Num.append(str(i))


def to_earth(n):
    low = n % 13
    hight = n // 13
    if hight == 0:
        return L[low]
    elif low == 0:
        return H[hight]
    else:
        return H[hight]+" "+L[low]

def to_mar(str):
    if len(str)>4:
        str_list = str.split(" ")
        hight = H.index(str_list[0])
        low = L.index(str_list[1])
        number = hight*13+low
        return number
    else:
        if str in L:
            return L.index(str)
        else:
            return H.index(str)*13


res = []
for i in range(N):
    number = input("")
    if number in Num:
        res.append(to_earth(int(number)))
    else:
        res.append(to_mar(number))



for i in range(N):
    print(res[i],end="")
    if i!=N-1:
        print()


