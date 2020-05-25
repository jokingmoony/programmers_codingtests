# https://programmers.co.kr/learn/courses/30/lessons/12984


def solution(land, P, Q):

    land_1d = []
    total = 0
    for i in land:
        for j in i:
            land_1d.append(j)
            total += j

    land_1d.sort()
    prev = 0
    answer = float('inf')
    already = -1
    for i, l in enumerate(land_1d):
        if l != already:
            up = l * i - prev
            down = total - prev - (len(land_1d) - i) * l
            answer = min(answer, P*up + Q*down)
            already = l
        prev += l
    
    return answer