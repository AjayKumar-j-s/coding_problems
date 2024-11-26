def skip(st):
    if(not(st)):
        return ""
    ch = "" if st[0] == "a" else st[0]
    return  ch + skip(st[1:])
def skipapp(st):
    if(not(st)):
        return ""
    if(st.startswith('app') and not(st.startswith("apple"))):
        return skipapp(st[3:])
    else:
        return st[0] + skipapp(st[1:])
def sub(p,up):
    if(not(up)):
        l = []
        l.append(p)
        return l
    c = up[0]
    left = sub(p+c,up[1:])
    right = sub(p,up[1:])
    print(left,right)
    return left+right
# print(skipapp("baccappdappledc"))
print(sub("","abc"))