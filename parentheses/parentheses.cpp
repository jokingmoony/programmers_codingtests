// https://programmers.co.kr/learn/courses/30/lessons/60058?language=cpp

#include <string>
#include <vector>
#include <stack>
#include <iostream>

using namespace std;

bool is_right(string p) {
    stack<char> p_stack;
    for (int i = 0; i < p.length(); i++) {
        if (p[i] == '(')
            p_stack.push(p[i]);
        else {
            if (p_stack.empty())
                return false;
            else
                p_stack.pop();
        }
    }
    if (p_stack.empty())
        return true;
    else
        return false;
}

void split_parenthesis(string p, string *u, string *v) {
    int len = p.length();
    int l = 0, r = 0;
    
    for (int i = 0; i < len; i++) {
        if (p[i] == '(')
            l++;
        else
            r++;
        if (l == r) {
            *u = p.substr(0, i + 1);
            *v = p.substr(i + 1, len - i);
            break;
        }
            
    }
}

string solution(string p) {
    string answer = "";
    if (p.empty())
        return p;

    string u, v;
    split_parenthesis(p, &u, &v);
	if (is_right(u))
        answer = u + solution(v);
    else {
        answer = '(' + solution(v) + ')';
        u.erase(0, 1);
        u.pop_back();
        for (int i = 0; i < u.length(); i++) {
            if (u[i] == '(')
                u[i] = ')';
            else
                u[i] = '(';
        }
        answer += u;
    }
    return answer;
}

int main() {
    cout << solution(string("())("));
    while (1) { }
}