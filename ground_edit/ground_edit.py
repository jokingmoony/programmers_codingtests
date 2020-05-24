# https://programmers.co.kr/learn/courses/30/lessons/12984

def process(land, mid, P, Q):
    cost = 0
    for rows in land:
        for block in rows:
            if block < mid:
                cost += (mid - block) * P
            else:
                cost += (block - mid) * Q

    return cost

def solution(land, P, Q):
    answer = float('inf')
    
    start = 1
    end = 10000000000
    
    while start < end:
        
        mid = (start + end) // 2
        cost = process(land, mid, P, Q)
        if answer > cost:
            answer = cost
            end = mid - 1
        else:
            start = mid + 1
            
    
    return answer