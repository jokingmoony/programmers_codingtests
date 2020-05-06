# https://programmers.co.kr/learn/courses/30/lessons/42891

from collections import deque


def solution(food_times, k):
    answer = 0
    index = 0
    n = len(food_times)
    foods = deque()
    food_number = 0
    
    for index, food in enumerate(food_times):
        foods.append((index + 1, food))
        
    while k > 0:
        if len(foods) == 0:
            return -1
        food_number, food_time = foods.popleft()
        food_time -= 1
        if food_time != 0:
            foods.append((food_number, food_time))
        k -= 1

    if len(foods) == 0:
        return -1
    return foods[0][0]
