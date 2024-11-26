def count(r,c):
    if(r == 1 or c == 1):
        return 1
    left = count(r-1,c)
    right = count(r,c-1)
    return left+right

def path(p,r,c):
    if(r == 1 and c == 1):
        l = []
        print(p)
        l.append(p)
        return l
    ans = []
    if(r>1):
       left =  path(p+"D",r-1,c)
       ans.extend(left)
    if(c>1):
       right =  path(p+"R",r,c-1)
       ans.extend(right)
    if(c>1 and r>1):
       g = path(p+"Di",r-1,c-1)
       ans.extend(g)
    return ans


print(path("",3,3))
