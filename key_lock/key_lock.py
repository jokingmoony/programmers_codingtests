# https://programmers.co.kr/learn/courses/30/lessons/60059

import copy

def rotate(matrix):
    N = len(matrix)
    assert len(matrix[0]) == N
    new_matrix = [list(range(N)) for x in list(range(N))]
    for i in range(N):
        for j in range(N):
            new_matrix[j][N-1-i] = matrix[i][j]

    return new_matrix
 
def check(matrix):
    N = len(matrix)
    assert len(matrix[0]) == N
    
    for i in range(N):
        for j in range(N):
            if matrix[i][j] != 1:
                return False
    
    return True
    
def solution(key, lock):
    M = len(key)
    N = len(lock)
    answer = False

    for rotate_cnt in range(4):
        key = rotate(key)
        for x_offset in range(-M+1, N):
            for y_offset in range(-M+1, N):
                lock_tmp = copy.deepcopy(lock)
                for i in range(0, N):
                    for j in range(0, N):
                        try:
                            assert i-y_offset >= 0 and j-x_offset >= 0
                            lock_tmp[i][j] ^= key[i-y_offset][j-x_offset]
                        except:
                            continue
                if check(lock_tmp) is True:
                    return True
    
    return answer