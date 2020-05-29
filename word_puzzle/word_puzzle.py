# https://programmers.co.kr/learn/courses/30/lessons/12983

def solution(strs, t):
    answer = 0
    
    n = len(t)
    dp = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
    for word in strs:
        for i, c in enumerate(t):
            if t[i:].startswith(word):
                dp[i+1][i+len(word)] = 1
                
    for L in range(2, n+1):
        for i in range(1, n-L+2):
            j = i + L - 1
#             dp[i][j]
            for k in range(i, j-1+1):
                dp[i][j] = min(dp[i][k] + dp[k+1][j], dp[i][j])
    
    if dp[1][n] == float('inf'):
        return -1
    else:
        return dp[1][n]