import heapq
def sort_by_frequency(arr):
    ans = []
    d = {}
    heapq.heapify(ans)
    for i in arr:
        d[i] = d.get(i,0)+1
    for i in d:
        heapq.heappush(ans,[-d[i],i])
    #print(ans)
    while(ans):
        a,b = heapq.heappop(ans)
        #print(ans)
        print(b,end = " ")






a = [1,1,1,2,2,4,4,3,3,5,5,5]
sort_by_frequency(a)