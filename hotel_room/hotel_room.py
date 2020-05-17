# https://programmers.co.kr/learn/courses/30/lessons/64063

def b_search(arr, start, end, n):
    i = (start + end) // 2
    if arr[i] == n or start >= end:
        return i
    elif arr[i] > n:
        return b_search(arr, start, i - 1, n)
    else:
        return b_search(arr, i + 1, end, n)

def solution(k, room_number):
    answer = []
    rooms = [i for i in range(k+1)]
    for req in room_number:
        index = b_search(rooms, 0, len(rooms)-1, req)
        if rooms[index] < req:
            room = rooms[index+1]
        else:
            room = rooms[index]
        answer.append(room)
        rooms.remove(room)
    return answer