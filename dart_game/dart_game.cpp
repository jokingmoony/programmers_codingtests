// https://programmers.co.kr/learn/courses/30/lessons/17682

#include <string>
#include <iostream>
#include <math.h>
using namespace std;

int solution(string dartResult) {
    int arr[3];
    int answer = 0;
    int j = -1;
    int len = dartResult.length();
    for (int i = 0; i < len; i++) {
        if (isdigit(dartResult[i])) {
            if (i != len - 1 && isdigit(dartResult[i + 1])) {
                arr[++j] = 10;
                i++;
            }
            else
                arr[++j] = dartResult[i] - '0';
        }
        else if (dartResult[i] == 'D') {
            arr[j] = pow(arr[j], 2);
        }
        else if (dartResult[i] == 'T') {
            arr[j] = pow(arr[j], 3);
        }
        else if (dartResult[i] == '#') {
            arr[j] *= -1;
        }
        else if (dartResult[i] == '*') {
            arr[j] *= 2;
            if (j != 0)
                arr[j - 1] *= 2;
        }
    }
    for (int i = 0; i < 3; i++)
        answer += arr[i];
    return answer;
}