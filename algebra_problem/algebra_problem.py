# https://programmers.co.kr/learn/courses/30/lessons/1843
def get_max(arr):
    res = 0
    if not '-' in arr:
        return sum(map(lambda x: int(x), arr[0::2]))
    
    for i in range(len(arr)):
        if arr[i] == '-':
            res = max(res, get_max(arr[:i]) - get_min(arr[i+1:]))
    return res
    
def get_min(arr):
    res = float('inf')
    if not '-' in arr:
        return sum(map(lambda x: int(x), arr[0::2]))
    
    for i in range(len(arr)):
        if arr[i] == '-':
            res = min(res, get_min(arr[:i]) - get_max(arr[i+1:]))
    
    return res


def solution(arr):
    answer = 1
    for i in range(len(arr)):
        cost = 0
        if arr[i] == '-':
            cost = get_max(arr[:i]) - get_min(arr[i+1:])
            if cost > answer:
                answer = cost
            
    return answer
