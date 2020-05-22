# https://programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        i = 0
        flag = True
        for s in skill_tree:
            if s in skill:
                if skill[i] == s:
                    i += 1
                else:
                    flag = False

        if flag:
            answer += 1
                
    return answer