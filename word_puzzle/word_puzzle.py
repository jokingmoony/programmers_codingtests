# https://programmers.co.kr/learn/courses/30/lessons/12983
# reference: https://whilescape.tistory.com/entry/Algorithm-programmerskakao2017%ED%8C%81%EC%8A%A4%ED%83%80%EC%9A%B4level4%EB%8B%A8%EC%96%B4-%ED%8D%BC%EC%A6%90
def solution(strs, t):
    dp = {}
    for i in range(len(t)):
        dp[i] = float('inf')
    
    for i in range(len(t) -1, -1, -1):
        for k in range(1, 6):
            if t[i:i+k] in strs:
                dp[i] = min(dp.get(i), dp.get(i+k, 0)+1)
    return dp.get(0) if dp.get(0) != float('inf') else -1