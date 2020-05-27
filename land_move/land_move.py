# https://programmers.co.kr/learn/courses/30/lessons/62050?language=python3
import sys
import math
sys.setrecursionlimit(100000)

def check(x, y, n):
    if x < 0 or x >= n:
        return False
    elif y < 0 or y >= n:
        return False
    return True

def dfs(i, j, area, visited, land, height):
    visited[i][j] = area
    offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    for x, y in offsets:
        nx, ny = i + x, j + y
        if check(nx, ny, len(land)):
            if not visited[nx][ny] and abs(land[i][j] - land[nx][ny]) <= height:
                dfs(nx, ny, area, visited, land, height)

def find(a, dset):
    while (a != dset[a-1]):
        a = dset[a-1];
    return a

def union(a, b, dset):
    a = find(a, dset)
    b = find(b, dset)
    dset[a-1] = b
                
def solution(land, height):
    answer = 0
    n = len(land)
    visited = [[0 for _ in range(n)] for _ in range(n)]

    # make area board
    area_num = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                area_num += 1
                dfs(i, j, area_num, visited, land, height)
#     print(visited)

    disjoint_set = [i for i in range(1, area_num + 1)]

    ladder_arr = []
    
    offsets = [(1, 0), (0, -1)]
    
    for i in range(n):
        for j in range(n):
            for x, y in offsets:
                nx, ny = x + i, y + j
                if check(nx, ny, n):
                    if visited[i][j] != visited[nx][ny]:
                        ladder_arr.append((visited[i][j], visited[nx][ny], abs(land[i][j] - land[nx][ny])))
    
    ladder_arr.sort(key=lambda x : x[2])

    cnt = 0
    for ladder in ladder_arr:
        s1, s2, val = ladder
        if cnt + 1 == area_num:
            break
        if find(s1, disjoint_set) != find(s2, disjoint_set):
            union(s1, s2, disjoint_set)
            answer += val
            cnt+=1

    return answer