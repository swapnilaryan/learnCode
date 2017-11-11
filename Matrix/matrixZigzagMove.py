matrix = []
result = []
r = 3
c = 3
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


def zigzag():
    global s
    m = 0  # for columns
    n = 0  # for rows
    i = 0
    j = 0
    k = 0

    if r==1 or c==1:
        for i in range(0, r):
            for j in range(0, c):
                s += str(matrix[i][j])+" "
        return s

    while k < r + c - 1 and (m < c or n < r):

        # print upwards
        while (0 <= i < r) and (0 <= j < c):
            # global s
            s = s + " " + str(matrix[i][j])
            i -= 1
            j += 1
        s += "\n"
        k += 1
        if i < 0 and j < c:
            i += 1
            j = k
        elif j >= c and k < r + c - 1:
            i = k % c + 1
            j = c - 1

        # print downwards
        while (0 <= i < r) and (0 <= j < c):
            s = s + " " + str(matrix[i][j])
            i += 1
            j -= 1

        s += "\n"
        k += 1
        if j < 0 and i < r:
            i = k
            j += 1
        elif i >= r and k < r + c - 1:
            j = k % r + 1
            i = r - 1


zigzag()

print s
