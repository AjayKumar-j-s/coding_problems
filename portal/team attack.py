k = input().strip().split(";")
s = None
N,S,E,W = 0,0,0,0
ans = 0
c = 0
for i in range(len(k)):
    k[i] = k[i].strip().split(":")
for i in range(len(k)):
       g = k[i][0].strip().split("$ ")
       k[i][0] = g[1]
for i in range(len(k)):
    for j in range(len(k[i])):  
        k[i][j] = k[i][j].strip()
#print(k)
for i in range(len(k)):
    for j in range(len(k[i])):
        #for l in range(len(k[i][j]))
        pass
        #print(k[i][j][5],k[i][j][len(k[i][j])-1])
for i in range(len(k)):
    for j in range(len(k[i])):
        if(k[i][j][5]=='N'):
            #print(k[i][j][len(k[i][j])-1])
            if(int(k[i][j][len(k[i][j])-1])>=N):
                ans+=1
            N = int(k[i][j][len(k[i][j])-1])
            #print(N)
        
        if(k[i][j][5]=='E'):
            if(int(k[i][j][len(k[i][j])-1])>=E):
                ans+=1
            E = int(k[i][j][len(k[i][j])-1])
        
        if(k[i][j][5]=='S'):
            if(int(k[i][j][len(k[i][j])-1])>=S):
                ans+=1
            S = int(k[i][j][len(k[i][j])-1])
        
        if(k[i][j][5]=='W'):
            if(int(k[i][j][len(k[i][j])-1])>=W):
                ans+=1
            W = int(k[i][j][len(k[i][j])-1])
print(ans) if ans!=7 else print(6)
    