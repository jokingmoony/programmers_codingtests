# https://programmers.co.kr/learn/courses/30/lessons/17680

from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque(maxlen=cacheSize)
    cities = list(map(lambda x : x.lower(), cities))
    for city in cities:
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        # city not in chace
        else:
            cache.append(city)
            answer += 5

    return answer