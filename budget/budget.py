# https://programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    answer = 0
    d.sort()
    for c in d:
        if budget - c >= 0:
            budget -= c
            answer += 1
        else:
            break
    return answer