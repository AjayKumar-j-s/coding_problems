def per(p,up):
    if(not(up)):
        print(p)
        return
    for i in range(len(p)+1):
        ch = up[0]
        f = p[0:i]
        s = p[i:len(p)]
        f.append(ch)
        per(f[:]+s[:],up[1:])

print(per([],[1,2,3]))
