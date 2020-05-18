#include <string>
#include <vector>
#include <iostream>
#include <map>

using namespace std;


map<long long, long long>m; 

long long find_next(long long x) {
	if (m[x] == 0) {
		m[x] = x + 1;
		return x;
	}
	m[x] = find_next(m[x]);
	return m[x];
}

vector<long long> solution(long long k, vector<long long> room_number) {
    vector<long long> answer;

	for (auto room : room_number) {
		long long n = find_next(room);
		answer.push_back(n);
	}

    return answer;
}

int main() {
	vector<long long> v {1, 3, 4, 1, 3, 1};
	vector<long long> answer = solution(10, v);
	for (auto i : answer) {
		cout << i << "\n"
	}
}