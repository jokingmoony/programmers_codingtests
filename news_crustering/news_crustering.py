# https://programmers.co.kr/learn/courses/30/lessons/17677

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    str1_dict = {}
    str2_dict = {}
    
    for i in range(len(str1) - 1):
        sub_str = str1[i:i+2]
        if sub_str not in str1_dict:
            str1_dict[sub_str] = 1
        else:
            str1_dict[sub_str] += 1
    
    for i in range(len(str2) - 1):
        sub_str = str2[i:i+2]
        if sub_str not in str2_dict:
            str2_dict[sub_str] = 1
        else:
            str2_dict[sub_str] += 1
    
    str1_dict = {k: v for k, v in str1_dict.items() if k.isalpha()}
    str2_dict = {k: v for k, v in str2_dict.items() if k.isalpha()}
    
    intersection_len = 0
    for key, val in str1_dict.items():
        if key in str2_dict:
            intersection_len += min(str1_dict[key], str2_dict[key])
    
    union = {**str1_dict, **str2_dict}
    for key, val in str1_dict.items():
        if key in union and val > union[key]:
            union[key] = val
            
    for key, val in str2_dict.items():
        if key in union and val > union[key]:
            union[key] = val
    
    union_len = 0
    for key, val in union.items():
        union_len += val
    
    if union_len == 0:
        answer = 65536
    else:
        answer = int(intersection_len / union_len * 65536)
    
    return answer