#include <iostream>
#include <cstdio>
#include <fstream>
#include <algorithm>

using namespace std;
int D[27][27];
int cross[27];
int max(int a, int b, int c) {
	return max(max(a, b), c);
}
int main() {
	FILE *inp = fopen("candle.inp", "r");
	FILE *out = fopen("candle.out", "w");

	int N;
	fscanf(inp, "%d", &N);
	char p1, p2, p3;
	fscanf(inp, " %c %c %c", &p1, &p2, &p3);

	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; ++j) {
			D[i][j] = 1e9;
		}
	}

	for (int i = 0; i < N; ++i) {
		char s;
		int size;
		fscanf(inp, " %c %d", &s, &size);
		cross[s-'a'] = size;
		for (int j = 0; j < size; ++j) {
			char t;
			int w;
			fscanf(inp, " %c %d", &t, &w);
			D[s - 'a'][t - 'a'] = w;
		}
	}

	for (int k = 0; k < N; ++k) {
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				if (D[i][j] > D[i][k] + D[k][j] + cross[k]) {
					D[i][j] = D[i][k] + D[k][j] + cross[k];
				}
			}
		}
	}
	int ans = 2e9;
	char pos;
	for (int i = 0; i < N; ++i) {
		if (D[p1 - 'a'][i] == 2e9) continue;
		if (D[p2 - 'a'][i] == 2e9) continue;
		if (D[p3 - 'a'][i] == 2e9) continue;
		int tmp = max(D[p1 - 'a'][i], D[p2 - 'a'][i], D[p3 - 'a'][i]);
		if (ans > tmp) {
			ans = tmp;
			pos = i;
		}
	}
	pos = pos + 'a';
	fprintf(out, "%c %d\n", pos, ans);
	//out << ans << pos + 'a' << endl;

	fclose(inp);
	fclose(out);
	return 0;
}