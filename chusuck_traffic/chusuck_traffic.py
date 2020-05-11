import datetime

def solution(lines):
    answer = 0
    
    traffics = []
    
    for line in lines:
        _, end_time, time = line.split()
        end = datetime.datetime.strptime(end_time,'%H:%M:%S.%f')
        time = float(time[:-1]) - 0.001
        time = datetime.timedelta(seconds=time)
        start = end - time
        traffics.append((start, end))

    for start, end in traffics:
        td = datetime.timedelta(seconds=0.999)
        times = [(start, start + td), (start - td, start), (end, end + td), (end - td, end)]
        for s, e in times:
            tmp = 0
            for start, end in traffics:
                if (start >= s and start <= e) or (end >= s and end <= e) or (start <= s and end >= e):
                    tmp += 1
            if tmp > answer:
                answer = tmp
    
    return answer