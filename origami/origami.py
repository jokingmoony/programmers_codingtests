# https://programmers.co.kr/learn/courses/30/lessons/62049

def b(cnt, n, c, answer):
    if cnt < n:
        b(cnt+1, n, 0, answer)
        answer.append(c)
        b(cnt+1, n, 1, answer)
        

def solution(n):
    answer = []
    b(0, n, 0, answer)
    return answer