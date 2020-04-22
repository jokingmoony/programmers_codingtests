# https://programmers.co.kr/learn/courses/30/lessons/60058?language=cpp


def split_parentheses(p):
    split_index = 0
    r = 0
    l = 0
    for i, c in enumerate(p):
        if c == '(':
            l += 1
        else:
            r += 1
        if l == r:
            split_index = i
            break
    u = p[0:split_index + 1]
    v = p[split_index + 1:]
    return u, v

def is_right(p):
    stack = []
    for c in p:
        if c == '(':
            stack.append(c)
        else:
            try:
                stack.pop()
            except:
                return False
            
    if len(stack) == 0:
        return True
    else:
        return False
    
def solution(p):
    if p == '' or p == None:
        return p
    answer = ''
    u, v = split_parentheses(p)
    
    if is_right(u):
        answer =  u + solution(v)
    else:
        answer = f'({solution(v)})'
        u = ''.join(map(lambda x : '(' if x == ')' else ')', u[1:-1]))
        answer += u
    return answer



if __name__ == "__main__":
	print(solution('(()))('))