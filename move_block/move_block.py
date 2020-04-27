# https://programmers.co.kr/learn/courses/30/lessons/60063

import numpy as np
from copy import deepcopy

def bfs(board, n, machine, visited):
    machine = deepcopy(machine)
    
    visited[machine[0], machine[1], 0] = True
    visited[machine[2], machine[3], 1] = True
    
    if visited[n, n, 0] and visited[n, n, 0]:
        return
    
    
    
    bfs(board, n, machine, visited)


def make_board(board):
    n = len(board)
    new_board = []
    for i in range(0, n+2):
        new_row = []
        for j in range(0, n+2):
            new_row.append(1)
        new_board.append(new_row)

    for i in range(1, n+1):
        for j in range(1, n+1):
            new_board[i][j] = board[i-1][j-1]

    return new_board


def solution(board):
    board = make_board(board)    
    visited = np.full((n+2, n+2, 2), False)
    machine = [0, 0, 1, 1]
    bfs(board, len(board), machine, visited)
    
    answer = 0
    return answer
