# https://programmers.co.kr/learn/courses/30/lessons/49995

def solution(cookie):
    answer = 0
    total = len(cookie)
    
    for b in range(total-1):
        c = b+1
        a, d = b, c
        
        x, y = cookie[b], cookie[c]
        
        while True:
            a_move = False
            d_move = False
            if x == y:
                answer = max(x, answer)
                a_move = True
                d_move = True
            elif x > y:
                d_move = True
            elif x < y:
                a_move = True
            
            if a_move:
                a -= 1
                if a < 0:
                    break
                else:
                    x += cookie[a]
            if d_move:
                d += 1
                if d >= total:
                    break
                else:
                    y += cookie[d]
                
            
    
    return answer