# https://programmers.co.kr/learn/courses/30/lessons/17681

def convert(n, x):
    res = [' ' for i in range(n)]
    i = 0
    while x > 0:
        if x % 2 == 1:
            res[i] = '#'
        x  = int(x / 2)
        i += 1
    return ''.join(res[::-1])

def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        answer.append(arr1[i] | arr2[i])
    
    answer = list(map(lambda x : convert(n, x), answer))
    
    return answer