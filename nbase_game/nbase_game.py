# https://programmers.co.kr/learn/courses/30/lessons/17687

numbers = '0123456789ABCDEF'

def number_to_base(n, b):
    if n == 0:
        return '0'
    digits = []
    while n:
        digits.append(numbers[n % b])
        n //= b
    return ''.join(digits[::-1])

def solution(n, t, m, p):
    answer = ''
    i = 0
    while len(answer) < m * t:
        number_string = number_to_base(i, n)
        i += 1
        answer += number_string
    answer = answer[p-1::m]
    
    return answer[:t]
        
    