matrix = []
result = []
r = 5
c = 5
k = 0
m = 0
for i in range(0, r):
    temp = []
    for j in range(0, c):
        k += 1
        temp.append(k)
    matrix.append(temp)

for i in range(0, r, 1):
    print matrix[i]

s = ""


def diagonallyUpwards():
    i = j = m = 0
    k = 0
    while k < r + c - 1 and m < c:
        while (0 <= i < r) and (0 <= j < c):
            global s
            s = s + " " + str(matrix[i][j])
            i -= 1
            j += 1
        s += "\n"
        k += 1
        if k < r:
            i = k
            j = 0
        else:
            i = r - 1
            m += 1
            j = m


diagonallyUpwards()

print s
