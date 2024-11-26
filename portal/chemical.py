from collections import deque
h = {}
for i in range(int(input())):
    s = input().split("=")
    s1 = s[1].split("+")
    h[s[0]] = s1
l = []
bow = 1
for i in range(int(input())):
        st = input()
        if(st not in l):
            q = deque()
            q.append(st)
            while(q):
                b = q.popleft()
                l.append(b)
                for j in h[b]:
                    if(j in h and j not in l):
                        bow+=1
                        q.append(j)
print(bow)
                    

    