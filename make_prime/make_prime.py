# https://programmers.co.kr/learn/courses/30/lessons/12977

from itertools import combinations

def is_prime(n):
    
    if n % 2 == 0:
        return False
    
    i = 3
    
    while i*i <= n:
        if n % i == 0:
            return False
        i += 2
    
    return True

def solution(nums):
    answer = 0
    
    combs = combinations(nums, 3)
    
    for comb in combs:
        if is_prime(sum(comb)):
            answer += 1

    return answer