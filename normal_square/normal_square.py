# https://programmers.co.kr/learn/courses/30/lessons/62048
import math

def check(arr):
    if min(arr) * max(arr) < 0:
        return True
    return False

def getEmpty(w, h):
    cnt = 0
    for r in range(w):
        for c in range(h):
            tmp = []
            for x, y in [(r, c), (r+1, c), (r, c+1), (r+1, c+1)]:
                tmp.append(h/w * x - y)
            
            if check(tmp):
                cnt += 1

    return cnt

def solution(w,h):
    answer = w * h
    ww = w
    hh = h
    g = math.gcd(w, h)
    
    answer -= (getEmpty(w//g, h//g) * g)
            
                
    return answer