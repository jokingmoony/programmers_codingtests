# https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0
    stack = []
    n = len(board)
    
    for x in moves:
        new = 0
        for y in range(n):
            if board[y][x-1] != 0:
                new = board[y][x-1]
                board[y][x-1] = 0
                break
        if len(stack) != 0 and stack[-1] == new:
            stack.pop()
            answer += 2
        elif new != 0:
            stack.append(new)
    
    
    
    
    return answer