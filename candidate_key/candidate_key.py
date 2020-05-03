# https://programmers.co.kr/learn/courses/30/lessons/42890

from itertools import combinations

def solution(relation):
    n = len(relation[0])
    rows = len(relation)
    combs = []
    cnt = 0
    unique_set = []
    
    for i in range(1, n+1):
        for j in combinations(range(n), i):
            combs.append(set(j))
    
    for combination in combs:
        sets = set()
        for record in relation:
            tmp = ''
            for comb in combination:
                tmp += record[comb]
            sets.add(tmp)

        if len(sets) == rows:
            cnt += 1     
            unique_set.append(combination)
        
    del_set = set()
    for min_set in unique_set:
        for com_set in unique_set:
            if min_set.issubset(com_set) and min_set != com_set:
                del_set.add(unique_set.index(com_set))
    
    cnt = len(unique_set) - len(del_set)
    return cnt