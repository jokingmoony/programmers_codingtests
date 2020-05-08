# https://programmers.co.kr/learn/courses/30/lessons/17679
def is_deletable_block(board, row, col):
    if board[row][col] != ' ' and \
        board[row][col] == board[row+1][col] and \
        board[row][col] == board[row][col+1] and \
        board[row][col] == board[row+1][col+1]:
        return True
    
    return False

def solution(m, n, board):
    answer = 0
    playing = True
    board = [list(x) for x in board]

    while playing:
        
        found_set = set()
        # find delete
        for i in range(m-1):
            for j in range(n-1):
                if is_deletable_block(board, i, j):
                    found_set.add((i, j))
                    found_set.add((i+1, j))
                    found_set.add((i, j+1))
                    found_set.add((i+1, j+1))
        
        # if not found exit game
        if len(found_set) == 0:
            playing = False

        # delete
        for row, col in found_set:
            board[row][col] = ' '
            answer += 1

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