// https://programmers.co.kr/learn/courses/30/lessons/1829

#include <vector>

using namespace std;

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.

int offset[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
bool visited[100][100] = {0,};

long long dfs(int m, int n, int r, int c, vector<vector<int>> picture) {
    long long cnt = 1;
    visited[r][c] = true;
    
    for (int i = 0; i < 4; i++) {
        int new_r = r + offset[i][0];
        int new_c = c + offset[i][1];
        if ((new_r >= 0 && new_r < m) && (new_c >= 0 && new_c < n))
            if (picture[new_r][new_c] == picture[r][c] && !visited[new_r][new_c]) {
                cnt += dfs(m, n, new_r, new_c, picture);
            }
    }
    return cnt;
}

vector<int> solution(int m, int n, vector<vector<int>> picture) {
    int number_of_area = 0;
    int max_size_of_one_area = 0;
    
    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    long long cnt = 0;
    
    for (int i = 0; i < 100; i++)
        for (int j = 0; j < 100; j++)
            visited[i][j] = false;
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (picture[i][j] != 0 && !visited[i][j]) {
                answer[0]++;
                cnt = dfs (m, n, i, j, picture);
                if (answer[1] < cnt)
                    answer[1] = cnt;
            }
        }
    }
    return answer;
}