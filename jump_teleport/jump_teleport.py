# https://programmers.co.kr/learn/courses/30/lessons/12980

def solution(n):
    ans = 1
    
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            ans += 1
            
    return ans