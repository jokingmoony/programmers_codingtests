# https://programmers.co.kr/learn/courses/30/lessons/64063

import sys
sys.setrecursionlimit(10**6) 

def find_next_room(m, room):
    if room not in m:
        m[room] = room + 1
        return room
    m[room] = find_next_room(m, m[room])
    return m[room]

def solution(k, room_number):
    answer = []
    m = dict()
    for room in room_number:
        next_room = find_next_room(m, room)
        answer.append(next_room)
    return answer