# https://programmers.co.kr/learn/courses/30/lessons/1843
def solution(arr):
    answer = 0
    n = len(arr) // 2 + 1
    nums = arr[::2]
    
    dp = [[[0, 0] for i in range(n+1)] for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(2):
            dp[i][i][j] = int(nums[i-1])

    for L in range(2, n+1):
        for i in range(1, n-L+2):
            j = i + L - 1
            dp[i][j][0] = -float('inf')
            dp[i][j][1] = float('inf')
            for k in range(i, j-1+1):
                if arr[2 * k - 1] == '-':
                    cost_max = dp[i][k][0] - dp[k+1][j][1]
                    cost_min = dp[i][k][1] - dp[k+1][j][0]
                else:
                    cost_max = dp[i][k][0] + dp[k+1][j][0]
                    cost_min = dp[i][k][1] + dp[k+1][j][1]
                
                dp[i][j][0] = max(cost_max, dp[i][j][0])
                dp[i][j][1] = min(cost_min, dp[i][j][1])
    
    return dp[1][n][0]