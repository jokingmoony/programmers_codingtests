# https://programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    answer = []
    word_dict = dict()
    
    for i in range(26):
        word_dict[i+1] = chr(ord('A') + i)
    dict_index = 27
    while len(msg) != 0:
        new_word = ''
        for index, word in word_dict.items():
            if msg.startswith(word):
                answer.append(index)
                if len(word) < len(msg):
                    new_word = msg[:len(word)+1]
                break
        if new_word:
            word_dict[dict_index] = new_word
            dict_index += 1
        word_dict = {k: v for k, v in sorted(word_dict.items(), key=lambda item: len(item[1]), reverse=True)}
        msg = msg[len(word):]
    
    return answer