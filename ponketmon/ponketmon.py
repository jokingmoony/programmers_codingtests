# https://programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
	
    answer = 0
    n = len(nums)
    x = n // 2
    sn = len(set(nums))
    answer = min(x, sn)
        
    return answer