# https://programmers.co.kr/learn/courses/30/lessons/17678

def solution(n, t, m, timetable):
    answer = ''
    
    
    ret = []
    start = int('09') * 60
    for time in timetable:
        hh, mm = time.split(":")
        ret.append(int(hh) * 60 + int(mm))
    ret.sort()
    
    tmp = dict()
    p = 0
    buses = [start + (i * t) for i in range(n)]
    for bus in buses:
        tmp[bus] = []
        cnt = 0
        for j in range(p, len(ret)):
            if ret[j] <= bus and cnt < m:
                p += 1
                cnt += 1
                tmp[bus].insert(0, ret[j])
#                 print(bus, ret[j])
    
    
    buses.sort(reverse=True)
    for bus in buses:
        if len(tmp[bus]) < m:
            answer = bus
            break
        else:
            s = set(tmp[bus])
            if len(s) == 1:
                continue
            else:
                answer = list(s)[-2]
                break
       
    if answer == '':
        min_time = ret[0]
        answer = min_time - 1
        
        
    hh = answer // 60
    mm = answer % 60
    answer = f'{hh:02d}:{mm:02d}'
#     print(tmp)
    
    return answer