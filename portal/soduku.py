def safe(g,r,c,num):
    for i in range(9):
        if(g[r][i]==num):
            return False
    for i in range(9):
        if(g[i][c]==num):
            return False
    sR = r-r%3
    sC = c-c%3
    for i in range(3):
        for j in range(3):
            if(g[sR+i][sC+j]==num):
                return False
    return True
def solve(g,r,c):
    if(r==8 and c == 9):
        return True
    if(c==9):
        r = r+1
        c = 0
    if(g[r][c]!="."):
        return solve(g,r,c+1)
    for n in range(1,10):
        if(safe(g,r,c,str(n))):
            g[r][c] = str(n)
            if(solve(g,r,c+1)):
                return True
        
            g[r][c] = "."
    return False
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
solve(board,0,0)
print(*board,sep = "\n")