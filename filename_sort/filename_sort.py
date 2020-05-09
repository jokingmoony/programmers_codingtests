# https://programmers.co.kr/learn/courses/30/lessons/17686

import re

def swap(x, y):
    tmp = x
    
    x = y
    y = x

def solution(files):
    answer = []
    for file in files:
        answer.extend(re.findall(r'(\D+)(\d+)(.*)', file))
    
    n = len(answer)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if answer[j][0].lower() > answer[j+1][0].lower():
                answer[j], answer[j+1] = answer[j+1], answer[j]
            elif answer[j][0].lower() == answer[j+1][0].lower():
                if int(answer[j][1]) > int(answer[j+1][1]):
                    answer[j], answer[j+1] = answer[j+1], answer[j]

    answer = [x[0] + x[1] + x[2] for x in answer]
    return answer