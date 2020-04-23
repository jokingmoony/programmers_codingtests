
# https://programmers.co.kr/learn/courses/30/lessons/60061

def check_constructed(constructed, x, y, built_type):
    built_type = 0 if built_type == 'pillar' else 1
    try:
        lst = list(filter(lambda lst: lst[0] == x and lst[1] == y, constructed))
    except:
        return False
    if len(lst) == 0:
        return False
    if len(lst) == 2:
        return True
    elif lst[0][2] == built_type:
        return True
    else:
        return False
    
    
def check_pillar(constructed, x, y):
    if y == 0:
        return True
    elif check_constructed(constructed, x, y, 'floor'):
        return True
    elif check_constructed(constructed, x-1, y, 'floor'):
        return True
    elif check_constructed(constructed, x, y-1, 'pillar'):
        return True
    return False

def check_floor(constructed, x, y):
    if y == 0:
        return True
    elif check_constructed(constructed, x-1, y, 'floor') and check_constructed(constructed, x+1, y, 'floor'):
        return True
    elif check_constructed(constructed, x, y-1, 'pillar') or check_constructed(constructed, x+1, y-1, 'pillar'):
        return True
    return False

def construct_floor(constructed, x, y, n):
    if x >= n or x < 0:
        return
    elif y > n or y < 0:
        return
    constructed.append([x, y, 1])
    if check_floor(constructed, x, y):
        return
    else:
        constructed.remove([x, y, 1])

def construct_pillar(constructed, x, y, n):
    if x > n or x < 0:
        return
    elif y >= n or y < 0:
        return
    constructed.append([x, y, 0])
    if check_pillar(constructed, x, y):
        return
    else:
        constructed.remove([x, y, 0])

def remove_pillar(constructed, x, y, n):
    if x > n or x < 0:
        return
    elif y >= n or y < 0:
        return
    try:
        constructed.remove([x, y, 0])
    except:
        return
    if check_constructed(constructed, x-1, y+1, 'floor') and check_floor(constructed, x-1, y+1) == False:
        constructed.append([x, y, 0])
        return
    if check_constructed(constructed, x, y+1, 'floor') and check_floor(constructed, x, y+1) == False:
        constructed.append([x, y, 0])
        return
    if check_constructed(constructed, x, y+1, 'pillar') and check_pillar(constructed, x, y+1) == False:
        constructed.append([x, y, 0])
        return
        

def remove_floor(constructed, x, y, n):
    if x >= n or x < 0:
        return
    elif y > n or y < 0:
        return
    try:
        constructed.remove([x, y, 1])
    except:
        return
    if check_constructed(constructed, x, y, 'pillar') and check_pillar(constructed, x, y) == False:
        constructed.append([x, y, 1])
        return
    if check_constructed(constructed, x+1, y, 'pillar') and check_pillar(constructed, x+1, y) == False:
        constructed.append([x, y, 1])
        return
    if check_constructed(constructed, x-1, y, 'floor') and check_floor(constructed, x-1, y) == False:
        constructed.append([x, y, 1])
        return
    if check_constructed(constructed, x+1, y, 'floor') and check_floor(constructed, x+1, y) == False:
        constructed.append([x, y, 1])
        return
    

def solution(n, build_frame):
    constructed = []
    
    for frame in build_frame:
        if frame[2] == 0:
            if frame[3] == 1:
                construct_pillar(constructed, frame[0], frame[1], n)
            else:
                remove_pillar(constructed, frame[0], frame[1], n)
        else:
            if frame[3] == 1:
                construct_floor(constructed, frame[0], frame[1], n)
            else:
                remove_floor(constructed, frame[0], frame[1], n)

    constructed = sorted(constructed)
    return constructed