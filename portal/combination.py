a = [5,4,6,1]
def sub(p,up):
    if(not(up)):
        print(p)
        return
    sub(p+[up[0]],up[1:])
    sub(p,up[1:])
    
# for i in range(int(input())):
#     n = int(input())
#     a = [int(i) for i in input().split()]
#     ans = []
#     t = int(input())
#     a.sort()
#     com([],a,t,ans)
#     res = []
#     for i in ans:
#         if(i not in res):
#             res.append(i)
#     if(res):
#         print("( ",end = '')
#         for i in range(len(res)):
#             for j in range(len(res[i])):
#                 print(res[i][j],end= " ")
#             if(i != len(res)-1):
#                print(end = ")( ")
#             else:
#                 print(")")
#     else:
#         print("Empty")

sub([],a)