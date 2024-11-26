dp = [-1] * 6
def findMaxSum(arr, n):
    # code here

    def find(idx):
        if (dp[idx] != -1):
            return dp[idx]

        if (idx == 0):
            return arr[idx]

        if (idx < 0):
            return 0

        p = arr[idx] + find(idx - 2)

        np = 0 + find(idx - 1)

        dp[idx] = max(p, np)

        return max(p, np)

    return find(n - 1)

n = 6
arr = [5, 5, 10, 100, 10, 5]
print(findMaxSum(arr,6))
print(dp)
