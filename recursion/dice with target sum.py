def find(ds,t):
    if(t == 0):
        print(ds)
        return
    for i in range(1,7):
        if(i<=t):
            ds.append(i)
            find(ds,t-i)
            ds.pop()
ans = []
find([],4)
print(ans)