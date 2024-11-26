r, c = 3,4
m = [
   [1,2,3,6],
   [5,3,7,9],
   [10,4,11,12]
   ]
v = [[0] * c for i in range(r)]
mx = 0
cnt = 0


def find(x, y, p):
    print(1)
    global cnt,mx
    if (x < r and y < c and v[x][y] == 0):
        if (m[x][y] - p == 1):
            cnt += 1
            mx = max(cnt,mx)
            v[x][y] = 1
            if (find(x, y + 1, m[x][y]) or find(x + 1, y, m[x][y]) or find(x-1,y,m[x][y]) or find(x,y-1,m[x][y])):
                return True
            cnt -= 1
            v[x][y] = 0
    return False

for i in range(r):
    for j in range(c):
        find(i, j, m[i][j] - 1)

print(mx)