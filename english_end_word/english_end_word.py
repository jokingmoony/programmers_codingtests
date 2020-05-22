# https://programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    answer = [0, 0]

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    buffer = []
    buffer.append(words.pop(0))
    
    for i, word in enumerate(words):
        if word in buffer or word[0] != buffer[-1][-1]:
            answer[0] = ((i + 1) % n + 1)
            answer[1] = ((i + 1) // n + 1)
            break
        else:
            buffer.append(word)

    return answer