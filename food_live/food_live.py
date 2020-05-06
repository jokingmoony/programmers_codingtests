# https://programmers.co.kr/learn/courses/30/lessons/42891
def solution(food_times, k):
    
    n = len(food_times)
    foods = sorted([[index, time] for index, time in enumerate(food_times)], key=lambda x: x[1])
    start = 0
    l = 0
    for _, time in foods:
        if k - n * (time - l) < 0:
            break
        
        start += 1
        k -= n * (time - l)
        l += time - l
        n -= 1
        
    if n == 0:
        return -1
    
    foods = sorted(foods[start:], key=lambda x:x[0])
    k %= n
    
    try:
        answer = foods[k][0] + 1
    except:
        return -1
    return answer
    