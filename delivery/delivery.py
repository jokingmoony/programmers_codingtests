# https://programmers.co.kr/learn/courses/30/lessons/12978

def solution(N, road, K):
    answer = 0
    q = []
    adj = {i: [] for i in range(1, N+1)}
    for r in road:
        a, b, w = r
        adj[a].append((b, w))
        adj[b].append((a, w))

    distance = [float('inf') for _ in range(N+1)]
    visited = [0 for _ in range(N+1)]
    distance[1] = 0
    
    q.append((0, 1))
    while (len(q) != 0):
        q.sort(key=lambda x: x[0])
        a = q[0][1]
        q.pop(0)
        if visited[a]:
            continue
        visited[a] = True
        for b, w in adj[a]:
            if distance[a] + w < distance[b]:
                distance[b] = distance[a] + w
                q.append((distance[b], b))
    
    for dist in distance:
        if dist <= K:
            answer += 1
    return answer