# https://programmers.co.kr/learn/courses/30/lessons/49994

def check_range(x, y):
    if (x >= -5 and x <= 5) and (y >= -5 and y <= 5):
        return True
    return False

def solution(dirs):
    answer = 0
    s = set()
    offset = {'U': (0, 1), 'D':(0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    
    for dir in dirs:
        off_x, off_y = offset[dir]
        new_x, new_y = x + off_x, y + off_y
        if check_range(new_x, new_y):
            s.add((new_x, new_y, x, y))
            s.add((x, y, new_x, new_y))
            x, y = new_x, new_y
    
    answer = len(s) // 2
    return answer