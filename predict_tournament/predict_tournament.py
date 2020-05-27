# https://programmers.co.kr/learn/courses/30/lessons/12985

def solution(n,a,b):
    answer = 0

    if a > b:
        a, b = b, a
    
    while a != b:
        if a % 2 == 0:
            a //= 2
        else:
            a = (a + 1) // 2
        
        if b % 2 == 0:
            b //= 2
        else:
            b = (b + 1) // 2
        answer += 1

    return answer