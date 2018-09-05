count = input("").split()
N = []
for i in range((int(count[0]) + 2)):
    number = input("").split()
    N.append(number)

Grade,Right = N[0],N[1]

for i in range(2, len(N)):
    grade = 0
    for j in range(len(Grade)):
        if (int(N[i][j]) == int(Right[j])):
            grade = grade + int(Grade[j])
    print(grade)
