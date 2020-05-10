# https://programmers.co.kr/learn/courses/30/lessons/17683

import datetime
import re

def get_time(start, end):
    start_time = datetime.datetime.strptime(start,'%H:%M')
    end_time = datetime.datetime.strptime(end,'%H:%M')
    
    return (end_time - start_time).seconds // 60

def encode(code):
    encoder = {'C':'a', 'C#':'b', 'D':'c', 'D#':'d', 'E':'e', 'E#':'z', 'F':'f', 'F#':'g', 'G':'h', 'G#':'i', 'A':'j', 'A#':'k', 'B':'l'}
    res = ''
    code = re.findall('\w#?', code)
    for c in code:
        res += encoder[c]
    return res

def make_sound(time, code):
    if time < len(code):
        return code[:time]
    res = []
    offset = time - len(code)
    multiple = int(offset / len(code))
    modular = offset % len(code)
    
    for i in range(0, multiple + 1):
        res.extend(code) 
    res.extend(code[:modular])
    
    return ''.join(res)

def solution(m, musicinfos):
    answer = []
    m = encode(m)
    for info in musicinfos:
        start, end, name, code = info.split(',')
        time = get_time(start, end)
        code = encode(code)
        sound = make_sound(time, code)
        if m in sound:
            if len(answer) == 0:
                answer = [name, time]
            elif answer[1] < time:
                answer = [name, time]
        
    
    if len(answer) == 0:
        return '(None)'
    else:
        return answer[0]