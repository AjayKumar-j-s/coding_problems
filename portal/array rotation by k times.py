def rotate(m,s):
    t,l=s,s
    b,r=len(m)-l-1,len(m[0])-l-1
    tp = m[t][l]
    for i in range(l,r):
        m[t][i] = m[t][i+1]
    for i in range(t,b):
        m[i][r] =m[i+1][r]
    for i in range(r,l,-1):
        m[b][i] = m[b][i-1]
    for i in range(b,t,-1):
        m[i][l] = m[i-1][l]
    m[t+1][l] = tp
r,c,k = (int(i) for i in input().split())
layer = min(r,c)//2
l = [[int(i) for i in input().split()]for j in range(r)]
for i in range(layer):
    for j in range(k):
        rotate(l,i)
for i in l:
    for j in i:
        print(j,end = " ")
    print()

        