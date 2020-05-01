# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    answer = []
    tmp = []
    for i in range(1, N+1):
        n = len(list(filter(lambda x : x >= i, stages)))
        if n == 0:
            tmp.append((i, 0.0))
        else:
            tmp.append((i, stages.count(i) / n))
    tmp.sort(key=lambda tup : tup[1], reverse=True)
    for t in tmp:
        answer.append(t[0])
    return answer