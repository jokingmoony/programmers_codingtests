# https://programmers.co.kr/learn/courses/30/lessons/64064

import re

visited = []
banned_lst = set()

def dfs(user_id, banned_id, index, n):
    global visited, banned_lst
    
    if n == len(banned_id):
        tmp = []
        for i, _ in enumerate(visited):
            if visited[i]:
                tmp.append(user_id[i])
        if len(tmp) == len(banned_id):
            banned_lst.add(tuple(tmp))
    else:
        for i, user in enumerate(user_id):
            reg = banned_id[index].replace('*','.')
            match = re.findall(reg, user)
            
            if match and len(user) == len(banned_id[index]):
                if visited[i] == False:
                    visited[i] = True
                    dfs(user_id, banned_id, index+1, n+1)
                    visited[i] = False
                
    
def solution(user_id, banned_id):
    global visited
    
    visited = [0 for x in range(len(user_id))]
    answer = 0
    dfs(user_id, banned_id, 0, 0)
    return len(banned_lst)