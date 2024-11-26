def maximumSwap(num):
    l = list(str(num))
    t = [0] * len(l)
    t[-1] = len(l) - 1
    for i in reversed(range(len(l) - 1)):
        if (l[t[i + 1]] > l[i]):
            t[i] = t[i + 1]
        else:
            t[i] = i
    for i in range(len(l)):
        if(i!=t[i]):
            l[i],l[t[i]] = l[t[i]],l[i]
            break
    print(l)

    print(t)
    return 1
n = 9973
maximumSwap(n)