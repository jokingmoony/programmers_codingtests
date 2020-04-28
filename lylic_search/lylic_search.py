# https://programmers.co.kr/learn/courses/30/lessons/60060

def solution(words, queries):
    answer = []
    words_set = []
    
    len_set = []
    for query in queries:
        len_set.append(len(query))
    
    for length in len_set:
        words_set.append(list(filter(lambda x : len(x) == length, words)))
    
    for i, query in enumerate(queries):
        cnt = 0
        for word in words_set[i]:
            cnt += 1
            for q, w in zip(query, word):
                    if q == '?':
                        continue
                    elif q != w:
                        cnt -= 1
                        break
        answer.append(cnt)
    
    return answer