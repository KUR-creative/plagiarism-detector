#include <iostream>
#include <fstream>
#include <string>
#define INF 99999
using namespace std;

int map[27][27], min_table[4][27], n, candle[27];
int start[3], min_pos, min_value = INF;

int ctoi(char target) {
	return target - 'a' + 1;
}

char itoc(int target) {
	return target + 'a' - 1;
}

int max_int(int a, int b) {
	if (a == INF) return b;
	else if (b == INF) return a;
	else return (a > b) ? a : b;
}

int dist(int i, int j, int k) {
	int dis = map[i][k] + map[k][j];
	if (i != k && j != k)
		dis += candle[k];
	return dis;
}

void floyd() {
	for (int k = 1; k <= n; k++)
		for (int i = 1; i <= n;i++)
			for (int j = 1; j <= n; j++)
				if (dist(i,j,k) < map[i][j])
					map[i][j] = dist(i,j,k);
}

int main() {
	ifstream inFile("candle.inp");
	ofstream outFile("candle.out");
	char temp = ' ';
	int repeat = -1;

	for (int i = 0; i <= 27; i++) {
		for (int j = 0; j <= 27; j++) {
			if (i != j) {
				map[i][j] = INF;
			}
			else { 
				map[i][i] = 0; 
			}
		}
	}

	inFile >> n;
	
	for (int i = 0; i < 3; i++) {
		inFile >> temp;
		start[i] = ctoi(temp);
	}

	for (int i = 1; i <= n; i++) {
		inFile >> temp;
		int pos_x = ctoi(temp);
		inFile >> repeat;
		candle[pos_x] = repeat;

		for (int j = 1; j <= repeat; j++) {
			inFile >> temp;
			int pos_y = ctoi(temp);
			inFile >> map[pos_x][pos_y];
 		}
	}

//	floyd_trio();
	floyd();

	for (int i = 0; i <= 2; i++) 
		for (int j = 1; j <= n; j++) 
			min_table[i + 1][j] = map[start[i]][j];
		
	for (int j = 1; j <= n; j++) {
		int largest_value = max_int(min_table[1][j], max_int(min_table[2][j], min_table[3][j]));
		if (min_value > largest_value) {
			min_value = largest_value;
			min_pos = j;
		}
	}
	
	outFile << itoc(min_pos) << " " << min_value;
	return 0;
}