# https://programmers.co.kr/learn/courses/30/lessons/62048

def check(arr):
    if min(arr) * max(arr) < 0:
        return True
    return False

def solution(w,h):
    answer = w * h
    
    for r in range(w):
        for c in range(h):
            tmp = []
            for x, y in [(r, c), (r+1, c), (r, c+1), (r+1, c+1)]:
                tmp.append(h/w * x - y)
            
            if check(tmp):
                answer -= 1
            
                
    return answer