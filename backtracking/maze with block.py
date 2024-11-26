def find(board,r,c,cnt):
    if(r==2 and c==2):
        board[r][c]= cnt
        print(*board,sep = "\n")
        print(cnt)
        return
    board[r][c] = cnt
    if(r<2):
        find(board,r+1,c,cnt+1)
    if(c<2):
        find(board, r, c+1, cnt + 1)
    board[r][c] = 0


board = [[0]*3 for i in range(3)]
find(board,0,0,1)
