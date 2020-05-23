# https://programmers.co.kr/learn/courses/30/lessons/12979

from math import ceil

def solution(n, stations, w):
    
    answer = 0
    last = [0]
    
    for station in stations:
        x, y = station-w, station+w
        dist = x - last[-1] -1
        if dist > 0:
            answer += ceil(dist / (2 * w + 1))
        last.append(y)
        
    y = stations[-1] + w
    if n - y > 0:
        answer += ceil((n - y) / (2 * w + 1))

    return answer