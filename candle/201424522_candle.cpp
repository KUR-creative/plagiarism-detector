#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int vertexWeight[26];
int edgeWeight[26][26];
char friends[3];

int shortest[3][26];

int n;

void Dijkstra(int friendIdx, int friendStart) {
	for (int i = 0; i < n; i++)
		shortest[friendIdx][i] = 100000000;

	shortest[friendIdx][friendStart] = -vertexWeight[friendStart];

	vector<int> visit;
	visit.push_back(friendStart);

	while (visit.size() != 0) {
		sort(visit.begin(), visit.end());

		for (int i = 0; i < n; i++) {
			if (edgeWeight[visit.front()][i] != 0) {
				if (shortest[friendIdx][i] > shortest[friendIdx][visit.front()] + edgeWeight[visit.front()][i] + vertexWeight[visit.front()]) {
					shortest[friendIdx][i] = shortest[friendIdx][visit.front()] + edgeWeight[visit.front()][i] + vertexWeight[visit.front()];
					visit.push_back(i);
				}
			}
		}

		visit.erase(visit.begin());
	}
}

int main(void) {
	ifstream fin("candle.inp");
	fin >> n;

	for (int i = 0; i < 3; i++) {
		fin >> friends[i];
		friends[i] -= 'a';
	}

	for (int i = 0; i < n; i++) {
		char temp1;
		fin >> temp1;
		temp1 -= 'a';

		fin >> vertexWeight[temp1];

		for (int j = 0; j < vertexWeight[temp1]; j++) {
			char temp2;
			fin >> temp2;
			temp2 -= 'a';

			fin >> edgeWeight[temp1][temp2];
		}
	}

	for (int i = 0; i < 3; i++)
		Dijkstra(i, friends[i]);

	ofstream fout("candle.out");

	int min = 100000000;
	char idx;

	for (int i = 0; i < n; i++) {
		int tempMax = (shortest[0][i] < shortest[1][i]) ? ((shortest[1][i] < shortest[2][i]) ? shortest[2][i] : shortest[1][i]) : ((shortest[0][i] < shortest[2][i]) ? shortest[2][i] : shortest[0][i]);

		if (tempMax < min) {
			min = tempMax;
			idx = i;
		}
	}

	fout << (char)(idx + 'a') << " " << min << endl;

	return 0;
}