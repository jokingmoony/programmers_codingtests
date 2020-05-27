# https://programmers.co.kr/learn/courses/30/lessons/12973

def solution(word):
    stack = []
    
    for c in word:
        stack.append(c)
        if len(stack) > 1:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
    
    if len(stack) == 0:
        return 1
    else:
        return 0

