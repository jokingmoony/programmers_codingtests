
def solution(s):
    answer = float('inf')

    for i in range(1, len(s) + 1):
        whole_words = ''
        prev_word = ''
        cnt = 1
        for j in range(0, len(s), i):
            if prev_word == '':
                prev_word = s[j:j + i]
            elif prev_word == s[j:j + i]:
                cnt += 1
            else:
                if cnt != 1:
                    whole_words += str(cnt) + prev_word
                else:
                    whole_words += prev_word
                cnt = 1
                prev_word = s[j:j + i]

        if cnt != 1:
            whole_words += str(cnt) + prev_word
        else:
            whole_words += prev_word
        if answer > len(whole_words):
            answer = len(whole_words)

    return answer

if __name__ == "__main__":
	if solution("aabbaccc") != 7:
		print('1 fail')
	elif solution("ababcdcdababcdcd") != 9:
		print('2 fail')
	elif solution("abcabcdede") != 8:
		print('3 fail')
	elif solution("abcabcabcabcdededededede") != 14:
		print('4 fail')
	elif solution("xababcdcdababcdcd") != 17:
		print('5 fail')
	else:
		print('success')
