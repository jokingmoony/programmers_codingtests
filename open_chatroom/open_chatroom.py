# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    actions = []
    id_dict = {}
    
    for r in record:
        action, uid, *name = r.split(' ')
        
        if action == 'Enter':
            actions.append((uid, 'enter'))
            id_dict[uid] = name[0]
        elif action == 'Leave':
            actions.append((uid, 'leave'))
        else:
            id_dict[uid] = name[0]
        
    for action in actions:
        uid = action[0]
        name = id_dict[uid]
        if action[1] == 'enter':
            answer.append(f'{name}님이 들어왔습니다.')
        else:
            answer.append(f'{name}님이 나갔습니다.')
    return answer