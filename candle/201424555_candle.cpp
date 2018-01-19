#include <iostream>
#include <fstream>
#include <queue>

using namespace std;

int node[30][30];
int a_dist[30], b_dist[30], c_dist[30];
int N;
int Ntime[30];

void printArray(int arr[30]);

void dij(int dist[30], int src) {
	queue<int> Q;
	for (int i = 0; i < N; i++) {
		dist[i] = 100000000;
	}
	dist[src] = -Ntime[src];
	
	Q.push(src);
	while (!Q.empty()) {
		int curr;
		curr = Q.front();
		Q.pop();
		
		for (int i = 0; i < N; i++) {
			if (dist[i] > dist[curr] + node[curr][i] + Ntime[curr]) {
				dist[i] = dist[curr] + node[curr][i] + Ntime[curr];
				Q.push(i);
			}
		}
	}
}

void printArray(int arr[30]) {
	for (int i = 0; i < N; i++) {
		cout << i << " : " << arr[i] << endl;
	}
}
int main() {
	ifstream fin("candle.inp");
	ofstream fout("candle.out");

	fin >> N;
	char a, b, c;
	fin >> a >> b >> c;
	int ia, ib, ic;
	ia = a - 97;
	ib = b - 97;
	ic = c - 97;

	for (int i = 0; i < 30; i++) {
		for (int j = 0; j < 30; j++) {
			node[i][j] = 100000000;
		}
	}
	
	for (int i = 0; i < N; i++) {
		char temp;
		int num, weight, src, dst;
		fin >> temp >> num;
		src = temp - 97;
		Ntime[src] = num;

		for (int j = 0; j < num; j++) {
			fin >> temp >> weight;
			dst = temp - 97;
			node[src][dst] = weight;
		}
	}

	dij(a_dist, ia);
	dij(b_dist, ib);
	dij(c_dist, ic);
	int sum_dist[30];
	for (int i = 0; i < N; i++) {
		sum_dist[i] = max(max(a_dist[i], b_dist[i]), c_dist[i]);
	}

	//printArray(sum_dist);

	int resultChar, resultDist;
	resultDist = 100000000;
	for (int i = 0; i < N; i++) {
		if (resultDist > sum_dist[i]) {
			resultDist = sum_dist[i];
			resultChar = i;
		}
	}

	fout << char(resultChar + 97) << " " << resultDist << endl;
}