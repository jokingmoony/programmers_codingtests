# https://programmers.co.kr/learn/courses/30/lessons/64062

def solution(stones, k):
    answer = 0
    stones_sorted = sorted(stones)
    
    appended = 0
    for min_stone in stones_sorted:
        min_stone -= appended
        appended += min_stone
        cnt = 0
        for i, stone in enumerate(stones):
            if stone == 0:
                cnt += 1
            else:
                cnt = 0
                stones[i] -= min_stone
            if cnt >= k:
                return answer
        answer += min_stone
    return answer