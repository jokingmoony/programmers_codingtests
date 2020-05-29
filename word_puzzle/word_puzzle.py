# https://programmers.co.kr/learn/courses/30/lessons/12983

def solution(strs, t):
    n = len(t)
    dp = [float('inf') for _ in range(n)]
    for i in range(1, n+1):
        for word in strs:
            l = len(word)
            if l > i:
                continue
            if word == t[i-l:i]:
                if i - l == 0:
                    dp[i-1] = 1
                    continue
                dp[i-1] = min(dp[i-1], dp[i-l-1]+1)
    
    answer = dp[n-1]
    if answer == float('inf'):
        return -1
    return answer