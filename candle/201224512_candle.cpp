#include <iostream>
#include <fstream>

using namespace std;
ifstream fin;
ofstream fout;
int n;

int getMax(int a, int b, int c) {
	int max;
	max = (a > b ? a : b) > c ? (a > b ? a : b) : c;
	return max;
}
int main() {
	char start = 0;
	char end = 0;
	char person[3];
	int weight;
	int dist[26][26];//97~122
	int sp[3][26];
	int check[3][26];
	int degree[26];
	fin.open("candle.inp");
	fout.open("candle.out");
	fin >> n;
	fin >> person[0] >> person[1] >> person[2];

	for (int i = 0; i < 26; i++)
		for (int j = 0; j < 26; j++)
			dist[i][j] = 9999;
	for (int i = 0; i < 26; i++)
		dist[i][i] = 0;
	for (int i = 0; i < 3; i++)
		for (int j = 0; j < 26; j++)
			check[i][j] = true;
	for (int i = 0; i < n; i++) {
		fin >> start;
		fin >>degree[start - 97];
		check[0][start - 97] = false;
		check[1][start - 97] = false;
		check[2][start - 97] = false;
		for (int j = 0; j < degree[start - 97]; j++) {
			fin >> end >> weight;
			dist[start - 97][end - 97] = weight;
		}
	}
	check[0][person[0] - 97] = true;
	check[1][person[1] - 97] = true;
	check[2][person[2] - 97] = true;
	for (int i = 0; i < 26; i++) {
		sp[0][i] = dist[person[0] - 97][i];
		sp[1][i] = dist[person[1] - 97][i];
		sp[2][i] = dist[person[2] - 97][i];
	}
	int min;
	int min_idx;
	for (int j = 0; j < 3; j++) {
		for (int k = 0; k < 25; k++) {
			min = 999;
			for (int i = 0; i < 26; i++) {
				if (!check[j][i] && sp[j][i] < min) {
					min = sp[j][i];
					min_idx = i;
				}
			}
			check[j][min_idx] = true;
			for (int i = 0; i < 26; i++) {
				if (sp[j][i] > sp[j][min_idx] + dist[min_idx][i]+degree[min_idx]) {
					sp[j][i] = sp[j][min_idx] + dist[min_idx][i]+ degree[min_idx];
				}
			}
		}
	}
	min = 999;
	char result;
	int temp;
	for (int i = 0; i < 26; i++) {
		temp = getMax(sp[0][i], sp[1][i], sp[2][i]);
		if (temp < min) {
			min = temp;
			min_idx = i;
		}
	}
	result = min_idx + 97;
	fout << result <<" " << min;

	return 0;
}