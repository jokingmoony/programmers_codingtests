# https://programmers.co.kr/learn/courses/30/lessons/60062
import copy

def solution(n, weak, dist):
    answer = 0
    min = len(dist) + 1
    checkers = sorted(copy.deepcopy(dist), reverse=True)

    for i, checker in enumerate(checkers):
        max_checked_walls = []
        max_checked_counts = 0
        for j in range(len(weak)):
            cnt = 0
            weak.insert(0, weak.pop())
            walls = copy.deepcopy(weak)
            start = walls.pop(0)
            checked_walls = list(map(lambda x : x % n if x >= n else x, list(range(start, checker + start + 1))))
            for wall in checked_walls:
                if wall in walls:
                    cnt += 1
            if max_checked_counts < cnt:
                max_checked_counts = cnt
                max_checked_walls = checked_walls
        
        print(checker, max_checked_walls)
        for wall in max_checked_walls:
            if wall in weak:
                weak.remove(wall)
                
        if len(weak) == 0:
            if min > i + 1:
                min = i + 1
            break
                
    if min == len(dist) + 1:
        return -1
    else:
        return min
            
    
#     for i in range(len(weak)):
#         weak.insert(0, weak.pop())
#         walls = copy.deepcopy(weak)
#         start = walls.pop(0)
#         for i, checker in enumerate(checkers):
#             for a in map(lambda x : x % n if x >= n else x, list(range(start, checker + start + 1))):
#                 if a in walls:
#                     walls.remove(a)
#             if len(walls) == 0:
#                 if i + 1 < min:
#                     min = i + 1
#                 break
#             else:
#                 start = walls.pop(0)
#     if min == len(dist) + 1:
#         return -1
#     else:
#         return min