# https://programmers.co.kr/learn/courses/30/lessons/17678

def solution(n, t, m, timetable):
    answer = ''
    
    times = []
    start = int('09') * 60
    
    for time in timetable:
        hh, mm = time.split(":")
        times.append(int(hh) * 60 + int(mm))
    times.sort()
    
    bus_crew_dict = dict()
    
    crew_id = 0
    buses = [start + (i * t) for i in range(n)]
    
    for bus in buses:
        bus_crew_dict[bus] = []
        crew_cnt = 0
        for j in range(crew_id, len(times)):
            if times[j] <= bus and crew_cnt < m:
                crew_id += 1
                crew_cnt += 1
                bus_crew_dict[bus].insert(0, times[j])
    
    last_bus = buses[-1]
    
    if len(bus_crew_dict[last_bus]) < m:
        answer = bus
    else:
        answer = bus_crew_dict[last_bus][0] - 1

    hh = answer // 60
    mm = answer % 60
    answer = f'{hh:02d}:{mm:02d}'
    
    return answer