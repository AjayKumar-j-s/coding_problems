"""n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]] """

n = 4
b = [["."]*4 for i in range(4)]
def safe(r,c):
    for i in range(r):
        if(b[i][c] != "."):
            return False
    maxl = min(r,c)
    for i in range(1,maxl+1):
        if(b[r-i][c-i] != "."):
            return False
    maxr = min(r,n-c-1)
    for i in range(1,maxr+1):
        if(b[r-i][c+i] != "."):
            return False
    return True

def solve(r):
    if(r == n):
        print(*b,sep = "\n")
        print()
        return 1
    for c in range(n):
        if(safe(r,c)):
            b[r][c] = "Q"
            solve(r+1)
            b[r][c] = "."
solve(0)

