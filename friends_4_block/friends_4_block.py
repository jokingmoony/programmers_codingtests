# https://programmers.co.kr/learn/courses/30/lessons/17679

def solution(m, n, board):
    answer = 0
    playing = True
    
    board = [list(x) for x in board]
    while playing:
        
        found_set = set()
        # find delete
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != ' ' and \
                    board[i][j] == board[i+1][j] and \
                    board[i][j] == board[i][j+1] and \
                    board[i][j] == board[i+1][j+1]:
                    found_set.add((i, j))
                    found_set.add((i+1, j))
                    found_set.add((i, j+1))
                    found_set.add((i+1, j+1))
        
        # if not found exit game
        if len(found_set) == 0:
            playing = False
            
        # delete
        answer += len(found_set)
        for found in found_set:
            board[found[0]][found[1]] = ' '
        
        # move
        for i in range(n):
            for j in range(m-1, -1, -1):
                if board[j][i] == ' ':
                    for k in range(j, -1, -1):
                        if board[k][i] != ' ':
                            board[j][i] = board[k][i]
                            board[k][i] = ' '
                            break        
    
    
    return answer