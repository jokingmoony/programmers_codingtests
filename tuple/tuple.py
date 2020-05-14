https://programmers.co.kr/learn/courses/30/lessons/64065

import re

def solution(s):
    answer = []
    s = s[1:-1]
    tuple_lst = []
    tmp_lst = (re.findall('\{\d+[,\d+]*\}', s))
    for t in tmp_lst:
        tuple_lst.append(re.findall('\d+', t))
    
    tuple_lst.sort(key=lambda x: len(x))
    for e in tuple_lst:
        new = set(answer) ^ set(e)
        answer.append(new.pop())
    answer = list(map(lambda x : int(x), answer))
    return answer