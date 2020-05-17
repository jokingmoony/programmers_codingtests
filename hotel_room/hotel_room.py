# https://programmers.co.kr/learn/courses/30/lessons/64063

def solution(k, room_number):
    answer = []
    rooms = {i:i+1 for i in range(0, k+2)}
    for req in room_number:
        if rooms[req] == req+1:
            answer.append(req)
            rooms[req] = rooms[req-1]
            rooms[req] = rooms[req+1]
        else:
            cur = req
            while rooms[cur] != cur + 1:
                cur += 1
            answer.append(cur)
            rooms[cur] = rooms[cur-1]
            rooms[cur] = rooms[cur+1]
    return answer