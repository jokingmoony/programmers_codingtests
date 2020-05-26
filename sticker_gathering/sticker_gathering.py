# https://programmers.co.kr/learn/courses/30/lessons/12971

def solution(sticker):

    answer = 0
    
    n = len(sticker)
    visited = [0 for _ in range(n)]
    
    arr = [(v, i) for i, v in enumerate(sticker)]
    
    arr.sort(reverse=True)
    
    for i in range(n):
        cost = 0
        for j in range(i, n):
            v, i = arr[j]
            if not visited[i]:
                visited[i-1] = True
                visited[i] = True
                visited[(i+1)%n] = True
                cost += v
            else:
                if cost < answer:
                    break
                else:
                    answer = cost
        for j in range(n):
            visited[j] = False
            

    return answer