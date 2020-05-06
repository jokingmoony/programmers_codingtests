# https://programmers.co.kr/learn/courses/30/lessons/42891
from collections import deque


def solution(food_times, k):
    
    n = len(food_times)
    foods = deque()
    food_number = 0
    
    times = int(k / n)
    offset = k % n
    
    for index, food in enumerate(food_times):
        foods.append([index + 1, food])
        
    while True:
        foods = deque(map(lambda x : [x[0], x[1] - times], foods))

        rest = -1 * sum(map(lambda x : x[1], list(filter(lambda x : x[1] < 0, foods))))
        foods = deque(filter(lambda x : x[1] > 0, foods))

        n = len(foods)
        
        if n == 0:
            return -1
        if rest == 0:
            break
        
        times = int(rest / n)
        
    while offset > 0:
        if len(foods) == 0:
            return -1
        food_number, food_time = foods.popleft()
        food_time -= 1
        if food_time != 0:
            foods.append((food_number, food_time))
        offset -= 1

    if len(foods) == 0:
        return -1
    return foods[0][0]
    
