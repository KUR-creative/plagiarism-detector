#include <iostream>
#include <fstream>
#include <algorithm>

#define INF 99999;

using namespace std;

int arr[26][26];
int intersection[26];
int main() {
	int N,i,j,k,to,from;
	int friends[3];
	char dummy;

	ifstream ifs("candle.inp");
	ofstream ofs("candle.out");
	for (i = 0; i < 26; i++) {
		for (j = 0; j < 26; j++) {
			if (i != j) arr[i][j] = INF;
		}
	}
	//input data 입력
	ifs >> N;
	for (i = 0; i < 3; i++) {
		ifs >> dummy;
		friends[i] = dummy - 'a';
	}
	for (i = 0; i < N; i++) {
		ifs >> dummy;
		to = dummy - 'a';
		ifs >> intersection[to];	
		for (j = 0; j < intersection[to]; j++) {
			ifs >> dummy;
			ifs >> arr[to][dummy - 'a'];
			arr[dummy - 'a'][to] = arr[to][dummy - 'a'];
		}
	}
	/*
	//입력 확인
	for (i = 0; i < N; i++) {
		for (j = 0; j < N; j++) {
			if (arr[i][j] == 99999) cout << "-  ";
			else cout << arr[i][j] << "  ";
		}
		cout << endl;
	}
	*/
	for (i = 0; i < N; i++) {
		for (j = 0; j < N; j++) {
			if (i == j) continue;
			for (k = 0; k < N; k++) {
				if (k != i && k != j) {
					to = arr[i][k] + arr[k][j] + intersection[k];
					if (arr[i][j] > to) {
						arr[i][j] = to;
					}
				}
			}
		}
	}
	/*
	cout << "-----------------------------------------------" << endl;;
	for (i = 0; i < N; i++) {
		for (j = 0; j < N; j++) {
			if (arr[i][j] == 99999) cout << "-  ";
			else cout << arr[i][j] << "  ";
		}
		cout << endl;
	}*/
	int maxtime = INF;
	for (i = 0; i < N; i++) {
		to = max(max(arr[friends[0]][i], arr[friends[1]][i]), arr[friends[2]][i]);
		if (maxtime > to) {
			maxtime = to;
			from = i;
		}
	}
	dummy = from + 'a';
	ofs << dummy << " " << maxtime;

	return 0;
}