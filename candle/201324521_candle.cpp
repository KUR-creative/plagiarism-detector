#include <iostream>
#include <fstream>

using namespace std;
int INF = 10000;
int ver_num;
char p1, p2, p3;

int w[26][26];
int adj[26][26];
int via[26][26];
int path[26];
int degree[26];
int max(int i,int j,int k) {
	if (i > j)
		if (k > i)
			return k;
		else
			return i;
	else
		if (k > j)
			return k;
		else
			return j;

}

void floyd() {
	for (int i = 0; i < ver_num; i++) {
		for (int j = 0; j < ver_num; j++) {			
			if (i == j)
				adj[i][j] = 0;
			else
				adj[i][j] = w[i][j];

		}
	}

	for (int k = 0; k < ver_num; k++)
	{
		for (int i = 0; i < ver_num; i++)
		{
			for (int j = 0; j < ver_num; j++)
			{
				
				if( k != i && k != j) {
					if (adj[i][k] + adj[k][j] + degree[k] < adj[i][j])
					{
						adj[i][j] = adj[i][k] + adj[k][j] + degree[k];    // 최단 거리
					}
				}
			}
		}
	}
	
}
int main() {
	ifstream in("candle.inp");
	ofstream on("candle.out");

	in >> ver_num;
	
	in >> p1 >> p2 >> p3;

	int i1 = p1 - 'a';
	int i2 = p2 - 'a';
	int i3 = p3 - 'a';

	while (!in.eof()) {
		char v;
		in >> v;
		int index = v - 'a';
		int row;
		in >> row;
		degree[index] = row;
		for (int i = 0; i < row; i++) {
			int index2;
			char v2;
			in >> v2;//상대 vertex index
			index2 = v2 - 'a';
			int t_w; //weight
			in >> t_w;
			w[index][index2] = t_w; // 저장
		}
	}


	for (int i = 0; i < ver_num; i++) {
		for (int j = 0; j < ver_num; j++) {
			if (w[i][j] == 0)
				w[i][j] = INF;
		}
	}

	floyd();
	
	
	int cost = INF;
	int min_index = 0;

	for (int i = 0; i < ver_num; i++) {
		for (int j = 0; j < ver_num; j++) {
			if (i == j)
				adj[i][j] = 0;
		}
	}

	for (int i = 0; i < ver_num; i++) {
		int temp_cost = max(adj[i1][i], adj[i2][i], adj[i3][i]);
		if (temp_cost < cost) {
			cost = temp_cost;
			min_index = i;
		}
	}

	char res = min_index + 'a';
	on << res <<" "<< cost<< endl;
	
	
}