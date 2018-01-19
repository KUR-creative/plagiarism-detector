#include <stdio.h>
#include <iostream>
#include <fstream>

using namespace std;

int max(int a, int b, int c) {
	if (a > b) {
		if (a > c) return a;
		else return c;
	}
	else {
		if (b > c) return b;
		else return c;
	}
}

bool active[26];
int d[26][26];
int w[26];
int num_of_vertex;
char v1, v2, v3;
int a1, a2, a3;

int main() {
	fstream in;
	fstream out;
	in.open("candle.inp", ios::in);
	out.open("candle.out", ios::out);
	in >> num_of_vertex;
	in >> v1 >> v2 >> v3;
	a1 = v1 - 97;
	a2 = v2 - 97;
	a3 = v3 - 97;
	for (int i = 0; i < 26; i++) {
		w[i] = 0;
		active[i] = false;
		for (int j = 0; j < 26; j++){
			d[i][j] = 1000000;
		}
	}
	for (int i = 0; i < 26; i++) 
		d[i][i] = 0;

	char a;
	int a_t;
	int n, dist;
	char x;
	int x_t;
	for (int i = 0; i < num_of_vertex; i++) {
		in >> a >> n;
		int a_t = a - 97;
		active[a_t] = true;
		for (int j = 1; j <= n * 2; j = j + 2) {
			in >> x;
			in >> dist;
			int x_t = x - 97;
			d[x_t][a_t] = dist;	d[a_t][x_t] = dist;
			active[x_t] = true;
			w[a_t]++;
		}
	}

	for (int k = 0; k < 26; ++k){
		for (int i = 0; i < 26; ++i){
			for (int j = 0; j < 26; ++j){
				if (active[i] && active[j] && active[k]) {
					if (d[i][j] > (d[i][k] + d[k][j]) + w[k]){
						d[i][j] = d[i][k] + d[k][j] + w[k];
					}
				}
			}
		}
	}
	int min_ = 1000000;
	int result = 0;
	char alpha = 0;
	for (int i = 0; i < 26; i++) {
		if (active[i]) {
			if (max(d[a1][i], d[a2][i], d[a3][i]) < min_) {
				min_ = max(d[a1][i], d[a2][i], d[a3][i]);
				result = min_;
				alpha = i + 97;
			}
		}
	}
	out << alpha << " " << min_ << endl;
	in.close();
	out.close();

	return 0;
}
