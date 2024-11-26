def combinationSum(candidates, target):
    ans = []

    def comb(idx, ds, t, s):
        if (t == s):
            ans.append(ds[:])
            return
        if (idx >= len(candidates) or s > t):
            return
        ds.append(candidates[idx])
        comb(idx, ds, t, s + candidates[idx])
        ds.pop()
        comb(idx + 1, ds, t, s)

    comb(0, [], target, 0)
    return ans
def comb(ans,arr,t,a):
    if(t == 0):
        ans.append(a[:])
        return
    for i in range(len(arr)):
        if(arr[i]<=t):
            a.append(arr[i])
            comb(ans,arr,t-arr[i],a)
            a.pop()


candidates = [2,3,5];target = 8
ans = []
a = []
ans = combinationSum(candidates,target)
print(ans)
# print(combinationSum(candidates,target))