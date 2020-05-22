# https://programmers.co.kr/learn/courses/30/lessons/12987

def solution(A, B):
    answer = 0
    B.sort(reverse=True)
    A.sort(reverse=True)
    i = 0
    
    for a in A:
        if B[i] > a:
            answer += 1
            i += 1
        else:
            B.pop()
    
    
    
    return answer