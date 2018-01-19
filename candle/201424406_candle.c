#include <stdio.h>

int cost[26][26];
int degree[26];
int result[4][26];

int getmax(int a, int b) {
	if (a > b)
		return a;
	return b;
}

int main() {
	FILE* fin = fopen("candle.inp", "r");
	FILE* fout = fopen("candle.out", "w");
	int Node, i, j, k;
	char friends[3];
	fscanf(fin, "%d\n%c %c %c ", &Node, &friends[0], &friends[1], &friends[2]);

	for (i = 0; i < Node; i++) {
		char temp;
		fscanf(fin, "%c ", &temp);
		int ind = temp - 'a';
		fscanf(fin, "%d ", &degree[ind]);
		for (j = 0; j < degree[ind]; j++) {
			char t;
			fscanf(fin, "%c ", &t);
			int indd = t - 'a';
			fscanf(fin, "%d ", &cost[ind][indd]);
		}
	}

	for (k = 0; k < Node; k++) {
		for (i = 0; i < Node; i++) {
			for (j = 0; j < Node; j++) {
				if (cost[i][j] == 0 || cost[i][j] > cost[i][k] + cost[k][j] + degree[k]) {
					if (cost[i][k] != 0 && cost[k][j] != 0)
						cost[i][j] = cost[i][k] + cost[k][j] + degree[k];
				}
			}
		}
	}

	for (i = 0; i < Node; i++) {
		result[0][i] = cost[friends[0] - 'a'][i];
		result[1][i] = cost[friends[1] - 'a'][i];
		result[2][i] = cost[friends[2] - 'a'][i];
		result[3][i] = getmax(result[0][i], getmax(result[1][i], result[2][i]));
	}

	int minind = 0, min = 100000000;
	for (i = 0; i < Node; i++) {
		if (result[3][i] < min) {
			minind = i;
			min = result[3][i];
		}
	}

	fprintf(fout, "%c %d\n", minind + 'a', min);
}