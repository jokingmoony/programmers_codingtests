# https://programmers.co.kr/learn/courses/30/lessons/64062

def bsearch(stones, start, end, k):
    res = 0
    
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for stone in stones:
            if stone - mid <= 0:
                cnt += 1
            elif cnt >= k:
                break
            else:
                cnt = 0
        
        if cnt >= k:
            end = mid - 1
        else:
            start = mid + 1
        
    res = start
    return res
    

def solution(stones, k):
    
    return bsearch(stones, 0, max(stones), k)