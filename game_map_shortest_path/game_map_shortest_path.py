# https://programmers.co.kr/learn/courses/30/lessons/1844

def check(x, y, n, m, visited, maps):
    if x < 0 or x >= n:
        return False
    if y < 0 or y >= m:
        return False
    if visited[x][y]:
        return False
    if maps[x][y] == 0:
        return False
    return True

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[0 for _ in range(m)] for _ in range(n)]

    queue = [(0, 0, 1)]
    visited[0][0] = 1
    
    while len(queue) != 0:
        x, y, c = queue.pop(0)
        if x == n-1 and y == m-1:
            return c
        for ax, ay in move:
            nx, ny = x + ax, y + ay
            if check(nx, ny, n, m, visited, maps):
                queue.append((nx, ny, c + 1))
                visited[nx][ny] = 1
        
    return -1